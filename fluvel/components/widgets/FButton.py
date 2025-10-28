from typing import Literal, TypedDict, Unpack

# Fluvel
from fluvel.core.abstract_models.FluvelWidget import FluvelWidget
from fluvel.core.abstract_models.FluvelTextWidget import FluvelTextWidget
from fluvel.components.gui import StringVar

from fluvel.core.enums.alignment import AlignmentTypes

# PySide6
from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon

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
    text            : str | list
    textvariable    : StringVar
    style           : ButtonStyles
    checkable       : bool
    icon            : QIcon
    icon_size       : tuple[int, int]
    
    # Shape and behavior
    size            : tuple[int, int]

    # Signals
    on_click        : callable
    on_pressed      : callable
    on_released     : callable
    on_toggled      : callable

    # Layout alignment
    alignment       : AlignmentTypes 


class FButton(QPushButton, FluvelWidget, FluvelTextWidget):
    """
    Clase base de **`Fluvel`** para **`QPushButton`**.
    """

    WIDGET_TYPE: str = "QPushButton"

    _MAPPING_METHODS: dict = {
        "text": "setText",
        "checkable": "setCheckable",
        "icon": "setIcon",
        "icon_size": "setIconSize",
        # Signals
        "on_click": "clicked",
        "on_pressed": "pressed",
        "on_released": "released",
        "on_toggled": "toggled",
        # Shape and behavior
        "size": "setFixedSize"
    }

    def __init__(self, **kwargs: Unpack[FButtonKwargs]):
        super().__init__()

        self._set_defaults()

        self.configure(**kwargs)

    def configure(self, **kwargs: Unpack[FButtonKwargs]) -> None:

        # Aplicando los estilos QSS
        kwargs = self._apply_styles(**kwargs)

        kwargs = self.get_static_text(**kwargs)

        if icon_size:=kwargs.get("icon_size"):

            kwargs["icon_size"] = QSize(*icon_size)

        configure_process(self, self._MAPPING_METHODS, **kwargs)


    def _set_defaults(self) -> None:

        self._set_widget_defaults()

        # Aplicar el cursor de puntero
        self.setCursor(Qt.PointingHandCursor)