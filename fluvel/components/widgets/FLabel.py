from typing import Literal, TypedDict, Unpack

# Fluvel
from fluvel.core.abstract_models.FluvelWidget import FluvelWidget
from fluvel.core.abstract_models.FluvelTextWidget import FluvelTextWidget
from fluvel.components.gui import StringVar

# PySide 6
from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt

# Fluvel core utils
from fluvel.core.core_utils import configure_process


LabelStyles = Literal["normal", "info", "success", "warning", "danger"]


class FLabelKwargs(TypedDict, total=False):
    content_id: str | tuple | None
    text: str | None
    textvariable: StringVar | None
    alignment: Qt.AlignmentFlag | None
    style: LabelStyles | None
    # pixmap
    # movie
    # wordWrap
    # indent
    # margin
    # scaled_contents
    # text_interaction_flags
    # has_selected_text
    # selected_text
    # buddy


class FLabel(QLabel, FluvelWidget, FluvelTextWidget):
    """
    Clase base de **`Fluvel`** para **`QLabel`**.
    """

    _MAPPING_METHODS = {
        "text": "setText",
        "content_id": "setText",
        "alignment": "setAlignment"
    }

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

        self.setOpenExternalLinks(True)

        self.setTextFormat(Qt.TextFormat.RichText)
