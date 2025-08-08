from typing import TypedDict, Unpack

# Fluvel
from core.FluvelWidget import FluvelWidget
from core.core_models.FluvelTextWidget import TextWidget

# PySide6
from PySide6.QtWidgets import QLineEdit

# Fluvel core utils
from core.core_utils import configure_process

class LineEditKwargs(TypedDict, total=False):
    content_id: str | tuple | None
    text: str | None
    placeholder_id: str | None

class LineEdit(QLineEdit, FluvelWidget, TextWidget):
    """
    Clase base de **`Fluvel`** para **`QLineEdit`**.
    """

    _MAPPING_METHODS = {
        "text": "setText",
        "placeholder_id": "setPlaceholderText"
    }

    def __init__(self, **kwargs: Unpack[LineEditKwargs]):
        super().__init__()
        
        self.configure(**kwargs)

    def configure(self, **kwargs: Unpack[LineEditKwargs]) -> None:

        kwargs = self.get_static_text(**kwargs)

        configure_process(self, self._MAPPING_METHODS, **kwargs)
