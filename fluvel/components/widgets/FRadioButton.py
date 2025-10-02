from typing import TypedDict, Unpack

# Fluvel
from fluvel.core.abstract_models.FluvelTextWidget import FluvelTextWidget

# PySide6
from PySide6.QtWidgets import QRadioButton

# Core
from fluvel.core.tools import configure_process

class FRadioButtonKwargs(TypedDict, total=False):
    text: str | list

class FRadioButton(QRadioButton, FluvelTextWidget):

    _MAPPING_METHODS: dict = {"text": "setText"}

    def __init__(self, **kwargs: Unpack[FRadioButtonKwargs]):
        super().__init__()

        self.configure(**kwargs)

    def configure(self, **kwargs: Unpack[FRadioButtonKwargs]) -> None:

        kwargs = self.get_static_text(**kwargs)

        configure_process(self, self._MAPPING_METHODS, **kwargs)