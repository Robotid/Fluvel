# core.GlobalContent.py
from utils import filter_by_extension
from pathlib import Path
from core.core_utils.content_loader import load_fluml
from src import convert_FLUML_to_HTML


class GlobalContent:
    """
    Una clase que almacena como atributos de clase
    estructuras de datos que contienen los recursos estáticos
    del proyecto y sirve como modelo para el acceso a través de controladores.
    """

    content_map: dict = {}

    @staticmethod
    def initialize(content_path: Path | str) -> None:
        """
        Esta función carga los archivos de contenido de la aplicación.
        """

        # Obtener los archivos estáticos
        files = filter_by_extension(content_path, ".fluml")

        # Concatenar el contenido de los archivos
        fluml_content: str = ""

        # Formar la cadena con todos los archivos
        for file in files:
            fluml_content += "{}\n".format(load_fluml(file))

        # Parsear el archivo
        html_content: dict = convert_FLUML_to_HTML(fluml_content)

        # Mapeamos los key-word arguments
        for _id, text in html_content.items():
            GlobalContent.content_map[_id] = text
