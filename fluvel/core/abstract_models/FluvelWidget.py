
class FluvelWidget:

    def _apply_styles(self, **kwargs) -> dict[str, any]:
        """
        Método que aplica los estilos QSS individuales del componente
        configurado en el parámetro 'style' de cada uno.
        """

        if style := kwargs.get("style"):

            if _property := self.property("class"):

                full_style = "{} {}".format(_property, style)

                self.setProperty("class", full_style)

            else:

                self.setProperty("class", style)
        
            kwargs.pop("style")

        return kwargs
