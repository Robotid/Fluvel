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
from PySide6.QtWidgets import QLayout
from PySide6.QtCore import QObject


# Define a type variable for layouts
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
        style: str | None,
        drag_window: bool
    ):
        """
        Initializes the :py:class:`~fluvel.core.abstract_models.ABCAbstractView.LayoutBuilder` instance.

        :param container: The layout or widget to which the new layout will be added.
        :type container: :py:class:`PySide6.QtWidgets.QLayout` or :py:class:`~fluvel.components.widgets.FContainer.FContainer`

        :param type_layout: The class of the layout to instantiate (e.g., :py:class:`~fluvel.components.layouts.VBoxLayout.VBoxLayout`).
        :type type_layout: type[TLayout]

        :param style: The QSS-style class name(s) to apply to the layout's parent container :py:class:`~fluvel.components.widgets.FContainer.FContainer`.
        :type style: str or None

        :param drag_window: Enable dragging of the Main Window.
        :type drag_window: bool
        """

        parent_widget = None
        
        # The container is a QLayout, 
        # which means that an FContainer must be created and added 
        # to the current QLayout (container parameter) 
        # for it to function as a new container for the requested QLayout.
        if isinstance(container, QLayout):
            
            # Based on the “drag_window” parameter, 
            # it decides whether the container is 
            # capable of dragging the main window.
            parent_widget = FContainer(movable=drag_window)

            # Then add the widget to the layout
            container.addWidget(parent_widget)

            # Finally, the requested layout is instantiated 
            # as a child of the newly created FContainer.
            self.layout: TLayout = type_layout(parent_widget) 

        # The container is a FContainer
        elif isinstance(container, FContainer):
            self.layout: TLayout = type_layout(container) 
            parent_widget = container

        else:
            raise TypeError("The container must be a QLayout or an FContainer.")

        # Apply styles to the container
        # By default, a transparent background is assigned.
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

    All :py:class:`~fluvel.core.abstract_models.ABCAbstractPage.AbstractPage` subclasses inherit from this metaclass to ensure 
    compatibility with both PySide6's signal/slot system and Python's abstract base classes.
    """
    pass

class AbstractPage(FContainer, ABC, metaclass=VBMeta):
    """
    Abstract base class for creating Views (pages) in Fluvel.

    This class provides the core declarative helper methods (context managers) 
    for UI construction, such as :py:meth:`Vertical`, :py:meth:`Horizontal`, etc.

    All application views must inherit from :py:class:`~fluvel.core.abstract_models.ABCAbstractPage.AbstractPage` and implement
    the :py:meth:`build_ui` method.

    :cvar app_root: The instance of the main application class (:py:class:`~fluvel.core.FluvelApp.FluvelApp`).
    :cvar main_window: The instance of the main window container (:py:class:`~fluvel.core.AppWindow.AppWindow`).
    """

    def __init__(self) -> None:
        """
        Initializes an instance of :py:class:`~fluvel.core.abstract_models.ABCAbstractPage.AbstractPage`.
        """
        super().__init__()
        

    @classmethod
    def _set_globals(cls, app_root, main_window: AppWindow):
        """
        Sets global references to the application root and main window.

        This is called internally by :py:class:`~fluvel.core.Router.Router.init`.

        :param app_root: The root application instance.
        :type app_root: :py:class:`~fluvel.core.App.FluvelApp`
        :param main_window: The main application window instance.
        :type main_window: :py:class:`~fluvel.core.AppWindow.AppWindow`
        :rtype: None
        """
        # The FluvelApp instance
        cls.app_root = app_root

        # The MainWindow instance
        cls.main_window = main_window

    def build_layout(
        self, 
        container: QLayout | FContainer | None, 
        type_layout: Type[TLayout], 
        style: str,
        drag_window: bool
    ) -> LayoutBuilder[TLayout]:
        """
        Internal factory method for creating a :py:class:`LayoutBuilder`.

        :param container: The container for the layout. Defaults to the view's root :py:attr:`container`.
        :type container: :py:class:`PySide6.QtWidgets.QLayout` or :py:class:`~fluvel.components.widgets.FContainer.FContainer` or :py:obj:`None`

        :param type_layout: The class of the layout to instantiate.
        :type type_layout: type[TLayout]

        :param style: The QSS-style class name(s) for the layout's parent widget.
        :type style: str

        :param drag_window: Enable dragging of the Main Window.
        :type drag_window: bool

        :returns: A configured :py:class:`LayoutBuilder`.
        :rtype: LayoutBuilder[TLayout]
        """
        
        # Si el contenedor es 'None', significa que el layout
        # debe adjuntarse a la propia Página (self).
        if container is None:
            layout_container = self

            # Si se pide 'drag_window' en el layout raíz,
            # hacemos que la Página (self) sea arrastrable.
            if drag_window:
                self.isMovable = True
        else:
            layout_container = container

        return LayoutBuilder(layout_container, type_layout, style, drag_window)

    def Vertical(
        self, 
        container: QLayout | FContainer | None = None,
        style: str | None = None,
        drag_window: bool = False
    ) -> LayoutBuilder[VBoxLayout]:
        """
        Creates a vertical box layout (:py:class:`~fluvel.components.layouts.VBoxLayout.VBoxLayout`) 
        using a context manager.

        :param container: The container for the layout. Defaults to the view's root :py:attr:`container`.
        :type container: :py:class:`PySide6.QtWidgets.QLayout` or :py:class:`~fluvel.components.widgets.FContainer.FContainer` or :py:obj:`None`

        :param style: The style for the layout's parent widget.
        :type style: str or None
        
        :param drag_window: Enable dragging of the Main Window.
        :type drag_window: bool
        
        :returns: A :py:class:`LayoutBuilder` for :py:class:`~fluvel.components.layouts.VBoxLayout.VBoxLayout`.
        :rtype: LayoutBuilder[VBoxLayout]
        
        Example:
        --------
        .. code-block:: python
            ...
            with self.Vertical() as v:
                v.Label(text="Hello")
        """

        return self.build_layout(container, VBoxLayout, style, drag_window)

    def Horizontal(
        self, 
        container: QLayout | FContainer | None = None, 
        style: str | None = None,
        drag_window: bool = False
    ) -> LayoutBuilder[HBoxLayout]:
        """
        Creates a horizontal box layout (:py:class:`~fluvel.components.layouts.HBoxLayout.HBoxLayout`) 
        using a context manager.

        :param container: The container for the layout. Defaults to the view's root :py:attr:`container`.
        :type container: :py:class:`PySide6.QtWidgets.QLayout` or :py:class:`~fluvel.components.widgets.FContainer.FContainer` or :py:obj:`None`

        :param style: The style for the layout's parent widget.
        :type style: str or None
        
        :param drag_window: Enable dragging of the Main Window.
                            Allows you to drag the Main Window
                            from the design area.
        :type drag_window: bool

        :returns: A :py:class:`LayoutBuilder` for :py:class:`~fluvel.components.layouts.HBoxLayout.HBoxLayout`.
        :rtype: LayoutBuilder[HBoxLayout]
        
        Example:
        --------
        .. code-block:: python
            ...
            with self.Horizontal() as h:
                h.Label(text="Hello")
        """

        return self.build_layout(container, HBoxLayout, style, drag_window)

    def Form(
        self, 
        container: QLayout | FContainer | None = None,
        style: str | None = None,
        drag_window: bool = False
    ) -> LayoutBuilder[FormLayout]:
        """
        Creates a form layout (:py:class:`~fluvel.components.layouts.FormLayout.FormLayout`) 
        using a context manager.

        :param container: The container for the layout. Defaults to the view's root :py:attr:`container`.
        :type container: :py:class:`PySide6.QtWidgets.QLayout` or :py:class:`~fluvel.components.widgets.FContainer.FContainer` or :py:obj:`None`

        :param style: The style for the layout's parent widget.
        :type style: str or None

        :param drag_window: Enable dragging of the Main Window.
        :type drag_window: bool

        :returns: A :py:class:`LayoutBuilder` for :py:class:`~fluvel.components.layouts.FormLayout.FormLayout`.
        :rtype: LayoutBuilder[FormLayout]
        """
        return self.build_layout(container, FormLayout, style, drag_window)

    def Grid(
        self, 
        container: QLayout | FContainer | None = None, 
        style: str | None = None,
        drag_window: bool = False
    ) -> LayoutBuilder[GridLayout]:
        """
        Creates a grid layout (:py:class:`~fluvel.components.layouts.GridLayout.GridLayout`) 
        using a context manager.

        :param container: The container for the layout. Defaults to the view's root :py:attr:`container`.
        :type container: :py:class:`PySide6.QtWidgets.QLayout` or :py:class:`~fluvel.components.widgets.FContainer.FContainer` or :py:obj:`None`

        :param style: The style for the layout's parent widget.
        :type style: str or None

        :param drag_window: Enable dragging of the Main Window.
        :type drag_window: bool

        :returns: A :py:class:`LayoutBuilder` for :py:class:`~fluvel.components.layouts.GridLayout.GridLayout`.
        :rtype: LayoutBuilder[GridLayout]
        """

        return self.build_layout(container, GridLayout, style, drag_window)

    def Stacked(self, container: QLayout | FContainer): ...

    def DockSection(
        self, 
        title: str,
        layout: str = "vertical",
        side: str = "left",
        style: str | None = None
    ) -> LayoutBuilder[VBoxLayout | HBoxLayout]:
        """
        TO DO: Esta es una funcionalidad aún no implementada
        """

        from PySide6.QtWidgets import QDockWidget
        from PySide6.QtCore import Qt

        layouts: dict[str, Type[QLayout]] = {
            "vertical": VBoxLayout,
            "horizontal": HBoxLayout 
        }

        dock_areas = {
            "right": Qt.DockWidgetArea.RightDockWidgetArea,
            "left": Qt.DockWidgetArea.LeftDockWidgetArea,
            "top": Qt.DockWidgetArea.TopDockWidgetArea,
            "bottom": Qt.DockWidgetArea.BottomDockWidgetArea
        }

        dock_widget = QDockWidget(title, self.main_window)

        dock_container = FContainer()

        dock_widget.setWidget(dock_container)

        dock_layout = layouts.get(layout)

        self.main_window.addDockWidget(dock_areas.get(side), dock_widget)

        return self.build_layout(dock_container, dock_layout, style, False)


    @abstractmethod
    def build_ui(self) -> None:
        """
        Abstract method for building the user interface.
        
        This method **must** be implemented by all classes inheriting from 
        :py:class:`~fluvel.core.abstract_models.ABCAbstractPage.AbstractPage` and is where the entire UI construction logic resides.
        :rtype: None
        """
        pass

class Page(AbstractPage):
    """
    Concrete class that inherits from :py:class:`~fluvel.core.abstract_models.ABCAbstractPage.AbstractPage`
    used for user interface composition via context handlers.   
    """
    pass