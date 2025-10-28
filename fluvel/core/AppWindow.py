from typing import TypedDict, Unpack, Tuple, List

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
    """
    Specifies the optional keyword arguments used to configure the main application window.
    """
    
    title       : str
    geometry    : Tuple[int, int, int, int] | List[int]
    size        : Tuple[int, int] | List[int]
    resizable   : bool
    min_size    : Tuple[int, int] | List[int]
    max_size    : Tuple[int, int] | List[int]
    min_width   : int
    min_height  : int
    max_width   : int
    max_height  : int
    opacity     : float
    show_mode   : WindowStates
    flags       : List[WindowFlags]
    attributes  : List[WidgetAttributes]

class AppWindow(QMainWindow):
    """
    The main window container for a Fluvel application.

    This class serves as the top-level "shell" for the entire user interface.
    It inherits from :py:class:`PySide6.QtWidgets.QMainWindow` and is responsible for
    managing core UI elements like the central widget area (a :py:class:`QStackedWidget`
    for the Router), the menu bar, and the overall window properties.

    The primary way to use this class is to subclass it in your project.

    :ivar root: The parent :py:class:`~fluvel.core.FluvelApp.FluvelApp` instance.
    :type root: :py:class:`~fluvel.core.FluvelApp.FluvelApp`

    **Example of Subclassing:**

    .. code-block:: python

        # In your project's window.py
        from fluvel.core import AppWindow, Router

        class MainWindow(AppWindow):
            def init_ui(self) -> None:
                \"\"\"
                This method is called after the core UI is initialized.
                It's the perfect place for initial setup.
                \"\"\"
                # Configure window properties
                self.configure(title="My First Fluvel App", size=[1024, 768])

                # Configure menu bar actions
                if self.menu_bar:
                    self.menu_bar.config(
                        on_triggered=[
                            ("quit", self.close),
                            ("about", lambda: Router.show("about_page"))
                        ]
                    )
    """

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
        "resizable": "setFixedSize",
        "min_width": "setMinimumWidth",
        "min_height": "setMinimumHeight",
        "max_width": "setMaximumWidth",
        "max_height": "setMaximumHeight",
        "min_size": "setMinimumSize",
        "max_size": "setMaximumSize",
        "opacity": "setWindowOpacity",
        "flags": "setWindowFlags",
        "show_mode": "setWindowState",
    }

    def __init__(self, root) -> None:
        """
        Initializes the AppWindow.

        It configures the window based on settings from ``AppConfig.window``, 
        initializes the core UI components, and calls the user's :py:meth:`init_ui` hook.

        :param root: The parent application instance (the :py:class:`~fluvel.core.FluvelApp.FluvelApp`).
        :type root: :py:class:`~fluvel.core.FluvelApp.FluvelApp`

        :rtype: None
        """
        super().__init__()

        # Saving the app instance of the FluvelApp
        self.root = root

        # Se configura con las especificaciones del archivo .toml
        self.configure(**vars(AppConfig.window))

        # Se inicializa y muestra UI
        self._init_core_ui()

    def configure(self, **kwargs: Unpack[AppWindowKwargs]) -> None:
        """
        Configures multiple window properties from a single call.

        This high-level method allows setting various window attributes using
        keyword arguments, which are typically loaded from the ``config.toml``
        file but can also be set programmatically.
        
        :param title: Sets the window title.
        :type  title: str

        :param geometry: The initial position and size of the window as a four-element sequence: ``(x, y, width, height)``.
        :type geometry: Tuple[int, int, int, int] or List

        :param size: Sets the initial window size as ``(width, height)``.
        :type size: Tuple[int, int] or List

        :param resizable: Toggles whether the user can resize the window.
        :type resizable: bool

        :param min_size: Sets the minimum window size.
        :type min_size: Tuple[int, int] or List

        :param max_size: Sets the maximum window size.
        :type max_size: Tuple[int, int] or List

        :param min_width: Sets the minimum allowed width for the window.
        :type min_width: int

        :param min_height: Sets the minimum allowed height for the window.
        :type min_height: int

        :param max_width: Sets the maximum allowed width for the window.
        :type max_width: int

        :param max_height: Sets the maximum allowed height for the window.
        :type max_height: int

        :param show_mode: Sets the initial window state (e.g., "Normal", "Maximized").
        :type show_mode: str

        :param flags: A List of window flags to apply (e.g., "frameless").
        :type flags: List[:py:data:`~fluvel.utils.tip_helpers.WindowFlags`]

        :param attributes: A List of widget attributes to configure low-level behavior.
        :type attributes: List[:py:data:`~fluvel.utils.tip_helpers.WidgetAttributes`]
    
        :rtype: None
        """

        if "resizable" in kwargs:
            if not kwargs["resizable"]:
                kwargs["resizable"] = (self.width(), self.height())
            else:
                kwargs.pop("resizable")
            
        if flags := kwargs.get("flags"):
            previous_flag = Qt.WindowType.Window
            for flag in flags:
                previous_flag = previous_flag | getattr(Qt.WindowType, self._FLAGS[flag])
            kwargs["flags"] = previous_flag
        
        if mode := kwargs.get("show_mode"):
            kwargs["show_mode"] = getattr(Qt.WindowState, f"Window{mode}")

        if attributes := kwargs.get("attributes"):
            for attr in attributes:
                attribute = getattr(Qt.WidgetAttribute, self._ATTRIBUTES[attr])
                self.setAttribute(attribute, True)
            kwargs.pop("attributes")

        configure_process(self, self._MAPPING_METHODS, **kwargs)

    # abstract method where the initial state is defined
    # of the UI via the -self.configure- method
    def init_ui(self) -> None: 
        """
        An overridable method for initial user UI configuration.

        This method is intended to be implemented in your subclass of :class:`AppWindow`.
        It is automatically called by Fluvel at the end of the initialization process,
        after the central widget and menu bar have been created.

        .. note::
           This is the designated "hook" for adding your application's initial
           setup logic, such as configuring menu actions or connecting signals.
        
        :rtype: None
        """
        pass

    def _init_core_ui(self) -> None:
        """
        Initializes the core UI components of the window.
        
        This internal method orchestrates the setup of the central widget and
        the menu bar, and then calls the user-defined :meth:`init_ui` hook.

        :rtype: None
        """

        # Configuring the layout
        self._set_central_widget()

        # Configuring the Top Menu Bar
        self._set_menu_bar()

        # Set initial configurations
        self.init_ui()

    def _set_menu_bar(self) -> None:
        """
        Initializes and sets up the main menu bar from the content configuration.
        """
        
        if menu := ContentHandler.MENU_CONTENT.get("main-menu", {}):
            
            # This is an instance of QMenuBar
            self.menu_bar = MenuBar(self, menu)

            # Adding the Menu Bar to the Window
            self.setMenuBar(self.menu_bar)

    def _update_ui(self, router) -> None:
        """
        Refreshes the entire UI during a hot-reload event.

        This method is called by the :py:class:`HReloader` to destroy and recreate
        UI components, ensuring that code changes are reflected visually.

        .. warning::
           This method is for internal use by the Hot-Reloading system and should
           not be called directly by application code.

        :param router: The application's Router instance, needed to re-render the current view.
        :type router: :py:class:`~fluvel.core.Router.Router`
        :rtype: None
        """
        reload_ui(self, router)
        
    def _set_central_widget(self) -> None:
        """
        Creates and configures the central :py:class:`PySide6.QtWidgets.QStackedWidget`.

        This widget serves as the container for all views managed by the
        :py:class:`~fluvel.core.Router.Router`.
        :rtype: None
        """
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)
