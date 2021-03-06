from typing import Callable, Any
from dearpygui import dearpygui
from dearpypixl.itemtypes import *

##################################################
####### NOTE: This file is auto-generated. #######
##################################################

__all__ = [
    "NodeEditor",
    "Node",
    "NodeAttribute",
    "NodeLink",
]


class NodeEditor(Widget):
    """Adds a node editor.

        Args:
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * width (int, optional): Width of the item.
            * height (int, optional): Height of the item.
            * parent (int | str, optional): Parent to add this item to. (runtime adding)
            * before (int | str, optional): This item will be displayed before the specified item in the parent.
            * callback (Callable, optional): Registers a callback.
            * show (bool, optional): Attempt to render widget.
            * filter_key (str, optional): Used by filter widget.
            * delay_search (bool, optional): Delays searching container for specified items until the end of the app. Possible optimization when a container has many children that are not accessed often.
            * tracked (bool, optional): Scroll tracking
            * track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            * delink_callback (Callable, optional): Callback ran when a link is detached.
            * menubar (bool, optional): Shows or hides the menubar.
            * minimap (bool, optional): Shows or hides the minimap.
            * minimap_location (int, optional): mvNodeMiniMap_Location_* constants.
    """
    width            : int      = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    height           : int      = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    callback         : Callable = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    show             : bool     = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    filter_key       : str      = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    delay_search     : bool     = ItemProperty(INFORM, None, None)
    tracked          : bool     = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    track_offset     : float    = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    delink_callback  : Callable = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    menubar          : bool     = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    minimap          : bool     = ItemProperty(CONFIG, "get_item_config", "set_item_config")  # Needs testing
    minimap_location : int      = ItemProperty(CONFIG, "get_item_config", "set_item_config")  # Needs testing

    is_resized : bool           = ItemProperty(STATES, "get_item_state", None, target="resized")
    is_hovered : bool           = ItemProperty(STATES, "get_item_state", None, target="hovered")
    is_visible : bool           = ItemProperty(STATES, "get_item_state", None, target="visible")
    rect_size  : list[int, int] = ItemProperty(STATES, "get_item_state", None, target="rect_size")

    __itemtype_id__   : ItemIdType = ItemIdType(dearpygui.mvNodeEditor, "mvNodeEditor")
    __is_container__  : bool       = True
    __is_root_item__  : bool       = False
    __is_value_able__ : bool       = False
    __able_parents__  : tuple      = ()
    __able_children__ : tuple      = (dearpygui.mvMenuBar, dearpygui.mvNode, dearpygui.mvNodeLink, dearpygui.mvActivatedHandler, dearpygui.mvActiveHandler, dearpygui.mvClickedHandler, dearpygui.mvDeactivatedAfterEditHandler, dearpygui.mvDeactivatedHandler, dearpygui.mvEditedHandler, dearpygui.mvFocusHandler, dearpygui.mvHoverHandler, dearpygui.mvResizeHandler, dearpygui.mvToggledOpenHandler, dearpygui.mvVisibleHandler)
    __commands__      : tuple      = ('get_selected_nodes', 'get_selected_links', 'clear_selected_nodes', 'clear_selected_links')
    __command__       : Callable   = dearpygui.add_node_editor

    def __init__(
        self,
        label              : str       = None,
        user_data          : Any       = None,
        use_internal_label : bool      = True,
        width              : int       = 0,
        height             : int       = 0,
        parent             : int | str = 0,
        before             : int | str = 0,
        callback           : Callable  = None,
        show               : bool      = True,
        filter_key         : str       = '',
        delay_search       : bool      = False,
        tracked            : bool      = False,
        track_offset       : float     = 0.5,
        delink_callback    : Callable  = '',
        menubar            : bool      = False,
        **kwargs
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            width=width,
            height=height,
            parent=parent,
            before=before,
            callback=callback,
            show=show,
            filter_key=filter_key,
            delay_search=delay_search,
            tracked=tracked,
            track_offset=track_offset,
            delink_callback=delink_callback,
            menubar=menubar,
            **kwargs,
        )


