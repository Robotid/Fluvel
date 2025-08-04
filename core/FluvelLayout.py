from typing import Unpack, overload

# Fluvel
from components.widgets.Labels.Label import Label, LabelKwargs
from components.widgets.Buttons.Button import Button, ButtonKwargs

# PySide6
from PySide6.QtWidgets import QWidget

class FluvelLayout:
    """
    Clase propia de `Fluvel` que proporciona los métodos para la adición de QWidgets en QLayouts.
    """

    def _process_kwargs(self, _type: QWidget, **kwargs) -> QWidget | None:
        """
        This method determines whether or not to create a Widget, depending on the supplied arguments.\n
        It then establishes parentage relationships and adds it to the Layout.
        """
        exist: bool = False

        # If the supplied argument is already a widget
        if "widget" in kwargs:
            widget: QWidget = kwargs["widget"]
            exist = True

        else:
            # Create the widget
            widget = _type(**kwargs)

        # Setting the parent, which will be the same as the Layout
        widget.setParent(self.parentWidget())

        # Add to layout
        self.addWidget(widget)

        # Return
        return widget if not exist else None

    @overload
    def add_label(self, **kwargs: Unpack[LabelKwargs]) -> Label: ...

    @overload
    def add_label(self, widget: Label) -> None: ...

    def add_label(self, **kwargs: Unpack[LabelKwargs]) -> Label | None:
        
        # creating the label if it doesn't exist or simply adding it to the layout
        label: Label | None = self._process_kwargs(_type=Label, **kwargs)

        # Return
        return label

    @overload
    def add_button(self, **kwargs: Unpack[ButtonKwargs]) -> Button: ...

    @overload
    def add_button(self, button: Button) -> None: ...

    def add_button(self, **kwargs: Unpack[ButtonKwargs]) -> Button | None:
        
        # creating the button if it doesn't exist or simply adding it to the layout
        button: Button | None = self._process_kwargs(_type=Button, **kwargs)

        # Return
        return button

    def add_input_field(self, **kwargs):
        ...