from typing import Literal, TypedDict, Unpack

# Fluvel
from fluvel.core.abstract_models.FluvelWidget import FluvelWidget
from fluvel.core.abstract_models.FluvelTextWidget import FluvelTextWidget
from fluvel.components.gui import StringVar

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


class FButtonKwargs(TypedDict, total=False):
    content_id: str | tuple | None
    text: str | None
    textvariable: StringVar | None
    style: ButtonStyles | None
    checkable: bool | None

    # Signals
    on_click: any 
    on_pressed: any
    on_released: any
    on_toggled: any


class FButton(QPushButton, FluvelWidget, FluvelTextWidget):
    """
    Clase base de **`Fluvel`** para **`QPushButton`**.
    """

    _MAPPING_METHODS = {
        "text": "setText",
        "content_id": "setText",
        "checkable": "setCheckable",
        # Signals
        "on_click": "clicked",
        "on_pressed": "pressed",
        "on_released": "released",
        "on_toggled": "toggled"
    }

    def __init__(self, **kwargs: Unpack[FButtonKwargs]):
        super().__init__()

        # Aplicando los estilos QSS
        kwargs = self._apply_styles(**kwargs)

        # Aplicar el cursor de puntero
        self.setCursor(Qt.PointingHandCursor)

        self.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        self.configure(**kwargs)

    def configure(self, **kwargs: Unpack[FButtonKwargs]) -> None:

        kwargs = self.get_static_text(**kwargs)

        configure_process(self, self._MAPPING_METHODS, **kwargs)


class FLinkButton(FButton):
    def __init__(self, link: str, **kwargs: Unpack[FButtonKwargs]):
        super().__init__(**kwargs)
        self.link = link
        self.clicked.connect(self.open_link)

    def open_link(self):
        QDesktopServices.openUrl(QUrl(self.link))
