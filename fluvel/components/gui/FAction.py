from typing import TypedDict, Unpack

# Fluvel
from fluvel.components.gui.StringVar import StringVar

# PySide6
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QAction



class FActionKwargs(TypedDict, total=False):

    text: str | StringVar

class FAction(QAction):

    _MAPPING_METHODS = {"text": "setText"}

    def __init__(self, parent: QWidget, **kwargs: Unpack[FActionKwargs]) -> None:
        super().__init__(parent)

        self.configure(**kwargs)

    def configure(self, **kwargs: Unpack[FActionKwargs]) -> None:

        if text:=kwargs.get("text"):

            if isinstance(text, StringVar):
                text.valueChanged.connect(self.setText)
                text = text.value
            
            self.setText(text)