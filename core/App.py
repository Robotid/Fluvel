# fluvel.core.App

from core.GlobalConfig import GlobalConfig
from PySide6.QtWidgets import QApplication
from core.core_utils.config_loader import load_app_config
from core.core_utils.theme_loader import load_style_sheet

class App(QApplication, GlobalConfig):
    def __init__(self, argv: list):
        """
        Global Main Properties:\n
            - self.config: dict -> Saves the provided application settings.\n
            - self.app_name: str -> Saves the name of the app from appconfig['app']['app_name'].\n
            - self.version: str -> Saves the version of the app from appconfig['app']['version'].\n
            - self.window_width: str -> Saves the width of the window from appconfig['window_size']['width'].\n
            - self.window_height: str -> Saves the height of the window from appconfig['window_size']['height'].\n
            - self.theme: str -> Global theme of the app from appconfig['app']['theme'].\n
        Global Database Properties:\n
            - self.db_host: str -> Saves the host of the DB from appconfig['database']['host'].\n
            - self.db_port: int -> Saves the port of the DB from appconfig['database']['port'].\n
            - self.db_user: str -> Saves the user of the DB from appconfig['database']['user'].\n
            - self.db_password: any -> -> Saves the password of the DB from appconfig['database']['password']\n
        """
        super().__init__(argv)
        
    def load(self, filename: str):
        """ 
        **IMPORTANT** Only supports TOML or JSON config files with the ***same*** configuration format.\n
        This method is responsible for loading the application's 
        global configuration provided by a JSON or TOML file.\n
        *If you have or want to create a different configuration style (format), 
        update the **`set_config_format()`** method of the **`fluvel.core.App`** class.*
        """

        # Se aplican los atributos globales del proyecto
        self.set_config_format(filename)

        # Aplicando los temas y estilos a los componentes
        self.set_theme()    
    
    def set_theme(self):
        """
        This method *loads* the *global theme* and *component styles* to be used in the application.
        """
        label_content = load_style_sheet("Label.qss", self.theme)
        push_button_content = load_style_sheet("PushButton.qss", self.theme)
        check_button_content = load_style_sheet("CheckButton.qss", self.theme)
        full_content = f"{label_content}{push_button_content}{check_button_content}"
        self.setStyleSheet(full_content)

    def set_config_format(self, filename: str) -> dict:
        """
        **IMPORTANT** This method loads the configuration from the **`appconfig`** 
        file TOML or JSON and defines the project's global attributes.
        The application configuration **`appconfig`** is stored in the ***`self.config: dict`*** property of the **`GlobalConfig`** Class.\n
        """

        # Obteniendo la información del archivo de configuración TOML o JSON
        appconfig = load_app_config(filename)

        # the global configuration dictionary is saved
        GlobalConfig.appconfig = appconfig

        # Configuring the global properties
        app = appconfig.get("app", {})
        window_size = appconfig.get("window_size", {})

        GlobalConfig.app_name = app.get("app_name", "UnknownApp")
        GlobalConfig.version = app.get("version", "N/A")
        GlobalConfig.window_width = window_size.get("width", 480)
        GlobalConfig.window_height = window_size.get("height", 640)
        GlobalConfig.theme = app.get("theme", "modern-dark")

        # Database config
        database = appconfig.get("database", {})
        GlobalConfig.db_host = database.get("host", "localhost")
        GlobalConfig.db_port = database.get("port", 5432)
        GlobalConfig.db_user = database.get("user", "admin")
        GlobalConfig.db_password = database.get("password", "a very powerful password")