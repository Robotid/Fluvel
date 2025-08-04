# fluvel.core.App

from typing import Literal

# Fluvel
from project import GlobalConfig
from models import GlobalContent

# PySide6
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Slot

# Utils
from core.core_utils.theme_loader import load_style_sheet
from utils.helper_functions import filter_by_extension
from utils.paths import THEMES_DIR, CONTENT_DIR

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

        # Se cargan los contenidos estáticos de la app
        self.set_static_content()

    def set_static_content(self):
        """
        Este método gestiona la carga de contenido estático de la aplicación.\n
        El orden de implementación no debería ser un problema.
        """

        # Cargando el contenido de texto estático de las vistas
        self.set_text_blocks()

        # Aplicando los temas y estilos a los componentes
        self.set_theme()

    def set_theme(self) -> None:
        """
        This method *loads* the *global theme* and *component styles* to be used in the application.
        """

        # Esto provee una apariencia consistente en todas las plataformas antes de aplicar los estilos QSS
        self.setStyle("Fusion")

        # Directorio donde se encuentran los archivos qss de los componentes
        theme_path = THEMES_DIR / self.theme

        # Lista con los archivos .qss
        qss_files: list = filter_by_extension(theme_path, ".qss")

        # Contenido que se cargará a la app
        qss_content: str = ""

        # Iterando y concatenando el contenido QSS de los archivos
        for qss_file in qss_files:
            qss_content += load_style_sheet(qss_file)

        # Cargando el tema a la app
        self.setStyleSheet(qss_content)
    
    def change_theme(self, new_theme: AppThemes) -> None:
        """
        This method changes the entire `appearance` of the application dynamically at runtime or development time.
        Args:
            new_theme (str): the name of the theme that will be displayed.
        """
        self.theme = new_theme

        self.set_theme()
    
    def set_text_blocks(self) -> None:
        """
        This method *loads* all static `.fluml` text files according to the application language.
        """

        content_folder = CONTENT_DIR / self.language

        GlobalContent.initialize(content_folder)
    
    def change_language(self, new_language: str) -> None:
        
        self.language = new_language

        self.set_text_blocks()
    
    def update_ui(self) -> None:
        ...