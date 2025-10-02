from typing import TypedDict, Unpack

# Fluvel
from fluvel.components.gui.StringVar import StringVar

# PySide6
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QAction


class FActionKwargs(TypedDict, total=False):

    text: str | StringVar | None

class FAction(QAction):

    _MAPPING_METHODS = {"text": "setText"}

    def __init__(self, parent: QWidget, **kwargs: Unpack[FActionKwargs]) -> None:
        super().__init__(parent)

        self.configure(**kwargs)

    def configure(self, **kwargs: Unpack[FActionKwargs]) -> None:

        if "text" in kwargs:
            string_var = kwargs["text"]
            string_var.valueChanged.connect(self.setText)
            self.setText(string_var.value)