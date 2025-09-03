from typing import TypedDict, Unpack

# Fluvel
from fluvel.core.abstract_models.FluvelWidget import FluvelWidget
from fluvel.core.abstract_models.FluvelTextWidget import FluvelTextWidget

# PySide6
from PySide6.QtWidgets import QLineEdit

# Fluvel core utils
from fluvel.core.core_utils import configure_process


class FLineEditKwargs(TypedDict, total=False):
    text: str | None
    placeholder_text: str | None


class FLineEdit(QLineEdit, FluvelWidget, FluvelTextWidget):
    """
    Clase base de **`Fluvel`** para **`QLineEdit`**.
    """

    _MAPPING_METHODS = {"text": "setText", "placeholder_text": "setPlaceholderText"}

    def __init__(self, **kwargs: Unpack[FLineEditKwargs]):
        super().__init__()

        self.configure(**kwargs)

    def configure(self, **kwargs: Unpack[FLineEditKwargs]) -> None:

        kwargs = self.get_static_text(**kwargs)

        configure_process(self, self._MAPPING_METHODS, **kwargs)
