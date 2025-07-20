# fluvel.core.MenuBar

from PySide6.QtWidgets import QMenuBar, QMainWindow
from core.core_utils import load_file
from typing import Literal
from core.core_utils.generate_menu_options import get_dynamic_menu_keys
from project.MenuOptions import MenuOptions

ActionTypes = Literal["triggered", "toggled", "changed", "hovered"]

ActionProperties = Literal["text", "icon", "shortcut", "statusTip",
                           "toolTip", "enabled", "visible", "checkable",
                           "menuRole", "data"]

class MenuBar:
    def __init__(self, parent: QMainWindow, menu_file: str):

        # the QMenuBar Widget
        self.menu_bar: QMenuBar = parent.menuBar()

        # Loading the MenuBar.toml file
        self.menu_info: dict = load_file(menu_file)

        # Decoding the menu info
        self.decode_config_menu()

    def decode_config_menu(self):

        all_menu_options = []

        self.options = {}

        option_dict = {}

        for top_menu, medium_menu in self.menu_info.items():

            set_top_option = self.menu_bar.addMenu(top_menu)

            sub_option = {}

            for sub_menu, value in medium_menu.items():

                if isinstance(value, dict):

                    set_top_option.addSeparator() # Añadiendo separador

                    for sub, val in value.items():

                        set_sub_option = set_top_option.addAction(val)

                        sub_option.update({sub: set_sub_option})

                        all_menu_options.append(sub)

                        setattr(self, sub, set_sub_option)

                else:

                    set_sub_option = set_top_option.addAction(value)

                    sub_option.update({sub_menu: set_sub_option})

                    all_menu_options.append(sub_menu)

                    setattr(self, sub_menu, set_sub_option)

                option_dict.update({top_menu.lower(): sub_option})

            self.options.update(option_dict)

            # Para el Literal
            get_dynamic_menu_keys(all_menu_options)

    def bind(self, menu_option: MenuOptions, action: ActionTypes, controller):

        getattr(getattr(self, menu_option), action).connect(controller)

    def set_property(self, menu_option: MenuOptions, property_to_change: ActionProperties, new_property):
        
        property_method = f"set{property_to_change.capitalize()}"

        getattr(getattr(self, menu_option), f"{property_method}")(new_property)







