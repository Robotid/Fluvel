from PySide6.QtCore import QObject, Signal, Property

class StringVar(QObject):

    # Se usa Camel-Case para mantener la consistencia
    # con la declaración de señales de PySide6
    valueChanged = Signal(str)

    # este atributo almacenará los textos
    _value: str = "" 

    def __init__(self, value: str = ""):
        super().__init__()

        self.value = value

    @Property(str, notify=valueChanged)
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value: str):
        if self._value != new_value:
            self._value = new_value
            self.valueChanged.emit(self._value)