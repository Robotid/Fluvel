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
        """ """

        if "content_id" in kwargs:
            
            content_id = kwargs["content_id"]

            kwargs = self.get_string_var(content_id, "content_id", "setText", **kwargs)
           
            
        if "placeholder_id" in kwargs:

            place_id = kwargs["placeholder_id"]

            kwargs = self.get_string_var(place_id, "placeholder_id", "setPlaceholderText", **kwargs)

            if "password" in place_id and isinstance(self, QLineEdit):

                # Changing the echo mode to password
                self.setEchoMode(self.EchoMode.Password)
            

        if "textvariable" in kwargs:

            kwargs = self._is_text_variable(**kwargs)


        return kwargs

    
    def _is_text_variable(self, **kwargs) -> dict[str, any]:

        string_var: StringVar = kwargs["textvariable"]

        string_var.valueChanged.connect(self.setText)

        kwargs["text"] = string_var.value

        kwargs.pop("textvariable")

        return kwargs

    def get_string_var(self, _id: str, flag: str, method: any, **kwargs) -> None:
        
        if isinstance(_id, tuple):

            content_id, *markers = _id

            string_var: StringVar = StyledText(content_id, *markers).var

        else:

            string_var: StringVar = StyledText(_id).var

        string_var.valueChanged.connect(getattr(self, method))

        kwargs[flag] = string_var.value

        return kwargs