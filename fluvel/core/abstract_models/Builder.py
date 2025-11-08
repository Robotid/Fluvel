from typing import TYPE_CHECKING

# Fluvel
from fluvel.components.widgets.FContainer import FContainer
from fluvel.core.abstract_models.LayoutBuilder import LayoutBuilder, TLayout, Type

# PySide6
from PySide6.QtWidgets import QLayout

# necessary to avoid circular imports of 
# layouts inherited from Builder
if TYPE_CHECKING:
    from fluvel.components.layouts import VBoxLayout, HBoxLayout, GridLayout, FormLayout

class Builder:
    """
    A Mixin that provides the declarative API ('Vertical','Horizontal', etc.)
    for building layouts using LayoutBuilder.
    """

    def build_layout(
        self, 
        type_layout: Type[TLayout], 
        style: str,
        drag_window: bool,
        stretch: int
    ) -> LayoutBuilder[TLayout]:
        """
        Internal factory method for creating a :py:class:`LayoutBuilder`.

        :param type_layout: The class of the layout to instantiate.
        :type type_layout: type[TLayout]

        :param style: The QSS-style class name(s) for the layout's container.
        :type style: str

        :param drag_window: Enable dragging of the Main Window.
        :type drag_window: bool

        :param stretch: The **stretch factor** to assign to the layout container.
        :type stretch: int

        :returns: A configured :py:class:`LayoutBuilder`.
        :rtype: LayoutBuilder[TLayout]
        """

        return LayoutBuilder(self, type_layout, style, drag_window, stretch)

    def Vertical(
        self, 
        style: str | None = None,
        drag_window: bool = False,
        stretch: int = 0,
    ) -> "LayoutBuilder[VBoxLayout]":
        """
        Creates a vertical box layout (:py:class:`~fluvel.components.layouts.VBoxLayout.VBoxLayout`) 
        using a context manager.

        :param style: The style for the layout's container.
        :type style: str or None
        
        :param drag_window: Enable dragging of the Main Window.
                            Allows you to drag the Main Window
                            from the design area.
        :type drag_window: bool

        :param stretch: The **stretch factor** to assign to the layout container.
        :type stretch: int
        
        :returns: A :py:class:`LayoutBuilder` for :py:class:`~fluvel.components.layouts.VBoxLayout.VBoxLayout`.
        :rtype: LayoutBuilder[VBoxLayout]
        
        Example:
        --------
        .. code-block:: python
            ...
            with self.Vertical() as v:
                v.Label(text="Hello")
        """
        from fluvel.components.layouts import VBoxLayout

        return self.build_layout(VBoxLayout, style, drag_window, stretch)

    def Horizontal(
        self, 
        style: str | None = None,
        drag_window: bool = False,
        stretch: int = 0,
    ) -> "LayoutBuilder[HBoxLayout]":
        """
        Creates a horizontal box layout (:py:class:`~fluvel.components.layouts.HBoxLayout.HBoxLayout`) 
        using a context manager.

        :param style: The style for the layout's container.
        :type style: str or None
        
        :param drag_window: Enable dragging of the Main Window.
                            Allows you to drag the Main Window
                            from the design area.
        :type drag_window: bool

        :param stretch: The **stretch factor** to assign to the layout container.
        :type stretch: int

        :returns: A :py:class:`LayoutBuilder` for :py:class:`~fluvel.components.layouts.HBoxLayout.HBoxLayout`.
        :rtype: LayoutBuilder[HBoxLayout]
        
        Example:
        --------
        .. code-block:: python
            ...
            with self.Horizontal() as h:
                h.Label(text="Hello")
        """
        from fluvel.components.layouts import HBoxLayout
        
        return self.build_layout(HBoxLayout, style, drag_window, stretch)

    def Form(
        self,
        style: str | None = None,
        drag_window: bool = False,
        stretch: int = 0,
    ) -> "LayoutBuilder[FormLayout]":
        """
        Creates a form layout (:py:class:`~fluvel.components.layouts.FormLayout.FormLayout`) 
        using a context manager.

        :param style: The style for the layout's container.
        :type style: str or None

        :param drag_window: Enable dragging of the Main Window.
                            Allows you to drag the Main Window
                            from the design area.
        :type drag_window: bool

        :param stretch: The **stretch factor** to assign to the layout container.
        :type stretch: int

        :returns: A :py:class:`LayoutBuilder` for :py:class:`~fluvel.components.layouts.FormLayout.FormLayout`.
        :rtype: LayoutBuilder[FormLayout]
        """
        from fluvel.components.layouts import FormLayout

        return self.build_layout(FormLayout, style, drag_window, stretch)

    def Grid(
        self, 
        style: str | None = None,
        drag_window: bool = False,
        stretch: int = 0,
    ) -> "LayoutBuilder[GridLayout]":
        """
        Creates a grid layout (:py:class:`~fluvel.components.layouts.GridLayout.GridLayout`) 
        using a context manager.

        :param style: The style for the layout's container.
        :type style: str or None

        :param drag_window: Enable dragging of the Main Window.
                            Allows you to drag the Main Window
                            from the design area.
        :type drag_window: bool

        :param stretch: The **stretch factor** to assign to the layout container.
        :type stretch: int

        :returns: A :py:class:`LayoutBuilder` for :py:class:`~fluvel.components.layouts.GridLayout.GridLayout`.
        :rtype: LayoutBuilder[GridLayout]
        """
        from fluvel.components.layouts import GridLayout

        return self.build_layout(GridLayout, style, drag_window, stretch)

    def Stacked(self): ... # TO DO

    # TO DO 
    def DockSection(
        self, 
        title: str,
        layout: str = "vertical",
        side: str = "left",
        style: str | None = None
    ) -> "LayoutBuilder[VBoxLayout | HBoxLayout]":
        """
        TO DO: Esta es una funcionalidad aún no implementada
        """

        from PySide6.QtWidgets import QDockWidget
        from PySide6.QtCore import Qt
        from fluvel.components.layouts import VBoxLayout, HBoxLayout

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

        return self.build_layout(dock_container, dock_layout, style, False, 0)