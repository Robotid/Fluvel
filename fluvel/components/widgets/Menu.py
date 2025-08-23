from typing import TypedDict, Unpack

# Fluvel
from fluvel.components.gui.StringVar import StringVar

# PySide6
from PySide6.QtWidgets import QMenu

class MenuKwargs(TypedDict, total=False):

    title: str | StringVar | None

class Menu(QMenu):

    def __init__(self, parent, **kwargs: Unpack[MenuKwargs]) -> None:
        super().__init__(parent)

        self.configure(**kwargs)

    def configure(self, **kwargs: Unpack[MenuKwargs]) -> None:

        if "title" in kwargs:

            string_var = kwargs["title"]

            string_var.valueChanged.connect(self.setTitle)

            self.setTitle(string_var.value)