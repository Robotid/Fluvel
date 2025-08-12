from typing import Literal, TypedDict, Unpack

# Fluvel
from fluvel.core.abstract_models.FluvelWidget import FluvelWidget
from fluvel.core.abstract_models.FluvelTextWidget import FluvelTextWidget

# PySide6
from PySide6.QtWidgets import QPushButton, QSizePolicy
from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QDesktopServices

# Fluvel core utils
from fluvel.core.core_utils import configure_process

ButtonStyles = Literal[
    "primary",
    "secondary",
    "info",
    "success",
    "warning",
    "danger",
    "dark",
    "light",
    "primary-outlined",
    "secondary-outlined",
    "info-outlined",
    "success-outlined",
    "warning-outlined",
    "danger-outlined",
    "dark-outlined",
    "light-outlined",
]


class ButtonKwargs(TypedDict, total=False):
    content_id: str | tuple | None
    text: str | None
    style: ButtonStyles | None


class Button(QPushButton, FluvelWidget, FluvelTextWidget):
    """
    Clase base de **`Fluvel`** para **`QPushButton`**.
    """

    _MAPPING_METHODS = {"text": "setText"}

    def __init__(self, **kwargs: Unpack[ButtonKwargs]):
        super().__init__()

        # Aplicando los estilos QSS
        kwargs = self._apply_styles(**kwargs)

        # Aplicar el cursor de puntero
        self.setCursor(Qt.PointingHandCursor)

        # self.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        self.configure(**kwargs)

    def configure(self, **kwargs: Unpack[ButtonKwargs]) -> None:

        kwargs = self.get_static_text(**kwargs)

        configure_process(self, self._MAPPING_METHODS, **kwargs)


class LinkButton(Button):
    def __init__(self, link: str, **kwargs: Unpack[ButtonKwargs]):
        super().__init__(**kwargs)
        self.link = link
        self.clicked.connect(self.open_link)

    def open_link(self):
        QDesktopServices.openUrl(QUrl(self.link))
