from typing import TypedDict, Unpack

# Fluvel
from fluvel.core.abstract_models.FluvelWidget import FluvelWidget
from fluvel.core.abstract_models.FluvelTextWidget import FluvelTextWidget

# PySide6
from PySide6.QtWidgets import QLineEdit

# Fluvel core utils
from fluvel.core.tools import configure_process


class FLineEditKwargs(TypedDict, total=False):
    text                : str
    placeholder_text    : str
    style               : str
    echo_mode           : str

class FLineEdit(QLineEdit, FluvelWidget, FluvelTextWidget):
    """
    Clase base de **`Fluvel`** para **`QLineEdit`**.
    """

    WIDGET_TYPE: str = "QLineEdit"

    _MAPPING_METHODS = {
        "text": "setText", 
        "placeholder_text": "setPlaceholderText",
        "echo_mode": "setEchoMode"
    }

    def __init__(self, **kwargs: Unpack[FLineEditKwargs]):
        super().__init__()

        self._set_widget_defaults()

        self.configure(**kwargs)

    def configure(self, **kwargs: Unpack[FLineEditKwargs]) -> None:

        kwargs = self._apply_styles(**kwargs)

        kwargs = self.get_static_text(**kwargs)

        if echo_mode:=kwargs.get("echo_mode"):
            kwargs["echo_mode"] = getattr(self.EchoMode, echo_mode)

        configure_process(self, self._MAPPING_METHODS, **kwargs)
