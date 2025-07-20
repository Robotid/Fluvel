# fluvel.core.AppWindow

from project import GlobalConfig
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QMenuBar
from core.MenuBar import MenuBar

class AppWindow(QMainWindow, GlobalConfig):
    def __init__(self):
        super().__init__()

        # Inicializar UI
        self.init_ui()

    def init_ui(self):
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
        self.set_menu_bar()

        # Display Widgets
        self.setUpMainWindow()

    def set_menu_bar(self):
        """
        Este método 
        """
        # This is not an instance of QMenuBar
        self.menu_bar = MenuBar(parent=self, menu_file="MenuBar.toml")

        # Creating the full_menu_options.txt file
        self.get_menu_bar_options()
    
    def get_menu_bar_options(self):
        """     
        This method generates the file `full_menu_options.txt` in the `project` folder.\n
        *The `full_menu_options.txt` file contains all the options in the MainWindow´s menu bar and how to refer to them.*
        """

        full_options: str = f"""
        {"# "*64}
        # All menu bar options will be available as properties of the MenuBar class.                                                   #     
        # Try to choose different names for each to avoid overrides.\n                                                                       
        # You can (and should) integrate them into your workflow by setting their methods and properties from                          #   
        # the menu_bar property of the main window class using the core methods self.menu_bar.bind() and self.menu_bar.set_property(). #
        {"# "*64}\n                                                                                                                                     
There are two ways to reference menu bar options as attributes of self.menu_bar:\n"""

        file_path = "project/full_menu_options.txt"

        for key, option in self.menu_bar.options.items():
            for option_name in option.keys():
                full_options += f"{key} -> {option_name}:\n\t self.menu_bar.options['{key}']['{option_name}'] \n\t self.menu_bar.{key}\n\n"
            full_options += "\n"

        try:
            with open(f"{file_path}", "w") as f:
                f.writelines(full_options)
                print(f"The file with the menu options was generated successfully. Check '{file_path}'.")

        except Exception as e:
            print(f"Ha ocurrido un error: {e}")

    def set_layout(self):
        pass

    def setUpMainWindow(self):
        """ Display `components` in the Main Window. """
        ...
