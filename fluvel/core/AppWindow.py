# fluvel.core.AppWindow

from pathlib import Path
from abc import abstractmethod

# Fluvel
from project import GlobalConfig
from core import App
from core.MenuBar import MenuBar

# PySide6 
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout

# Utils
from utils.paths import CONTENT_DIR

class AppWindow(QMainWindow, GlobalConfig):
    def __init__(self, root: App) -> None:
        super().__init__()

        # Saving the app instance of the QApplication/App()
        self.root = root

        # Inicializar UI
        self._init_ui()

    def _init_ui(self) -> None:
        """
        This method performs the main configurations of the application's user interface window.
        """

        self.setWindowTitle(f"{self.app_name} - {self.version}")
        self.setGeometry(100, 100, self.window_width, self.window_height)

        # Configuring the layout
        self.set_layout()

        # Configuring the Top Menu Bar
        self.set_menu_bar()

        # Display views
        self.setUpMainWindow()

    def set_menu_bar(self) -> None:
        """
        **`IMPORTANT`** Este método inicializa el proceso para la creación del menú dinámico
        """

        menu_file: Path = CONTENT_DIR / self.language / "menus" / "menu.fluml"

        # This is not an instance of QMenuBar
        self.menu_bar = MenuBar(parent = self, menu_file = menu_file)

        # Creating the full_menu_options.txt file
        if self.DEV_MODE:
            self.set_menu_bar_options()
    
    def set_menu_bar_options(self) -> None:
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
        """
        Configuraciones iniciales del layout de la ventana principal.\n
        Por defecto se provee un QWidget() central para implementar los diseños.
        """

        self.central_widget = QWidget()

        self.central_widget.setObjectName("central-widget")

        self.setCentralWidget(self.central_widget)
    
    def config(self, **kwargs) -> None: ...

    def setUpMainWindow(self) -> None: ...
