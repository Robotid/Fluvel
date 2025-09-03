from pathlib import Path
import json

# Fluvel Utils
from fluvel.utils.paths import CONTENT_DIR, PROD_CONTENT_DIR
from fluvel.src import convert_FLUML_to_HTML, convert_FLUML_to_JSON
from fluvel.core.core_utils.content_loader import load_fluml

# Exceptions
from fluvel.core.exceptions import ContentLoadingError

class ContentHandler:
    """
    Gestiona la carga y el procesamiento de los archivos de contenido.

    Esta clase es responsable de interactuar con el sistema de archivos para
    encontrar, leer y procesar los archivos de contenido.
    """
    MENU_CONTENT: str
    STATIC_CONTENT: str
    current_lang: str = None

    @classmethod
    def load_content(cls, mode: str, lang: str) -> None:
        """
        Inicializa el manejador de contenido según el entorno (prod/dev) y el idioma.

        Args:
            mode (str): El modo de ejecución ('production' o 'development').
            lang (str): El código del idioma a cargar (ej. 'es', 'en').
        """

        if lang != cls.current_lang:

            cls.current_lang = lang

            if mode == "production":

                # en producción, se cargan los archivos .json pre-compilados
                cls.select_mode("json", PROD_CONTENT_DIR / cls.current_lang)

            else:

                # en desarrollo, se implementa la carga de archivos .fluml
                cls.select_mode("fluml", CONTENT_DIR / cls.current_lang)

    @classmethod
    def select_mode(cls, extension: str, content_folder: Path) -> None:
        """
        Su función es la carga y procesamiento de archivos según la extensión y la ruta.

        Args:
            extension (str): La extensión de archivo a buscar ('fluml' or 'json').
            content_folder (Path): La carpeta raíz del contenido para un idioma.
        """
        menu_file, files = cls.load_files(content_folder, extension)

        # Procesa y almacena los diccionarios de contenido crudo.
        cls.MENU_CONTENT: dict = cls.process_menu(menu_file, extension)

        cls.STATIC_CONTENT: dict = cls.process_static(files, extension)

    @staticmethod
    def process_menu(menu_file: Path, extension: str) -> dict:
        """
        Parsea el archivo de menú y lo devuelve como un diccionario.
        """

        if extension == "fluml":

            return convert_FLUML_to_JSON(menu_file)

        with open(menu_file, "r", encoding="utf-8") as f:

            return json.load(f)

    @classmethod
    def process_static(cls, files: list[Path], extension: str) -> dict:
        """
        Concatena y parsea todos los archivos de contenido estático.
        """

        if extension == "fluml":

            fluml_content = ""

            for file in files:
                fluml_content += "{}\n".format(load_fluml(file))

            html_content: dict = convert_FLUML_to_HTML(fluml_content)

            return html_content
        
        lang_file = PROD_CONTENT_DIR / cls.current_lang / f"{cls.current_lang}.json"
        
        with open(lang_file, "r", encoding="utf-8") as f:

            return json.load(f)

    @staticmethod
    def load_files(content_folder: Path, extension: str) -> tuple[Path, list[Path]]:
        """
        Encuentra los archivos de menú y contenido estático en el disco.

        Args:
            content_folder (Path): La carpeta donde buscar los archivos.
            extension (str): La extensión de los archivos a buscar.

        Returns:
            tuple[Path, list[Path]]: Una tupla conteniendo la ruta al archivo
                                     de menú y una lista de rutas a los demás
                                     archivos de contenido.
        """
        try:
            # Menu File
            menu_file: Path = next(content_folder.rglob(f"menu.{extension}"))

            # Static Content
            to_ignore = ("menu.fluml", "menu.json")

            files = [
                file
                for file in content_folder.rglob(f"*.{extension}")
                if file.name not in to_ignore
            ]

            return menu_file, files

        except StopIteration:

            raise ContentLoadingError(f"Error trying to load ./build_resources/ JSON files. The folder may not exist.")