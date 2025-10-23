"""
This module contains the fundamental logic for creating declarative layouts in Fluvel.

It defines the core abstract class for all views and the context manager 
responsible for building nested PySide6 layouts.
"""

from typing import TypeVar, Generic, Type
from abc import ABC, abstractmethod, ABCMeta

# Fluvel
from fluvel.components.layouts import FormLayout, HBoxLayout, VBoxLayout, GridLayout
from fluvel.components.widgets.FContainer import FContainer
from fluvel.core.AppWindow import AppWindow

# PySide6
from PySide6.QtWidgets import QLayout, QFrame
from PySide6.QtCore import QObject


# Definir una variable de tipo para los layouts
TLayout = TypeVar("TLayout", bound=QLayout)

class LayoutBuilder(Generic[TLayout]):
    """
    Context manager for the declarative creation of PySide6 layouts.

    This class allows developers to build nested layouts intuitively using the 
    :keyword:`with` syntax, automatically handling the addition of the new layout 
    to an existing container (:py:class:`PySide6.QtWidgets.QLayout` or :py:class:`~fluvel.components.widgets.FContainer.FContainer`).

    :ivar layout: The instantiated :py:class:`PySide6.QtWidgets.QLayout`.
    :type layout: TLayout
    """

    def __init__(
        self, 
        container: QLayout | FContainer, 
        type_layout: Type[TLayout],
        style: str | None
    ):
        """
        Initializes the :py:class:`~fluvel.core.abstract_models.ABCAbstractView.LayoutBuilder` instance.

        :param container: The layout or widget to which the new layout will be added.
        :type container: :py:class:`PySide6.QtWidgets.QLayout` or :py:class:`~fluvel.components.widgets.FContainer.FContainer`
        :param type_layout: The class of the layout to instantiate (e.g., :py:class:`~fluvel.components.layouts.VBoxLayout.VBoxLayout`).
        :type type_layout: type[TLayout]
        :param style: The QSS-style class name(s) to apply to the layout's parent container :py:class:`~fluvel.components.widgets.FContainer.FContainer`.
        :type style: str or None
        """

        parent_widget = None
        
        # the container is a layout
        if isinstance(container, QLayout):
            parent_widget = FContainer()
            container.addWidget(parent_widget)
            self.layout: TLayout = type_layout(parent_widget) 

        # the container is a widget
        elif isinstance(container, QFrame):
            self.layout: TLayout = type_layout(container) 
            parent_widget = container

        else:
            raise TypeError("El contenedor debe ser un QLayout o un FContainer.")

        style: str = style if style else "bg-transparent"

        parent_widget.configure(style=style)

            
    def __enter__(self) -> TLayout:
        """
        Context manager entry method.
        
        Returns the layout instance so it can be used inside the :keyword:`with` block.
        
        :returns: The instantiated layout object.
        :rtype: TLayout
        """
        return self.layout

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Context manager exit method.
        
        :returns: Always returns :py:obj:`False` to avoid suppressing exceptions.
        :rtype: bool
        """
        return False

class VBMeta(type(QObject), ABCMeta):
    """
    Unified Metaclass that resolves conflicts when combining 
    :py:class:`PySide6.QtCore.QObject` and :py:class:`abc.ABCMeta`.

    All :py:class:`~fluvel.core.abstract_models.ABCAbstractView.AbstractView` subclasses inherit from this metaclass to ensure 
    compatibility with both PySide6's signal/slot system and Python's abstract base classes.
    """

    pass

class AbstractView(QObject, ABC, metaclass=VBMeta):
    """
    Abstract base class for creating Views (pages) in Fluvel.

    This class provides the core declarative helper methods (context managers) 
    for UI construction, such as :py:meth:`Vertical`, :py:meth:`Horizontal`, etc.

    All application views must inherit from :py:class:`AbstractView` and implement
    the :py:meth:`build_ui` method.

    :cvar app_root: The instance of the main application class (:py:class:`~fluvel.core.FluvelApp.FluvelApp`).
    :cvar main_window: The instance of the main window container (:py:class:`~fluvel.core.AppWindow.AppWindow`).
    :ivar _container: The root :py:class:`~fluvel.components.widgets.FContainer.FContainer` container for this view.
    """

    _container: FContainer

    def __init__(self, container: FContainer | QLayout | None) -> None:
        """
        Initializes an instance of :py:class:`AbstractView`.

        It establishes the root :py:attr:`container` for the view. If :py:obj:`None` 
        or a :py:class:`QLayout` is passed, a blank :py:class:`FContainer` is created as the container.

        :param container: The initial container for the view.
        :type container: :py:class:`~fluvel.components.widgets.FContainer.FContainer`, :py:class:`PySide6.QtWidgets.QLayout` or :py:obj:`None`
        :raises TypeError: If the container is neither a :py:class:`FContainer` nor a :py:class:`QLayout`.
        """
        super().__init__()
        self.container = container

    @classmethod
    def _set_globals(cls, app_root, main_window: AppWindow):
        """
        Sets global references to the application root and main window.

        This is called internally by :py:class:`~fluvel.core.Router.Router.init`.

        :param app_root: The root application instance.
        :param main_window: The main application window instance.
        :type main_window: :py:class:`~fluvel.core.AppWindow.AppWindow`
        :rtype: None
        """
        cls.app_root = app_root
        cls.main_window = main_window

    @property
    def container(self) -> FContainer:
        """
        The root :py:class:`FContainer` container of the view.
        """
        return self._container

    @container.setter
    def container(self, container: FContainer | QLayout | None) -> None:
        """
        Setter for the root container. Automatically creates a blank FContainer
        if the input is None or a QLayout.
        """

        if isinstance(container, FContainer):
            self._container = container

        # If the container is None or a QLayout, a blank FContainer is automatically
        # created to serve as the view's root widget.
        elif container is None or isinstance(container, QLayout):
            blank_container = FContainer()
            self._container = blank_container

        else:
            raise TypeError("The container must be a QLayout or a FContainer.")

    def build_layout(
        self, container: QLayout | FContainer | None, 
        type_layout: Type[TLayout], 
        style: str
    ) -> LayoutBuilder[TLayout]:
        """
        Internal factory method for creating a :py:class:`LayoutBuilder`.

        :param container: The container for the layout. Defaults to the view's root :py:attr:`container`.
        :type container: :py:class:`PySide6.QtWidgets.QLayout` or :py:class:`~fluvel.components.widgets.FContainer.FContainer` or :py:obj:`None`
        :param type_layout: The class of the layout to instantiate.
        :type type_layout: type[TLayout]
        :param style: The CSS-style class name(s) for the layout's parent widget.
        :type style: str
        :returns: A configured :py:class:`LayoutBuilder`.
        :rtype: LayoutBuilder[TLayout]
        """
        
        container = self.container if container is None else container

        return LayoutBuilder(container, type_layout, style)

    def Vertical(
        self, 
        container: QLayout | FContainer | None = None,
        style: str | None = None
    ) -> LayoutBuilder[VBoxLayout]:
        """
        Creates a vertical box layout (:py:class:`~fluvel.components.layouts.VBoxLayout.VBoxLayout`) 
        using a context manager.

        :param container: The container for the layout. Defaults to the view's root :py:attr:`container`.
        :type container: :py:class:`PySide6.QtWidgets.QLayout` or :py:class:`~fluvel.components.widgets.FContainer.FContainer` or :py:obj:`None`
        :param style: The style for the layout's parent widget.
        :type style: str or None
        :returns: A :py:class:`LayoutBuilder` for :py:class:`~fluvel.components.layouts.VBoxLayout.VBoxLayout`.
        :rtype: LayoutBuilder[VBoxLayout]
        
        Example:
        --------
        .. code-block:: python
            ...
            with self.Vertical() as v:
                v.Label(text="Hello")
        """

        return self.build_layout(container, VBoxLayout, style)

    def Horizontal(
        self, 
        container: QLayout | FContainer | None = None, 
        style: str | None = None
    ) -> LayoutBuilder[HBoxLayout]:
        """
        Creates a horizontal box layout (:py:class:`~fluvel.components.layouts.HBoxLayout.HBoxLayout`) 
        using a context manager.

        :param container: The container for the layout. Defaults to the view's root :py:attr:`container`.
        :type container: :py:class:`PySide6.QtWidgets.QLayout` or :py:class:`~fluvel.components.widgets.FContainer.FContainer` or :py:obj:`None`
        :param style: The style for the layout's parent widget.
        :type style: str or None
        :returns: A :py:class:`LayoutBuilder` for :py:class:`~fluvel.components.layouts.HBoxLayout.HBoxLayout`.
        :rtype: LayoutBuilder[HBoxLayout]
        
        Example:
        --------
        .. code-block:: python
            ...
            with self.Horizontal() as h:
                h.Label(text="Hello")
        """

        return self.build_layout(container, HBoxLayout, style)

    def Form(
        self, 
        container: QLayout | FContainer | None = None,
        style: str | None = None
    ) -> LayoutBuilder[FormLayout]:
        """
        Creates a form layout (:py:class:`~fluvel.components.layouts.FormLayout.FormLayout`) 
        using a context manager.

        :param container: The container for the layout. Defaults to the view's root :py:attr:`container`.
        :type container: :py:class:`PySide6.QtWidgets.QLayout` or :py:class:`~fluvel.components.widgets.FContainer.FContainer` or :py:obj:`None`
        :param style: The style for the layout's parent widget.
        :type style: str or None
        :returns: A :py:class:`LayoutBuilder` for :py:class:`~fluvel.components.layouts.FormLayout.FormLayout`.
        :rtype: LayoutBuilder[FormLayout]
        """
        return self.build_layout(container, FormLayout, style)

    def Grid(
        self, 
        container: QLayout | FContainer | None = None, 
        style: str | None = None
    ) -> LayoutBuilder[GridLayout]:
        """
        Creates a grid layout (:py:class:`~fluvel.components.layouts.GridLayout.GridLayout`) 
        using a context manager.

        :param container: The container for the layout. Defaults to the view's root :py:attr:`container`.
        :type container: :py:class:`PySide6.QtWidgets.QLayout` or :py:class:`~fluvel.components.widgets.FContainer.FContainer` or :py:obj:`None`
        :param style: The style for the layout's parent widget.
        :type style: str or None
        :returns: A :py:class:`LayoutBuilder` for :py:class:`~fluvel.components.layouts.GridLayout.GridLayout`.
        :rtype: LayoutBuilder[GridLayout]
        """

        return self.build_layout(container, GridLayout, style)


    def Stacked(self, container: QLayout | FContainer): ...

    @abstractmethod
    def build_ui(self) -> None:
        """
        Abstract method for building the user interface.
        
        This method **must** be implemented by all classes inheriting from 
        :py:class:`AbstractView` and is where the entire UI construction logic resides.
        :rtype: None
        """
        pass

class View(AbstractView):
    """
    Concrete class that inherits from :py:class:`AbstractView`.
    """
    pass