from typing import Literal, TypedDict, Unpack

# Fluvel
from fluvel.core.abstract_models.FluvelWidget import FluvelWidget
from fluvel.core.abstract_models.FluvelTextWidget import FluvelTextWidget
from fluvel.components.gui import StringVar

# PySide6
from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt, QTimer

# Fluvel core utils
from fluvel.core.core_utils import configure_process


LabelStyles = Literal["normal", "info", "success", "warning", "danger"]


class FLabelKwargs(TypedDict, total=False):
    text: str | list
    textvariable: StringVar
    alignment: Qt.AlignmentFlag
    style: LabelStyles


class FLabel(QLabel, FluvelWidget, FluvelTextWidget):
    """
    Clase base de **`Fluvel`** para **`QLabel`**.
    """

    _MAPPING_METHODS = {"text": "setText", "alignment": "setAlignment"}

    def __init__(self, **kwargs: Unpack[FLabelKwargs]):
        super().__init__()

        # Configurando las propiedades por defecto de un Label
        self._set_defaults()

        # Aplicando los estilos QSS
        kwargs = self._apply_styles(**kwargs)

        self.configure(**kwargs)

    def configure(self, **kwargs: Unpack[FLabelKwargs]) -> None:

        kwargs = self.get_static_text(**kwargs)

        configure_process(self, self._MAPPING_METHODS, **kwargs)

    def _set_defaults(self) -> None:

        # Por defecto acepta la apertura de
        # enlaces externos
        self.setOpenExternalLinks(True)

        # Por defecto su formato de texto es RichText
        self.setTextFormat(Qt.TextFormat.RichText)