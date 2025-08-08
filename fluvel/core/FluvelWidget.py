
# PySide6
from PySide6.QtCore import Qt

# Separar por propiedades de diseño y propiedades de estilo

class FluvelWidget:
    
    # Alingment Flags
    TOP = Qt.AlignmentFlag.AlignTop
    BOTTOM = Qt.AlignmentFlag.AlignBottom
    RIGHT = Qt.AlignmentFlag.AlignRight
    LEFT = Qt.AlignmentFlag.AlignLeft
    CENTER = Qt.AlignmentFlag.AlignCenter
    H_CENTER = Qt.AlignmentFlag.AlignHCenter
    V_CENTER = Qt.AlignmentFlag.AlignVCenter
    # JUSTIFY = Qt.AlignmentFlag.AlignJustify # No es muy usado
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

    def _apply_styles(self, **kwargs) -> dict[str, any]:
        """
        Método que aplica los estilos QSS individuales del componente
        configurado en el parámetro 'style' de cada uno.
        """

        if "style" in kwargs:

            self.setProperty("class", kwargs["style"])
            kwargs.pop("style")
        
        return kwargs
