import importlib, functools
from typing import Type
from PySide6.QtWidgets import QWidget

# Tip-helpers
from fluvel.utils.tip_helpers import AllWidgetsTypes

class Factory:
    """
    Manages the creation of reusable, customized QWidget components.

    This class provides a decorator-based system to define new, pre-configured
    component types from base Fluvel widgets.

    :cvar _stock: A cache dictionary to store imported widget classes.
    :type _stock: dict[str, Type[QWidget]]
    """

    _stock: dict[str, Type[QWidget]] = {}

    class Target:
        """
        An internal helper class to manage the dynamic import of widgets.

        This class handles the logic for dynamic importing and caching of
        QWidget classes, ensuring that each widget module is loaded only once.

        :ivar WidgetClass: The imported QWidget class.
        :type WidgetClass: Type[QWidget]
        """
        
        def __init__(self, widget_target: str):
            """
            Initializes the Target and loads the target widget class into the cache.

            :param widget_target: The class name of the widget to import.
            :type widget_target: str
            """

            if widget_target not in Factory._stock:

                widget_module = importlib.import_module(f"fluvel.components.widgets.{widget_target}")

                Factory._stock[widget_target] = getattr(widget_module, widget_target)

            self.WidgetClass = Factory._stock[widget_target]
            
    @classmethod
    def compose(cls, target: AllWidgetsTypes):
        """
        A decorator that turns a configuration function into a component factory.

        This method wraps a function that returns a configuration dictionary.
        The decorated function becomes a new component that, when called, creates
        an instance of the target widget with the specified configuration.

        :param target: The class name of the base widget to create (e.g., "FButton").
        :type target: str
        :returns: A decorator that produces a QWidget component factory.
        :rtype: callable

        Example:
        --------
        .. code-block:: python

            # In components/custom.py
            from fluvel.composer import Factory

            @Factory.compose(target="FButton")
            def PrimaryButton(text: str):
                return {
                    "text": text,
                    "style": "primary bold"
                }

            # In a View
            from components.custom import PrimaryButton
            ...
            with self.Vertical() as v:
        
                # 1) Creates an FButton with text="Submit" and style="primary bold"
                v.addWidget(PrimaryButton(text="Submit"))
                
                # 2) or create a method to speed up adding the factory component to the layout
                v.PrimaryButton = v.from_factory(PrimaryButton)
                v.PrimaryButton(text="Submit")
        """
        
        object_target = cls.Target(target)

        def decorator(func):
            
            @functools.wraps(func)
            def component_wrapper(*args, **user_kwargs) -> QWidget:

                base_config = func(*args, **user_kwargs) 

                return object_target.WidgetClass(**base_config)

            return component_wrapper

        return decorator