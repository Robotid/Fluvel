from typing import TypeDict, Unpack

# PySide6
from PySide6.QtWidgets import QRadioButton

class FRadioButtonKwargs(TypeDict, total=False):
    ...

class FRadioButton(QRadioButton):

    _MAPPING_METHODS: dict = {}

    def __init__(self, **kwargs: Unpack[FRadioButtonKwargs]):

        ...

    def configure(self, **kwargs: Unpack[FRadioButtonKwargs]) -> None:

        ...