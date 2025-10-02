from typing import TypedDict, Unpack

# Fluvel
from fluvel.core.MenuBar import MenuBar
from fluvel._user.GlobalConfig import AppConfig

# Fluvel Controllers
from fluvel.controllers.ContentHandler import ContentHandler
from fluvel.controllers.reload_ui import reload_ui

# Core Process
from fluvel.core.tools.core_process import configure_process

# PySide6
from PySide6.QtWidgets import QMainWindow, QStackedWidget
from PySide6.QtCore import Qt

# Utils
from fluvel.utils.tip_helpers import WindowFlags, WidgetAttributes, WindowStates

class AppWindowKwargs(TypedDict, total=False):

    title: str
    geometry: tuple | list
    size: tuple[int, int] | list
    fixed_size: tuple | list
    min_size: tuple | list
    max_size: tuple | list
    min_width: int
    min_height: int
    max_width: int
    max_height: int
    opacity: float
    show_mode: WindowStates
    flags: list[WindowFlags]
    attributes: list[WidgetAttributes]

class AppWindow(QMainWindow):

    _FLAGS = {
        "frameless": "FramelessWindowHint",
        "always-on-top": "WindowStaysOnTopHint",
        "always-on-bottom": "WindowStaysOnBottomHint",
        "title": "WindowTitleHint",
        "sys-menu": "WindowSystemMenuHint",
        "maximize-button": "WindowMaximizeButtonHint",
        "minimize-button": "WindowMinimizeButtonHint",
        "close-button": "WindowCloseButtonHint",
        "click-through": "WindowTransparentForInput",
    }

    _ATTRIBUTES = {
        "enable-hover": "WA_Hover",
        "opaque-paint-event": "WA_OpaquePaintEvent",
        "no-system-background": "WA_NoSystemBackground",
        "delete-on-close": "WA_DeleteOnClose",
        "styled-background": "WA_StyledBackground",
        "translucent-background": "WA_TranslucentBackground"
    }

    _MAPPING_METHODS = {
        "title": "setWindowTitle", 
        "geometry": "setGeometry",
        "size": "resize",
        "min_width": "setMinimumWidth",
        "min_height": "setMinimumHeight",
        "max_width": "setMaximumWidth",
        "max_height": "setMaximumHeight",
        "fixed_size": "setFixedSize",
        "min_size": "setMinimumSize",
        "max_size": "setMaximumSize",
        "opacity": "setWindowOpacity",
        "flags": "setWindowFlags",
        "show_mode": "setWindowState",
    }

    def __init__(self, root) -> None:
        super().__init__()

        # Saving the app instance of the FluvelApp
        self.root = root

        # Se configura con las especificaciones del archivo .toml
        self.configure(**vars(AppConfig.window))

        # Se inicializa y muestra UI
        self._init_core_ui()

    def configure(self, **kwargs: Unpack[AppWindowKwargs]) -> None:

        if "flags" in kwargs:
            previous_flag = Qt.WindowType.Window
            for flag in kwargs["flags"]:
                previous_flag = previous_flag | getattr(Qt.WindowType, self._FLAGS[flag])
            kwargs["flags"] = previous_flag

        if "show_mode" in kwargs:
            mode = getattr(Qt.WindowState, f"Window{kwargs["show_mode"]}")
            kwargs["show_mode"] = mode

        if "window_attributes" in kwargs:
            for attr in kwargs["window_attributes"]:
                attribute = getattr(Qt.WidgetAttribute, self._ATTRIBUTES[attr])
                self.setAttribute(attribute, True)
            kwargs.pop("window_attributes")
            
        configure_process(self, self._MAPPING_METHODS, **kwargs)

    # abstract method where the initial state is defined
    # of the UI via the -self.configure- method
    def init_ui(self) -> None: pass

    def _init_core_ui(self) -> None:
        """
        This method performs the core configurations of the application's user interface window.
        """

        # Configuring the layout
        self._set_central_widget()

        # Configuring the Top Menu Bar
        self._set_menu_bar()

        # Set initial configurations
        self.init_ui()

    def _set_menu_bar(self) -> None:
        """
        Este método inicializa el proceso para la creación del menú dinámico.
        """
        
        if menu := ContentHandler.MENU_CONTENT.get("main-menu", {}):
            
            # This is an instance of QMenuBar
            self.menu_bar = MenuBar(self, menu)

            # Adding the Menu Bar to the Window
            self.setMenuBar(self.menu_bar)

    def update_ui(self, router):
        """
        Método llamado por el hreloader para actualizar la interfaz.
        """

        reload_ui(self, router)
        
    def _set_central_widget(self) -> None:
        """
        Configuraciones iniciales del layout de la ventana principal.\n
        Por defecto se provee un QWidget() central para implementar los diseños.
        """

        self.central_widget = QStackedWidget()

        self.central_widget.setObjectName("central-widget")

        self.setCentralWidget(self.central_widget)
