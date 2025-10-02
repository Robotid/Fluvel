from typing import Literal, TypedDict, Unpack

# Fluvel
from fluvel.core.abstract_models.FluvelWidget import FluvelWidget
from fluvel.core.abstract_models.FluvelTextWidget import FluvelTextWidget
from fluvel.components.gui import StringVar

# PySide6
from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QDesktopServices

# Fluvel core utils
from fluvel.core.tools import configure_process

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


class FButtonKwargs(TypedDict, total=False):
    text: str | list
    textvariable: StringVar
    style: ButtonStyles
    checkable: bool

    # Signals
    on_click: callable
    on_pressed: callable
    on_released: callable
    on_toggled: callable


class FButton(QPushButton, FluvelWidget, FluvelTextWidget):
    """
    Clase base de **`Fluvel`** para **`QPushButton`**.
    """

    _MAPPING_METHODS: dict = {
        "text": "setText",
        "checkable": "setCheckable",
        # Signals
        "on_click": "clicked",
        "on_pressed": "pressed",
        "on_released": "released",
        "on_toggled": "toggled",
    }

    def __init__(self, **kwargs: Unpack[FButtonKwargs]):
        super().__init__()

        # Aplicando los estilos QSS
        kwargs = self._apply_styles(**kwargs)

        # Aplicar el cursor de puntero
        self.setCursor(Qt.PointingHandCursor)

        self.configure(**kwargs)

    def configure(self, **kwargs: Unpack[FButtonKwargs]) -> None:

        kwargs = self.get_static_text(**kwargs)

        configure_process(self, self._MAPPING_METHODS, **kwargs)


class FLinkButton(FButton):
    def __init__(self, url: str, **kwargs: Unpack[FButtonKwargs]):
        super().__init__(**kwargs)
        self.url = url
        self.clicked.connect(self.open_link)

    def open_link(self):
        QDesktopServices.openUrl(QUrl(self.url))
