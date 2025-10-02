import sys, importlib

# Fluvel
from fluvel.controllers.main_controller import init_content
from fluvel._user.GlobalConfig import AppConfig
from fluvel.core.Router import Router
from fluvel.controllers.ContentHandler import ContentHandler

# PySide6
from PySide6.QtWidgets import QApplication

# Exception Handler
from fluvel.core.exceptions.expect_handler import expect

class FluvelApp:

    def __init__(self, window_module_path: str | None = None, config_file: str = "appconfig.toml") -> None:
        
        # The instance of QApplication
        self._app = QApplication()
        
        # Start initial config
        self._load(config_file)

        # The instance of AppWindow(QMainWindow)
        self.main_window = self._create_main_window(window_module_path)

        # Start router config
        Router.init(self.main_window)

    def _load(self, filename: str) -> None:
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

    def _create_main_window(self, window_module_path: str | None):
        
        # The default is "window" if no alternative module defining AppWindow is provided.
        window_module_path = "window" if not window_module_path else window_module_path
        
        # Loading module
        window_module = importlib.import_module(window_module_path)

        # Return an instance of MainWindow(AppWindow)
        return window_module.MainWindow(self)

    def run(self) -> None:
        """
        Starts the application's event loop.
        """

        # Display window
        self.main_window.show()

        # Init mainloop
        sys.exit(self._app.exec())

    @expect.ErrorImportingModule(stop=True)
    def register(self, initial: str, views: list[str]) -> None:
        """
        Registra las vistas de la aplicación.
        
        :param initial: Nombre de la ruta de la vista inicial.
        :type initial: str
        :param views: Nombres de los módulos de las vistas.
        :type views: list[str]
        """
        # Importing view modules
        for view_name in views:
            importlib.import_module(view_name)

        # Show initial view
        Router.show(initial)
                
    def set_static_content(self) -> None:
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
        self._app.setStyle("Fusion")

        qss_content: str = ContentHandler.process_theme()

        # Cargando el tema a la ui
        self._app.setStyleSheet(qss_content)

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