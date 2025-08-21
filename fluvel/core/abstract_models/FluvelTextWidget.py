# Fluvel
from fluvel.components.gui import StyledText, StringVar

# PySide6
from PySide6.QtWidgets import QLineEdit


class FluvelTextWidget:
    """
    Clase que se encarga de obtener el contenido estático usando
    el método get_static_text y la clase StyledText o StringVar.
    Una vez obtenidos los bloques de contenido estático,
    modifica y retorna los respectivos kwargs.
    """

    def get_static_text(self, **kwargs) -> dict[str, any]:
        """
        Procesa y retorna los argumentos de los widgets para manejar el contenido estático y dinámico.

        Args:
            **kwargs: Argumentos del constructor del widget.

        Returns:
            dict[str, any]: Un diccionario con los argumentos procesados.
        """

        if "text" in kwargs:

            content_id = kwargs["text"]

            kwargs = self.get_string_var(content_id, "text", "setText", **kwargs)

        if "placeholder_text" in kwargs:

            place_id = kwargs["placeholder_text"]

            kwargs = self.get_string_var(
                place_id, "placeholder_text", "setPlaceholderText", **kwargs
            )

            if "password" in place_id and isinstance(self, QLineEdit):

                # Changing the echo mode to password
                self.setEchoMode(self.EchoMode.Password)

        if "textvariable" in kwargs:

            kwargs = self._is_text_variable(**kwargs)

        return kwargs

    def _is_text_variable(self, **kwargs) -> dict[str, any]:
        """
        Conecta un StringVar a un widget.

        Args:
            **kwargs: Argumentos del constructor del widget.

        Returns:
            dict[str, any]: Argumentos actualizados sin la clave 'textvariable'.
        """

        string_var: StringVar = kwargs["textvariable"]

        string_var.valueChanged.connect(self.setText)

        kwargs["text"] = string_var.value

        kwargs.pop("textvariable")

        return kwargs

    def get_string_var(self, _id: str, flag: str, method: any, **kwargs) -> None:
        """
        Obtiene un StringVar para un ID de contenido y lo conecta a un método del widget.

        Args:
            _id (str | list): El ID de contenido o una lista que contiene el ID y marcadores de posición.
            flag (str): La clave del argumento ('text' o 'placeholder_text').
            method (any): El método del widget al que se conectará (e.g., setText).
            **kwargs: Argumentos del constructor del widget.
        """

        if isinstance(_id, list):

            content_id, *markers = _id

            string_var: StringVar = StyledText(content_id, *markers).var

            string_var.valueChanged.connect(getattr(self, method))

            kwargs[flag] = string_var.value

        # Si es un texto simple (una instancia de str), no ocurre nada

        return kwargs
