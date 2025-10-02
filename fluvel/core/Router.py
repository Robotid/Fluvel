from dataclasses import dataclass 
from typing import Type

# Fluvel
from fluvel.core.abstract_models.ABCAbstractView import AbstractView
from fluvel.core.AppWindow import AppWindow

from fluvel.composer import Animator

class Router:

    @dataclass
    class Route:
        name: str
        view_class: Type[AbstractView]
        view_instance: AbstractView = None

    _window: AppWindow
    _routes: dict[str, Route] = {}
    _current_route: Route = None

    @classmethod
    def init(cls, window: AppWindow) -> None:
        cls._window = window
        AbstractView._set_globals(cls._window.root, cls._window)

    @classmethod
    def route(cls, name: str):

        def wrapper(view_class: Type[AbstractView]):
            
            if name in cls._routes:
                cls._routes[name].view_class = view_class
            else:
                cls._routes[name] = cls.Route(name, view_class)

            return view_class

        return wrapper
                
    @classmethod
    def show(cls, name: str) -> None:
        """
        Display the view given in the Central Widget of the Window with a fade-in animation.
    
        :param name: The name of the route assigned to the view
        :type name: str
    
        :raises: 
            ValueError: If the route name was not found.
        """
    
        if name not in cls._routes:
            raise ValueError(f"Route '{name}' not found. Make sure it is registered in the FluvelApp.")
        
        route: Router.Route = cls._routes[name]
        
        if not route.view_instance:

            route.view_instance = route.view_class(None) 
            route.view_instance.build_ui()
            
            cls._window.central_widget.addWidget(route.view_instance.container)
        
        if cls._current_route != route:
            
            # Set current route
            cls._current_route = route
            
            
            # Show the view in the central widget
            target_widget = route.view_instance.container
            cls._window.central_widget.setCurrentWidget(target_widget)
            
            # Set animation
            animation = Animator.fade_in(target_widget)
            animation.start()