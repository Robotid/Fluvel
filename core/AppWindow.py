# fluvel.core.AppWindow

from project import GlobalConfig
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QMenuBar
from core.MenuBar import MenuBar
from pathlib import Path

class AppWindow(QMainWindow, GlobalConfig):
    def __init__(self) -> None:
        super().__init__()

        # Inicializar UI
        self.__init_ui()

    def __init_ui(self) -> None:
        """
        This method performs the main configurations of the application's user interface window.
        """
        self.setWindowTitle(f"{self.app_name} - {self.version}")
        self.setGeometry(100, 100, self.window_width, self.window_height)

        # Configuring the layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.layout: QVBoxLayout = QVBoxLayout()
        central_widget.setLayout(self.layout)

        # Configuring the Top Menu Bar
        self.__set_menu_bar()

        # Display views
        self.setUpMainWindow()

    def __set_menu_bar(self) -> None:
        """
        **`IMPORTANT`** Este método se encarga de  
        """
        
        menu_file: Path = self.APP_ROOT / "views" / "menus" / "menu.fluml"

        # This is not an instance of QMenuBar
        self.menu_bar = MenuBar(parent = self, menu_file = menu_file)

        # Creating the full_menu_options.txt file
        if self.DEV_MODE:
            self.get_menu_bar_options()
    
    def get_menu_bar_options(self) -> None:
        """     
        This method generates the file `log_menu_options.txt` in the `project` folder.\n
        *The `full_menu_options.txt` file contains all the options in the MainWindow's menu bar and how to refer to them.*
        """

        full_options: str = f"""
        {"# "*64}
        # All menu bar options will be available as properties of the MenuBar class.                                                   #     
        # Try to choose different names for each to avoid overrides.\n                                                                       
        # You can (and should) integrate them into your workflow by setting their methods and properties from                          #   
        # the menu_bar property of the main window class using the core methods self.menu_bar.bind() and self.menu_bar.set_property(). #
        {"# "*64}\n\n"""

        file_path: str = "project/log_menu_options.txt"

        try:
            for menu, option in self.menu_bar.options.items():
                for option_name in option.keys():
                    full_options += f"{menu} -> {option_name}:\n\t self.menu_bar.options['{menu}']['{option_name}'] \n\t self.menu_bar.{option_name}\n\n"
                full_options += "\n"
            with open(f"{file_path}", "w") as f:
                f.writelines(full_options)
                print(f"The file with the menu options was generated successfully. Check '{file_path}'.")
        except Exception as e:
            print(f"An error has occurred: {e}")

    def set_layout(self) -> None:
        pass

    def setUpMainWindow(self) -> None: ...
 