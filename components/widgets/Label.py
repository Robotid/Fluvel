from typing import Literal, TypedDict, Unpack

# Fluvel
from components.gui import StyledText
from core.FluvelWidget import FluvelWidget
from core.core_models.FluvelTextWidget import TextWidget

# PySide 6
from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt

# Fluvel core utils
from core.core_utils import configure_process

LabelStyles = Literal["normal", "info", "success", "warning", "danger"]

class LabelKwargs(TypedDict, total=False):
    content_id: StyledText | None
    text: str | None
    alignment: Qt.AlignmentFlag | None
    style: LabelStyles | None
    # pixmap
    # movie
    # wordWrap
    # indent
    # margin
    # scaled_contents
    # open_external_links
    # text_interaction_flags
    # has_selected_text
    # selected_text
    # buddy

class Label(QLabel, FluvelWidget, TextWidget):
    """
    Clase base de **`Fluvel`** para **`QLabel`**.
    """

    _MAPPING_METHODS = {
        "text": "setText",
        "alignment": "setAlignment"
    }

    def __init__(self, **kwargs: Unpack[LabelKwargs]):
        super().__init__()

        # Aplicando los estilos QSS
        kwargs = self._apply_styles(**kwargs)

        self.configure(**kwargs)

    def configure(self, **kwargs: Unpack[LabelKwargs]) -> None:

        kwargs = self.get_static_text(**kwargs)

        configure_process(self, self._MAPPING_METHODS, **kwargs)
