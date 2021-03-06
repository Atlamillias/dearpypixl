import datetime
import os

from dearpypixl import Application, Viewport
from dearpypixl.containers import Window, ChildWindow, Group, TreeNode
from dearpypixl.basic import Text
from dearpypixl.misc import Separator
from dearpypixl.constants import Key, Mouse
from dearpypixl.itemtypes import Item, AppEvents





class AppInfo(ChildWindow):
    keys_down = []
    mice_down = []
    _info = (
        "Runtime",
        "Frames (all)",
        "Frames (/s)",
    )
    _mouse_poll = (
        "Cursor pos",
        "Up (previous)",
        "Down (previous)"
        "Down (current)",
    )
    _key_poll = (
        ""
    )
    __itemtype_id__ = None

    def __init__(self):
        super().__init__(
            autosize_x=True,
            parent=Window(label="AppInfo", width=400, height=500)
        )
        self.App = Application()
        self.Vp = Viewport()
        self.appevents = AppEvents()
        self.AppInfo = Group(parent=self, horizontal=True, theme=True, events=True)
        # appinfo
        self.pid = None
        self.runtime = None
        self.frames_all = None
        self.frames_per_sec = None
        # mouse
        self.mouse_pos = None
        self.mouse_drag_delta_now = None
        self.mouse_down_now = None
        self.mouse_up_prev = None
        self.mouse_whl_prev = None
        # keyboard
        self.key_down_now = None
        self.key_up_prev = None

        self._main_setup()

    def _main_setup(self):
        with self:
            # appinfo
            with self.AppInfo:
                with Group():
                    Text("Process ID")
                    Text("Runtime")
                    Text("Frames (all)")
                    Text("Frames (/s)")
                    Separator()
                    Text("Position")
                    Text("Drag delta")
                    Text("Down (current)")
                    Text("Up (previous)")
                    Text("Scroll (previous)")
                    Separator()
                    Text("Down (current)")
                    Text("Up (previous)")
                with Group():
                    self.pid = Text(f":    {os.getpid()}", color=[150, 150, 150])
                    self.runtime = Text(":", color=[150, 150, 150])
                    self.frames_all = Text(":", color=[150, 150, 150])
                    self.frames_per_sec = Text(":", color=[150, 150, 150])
                    Separator()
                    self.mouse_pos = Text(":", color=[150, 150, 150])
                    self.mouse_drag_delta_now = Text(
                        ":", color=[150, 150, 150])
                    self.mouse_down_now = Text(":", color=[150, 150, 150])
                    self.mouse_up_prev = Text(":", color=[150, 150, 150])
                    self.mouse_whl_prev = Text(":", color=[150, 150, 150])
                    Separator()
                    self.key_down_now = Text(":", color=[150, 150, 150])
                    self.key_up_prev = Text(":", color=[150, 150, 150])

            @self.App.on_render
            def update_render_info():
                # AppInfo
                self.runtime.value = f":    {datetime.timedelta(seconds=self.App.runtime())}"
                self.frames_all.value = f":    {self.App.frames()}"
                self.frames_per_sec.value = f":    {self.App.framerate()}"
                # Mouse
                x, y = self.Vp.local_mouse_pos
                self.mouse_pos.value = f":    {x}, {y}"

            @self.appevents.on_key_press(key=Key.ANY.value)
            def update_on_keypress(sender, sender_data, user_data):
                if sender_data not in self.keys_down:
                    self.keys_down.append(sender_data)
                set_key_down_value()

            @self.appevents.on_key_up(key=Key.ANY.value)
            def update_on_keyup_info(sender, sender_data, user_data):
                self.keys_down.remove(sender_data)
                self.key_up_prev.value = f":    {Key(sender_data).name}"
                set_key_down_value()

            def set_key_down_value():
                key_str = f":    "
                key_str += " + ".join(
                    (f"{Key(k).name}" for k in self.keys_down)).rstrip(" + ")
                self.key_down_now.value = key_str

            @self.appevents.on_mouse_button_click(button=Mouse.ANY.value)
            def update_mouse_click(sender, sender_data, user_data):
                if sender_data not in self.mice_down:
                    self.mice_down.append(sender_data)
                self.mouse_drag_delta_now.value = f":    0, 0"
                set_mouse_click_value()

            @self.appevents.on_mouse_button_up(button=Mouse.ANY.value)
            def update_mouse_up(sender, sender_data, user_data):
                self.mice_down.remove(sender_data)
                self.mouse_up_prev.value = f":    {Mouse(sender_data).name}"
                set_mouse_click_value()

            def set_mouse_click_value():
                mouse_str = f":    "
                mouse_str += " + ".join(
                    (f"{Mouse(b).name}" for b in self.mice_down)).rstrip(" + ")
                self.mouse_down_now.value = mouse_str

            @self.appevents.on_mouse_wheel_scroll
            def update_mouse_scroll(sender, sender_data, user_data):
                self.mouse_whl_prev.value = f":    {sender_data}"

            @self.appevents.on_mouse_drag
            def update_mouse_drag(sender, sender_data):
                self.mouse_drag_delta_now.value = f":    {sender_data[1]}, {sender_data[2]}"
