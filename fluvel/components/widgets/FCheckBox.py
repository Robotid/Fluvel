from typing import TypedDict, Unpack

# Fluvel
from fluvel.core.abstract_models.FluvelTextWidget import FluvelTextWidget
from fluvel.core.abstract_models.FluvelWidget import FluvelWidget
from fluvel.components.gui import StringVar

# PySide6
from PySide6.QtWidgets import QCheckBox

# Core-Utils
from fluvel.core.core_utils.core_process import configure_process


class FCheckBoxKwargs(TypedDict, total=False):
    text: str | list | None
    textvariable: StringVar | None


class FCheckBox(QCheckBox, FluvelTextWidget, FluvelWidget):

    _MAPPING_METHODS = {"text": "setText"}

    def __init__(self, **kwargs: Unpack[FCheckBoxKwargs]):
        super().__init__()

        self.configure(**kwargs)

    def configure(self, **kwargs: Unpack[FCheckBoxKwargs]) -> None:

        kwargs = self.get_static_text(**kwargs)

        configure_process(self, self._MAPPING_METHODS, **kwargs)
