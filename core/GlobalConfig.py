# fluvel.core.GlobalConfig

class GlobalConfig:
    """
    **IMPORTANT** Adapt the attributes of this class and the ***`fluvel.core.App.set_config_format()`*** 
    method according to the configuration style you prefer/use in your project.\n
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

    # Fluvel's main class hierarchy
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

    # Configuring the global properties
    appconfig: dict

    # Main info of the App
    app_name: str
    version: str
    window_width: int
    window_height: int
    theme: str

    # Database info
    db_host: str
    db_port: int
    db_user: str
    db_password: any

    # Default paths
    default_icon: str
