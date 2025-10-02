# fluvel.core.MenuBar
from typing import Callable, Any, Tuple, List, Optional, Dict, Literal
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

    def __init__(self, parent: QMainWindow, structure: dict):
        super().__init__(parent)

        # The names of all menu options will be added to this list.
        self.all_menu_options: list = []

        self.menu = FMenu(self, menu_structure=structure)
        
        # Generate the literal that contains all menu options
        if AppConfig.fluvel.DEV_MODE:
            set_dynamic_menu_keys(self.menu.all_menu_options)

    def get_item(self, item_name: str) -> FAction | FMenu:
        return getattr(self, item_name)
    
    def bind(
        self, menu_option: MenuOptions, action: ActionTypes, controller: Callable
    ) -> None:
        """
        Args:
            menu_option (str): Option of the Menu Bar
            action (str): Type of action method
            controller (any): Some controller that responds to the action
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
        Args:
            menu_option (str): Option of the Menu Bar.
            property_to_change (str): Property that will be changed.
            new_value (any): The new value of the property.
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
        Args:
            menu_option (str): Option of the Menu Bar.
            new_shortcut (str): The new shortcut that will be assigned.
            controller (any): Some controller that responds to the action.
        """
        self.set_property(menu_option, "Shortcut", new_shortcut)

        command = partial(controller, *args, **kwargs)

        self.bind(menu_option, "triggered", command)

    def on_triggered(self, menu_option: MenuOptions, controller: Callable, *args, **kwargs) -> None:

        command = partial(controller, *args, **kwargs)  

        self.bind(menu_option, "triggered", command)

    def on_hovered(self, menu_option: MenuOptions, controller: Callable, *args, **kwargs) -> None:

        command = partial(controller, *args, **kwargs) if kwargs else partial(controller, *args)

        self.bind(menu_option, "hovered", command)

    def on_changed(self, menu_option: MenuOptions, controller: Callable, *args, **kwargs) -> None:

        command = partial(controller, *args, **kwargs)

        self.bind(menu_option, "changed", command)

    def config(
    self,
    properties: List[Tuple[MenuOptions, ActionProperties, MenuOptions]] | None = None,
    on_triggered: Optional[List[Tuple[MenuOptions, Callable, Any]]] = None,
    shortcuts: List[Tuple[MenuOptions, StandardActionShortcut, Callable, Any]] | None = None,
    on_hovered: List[Tuple[Literal[MenuOptions], Callable, Any]] | None= None,
    ) -> None:

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

    @staticmethod
    def _get_config_arguments(args: tuple) -> tuple[list, dict[str, Any]]:

        _args = [arg for arg in args if not isinstance(arg, dict)]

        try:
            _kwargs = args[len(_args)]
        except IndexError:
            _kwargs = {}

        return _args, _kwargs