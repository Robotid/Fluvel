# project.GlobalConfig

from core.core_utils import load_app_config, APP_ROOT, get_default_config

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
        - self.theme: str -> Global theme of the app from appconfig['app']['theme'].\n
    Global Database Properties:\n
        - self.db_host: str -> Saves the host of the DB from appconfig['database']['host'].\n
        - self.db_port: int -> Saves the port of the DB from appconfig['database']['port'].\n
        - self.db_user: str -> Saves the user of the DB from appconfig['database']['user'].\n
        - self.db_password: any -> -> Saves the password of the DB from appconfig['database']['password']\n
    """

    # Fluvel's Global Configuration Hierarchy
    # ┌──────────────────┐   ┌───────────────────┐   ┌────────────────────┐
    # │ QMainWindow()    │   │ GlobalConfig()    │   │ QApplication()     │
    # └────────┬─────────┘   └────────┬──────────┘   └────────┬───────────┘
    #          │                      │                       │
    #          │                      │                       │
    #          └────────┬─────────────┴──────────────┬────────┘
    #                   │                            │
    #        ┌──────────▼────────────┐    ┌──────────▼─────────┐
    #        │    AppWindow()        │    │      App()         │
    #        └──────────┬────────────┘    └────────────────────┘
    #                   │
    #                   ▼
    #         ┌─────────────────────┐
    #         │   MainWindow()      │
    #         └─────────────────────┘

    # [core utils]
    APP_ROOT: str = APP_ROOT

    # [appconfig]
    appconfig: dict

    # [app]
    app_name: str
    version: str
    window_width: int
    window_height: int
    theme: str

    # [database]
    db_host: str
    db_port: int
    db_user: str
    db_password: any

    # [defaults]
    default_icon: str

    def set_config_format(self, filename: str):
        """
        **IMPORTANT** This method loads the configuration from the **`appconfig`** 
        file TOML or JSON and defines the project's global attributes.
        The application configuration **`appconfig`** is stored in the ***`self.appconfig: dict`*** property of the **`GlobalConfig`** Class.\n
        """

        # Obtaining information from the TOML or JSON configuration file
        appconfig: dict = load_app_config(filename)

        # the global configuration dictionary is saved
        GlobalConfig.appconfig: dict = appconfig

        # Configuring the global properties
        app = appconfig.get("app", {})
        window_size = appconfig.get("window_size", {})

        GlobalConfig.app_name = app["app_name"]
        GlobalConfig.version = app["version"]
        GlobalConfig.window_width = window_size["width"]
        GlobalConfig.window_height = window_size["height"]
        GlobalConfig.theme = app["theme"]

        # Database config
        database = appconfig["database"]

        GlobalConfig.db_host = database["host"]
        GlobalConfig.db_port = database["port"]
        GlobalConfig.db_user = database["user"]
        GlobalConfig.db_password = database["password"]