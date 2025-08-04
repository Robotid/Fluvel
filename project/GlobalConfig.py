# project.GlobalConfig

from core.core_utils import load_app_config, APP_ROOT

class GlobalConfig:
    """
    **IMPORTANT** Adapt the attributes of the **`GlobalConfig`** class and the ***`project.GlobalConfig.set_config_format()`*** 
    method according to the configuration style you prefer/use in your project.\n
    *To view your project's global variables, use "**`fluvel show-globals`**" in the **CLI***.\n
    Global Main Properties:\n
        - self.APP_ROOT: str -> Contains the absolute path to the main project folder.\n
        - self.appconfig: dict -> Saves the provided application settings.\n
        - self.app_name: str -> Saves the name of the app from appconfig['app']['app_name'].\n
        - self.version: str -> Saves the version of the app from appconfig['app']['version'].\n
        - self.window_width: str -> Saves the width of the window from appconfig['window_size']['width'].\n
        - self.window_height: str -> Saves the height of the window from appconfig['window_size']['height'].\n
        - self.theme: str -> Global ui theme of the app from appconfig['app']['theme'].\n
        - self.lang: str -> Global ui language of the app from appconfig['app']['lang'].\n
    Global Database Properties:\n
        - self.db_host: str -> Saves the host of the DB from appconfig['database']['host'].\n
        - self.db_port: int -> Saves the port of the DB from appconfig['database']['port'].\n
        - self.db_user: str -> Saves the user of the DB from appconfig['database']['user'].\n
        - self.db_password: any -> Saves the password of the DB from appconfig['database']['password']\n
    """

    # [core utils]
    APP_ROOT = APP_ROOT
    DEV_MODE: bool

    # [appconfig]
    CONFIG: dict
    
    # Your customization 
    # starts here
    # │
    # ▼

    # [app]
    app_name: str
    version: str
    window_width: int
    window_height: int
    theme: str
    language: str

    # [database]
    db_host: str
    db_port: int
    db_user: str
    db_password: any

    # [defaults]
    default_icon: str

    def set_config_format(self, filename: str) -> None:
        """
        **IMPORTANT** This method loads the configuration from the **`appconfig`** 
        file TOML or JSON and defines the project's global attributes.
        The application configuration **`appconfig`** is stored in the ***`self.appconfig: dict`*** property of the **`GlobalConfig`** Class.\n
        """

        # Obtaining information from the TOML or JSON configuration file
        appconfig: dict = load_app_config(filename, {})

        GlobalConfig.DEV_MODE = appconfig.get("DEV_MODE", True)

        # the global configuration dictionary is saved
        GlobalConfig.CONFIG = appconfig

        # Configuring the global properties
        app: dict = appconfig.get("app", {})
        window_size: dict = appconfig.get("window_size", {})

        GlobalConfig.app_name = app.get("app_name", "-")
        GlobalConfig.version = app.get("version", "-")
        GlobalConfig.window_width = window_size.get("width", 640)
        GlobalConfig.window_height = window_size.get("height", 480)
        GlobalConfig.theme = app.get("theme", "bootstrap")
        GlobalConfig.language = app.get("language", "en")

        # Database config
        database: dict = appconfig.get("database", {})

        GlobalConfig.db_host = database.get("host", "-")
        GlobalConfig.db_port = database.get("port", "-")
        GlobalConfig.db_user = database.get("user", "-")
        GlobalConfig.db_password = database.get("password", "-")