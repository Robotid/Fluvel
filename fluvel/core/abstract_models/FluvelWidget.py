# PySide6
from PySide6.QtCore import Qt

# Separar por propiedades de diseño y propiedades de estilo


class FluvelWidget:

    def _apply_styles(self, **kwargs) -> dict[str, any]:
        """
        Método que aplica los estilos QSS individuales del componente
        configurado en el parámetro 'style' de cada uno.
        """

        if "style" in kwargs:

            self.setProperty("class", kwargs["style"])
            kwargs.pop("style")

        return kwargs