class Node(Widget):
    """Adds a node to a node editor.

        Args:
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * parent (int | str, optional): Parent to add this item to. (runtime adding)
            * before (int | str, optional): This item will be displayed before the specified item in the parent.
            * payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            * drag_callback (Callable, optional): Registers a drag callback for drag and drop.
            * drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            * show (bool, optional): Attempt to render widget.
            * pos (list[int] | tuple[int, ...], optional): Places the item relative to window coordinates, [0,0] is top left.
            * filter_key (str, optional): Used by filter widget.
            * delay_search (bool, optional): Delays searching container for specified items until the end of the app. Possible optimization when a container has many children that are not accessed often.
            * tracked (bool, optional): Scroll tracking
            * track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            * draggable (bool, optional): Allow node to be draggable.
    """
    payload_type  : str                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    drag_callback : Callable                    = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    drop_callback : Callable                    = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    show          : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    pos           : list[int] | tuple[int, ...] = ItemProperty(CONFIG, "get_item_state", "set_item_config")
    filter_key    : str                         = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    delay_search  : bool                        = ItemProperty(INFORM, None, None)
    tracked       : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    track_offset  : float                       = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    draggable     : bool                        = ItemProperty(CONFIG, "get_item_config", "set_item_config")

    is_resized        : bool           = ItemProperty(STATES, "get_item_state", None, target="resized")
    is_middle_clicked : bool           = ItemProperty(STATES, "get_item_state", None, target="middle_clicked")
    is_right_clicked  : bool           = ItemProperty(STATES, "get_item_state", None, target="right_clicked")
    is_left_clicked   : bool           = ItemProperty(STATES, "get_item_state", None, target="left_clicked")
    is_hovered        : bool           = ItemProperty(STATES, "get_item_state", None, target="hovered")
    is_clicked        : bool           = ItemProperty(STATES, "get_item_state", None, target="clicked")
    is_visible        : bool           = ItemProperty(STATES, "get_item_state", None, target="visible")
    rect_size         : list[int, int] = ItemProperty(STATES, "get_item_state", None, target="rect_size")

    __itemtype_id__   : ItemIdType = ItemIdType(dearpygui.mvNode, "mvNode")
    __is_container__  : bool       = True
    __is_root_item__  : bool       = False
    __is_value_able__ : bool       = False
    __able_parents__  : tuple      = (dearpygui.mvTemplateRegistry, dearpygui.mvStage, dearpygui.mvNodeEditor)
    __able_children__ : tuple      = (dearpygui.mvNodeAttribute, dearpygui.mvActiveHandler, dearpygui.mvClickedHandler, dearpygui.mvHoverHandler, dearpygui.mvVisibleHandler, dearpygui.mvDragPayload)
    __command__       : Callable   = dearpygui.add_node

    def __init__(
        self,
        label              : str                         = None,
        user_data          : Any                         = None,
        use_internal_label : bool                        = True,
        parent             : int | str                   = 0,
        before             : int | str                   = 0,
        payload_type       : str                         = '$$DPG_PAYLOAD',
        drag_callback      : Callable                    = None,
        drop_callback      : Callable                    = None,
        show               : bool                        = True,
        pos                : list[int] | tuple[int, ...] = [],
        filter_key         : str                         = '',
        delay_search       : bool                        = False,
        tracked            : bool                        = False,
        track_offset       : float                       = 0.5,
        draggable          : bool                        = True,
        **kwargs
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            before=before,
            payload_type=payload_type,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            show=show,
            pos=pos,
            filter_key=filter_key,
            delay_search=delay_search,
            tracked=tracked,
            track_offset=track_offset,
            draggable=draggable,
            **kwargs,
        )


