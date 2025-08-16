# core.GlobalContent.py
from fluvel.utils import filter_by_extension
from pathlib import Path
from fluvel.core.core_utils.content_loader import load_fluml
from fluvel.src import convert_FLUML_to_HTML
from fluvel.components.gui import StringVar

class GlobalContent:
    """
    Una clase que almacena como atributos de clase
    estructuras de datos que contienen los recursos estáticos
    del proyecto y sirve como modelo para el acceso a través de controladores.
    """

    content_map: dict[str, StringVar] = {}
    
    @staticmethod
    def initialize(content_path: Path | str) -> None:
        """
        Este método carga y mapea a `id -> StringVar` los 
        archivos `.fluml` de la aplicación o actualiza los existentes
        con nuevos valores.
        """

        files = filter_by_extension(content_path, ".fluml")

        fluml_content: str = ""

        for file in files:
            fluml_content += "{}\n".format(load_fluml(file))

        html_content: dict = convert_FLUML_to_HTML(fluml_content)

        # Si el content_map no existe (al momento de la inicialización de la app)
        if not GlobalContent.content_map:

            for _id, text in html_content.items():

                GlobalContent.content_map[_id] = StringVar(text)
    
        else:

            GlobalContent._update_content(html_content)

    @staticmethod
    def _update_content(html_content: dict) -> None:
        
        for _id, text in html_content.items():
            # Se actualizan los StringVar y estos
            # a su vez emiten las señales para
            # modificar el texto de los Widgets
            GlobalContent.content_map[_id].value = text