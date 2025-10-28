from typing import TypedDict, Unpack

# Fluvel
from fluvel.core.abstract_models.FluvelWidget import FluvelWidget

# PySide6
from PySide6.QtWidgets import QFrame

class FContainerKwargs(TypedDict, total=False):

    style: str

class FContainer(QFrame, FluvelWidget):

    WIDGET_TYPE: str = "QFrame"

    def __init__(self, **kwargs: Unpack[FContainerKwargs]):
        super().__init__()

        self._set_widget_defaults()

        self.configure(**kwargs)

    def configure(self, **kwargs: Unpack[FContainerKwargs]) -> None:

        kwargs = self._apply_styles(**kwargs)

