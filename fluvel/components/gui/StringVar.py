# PySide6
from PySide6.QtCore import QObject, Signal, Property


class StringVar(QObject):
    """
    Clase para representar una cadena de texto dinámica.
    Emite una señal cuando su valor es modificado.
    """

    # Se usa Camel-Case para mantener la consistencia
    # con la declaración de señales de PySide6
    valueChanged = Signal(str)

    # Este atributo almacena el texto que se usará
    # en los Widgets
    _value: str = ""

    # Este atributo almacena el texto original
    # con sus respectivos marcadores de posición
    # (si los contiene)
    _base_text: str = ""

    # Este atributo almacena un diccionario con los
    # objetos StringVar o 'str' que sustituyen a los
    # marcadores de posición en el texto, por los que
    # son mapeados según su posición.
    # ejemplo:
    # {0: StringVar, 1: str, 2: StringVar, 3: StringVar} y así...
    _MAPPING_MARKERS: dict = {}

    def __init__(self, value: str = ""):
        """
        Inicializa una instancia de StringVar.

        Args:
            value (str): El valor inicial de la cadena.
        """
        super().__init__()

        self.value = value

    @Property(str, notify=valueChanged)
    def value(self) -> str:
        """
        Getter para el valor de la cadena.

        Returns:
            str: El valor actual de la cadena.
        """
        return self._value

    @value.setter
    def value(self, new_value: str) -> None:
        """
        Setter para el valor de la cadena. Emite la señal `valueChanged`.

        Args:
            new_value (str): El nuevo valor para la cadena.
        """
        if self._value != new_value:

            self._value = new_value

            self.valueChanged.emit(self._value)

    @Property(str, notify=valueChanged)
    def base_text(self) -> str:
        """
        Getter para el texto base de la cadena.

        Este valor no incluye los marcadores de posición reemplazados.

        Returns:
            str: El texto base con marcadores.
        """
        return self._base_text

    @base_text.setter
    def base_text(self, new_value: str) -> None:
        """
        Setter para el texto base de la cadena.

        Cuando este valor cambia, se llama automáticamente al método `replace_markers`
        para reconstruir la cadena final y emitir la señal `valueChanged`.

        Args:
            new_value (str): El nuevo texto base.
        """
        if self._base_text != new_value:

            self._base_text = new_value

            self.replace_markers()

    def replace_markers(self) -> None:
        """
        Reemplaza los marcadores de posición ($0, $1, etc.) en el texto con los valores dados.

        Args:
            placeholders (tuple): Una tupla de cadenas o StringVars para los marcadores.
        """

        # El nuevo valor del StringVar
        new_value: str = self._base_text

        # Iteramos y reemplazamos los marcadores con texto
        for i, marker in self._MAPPING_MARKERS.items():

            if isinstance(marker, str):
                # El marcador es un simple texto tipo 'str', así que
                # no se intenta acceder a su atributo value
                new_value = new_value.replace(f"${i}", marker)

            else:
                # El marcador es un StringVar, por lo que obtenemos
                # el texto a través de su atributo value
                new_value = new_value.replace(f"${i}", marker.value)

        # Reemplazamos el texto antiguo con
        # el nuevo generado llamando al '@value.setter'
        self.value = new_value
