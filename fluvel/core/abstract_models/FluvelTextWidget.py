# Fluvel
from components.gui import StyledText

# PySide6
from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt


class FluvelTextWidget:
    """
    Clase que se encarga de obtener el contenido estático usando
    el método get_static_text y la clase StyledText.
    Una vez obtenidos los bloques de contenido estático,
    modifica y retorna los respectivos kwargs.
    """

    def get_static_text(self, **kwargs) -> dict[str, any]:
        """
        if isinstance(kwargs["content_id"], tuple):
            _id, *placeholders = kwargs["content_id"]

            text = StyledText(_id, *placeholders)
        """

        if "content_id" in kwargs:

            text = StyledText(kwargs["content_id"]).text

            # Habilitar la apertura de enlaces
            if isinstance(self, QLabel):

                self.setTextFormat(Qt.TextFormat.RichText)

                self.setOpenExternalLinks(True)

            # Setting the value in kwargs
            kwargs["text"] = text

            kwargs.pop("content_id")

        if "placeholder_id" in kwargs:

            placeholder_text = StyledText(kwargs["placeholder_id"]).text

            # El campo es para una contraseña
            if "password" in kwargs["placeholder_id"]:
                # Changing the echo mode to password
                self.setEchoMode(self.EchoMode.Password)

            # Setting the value in kwargs
            kwargs["placeholder_id"] = placeholder_text

        return kwargs
