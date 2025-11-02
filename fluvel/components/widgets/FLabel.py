from typing import Literal, TypedDict, Unpack

# Fluvel
from fluvel.core.abstract_models.FluvelWidget import FluvelWidget
from fluvel.core.abstract_models.FluvelTextWidget import FluvelTextWidget
from fluvel.components.gui import StringVar

# PySide6
from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt

# Fluvel core utils
from fluvel.core.tools import configure_process
from fluvel.core.enums.alignment import Alignment, AlignmentTypes

FLabelKeys = Literal[
    "text",
    "textvariable",
    "style",
    "wordwrap",
    "align"
]

class FLabelKwargs(TypedDict, total=False):
    text            : str | list
    textvariable    : StringVar
    style           : str
    wordwrap        : bool
    align           : AlignmentTypes

    # Layout alignment
    alignment       : AlignmentTypes 

class FLabel(QLabel, FluvelWidget, FluvelTextWidget):
    """
    Clase base de **`Fluvel`** para **`QLabel`**.
    """

    _MAPPING_METHODS = {
        "text": "setText", 
        "align": "setAlignment", 
        "wordwrap": "setWordWrap",
    }

    def __init__(self, **kwargs: Unpack[FLabelKwargs]):
        super().__init__()

        # Configurando las propiedades por defecto de un Label
        self._set_defaults()

        self.configure(**kwargs)

    def configure(self, **kwargs: Unpack[FLabelKwargs]) -> None:

        # Aplicando los estilos QSS
        kwargs = self._apply_styles(**kwargs)

        # Aplicando el texto
        kwargs = self.get_static_text(**kwargs)

        if align:=kwargs.get("align"):

            kwargs["align"] = Alignment.get(align)

        configure_process(self, self._MAPPING_METHODS, **kwargs)

    def _set_defaults(self) -> None:

        self._set_widget_defaults()

        # Por defecto acepta la apertura de
        # enlaces externos
        self.setOpenExternalLinks(True)

        # Por defecto su formato de texto es RichText
        self.setTextFormat(Qt.TextFormat.RichText)

    def __setitem__(self, key: FLabelKeys, value: any):

        self.configure(**{key: value})
    
    def __getitem__(self, key: FLabelKeys):
         
        if key=="text":
            return self.text()
        
        if key=="align":
            return self.alignment()