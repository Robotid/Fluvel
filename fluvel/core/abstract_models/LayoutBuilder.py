from typing import TypeVar, Generic, Type

from fluvel.components.widgets.FContainer import FContainer

# PySide6
from PySide6.QtWidgets import QLayout

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
        drag_window: bool,
        stretch: int
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

        :param stretch: The **stretch factor** to assign to the layout container.
        :type stretch: int
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
            container.add_widget(parent_widget, stretch=stretch)

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