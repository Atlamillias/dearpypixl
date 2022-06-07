from typing import Callable, Any, Sequence
from dataclasses import dataclass
from time import sleep
from dearpygui._dearpygui import (
    get_frame_count,
    set_frame_callback,
    set_exit_callback,
    get_total_time,
)

from dearpypixl.components import prep_callback, get_positional_args_count
from dearpypixl.components.utilities import TypeGuard

__all__ = [

]


def _not_implemented(*args, **kwargs):
    raise NotImplementedError


ALL_FRAMES =  0
LAST_FRAME = -1


@dataclass(repr=False)
class FrameEvent:
    _callback : Callable
    _user_data: Any = None
    _sender   : Any = None
    _app_data : Any = None

    def __post_init__(self) -> None:
        # Note that DearPyGui doesn't send any arguments to callbacks set
        # with `dpg.set_exit_callback` or `dpg.set_frame_callback` even if you
        # include user_data. This implementation will send arguments regardless
        # (if able) to emulate the missing behavior... 
        self._pos_arg_cnt  = ...
        self._arguments    = ...
        self._unwrapped_cb = self._callback
        self.update(callback=self._callback)

    def  __repr__(self) -> str:
        return f"{type(self).__qualname__}(callback={self._callback!r}, user_data={self._user_data!r})"

    def __call__(self, *_, **kwargs) -> None:
        self._callback(*self._arguments, **kwargs)

    @property
    def callback(self) -> Callable:
        return self._callback

    @property
    def sender(self) -> Any:
        return self._sender

    @property
    def app_data(self) -> Any:
        return self._app_data

    @property
    def user_data(self) -> Any:
        return self._user_data

    def update(self, *, callback: Callable = None, sender: Any = ..., app_data: Any = ..., user_data: Any = ...) -> None:
        if sender != ...:
            self._sender = sender
            # re-wrap callback because `prep_callback` replaces 'sender' with the
            # first argument used to call it...
            self._callback = prep_callback(self._sender or self, self._unwrapped_cb)
        if app_data != ...:
            self._app_data = app_data
        if user_data != ...:
            self._user_data = user_data
        
        if callback:
            if not callable(callback):
                raise ValueError("`callback` is not callable.")
            self._unwrapped_cb = callback
            self._callback     = prep_callback(self._sender or self, self._unwrapped_cb)
            self._pos_arg_cnt  = get_positional_args_count(self._unwrapped_cb)

        # `prep_callback` has `sender` bound already
        self._arguments = (None, self._app_data, self._user_data)[:self._pos_arg_cnt]


class FrameEvents(dict):
    """A dictionary-like object that manages frame callbacks.

    Almost every method accepts a `frame` (int) argument. This argument must
    be must be greater than or equal to -1. A value of -1 specifies callbacks to
    run on the last frame (application exit) and a value of 0 specifies callbacks
    scheduled to run every frame. Every other value is tied to a specific frame
    (rendered or otherwise).

    DearPyGui only allows a maximum of 50 callbacks to be scheduled between all
    frames IN TOTAL*. However, you can schedule as many callbacks as you want for
    the "last frame" (-1) and "all frames" (0).

    * This may actually just be a total of 50 scheduled callbacks period. Not sure...
    """
    # NOTE: I really wouldn't create more than one instance of this (see `flush`
    # method comments).
    setdefault = _not_implemented  # see the `get` method
    pop        = _not_implemented  # see the `flush` method
    popitem    = _not_implemented
    update     = _not_implemented  # TODO:

    _keyguard  = TypeGuard((int,), lambda key: key >= -1)

    ALL_FRAMES =  ALL_FRAMES
    LAST_FRAME =  LAST_FRAME

    def __init__(self) -> None:  # Removed functionality to initialize w/arguments.
        super().__init__()
        # self[ 0]  # stores callbacks that run mid-render loop ("all frames")
        # self[-1]  # stores callbacks that run on application exit ("last frame")
        self._updates      = self[0]

    def _set_frame_callback(self, frame: int) -> None:
        """Sets the main callback for a specific frame. It will call any event
        that is set to run on that frame.
        """
        def frame_callback(*args, **kwargs) -> None:
            for event in self[frame]:
                event(*args, **kwargs)

        if frame == LAST_FRAME:
            set_exit_callback(frame_callback)
        else:
            set_frame_callback(frame, frame_callback)

    @_keyguard.wraps(target_idx=1)
    def get(self, frame: int) -> list[FrameEvent]:
        """Return the list of callbacks set to run on the specified frame.

        Args:
            * frame (int): Frame to query.
        """
        # This is basically a combination of `setdefault` and `get` methods.
        if frame not in self:
            super().__setitem__(frame, [])
            self._set_frame_callback(frame)
        return super().__getitem__(frame)

    @_keyguard.wraps(target_idx=1)
    def __setitem__(self, frame: int, callback: FrameEvent | tuple[Callable, Any] | Callable):
        # No work needs to be done.
        if isinstance(callback, FrameEvent):
            return self[frame].append(callback)
        # Create a FrameEvent instance for the callback.
        elif not isinstance(callback, Sequence):
            callback = (callback,)
        self[frame].append(FrameEvent(*callback))

    __getitem__ = get

    def clear(self) -> None:
        """Clear/unregister all callbacks for all frames.
        """
        for frame_events in self.values():
            frame_events.clear()

    def flush(self, frame: int = None) -> None:
        """Clear/unregister all callbacks for the specified frame.

        Args:
            * frame (int, optional): Clear callbacks for this frame. If
            default, clears callbacks for frames already rendered.
        """
        # Once added, a frame key should NEVER be deleted, even if it's
        # empty (so no `self.pop`). When the default key/value is initially
        # added, `dpg.set_frame_callback` is called creating setting a main
        # callback loop for that frame. If the key (frame) is re-created
        # for a frame that has not been rendered yet, another main loop will
        # be created for the same frame. Technically, it's safe to destroy
        # keys for frames already rendered, but why complicate things...?
        if frame is None:  # all previously-rendered frames
            current_frame = get_frame_count()
            for _, f in enumerate(self):
                if current_frame > f:
                    self[f].clear()
        else:                       
            self[frame].clear()

    def on_frame(self, callback: Callable = None, /, *, frame: int = ALL_FRAMES, user_data: Any = None, **kwargs):
        """(Decorator) Schedules a callback to run on a specific frame. 

        Args:
            * callback (Callable): Callable object to run.
            * frame (int, optional): The callback will run before this frame
            is rendered. If this value is 0, it will run every frame. If -1,
            it will run on the last frame (application exit). Defaults to 0.
            * user_data (Any, optional): This will be sent as the third positional
            argument to <callback>. Defaults to None.
        """
        def _on_frame(_callback):
            self[frame] = _callback, user_data, kwargs
            return _callback

        if callback is None:
            return _on_frame
        return _on_frame(callback)

    def __call__(self) -> None:
        # WIP for real-time render/event loop (Application._start)
        """Advances the update loop by one event..
        """
        updates = iter(self._updates)
        while True:
            try:
                next(updates)()
            except StopIteration:
                updates = iter(self._updates)
                continue
            yield None
