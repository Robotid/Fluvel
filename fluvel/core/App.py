# Fluvel

from fluvel.controllers.main_controller import init_content
from fluvel._user.Config import AppConfig

# PySide6
from PySide6.QtWidgets import QApplication

# Utils
from .core_utils.theme_loader import load_style_sheet
from fluvel.utils.paths import THEMES_DIR


class App(QApplication):

    def __init__(self, argv: list) -> None:
        super().__init__(argv)

    def load(self, filename: str) -> None:
        """
        **IMPORTANT** Only supports TOML or JSON config files with the ***same*** configuration format.\n
        This method is responsible for loading the application's
        global configuration provided by a JSON or TOML file.\n
        *If you have or want to create a different configuration style (format),
        update the **`properties`** and the **`set_config_format()`** method of the **`project.AppConfig`** class.*
        """

        AppConfig.init_config(filename)

        # Se cargan los contenidos estáticos de la ui
        self.set_static_content()

    def set_static_content(self):
        """
        Este método gestiona la carga de contenido estático de la aplicación.\n
        El orden de implementación no debería ser un problema.
        """

        # Cargando el contenido de texto estático de las vistas
        self._set_content()

        # Aplicando los temas y estilos a los componentes
        self._set_theme()

    def _set_theme(self) -> None:
        """
        This method *loads* the *global theme* and *component styles* to be used in the application.
        """

        # Esto provee una apariencia consistente en todas las plataformas antes de aplicar los estilos QSS
        self.setStyle("Fusion")

        # Directorio donde se encuentran los archivos qss de los componentes
        theme_path = THEMES_DIR / AppConfig.ui.theme

        # Lista con los archivos .qss
        qss_files: list = theme_path.rglob("*.qss")

        # Contenido que se cargará a la ui
        qss_content: str = ""

        # Iterando y concatenando el contenido QSS de los archivos
        for qss_file in qss_files:
            qss_content += load_style_sheet(qss_file)

        # Cargando el tema a la ui
        self.setStyleSheet(qss_content)

    def change_theme(self, new_theme: str) -> None:
        """
        This method changes the entire `appearance` of the application dynamically at runtime or development time.
        Args:
            new_theme (str): the name of the theme that will be displayed.
        """
        # Change theme
        AppConfig.ui.theme = new_theme

        # Update theme
        self._set_theme()

    def _set_content(self) -> None:
        """
        This method *loads* all static `.fluml` text files according to the application language.
        """

        init_content(lang=AppConfig.ui.language)

    def change_language(self, new_language: str) -> None:

        # Change language
        AppConfig.ui.language = new_language
        
        # Update text content
        self._set_content()