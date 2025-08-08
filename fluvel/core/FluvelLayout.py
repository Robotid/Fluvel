from typing import Unpack, overload, TypedDict, TypeVar

# Flvuel Core
from core.core_utils import configure_process
from core.FluvelWidget import FluvelWidget

# Fluvel Widgets
from components.widgets.Label import Label, LabelKwargs
from components.widgets.Button import Button, ButtonKwargs

# PySide6
from PySide6.QtWidgets import QWidget, QLayout
from PySide6.QtCore import Qt

class LayoutKwargs(TypedDict, total=False):
    """
    Argumentos de palabra clave para la configuración de la distribución del layout.
    """
    alignment: Qt.AlignmentFlag | None
    spacing: int | None
    margins: tuple[int, int, int, int] | None
    size_constraint: QLayout.SizeConstraint | None

TWidget = TypeVar("TWidget", bound=QWidget)    
    
class FluvelLayout(FluvelWidget):
    """
    Clase propia de `Fluvel` que proporciona los métodos para la adición de QWidgets en QLayouts.
    """

    # Size Contraints
    DEFAULT = QLayout.SizeConstraint.SetDefaultConstraint
    FIXED = QLayout.SizeConstraint.SetFixedSize
    MINIMUM = QLayout.SizeConstraint.SetMinimumSize
    MAXIMUM = QLayout.SizeConstraint.SetMaximumSize
    WITHOUT = QLayout.SizeConstraint.SetNoConstraint
    MIN_AND_MAX = QLayout.SizeConstraint.SetMinAndMaxSize

    _MAPPING_METHODS = {
        "alignment": "setAlignment",
        "spacing": "setSpacing",
        "margins": "setContentsMargins",
        "size_constraint": "setSizeConstraint"
    }

    def adjust(self, **kwargs: Unpack[LayoutKwargs]) -> None:
        """
        Este método ajusta la configuración de la distribución del layout, permitiendo
        configurar varios atributos en una sola llamada.

        Args:
            alignment (Qt.AlignmentFlag): Alineación de los elementos.\n
                Puede ser uno de los siguientes valores predefinidos:
                Alineaciones Básicas
                - `self.TOP`
                - `self.RIGHT`
                - `self.BOTTOM`
                - `self.LEFT`
                Centrado
                - `self.H_CENTER` (Centrado horizontal)
                - `self.V_CENTER` (Centrado vertical)
                - `self.CENTER` (Centrado horizontal y vertical)
                Combinaciones Predefinidas
                - `self.TOP_RIGHT`
                - `self.TOP_LEFT`
                - `self.BOTTOM_RIGHT`
                - `self.BOTTOM_LEFT`
                - `self.CENTER_TOP `
                - `self.CENTER_RIGHT`
                - `self.CENTER_BOTTOM `
                - `self.CENTER_LEFT`
            spacing (int): Espacio en píxeles entre los elementos.
            margins (tuple[int, int, int, int]): Márgenes alrededor del layout.
                Siguiendo el orden: `left`, `top`, `right`, `bottom`.
            size_constraint (QLayout.SizeConstraint): Restricción de tamaño para el layout.\n
                Puede ser uno de los siguientes valores predefinidos:
                - `self.DEFAULT`
                - `self.FIXED`
                - `self.MINIMUM`
                - `self.MAXIMUM`
                - `self.WITHOUT`
                - `self.MIN_AND_MAX`   
        """
        configure_process(self, self._MAPPING_METHODS, **kwargs)

    def _process_kwargs(self, _type: type[TWidget], *args, **kwargs) -> TWidget | None:
        """
        This method determines whether or not to create a Widget, depending on the supplied arguments.\n
        It then establishes parentage relationships and adds it to the Layout.
        """
        exist: bool = False

        # If the supplied argument is already a widget
        if len(args)>0:
            widget = args[0]
            exist = True
 
        else:
            # Create the widget
            widget = _type(**kwargs)

        # Setting the parent, which will be the same as the Layout
        widget.setParent(self.parentWidget())

        # Add to layout
        self.addWidget(widget)

        # Return
        return None if exist else widget


    @overload
    def add_label(self, **kwargs: Unpack[LabelKwargs]) -> Label: ...

    @overload
    def add_label(self, arg__1: Label) -> None: ...

    def add_label(self, *args, **kwargs) -> Label | None:

        # create the label if it doesn't exist or just add it to the layout, 
        # then return the Label instance or None if the widget is already provided
        return self._process_kwargs(Label, *args, **kwargs)


    @overload
    def add_button(self, **kwargs: Unpack[ButtonKwargs]) -> Button: ...

    @overload
    def add_button(self, arg__1: Button) -> None: ...

    def add_button(self, *args, **kwargs) -> Button | None:
        
        # create the button if it doesn't exist or just add it to the layout,
        # then return the Button instance or None if it's already a widget
        return self._process_kwargs(Button, *args, **kwargs)


    def add_input_field(self, **kwargs):
        ...