# Fluvel
from fluvel.components.gui import StyledText

# PySide6
from PySide6.QtWidgets import QLabel, QLineEdit
from PySide6.QtCore import Qt


class FluvelTextWidget:
    """
    Clase que se encarga de obtener el contenido estático usando
    el método get_static_text y la clase StyledText.
    Una vez obtenidos los bloques de contenido estático,
    modifica y retorna los respectivos kwargs.
    """

    def get_static_text(self, **kwargs) -> dict[str, any]:
        """ """

        if "content_id" in kwargs:

            kwargs = self._is_text_content(**kwargs)

        if "placeholder_id" in kwargs:

            kwargs = self._is_placeholder_content(**kwargs)

        return kwargs

    def _is_text_content(self, **kwargs) -> dict[str, any]:

        content_id = kwargs["content_id"]

        # El Texto contiene marcadores de posición
        if isinstance(content_id, tuple):

            kwargs["text"] = self._process_markers(content_id)

        if isinstance(content_id, str):

            kwargs["text"] = self._process_content(content_id)

        # Habilitar la apertura de enlaces si es un Label
        if isinstance(self, QLabel):

            self.setTextFormat(Qt.TextFormat.RichText)

            self.setOpenExternalLinks(True)

        kwargs.pop("content_id")

        return kwargs

    def _is_placeholder_content(self, **kwargs) -> dict[str, any]:

        place_id = kwargs["placeholder_id"]

        # El Texto contiene marcadores de posición
        if isinstance(place_id, tuple):

            kwargs["placeholder_id"] = self._process_markers(place_id)

        if isinstance(place_id, str):

            # Setting the value in kwargs
            kwargs["placeholder_id"] = self._process_content(place_id)

        # El campo es para una contraseña
        if "password" in place_id and isinstance(self, QLineEdit):
            # Changing the echo mode to password
            self.setEchoMode(self.EchoMode.Password)

        return kwargs

    def _process_markers(self, content: tuple) -> str:

        _id, *placeholders = content

        return StyledText(_id, *placeholders).text

    def _process_content(self, content: str) -> str:

        return StyledText(content).text
