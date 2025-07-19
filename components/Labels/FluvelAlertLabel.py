from PySide6.QtWidgets import QLabel, QHBoxLayout, QFrame
from typing import Literal

AlertTypes = Literal["InfoAlert", "DangerAlert", "WarningAlert", "SuccessAlert"]

class FluvelAlertLabel(QFrame):
    """
    Clase base de **`Fluvel`** para etiquetas de alerta estilizadas. Las subclases deben definir el atributo **`_alert_type`**.
    """

    _alert_type: AlertTypes
    _icon: str #para implementar después

    def __init__(self, text: str):
        super().__init__()

        self.setObjectName(self._alert_type)

        # Texto del mensaje
        text_label = QLabel(text)
        text_label.setObjectName(f"{self._alert_type}Text")

        text_label.setWordWrap(True)  # Para múltiples líneas

        # Layout interno
        layout = QHBoxLayout()
        layout.addWidget(text_label)
        layout.setContentsMargins(1,1,1,1)
        layout.setSpacing(5)

        self.setLayout(layout)
        self.setFixedHeight(50)

class AlertLabel(FluvelAlertLabel):
    def __init__(self, text: str, _type: AlertTypes):

        # set the alert type
        self._alert_type = _type

        super().__init__(text)

class InfoAlert(FluvelAlertLabel):
    _alert_type = "InfoAlert"

class DangerAlert(FluvelAlertLabel):
    _alert_type = "DangerAlert"

class WarningAlert(FluvelAlertLabel):
    _alert_type = "WarningAlert"

class SuccessAlert(FluvelAlertLabel):
    _alert_type = "SuccessAlert"