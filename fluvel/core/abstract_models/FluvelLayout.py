from typing import Unpack, overload, TypedDict, TypeVar, Callable

# Flvuel Core
from fluvel.core.tools import configure_process

# Fluvel Widgets
from fluvel.components.widgets.FLabel import FLabel, FLabelKwargs
from fluvel.components.widgets.FButton import FButton, FButtonKwargs
from fluvel.components.widgets.FLineEdit import FLineEdit, FLineEditKwargs
from fluvel.components.widgets.FCheckBox import FCheckBox, FCheckBoxKwargs
from fluvel.components.widgets.FRadioButton import FRadioButton, FRadioButtonKwargs

# PySide6
from PySide6.QtWidgets import QWidget, QLayout
from PySide6.QtCore import Qt


TWidget = TypeVar("TWidget", bound=QWidget)


class LayoutKwargs(TypedDict, total=False):
    """
    Argumentos de palabra clave para la configuración de la distribución del layout.
    """

    alignment: Qt.AlignmentFlag
    spacing: int
    margins: tuple[int, int, int, int]
    size_constraint: QLayout.SizeConstraint
    

class FluvelLayout:
    """
    Clase propia de `Fluvel` que proporciona los métodos para la adición de QWidgets en QLayouts.

    :cvar TOP: Qt.AlignmentFlag.AlignTop.
    :cvar BOTTOM: Qt.AlignmentFlag.AlignBottom.
    :cvar RIGHT: Qt.AlignmentFlag.AlignRight.
    :cvar LEFT: Qt.AlignmentFlag.AlignLeft.
    :cvar CENTER: Qt.AlignmentFlag.AlignCenter.
    :cvar H_CENTER: Qt.AlignmentFlag.AlignHCenter.
    :cvar V_CENTER: Qt.AlignmentFlag.AlignVCenter.
    :cvar JUSTIFY: Qt.AlignmentFlag.AlignJustify.
    :cvar BASELINE: Qt.AlignmentFlag.AlignBaseline
    """

    # Alingment Flags
    TOP = Qt.AlignmentFlag.AlignTop
    BOTTOM = Qt.AlignmentFlag.AlignBottom
    RIGHT = Qt.AlignmentFlag.AlignRight
    LEFT = Qt.AlignmentFlag.AlignLeft
    CENTER = Qt.AlignmentFlag.AlignCenter
    H_CENTER = Qt.AlignmentFlag.AlignHCenter
    V_CENTER = Qt.AlignmentFlag.AlignVCenter
    JUSTIFY = Qt.AlignmentFlag.AlignJustify
    BASELINE = Qt.AlignmentFlag.AlignBaseline

    # Combinations
    TOP_LEFT = TOP | LEFT
    TOP_RIGHT = TOP | RIGHT
    BOTTOM_LEFT = BOTTOM | LEFT
    BOTTOM_RIGHT = BOTTOM | RIGHT
    CENTER_TOP = TOP | H_CENTER
    CENTER_RIGHT = RIGHT | V_CENTER
    CENTER_BOTTOM = BOTTOM | H_CENTER
    CENTER_LEFT = LEFT | V_CENTER

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
                - `layout.TOP`
                - `layout.RIGHT`
                - `layout.BOTTOM`
                - `layout.LEFT`
                - `layout.JUSTIFY`
                - `layout.BASELINE`
                Centrado
                - `layout.H_CENTER` (Centrado horizontal)
                - `layout.V_CENTER` (Centrado vertical)
                - `layout.CENTER` (Centrado horizontal y vertical)
                Combinaciones Predefinidas
                - `layout.TOP_RIGHT`
                - `layout.TOP_LEFT`
                - `layout.BOTTOM_RIGHT`
                - `layout.BOTTOM_LEFT`
                - `layout.CENTER_TOP `
                - `layout.CENTER_RIGHT`
                - `layout.CENTER_BOTTOM `
                - `layout.CENTER_LEFT`
            spacing (int): Espacio en píxeles entre los elementos.
            margins (tuple[int, int, int, int]): Márgenes alrededor del layout.
                Siguiendo el orden: `left`, `top`, `right`, `bottom`.
            size_constraint (QLayout.SizeConstraint): Restricción de tamaño para el layout.\n
                Puede ser uno de los siguientes valores predefinidos:
                - `layout.DEFAULT`
                - `layout.FIXED`
                - `layout.MINIMUM`
                - `layout.MAXIMUM`
                - `layout.WITHOUT`
                - `layout.MIN_AND_MAX`
        """
        configure_process(self, self._MAPPING_METHODS, **kwargs)

    def _process_kwargs(self, _type: type[TWidget], *args, **kwargs) -> TWidget | None:
        """
        This method determines whether or not to create a Widget, depending on the supplied arguments.\n
        It then establishes parentage relationships and adds it to the Layout.
        """
        exists: bool = False

        # If the supplied argument is already a widget
        if args:
            widget = args[0]
            exists = True

        else:
            # Create the widget
            widget = _type(**kwargs)
            
        # Add to layout
        self.addWidget(widget)

        # Return
        return None if exists else widget

    
    # --------------------------------- API ----------------------------------------------

    def from_factory(self, factory_widget: Callable, returns: bool = False) -> Callable:

        def addWidgetToLayout(*args, **kwargs) -> QWidget | None:

            widget = factory_widget(*args, **kwargs)

            self.addWidget(widget)

            if returns:
                return widget

        return addWidgetToLayout
    
    def Template(self, view_class) -> None:

        # view_class: Template -> fluvel/core/abstract_models/ABCAbstractView/Template
        view_instance = view_class(self)

        view_instance.build_ui()
        
        # Añado el QWidget contenedor de la clase vista
        self.addWidget(view_instance.container)


    @overload
    def Label(self, **kwargs: Unpack[FLabelKwargs]) -> FLabel: ...

    @overload
    def Label(self, arg__1: FLabel) -> None: ...

    def Label(self, *args, **kwargs) -> FLabel | None:
        """
        Creates and adds a Label widget to the layout.
    
        This method can either create a new :class:`~fluvel.components.widgets.FLabel`
        instance based on the provided keyword arguments or add an existing one
        to the layout.
    
        :param text: The text to display on the label. Can be a string or a list
                     for i18n lookup.
        :type text: str | Stringvar | list[str]
        :param style: A string of space-separated QSS class names to apply to the label.
        :type style: str
        :param alignment: The alignment of the label's text.
        :type alignment: Qt.AlignmentFlag
        
        .. seealso::
            :class:`~fluvel.components.widgets.FLabel` for all available parameters
            and signals.

        :returns: The created :class:`~fluvel.components.widgets.FLabel` instance, or
                  None if an existing widget was provided.
        :rtype: FLabel | None
    
        Example:
        --------
        .. code-block:: python
            ...
            with self.Vertical(self.container) as v:
                # Creates a new label
                my_label = v.Label(text="Hello, Fluvel", style="h1 bold")
                
                # Adds an existing label
                my_label_2 = FLabel(text="Already created")
                v.Label(my_label_2)
        
        """

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
    def LineEdit(self, **kwargs: Unpack[FLineEditKwargs]) -> FLineEdit: ...

    @overload
    def LineEdit(self, arg__1: FLineEdit) -> None: ...

    def LineEdit(self, *args, **kwargs) -> FLineEdit | None:

        # create the line edit if it doesn't exist or just add it to the layout,
        # then return the FLineEdit instance or None if it's already a widget
        return self._process_kwargs(FLineEdit, *args, **kwargs)
    
    @overload
    def CheckBox(self, **kwargs: Unpack[FCheckBoxKwargs]) -> FCheckBox: ...
    
    @overload
    def CheckBox(self, arg__1: FCheckBox) -> None: ...
    
    def CheckBox(self, *args, **kwargs) -> FCheckBox | None:
        
        # create the CheckBox if it doesn't exist or just add it to the layout,
        # then return the FCheckBox instance or None if it's already a widget
        return self._process_kwargs(FCheckBox, *args, **kwargs)

    @overload
    def RadioButton(self, **kwargs: Unpack[FRadioButtonKwargs]) -> FRadioButton: ...
    
    @overload
    def RadioButton(self, arg__1: FRadioButton) -> None: ...
    
    def RadioButton(self, *args, **kwargs) -> FRadioButton | None:
        
        # create the RadioButton if it doesn't exist or just add it to the layout,
        # then return the FRadioButton instance or None if it's already a widget
        return self._process_kwargs(FRadioButton, *args, **kwargs)