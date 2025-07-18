from PySide6.QtWidgets import QLabel
from typing import Literal

LabelType = Literal["InfoAlert", "WarningAlert", "SuccessAlert", "DangerAlert"]

class FluvelLabel(QLabel):
    """
    Clase base de **`Fluvel`** para etiquetas estilizadas. Las subclases deben definir el atributo '_label_type'.
    """

    _label_type: LabelType

    def __init__(self, text: str):
        super().__init__(text)
        
        # Nombre Representativo del componente en el archivo 'theme/push_button.qss'
        self.setObjectName(self._label_type) 

class Label(FluvelLabel):
    def __init__(self, text: str, _type: LabelType = "Label"):
        
        # set the label type
        self._label_type = _type

        super().__init__(text)

class InfoAlert(FluvelLabel):
    _label_type = "InfoAlert"

class WarningAlert(FluvelLabel):
    _label_type = "WarningAlert"

class SuccessAlert(FluvelLabel):
    _label_type = "SuccessAlert"

class DangerAlert(FluvelLabel):
    _label_type = "DangerAlert"

