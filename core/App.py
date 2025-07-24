# fluvel.core.App

from typing import Literal

# PySide6 - Fluvel
from project import GlobalConfig
from PySide6.QtWidgets import QApplication

# Utils
from core.core_utils.theme_loader import load_style_sheet, get_theme_path
from utils.helper_functions import filter_by_extension

AppThemes = Literal["bootstrap", "clean-light", "modern-dark", "modern-dark-esmerald"]

class App(QApplication, GlobalConfig):
    def __init__(self, argv: list) -> None:
        super().__init__(argv)

    def load(self, filename: str) -> None:
        """
        **IMPORTANT** Only supports TOML or JSON config files with the ***same*** configuration format.\n
        This method is responsible for loading the application's
        global configuration provided by a JSON or TOML file.\n
        *If you have or want to create a different configuration style (format),
        update the **`properties`** and the **`set_config_format()`** method of the **`project.GlobalConfig`** class.*
        """

        # Se aplican los atributos globales del proyecto
        self.set_config_format(filename)

        # Aplicando los temas y estilos a los componentes
        self.set_theme()

    def set_theme(self) -> None:
        """
        This method *loads* the *global theme* and *component styles* to be used in the application.
        """

        # Esto provee una apariencia consistente en todas las plataformas antes de aplicar los estilos QSS
        self.setStyle("Fusion")

        # Directorio donde se encuentran los archivos qss de los componentes
        theme_path = get_theme_path(self.theme)

        # Lista con los archivos .qss
        qss_files: list = filter_by_extension(theme_path, ".qss")

        # Contenido que se cargará a la app
        qss_content: str = ""

        # Iterando y concatenando el contenido QSS de los archivos
        for qss_file in qss_files:
            qss_content += load_style_sheet(qss_file)

        # Cargando el tema a la app
        self.setStyleSheet(qss_content)
    
    def change_theme(self, new_theme: AppThemes):
        """
        This method changes the entire `appearance` of the application dynamically at runtime or development time.
        """
        self.theme = new_theme

        self.set_theme()