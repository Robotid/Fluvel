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
        Este método carga y mapea a `ID: str -> CONTENT: StringVar` los
        archivos `.fluml` de la aplicación o actualiza los existentes
        con nuevos valores.

        Args:
            content_path (Path | str): La ruta al directorio con los archivos .fluml.

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
        """
        Actualiza el valor de los StringVars existentes con nuevos contenidos.

        Args:
            html_content (dict): Un diccionario con los nuevos IDs y valores.
        """ 

        for _id, text in html_content.items():

            # Actualizamos el texto base del StringVar
            # Lo que desencaden una serie de eventos dentro
            # de la clase StringVar para actualizar el contenido
            GlobalContent.content_map[_id].base_text = text
