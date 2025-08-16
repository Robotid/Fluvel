# fluvel.core.App

from typing import Literal

# Fluvel
from fluvel.models import GlobalContent

# PySide6
from PySide6.QtWidgets import QApplication

# Utils
from .core_utils.theme_loader import load_style_sheet
from fluvel.utils.helper_functions import filter_by_extension
from fluvel.utils.paths import THEMES_DIR, CONTENT_DIR

AppThemes = Literal["bootstrap", "modern-dark", "clean-light"]


class App(QApplication):

    def __init__(self, argv: list) -> None:
        super().__init__(argv)

        # Variable de tipo GlobalConfig que
        # almacenará la configuración global de la app
        self.config = None

    def load(self, config_instance: any) -> None:
        """
        **IMPORTANT** Only supports TOML or JSON config files with the ***same*** configuration format.\n
        This method is responsible for loading the application's
        global configuration provided by a JSON or TOML file.\n
        *If you have or want to create a different configuration style (format),
        update the **`properties`** and the **`set_config_format()`** method of the **`project.GlobalConfig`** class.*
        """

        self.config = config_instance

        # Se cargan los contenidos estáticos de la app
        self.set_static_content()

    def set_static_content(self):
        """
        Este método gestiona la carga de contenido estático de la aplicación.\n
        El orden de implementación no debería ser un problema.
        """

        # Cargando el contenido de texto estático de las vistas
        self.set_static_text_blocks()

        # Aplicando los temas y estilos a los componentes
        self.set_theme()

    def set_theme(self) -> None:
        """
        This method *loads* the *global theme* and *component styles* to be used in the application.
        """

        # Esto provee una apariencia consistente en todas las plataformas antes de aplicar los estilos QSS
        self.setStyle("Fusion")

        # Directorio donde se encuentran los archivos qss de los componentes
        theme_path = THEMES_DIR / self.config.theme

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
        # Change theme
        self.config.theme = new_theme

        # Update app
        self.set_theme()

    def set_static_text_blocks(self) -> None:
        """
        This method *loads* all static `.fluml` text files according to the application language.
        """

        content_folder = CONTENT_DIR / self.config.language

        GlobalContent.initialize(content_folder)

    def change_language(self, new_language: str) -> None:

        self.config.language = new_language

        self.config.CONFIG["app"]["language"] = new_language

        self.set_static_text_blocks()

        self.config.set_config_format(self.config.CONFIG)
