from dataclasses import dataclass 
from typing import Type

# Fluvel
from fluvel.core.abstract_models.ABCAbstractView import AbstractView
from fluvel.core.AppWindow import AppWindow

# Composer
from fluvel.composer import Animator

# PySide6
from PySide6.QtWidgets import QStackedWidget

class Router:
    """
    Manages the navigation flow and registration of views (pages) within the application.
    
    The Router is a static utility class that uses the main window's central widget 
    (:py:class:`PySide6.QtWidgets.QStackedWidget`) to display views. It handles 
    lazy instantiation of views and provides methods for animation during transitions.
    """

    @dataclass
    class Route:
        """
        Data structure representing a registered application route

        :ivar name: A unique name for each route (e.g., "login")
        :type name: str

        :ivar view_class: The uninstantiated class of the view, decorated by :py:func:`route`.
        :type view_class: Type[:py:class:`~fluvel.core.abstract_models.ABCAbstractView.AbstractView`]

        :ivar view_instance: The actual instance of the view after it has been shown for the first time.
        :type view_instance: :py:class:`~fluvel.core.abstract_models.ABCAbstractView.AbstractView`
        
        """
        name:           str
        view_class:     Type[AbstractView]
        view_instance:  AbstractView = None

    _window:        AppWindow
    _routes:        dict[str, Route] = {}
    _current_route: Route = None

    @classmethod
    def init(cls, window: AppWindow) -> None:
        """
        Initializes the router by linking it to the main application window.
        
        This method must be called before registering or showing any routes.
        It also sets global variables on the :py:class:`~fluvel.core.abstract_models.ABCAbstractView.AbstractView`
        base class for access to the root window components.

        :param window: The main application window instance containing the central widget.
        :type window: :py:class:`~fluvel.core.AppWindow`
        :rtype: None
        """
        cls._window = window
        AbstractView._set_globals(cls._window.root, cls._window)
              
    @classmethod
    def show(cls, name: str, animation: str | None = "fade_in") -> None:
        """
        Displays the view assigned to the given route name in the central widget 
        of the main window, optionally applying an animation.

        Views are instantiated **lazily**: the view's ``build_ui()`` method is only called 
        the first time the view is requested via this method.

        :param name: The name of the route assigned to the view (e.g., "home").
        :type name: str
        :param animation: The name of the animation to display during the transition (e.g., "fade_in"). 
                          If :py:obj:`None`, no animation is applied.
        :type animation: str or None

        :raises ValueError: If the provided route ``name`` was not found in the registered routes.
        :rtype: None
        """

        # if a view with the route name does not exist
        if name not in Router._routes:
            raise ValueError(f"Route '{name}' not found. Make sure it is registered in the FluvelApp.")

        # The route (Router.Route)
        route: Router.Route = Router._routes[name]

        # The central widget (QStackedWidget)
        central_widget: QStackedWidget = cls._window.central_widget

        if not route.view_instance:

            # Instantiate the view
            route.view_instance = route.view_class(None) 
            route.view_instance.build_ui()

            # Add view container to QStackedWidget stack
            central_widget.addWidget(route.view_instance.container)

        if cls._current_route != route:

            # Set current route
            cls._current_route = route

            # Show the view in the central widget
            target_widget = route.view_instance.container
            central_widget.setCurrentWidget(target_widget)

            # Set animation
            if animation:
                anim = getattr(Animator, animation)(target_widget)
                anim.start()

def route(name: str):
    """
    Decorator used to register a view class with the :py:class:`Router`.

    The view class is linked to the provided route name, allowing it to be displayed
    via :py:meth:`Router.show`. This decorator ensures that if a view with the same
    name is decorated again, the view class is simply updated.

    :param name: The unique name used to identify the view in the router (e.g., "login").
    :type name: str
    :returns: A wrapper that accepts the view class.
    :rtype: callable
    
    Example
    -------
    .. code-block:: python
    
        from fluvel import View
        
        @route("login")
        class LoginView(View):
            def build_ui(self):
                # ... UI implementation ...
                pass
    """

    def wrapper(view_class: Type[AbstractView]):
        
        if name in Router._routes:
            Router._routes[name].view_class = view_class
        else:
            Router._routes[name] = Router.Route(name, view_class)
        return view_class
    
    return wrapper