class NodeAttribute(Widget):
    """Adds a node attribute to a node.

        Args:
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * indent (int, optional): Offsets the widget to the right the specified number multiplied by the indent style.
            * parent (int | str, optional): Parent to add this item to. (runtime adding)
            * before (int | str, optional): This item will be displayed before the specified item in the parent.
            * show (bool, optional): Attempt to render widget.
            * filter_key (str, optional): Used by filter widget.
            * tracked (bool, optional): Scroll tracking
            * track_offset (float, optional): 0.0f:top, 0.5f:center, 1.0f:bottom
            * attribute_type (int, optional): mvNode_Attr_Input, mvNode_Attr_Output, or mvNode_Attr_Static.
            * shape (int, optional): Pin shape.
            * category (str, optional): Category
    """
    indent         : int   = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    show           : bool  = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    filter_key     : str   = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    tracked        : bool  = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    track_offset   : float = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    attribute_type : int   = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    shape          : int   = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    category       : str   = ItemProperty(CONFIG, "get_item_config", "set_item_config")

    is_hovered        : bool     = ItemProperty(STATES, "get_item_state", None, target="hovered")

    __itemtype_id__   : ItemIdType = ItemIdType(dearpygui.mvNodeAttribute, "mvNodeAttribute")
    __is_container__  : bool       = True
    __is_root_item__  : bool       = False
    __is_value_able__ : bool       = False
    __able_parents__  : tuple      = (dearpygui.mvTemplateRegistry, dearpygui.mvStage, dearpygui.mvNode)
    __able_children__ : tuple      = ()
    __constants__     : tuple      = ('mvNodeAttribute', 'mvNode_PinShape_Circle', 'mvNode_PinShape_CircleFilled', 'mvNode_PinShape_Triangle', 'mvNode_PinShape_TriangleFilled', 'mvNode_PinShape_Quad', 'mvNode_PinShape_QuadFilled', 'mvNode_Attr_Input', 'mvNode_Attr_Output', 'mvNode_Attr_Static')
    __command__       : Callable   = dearpygui.add_node_attribute

    def __init__(
        self,
        label              : str       = None,
        user_data          : Any       = None,
        use_internal_label : bool      = True,
        indent             : int       = -1,
        parent             : int | str = 0,
        before             : int | str = 0,
        show               : bool      = True,
        filter_key         : str       = '',
        tracked            : bool      = False,
        track_offset       : float     = 0.5,
        attribute_type     : int       = 0,
        shape              : int       = 1,
        category           : str       = 'general',
        **kwargs
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            indent=indent,
            parent=parent,
            before=before,
            show=show,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            attribute_type=attribute_type,
            shape=shape,
            category=category,
            **kwargs,
        )


class NodeLink(Widget):
    """Adds a node link between 2 node attributes.

        Args:
            * attr_1 (int | str):
            * attr_2 (int | str):
            * label (str, optional): Overrides 'name' as label.
            * user_data (Any, optional): User data for callbacks
            * use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            * tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            * parent (int | str, optional): Parent to add this item to. (runtime adding)
            * show (bool, optional): Attempt to render widget.
    """
    attr_1 : int | str = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    attr_2 : int | str = ItemProperty(CONFIG, "get_item_config", "set_item_config")
    show   : bool      = ItemProperty(CONFIG, "get_item_config", "set_item_config")

    is_hovered : bool = ItemProperty(STATES, "get_item_state", None, target="hovered")

    __itemtype_id__   : ItemIdType = ItemIdType(dearpygui.mvNodeLink, "mvNodeLink")
    __is_container__  : bool       = False
    __is_root_item__  : bool       = False
    __is_value_able__ : bool       = False
    __able_parents__  : tuple      = (dearpygui.mvTemplateRegistry, dearpygui.mvStage, dearpygui.mvNodeEditor)
    __able_children__ : tuple      = ()
    __command__       : Callable   = dearpygui.add_node_link

    def __init__(
        self,
        attr_1            : int | str,
        attr_2            : int | str,
        label             : str             = None,
        user_data         : Any             = None,
        use_internal_label: bool            = True,
        parent            : int | str       = 0,
        show              : bool            = True,
        **kwargs
    ) -> None:
        super().__init__(
            attr_1=attr_1,
            attr_2=attr_2,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            show=show,
            **kwargs,
        )
