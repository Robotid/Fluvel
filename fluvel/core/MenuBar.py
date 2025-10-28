# fluvel.core.MenuBar
from typing import Callable, Any, Tuple, List, Optional, Literal
from functools import partial

# Fluvel
from fluvel.components.gui.FAction import FAction
from fluvel.components.widgets.FMenu import FMenu
from fluvel._user.GlobalConfig import AppConfig

# PySide6
from PySide6.QtWidgets import QMenuBar, QMainWindow

# Utils
from fluvel._user.MenuOptions import MenuOptions
from fluvel.core.tools.generate_menu_options import set_dynamic_menu_keys
from fluvel.utils.tip_helpers import ActionProperties, ActionTypes, StandardActionShortcut

class MenuBar(QMenuBar):
    """
    A high-level wrapper around :py:class:`PySide6.QtWidgets.QMenuBar` for Fluvel applications.

    This class simplifies the configuration of menu items by abstracting complex
    signal connections and property settings into simple, readable methods like 
    :py:meth:`bind`, :py:meth:`set_property`, and the centralized :py:meth:`config` method.

    The actual menu structure (menus, sub-menus, and actions) is built internally 
    by :py:class:`~fluvel.components.widgets.FMenu` based on content files.
    """

    def __init__(self, parent: QMainWindow, structure: dict):
        """
        Initializes the MenuBar and builds its structure.

        :param parent: The parent window, typically an :py:class:`~fluvel.core.AppWindow` instance.
        :type parent: :py:class:`PySide6.QtWidgets.QMainWindow`
        :param structure: A dictionary representing the hierarchical structure of the menu 
                          (loaded from a configuration file).
        :type structure: dict
        """
        super().__init__(parent)

        self.menu = FMenu(self, menu_structure=structure)
        
        # Generate the literal that contains all menu options
        if AppConfig.fluvel.DEV_MODE:
            set_dynamic_menu_keys(self.menu.all_menu_options)

    def get_item(self, item_name: str) -> FAction | FMenu:
        """
        Retrieves a menu item (either a menu or an action) by its string name.

        The item is accessed as an attribute of the :py:class:`MenuBar` instance.

        :param item_name: The name of the menu item (action or submenu) to retrieve.
        :type item_name: :py:class:`~fluvel._user.MenuOptions`
        :returns: The corresponding :py:class:`~fluvel.components.gui.FAction` or :py:class:`~fluvel.components.widgets.FMenu` object.
        :rtype: :py:class:`~fluvel.components.gui.FAction` or :py:class:`~fluvel.components.widgets.FMenu`
        """
        return getattr(self, item_name)
    
    def bind(
        self, menu_option: MenuOptions, action: ActionTypes, controller: Callable
    ) -> None:
        """
        Connects a controller (callback function) to a specific signal of a menu item.

        This is the low-level method used by all ``on_*`` and ``add_shortcut`` methods.

        :param menu_option: The name of the menu action.
        :type menu_option: :py:class:`~fluvel._user.MenuOptions`
        :param action: The name of the signal/action method to connect to (e.g., ``"triggered"``, ``"hovered"``).
        :type action: :py:class:`~fluvel.utils.tip_helpers.ActionTypes`
        :param controller: The callable function or method to execute when the action is fired.
        :type controller: :py:class:`typing.Callable`
        :rtype: None
        """
        menu_item = self.get_item(menu_option)
        getattr(menu_item, action).connect(controller)

    def set_property(
        self,
        menu_option: MenuOptions,
        property_to_change: ActionProperties,
        new_value: Any,
    ) -> None:
        """
        Sets a specific property (e.g., ``"Text"``, ``"Checked"``) for a menu item.

        The method constructs the appropriate setter method name (e.g., ``set + PropertyToChange``) 
        and calls it on the item.

        :param menu_option: The name of the menu action.
        :type menu_option: :py:class:`~fluvel._user.MenuOptions`
        :param property_to_change: The property to change (e.g., ``"Text"``, ``"Enabled"``).
        :type property_to_change: :py:class:`~fluvel.utils.tip_helpers.ActionProperties`
        :param new_value: The new value for the property.
        :type new_value: any
        :rtype: None
        """
        property_method = f"set{property_to_change}"
        menu_item = self.get_item(menu_option)
        getattr(menu_item, property_method)(new_value)
    
    def add_shortcut(
        self,
        menu_option: MenuOptions,
        new_shortcut: StandardActionShortcut,
        controller: Callable,
        *args,
        **kwargs
    ) -> None:
        """
        Assigns a keyboard shortcut and connects a controller to the action's ``triggered`` signal.

        :param menu_option: The name of the menu action.
        :type menu_option: :py:class:`~fluvel._user.MenuOptions`
        :param new_shortcut: The shortcut string (e.g., ``"Ctrl+S"``).
        :type new_shortcut: :py:class:`~fluvel.utils.tip_helpers.StandardActionShortcut`
        :param controller: The callable function or method to execute when the shortcut is used.
        :type controller: :py:class:`typing.Callable`
        :param args: Positional arguments to be passed to the controller.
        :param kwargs: Keyword arguments to be passed to the controller.
        :rtype: None
        """
        self.set_property(menu_option, "Shortcut", new_shortcut)

        command = partial(controller, *args, **kwargs)

        self.bind(menu_option, "triggered", command)

    def on_triggered(self, menu_option: MenuOptions, controller: Callable, *args, **kwargs) -> None:
        """
        Connects a controller to the action's ``triggered`` signal (when the item is clicked/activated).

        :param menu_option: The name of the menu action.
        :type menu_option: :py:class:`~fluvel._user.MenuOptions`
        :param controller: The callable function or method to execute.
        :type controller: :py:class:`typing.Callable`
        :param args: Positional arguments to be passed to the controller.
        :param kwargs: Keyword arguments to be passed to the controller.
        :rtype: None
        """
        command = partial(controller, *args, **kwargs)  

        self.bind(menu_option, "triggered", command)

    def on_hovered(self, menu_option: MenuOptions, controller: Callable, *args, **kwargs) -> None:
        """
        Connects a controller to the action's ``hovered`` signal (when the mouse moves over the item).

        :param menu_option: The name of the menu action.
        :type menu_option: :py:class:`~fluvel._user.MenuOptions`
        :param controller: The callable function or method to execute.
        :type controller: :py:class:`typing.Callable`
        :param args: Positional arguments to be passed to the controller.
        :param kwargs: Keyword arguments to be passed to the controller.
        :rtype: None
        """
        command = partial(controller, *args, **kwargs) if kwargs else partial(controller, *args)

        self.bind(menu_option, "hovered", command)

    def on_changed(self, menu_option: MenuOptions, controller: Callable, *args, **kwargs) -> None:
        """
        Connects a controller to the action's ``changed`` signal (typically used for checked/unchecked states).

        :param menu_option: The name of the menu action.
        :type menu_option: :py:class:`~fluvel._user.MenuOptions`
        :param controller: The callable function or method to execute.
        :type controller: :py:class:`typing.Callable`
        :param args: Positional arguments to be passed to the controller.
        :param kwargs: Keyword arguments to be passed to the controller.
        :rtype: None
        """

        command = partial(controller, *args, **kwargs)

        self.bind(menu_option, "changed", command)

    def config(
        self,
        properties: List[Tuple[MenuOptions, ActionProperties, MenuOptions]] | None = None,
        on_triggered: Optional[List[Tuple[MenuOptions, Callable, Any]]] = None,
        shortcuts: List[Tuple[MenuOptions, StandardActionShortcut, Callable, Any]] | None = None,
        on_hovered: List[Tuple[Literal[MenuOptions], Callable, Any]] | None= None,
        on_changed: List[Tuple[Literal[MenuOptions], Callable, Any]] | None = None
    ) -> None:
        """
        Provides a single, declarative interface to configure multiple properties, 
        shortcuts, and event handlers for the menu bar.

        All parameters accept a list of tuples, where each tuple defines the action 
        or binding for a specific menu item. This is the recommended high-level method 
        for menu configuration.

        :param properties: A list of tuples: ``(menu_option, property_to_set, new_value)`` to change item properties.
        :type properties: list[tuple[:py:class:`~fluvel._user.MenuOptions`, :py:class:`~fluvel.utils.tip_helpers.ActionProperties`, :py:class:`typing.Any`]]
        :param on_triggered: A list of tuples: ``(menu_option, controller_function, *args, **kwargs)`` to bind to the ``triggered`` signal.
        :type on_triggered: list[tuple[:py:class:`~fluvel._user.MenuOptions`, :py:class:`typing.Callable`, :py:class:`typing.Any`]]
        :param shortcuts: A list of tuples: ``(menu_option, shortcut_string, controller_function, *args, **kwargs)`` to assign a shortcut and bind the action.
        :type shortcuts: list[tuple[:py:class:`~fluvel._user.MenuOptions`, :py:class:`~fluvel.utils.tip_helpers.StandardActionShortcut`, :py:class:`typing.Callable`, :py:class:`typing.Any`]]
        :param on_hovered: A list of tuples to bind to the ``hovered`` signal.
        :type on_hovered: list[tuple[:py:class:`~fluvel._user.MenuOptions`, :py:class:`typing.Callable`, :py:class:`typing.Any`]]
        :param on_changed: A list of tuples to bind to the ``changed`` signal.
        :type on_changed: list[tuple[:py:class:`~fluvel._user.MenuOptions`, :py:class:`typing.Callable`, :py:class:`typing.Any`]]
        :rtype: None
        """
        if properties:
            for menu_option, new_property, new_value in properties:
                self.set_property(menu_option, new_property, new_value)

        if shortcuts:
            for menu_option, shortcut, function, *args in shortcuts:
                _args, _kwargs = self._get_config_arguments(args)
                self.add_shortcut(menu_option, shortcut, function, *_args, **_kwargs)

        if on_triggered:
            for menu_option, function, *args in on_triggered:
                _args, _kwargs = self._get_config_arguments(args)
                self.on_triggered(menu_option, function, *_args, **_kwargs)

        if on_hovered:
            for menu_option, function, *args in on_hovered:
                _args, _kwargs = self._get_config_arguments(args)
                self.on_hovered(menu_option, function, *_args, **_kwargs)

        if on_changed:
            for menu_option, function, *args in on_changed:
                _args, _kwargs = self._get_config_arguments(args)
                self.on_changed(menu_option, function, *_args, **_kwargs)

    @staticmethod
    def _get_config_arguments(args: tuple) -> tuple[list, dict[str, Any]]:
        """
        Internal static method to separate positional and keyword arguments 
        from a list passed by the :py:meth:`config` method.

        This method should not be called directly.
        """
        _args = [arg for arg in args if not isinstance(arg, dict)]
        try:
            _kwargs = args[len(_args)]
        except IndexError:
            _kwargs = {}

        return _args, _kwargs