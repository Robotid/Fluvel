from PySide6.QtWidgets import QLabel, QHBoxLayout, QFrame
from typing import Literal

AlertTypes = Literal["FluvelInfoAlert", "FluvelDangerAlert", "FluvelWarningAlert", "FluvelSuccessAlert"]

class FluvelAlertLabel(QFrame):
    """
    Clase base de **`Fluvel`** para etiquetas de alerta estilizadas. Las subclases deben definir el atributo **`_alert_type`**.
    """

    _alert_type: AlertTypes
    _icon: str #para implementar después

    def __init__(self, text: str) -> None:
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

class FluvelAlert(FluvelAlertLabel):
    def __init__(self, text: str, _type: AlertTypes):

        # set the alert type
        self._alert_type = _type

        super().__init__(text)

class FluvelInfoAlert(FluvelAlertLabel):
    _alert_type = "FluvelInfoAlert"

class FluvelDangerAlert(FluvelAlertLabel):
    _alert_type = "FluvelDangerAlert"

class FluvelWarningAlert(FluvelAlertLabel):
    _alert_type = "FluvelWarningAlert"

class FluvelSuccessAlert(FluvelAlertLabel):
    _alert_type = "FluvelSuccessAlert"