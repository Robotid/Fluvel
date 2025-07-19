# fluvel.core.MenuBar

from PySide6.QtWidgets import QMenuBar, QMainWindow
from core.core_utils import load_file

class MenuBar():
    def __init__(self, parent: QMainWindow, menu_file: str):
        
        # the QMenuBar Widget
        self.menu_bar: QMenuBar = parent.menuBar()

        # Loading the MenuBar.toml file
        self.menu_info: dict = load_file(menu_file)

        # Decoding the menu info 
        self.decode_config_menu()

        self.options["file"]["quit"].triggered.connect(parent.close)

    def decode_config_menu(self):
        
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
                
                else:

                    set_sub_option = set_top_option.addAction(value)

                    sub_option.update({sub_menu: set_sub_option})
            
                option_dict.update({top_menu.lower(): sub_option})

            self.options.update(option_dict)

        print(self.options)


            
            





