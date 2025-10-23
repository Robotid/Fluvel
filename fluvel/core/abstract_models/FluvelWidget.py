from fluvel.src.QSSProcessor.qss_processor import process_qss

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

            self.setStyleSheet(process_qss(style, self.WIDGET_TYPE, self.obj_name))

            kwargs.pop("style")

        return kwargs
    
    def _set_widget_defaults(self) -> None:

        # Estableciendo el nombre del objeto para
        # aplicar los estilos QSS
        self.obj_name: str = str(id(self))
        self.setObjectName(self.obj_name)