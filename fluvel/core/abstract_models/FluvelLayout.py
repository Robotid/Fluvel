from typing import Unpack, overload, TypedDict, TypeVar

# Flvuel Core
from fluvel.core.core_utils import configure_process
from fluvel.core.abstract_models.FluvelWidget import FluvelWidget

# Fluvel Widgets
from fluvel.components.widgets.FLabel import FLabel, FLabelKwargs
from fluvel.components.widgets.FButton import FButton, FButtonKwargs
from fluvel.components.widgets.LineEdit import LineEdit, LineEditKwargs

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
        "size_constraint": "setSizeConstraint",
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
        exists: bool = False

        # If the supplied argument is already a widget
        if len(args) > 0:
            widget = args[0]
            exists = True

        else:
            # Create the widget
            widget = _type(**kwargs)

        # Setting the parent, which will be the same as the Layout
        widget.setParent(self.parentWidget())

        # Add to layout
        self.addWidget(widget)

        # Return
        return None if exists else widget

    @overload
    def Label(self, **kwargs: Unpack[FLabelKwargs]) -> FLabel: ...

    @overload
    def Label(self, arg__1: FLabel) -> None: ...

    def Label(self, *args, **kwargs) -> FLabel | None:

        # create the label if it doesn't exist or just add it to the layout,
        # then return the FLabel instance or None if the widget is already provided
        return self._process_kwargs(FLabel, *args, **kwargs)

    @overload
    def Button(self, **kwargs: Unpack[FButtonKwargs]) -> FButton: ...

    @overload
    def Button(self, arg__1: FButton) -> None: ...

    def Button(self, *args, **kwargs) -> FButton | None:

        # create the button if it doesn't exist or just add it to the layout,
        # then return the FButton instance or None if it's already a widget
        return self._process_kwargs(FButton, *args, **kwargs)

    @overload
    def addLineEdit(self, **kwargs: Unpack[LineEditKwargs]) -> LineEdit: ...

    @overload
    def addLineEdit(self, arg__1: LineEdit) -> None: ...

    def addLineEdit(self, *args, **kwargs) -> LineEdit | None:

        # create the button if it doesn't exist or just add it to the layout,
        # then return the FButton instance or None if it's already a widget
        return self._process_kwargs(LineEdit, *args, **kwargs)
