from pathlib import Path
import json

# Fluvel Utils
from fluvel.utils.paths import CONTENT_DIR, PROD_CONTENT_DIR, THEMES_DIR, PROD_THEMES_DIR
from fluvel.src import convert_FLUML_to_HTML
from fluvel.core.tools.content_loader import load_fluml
from fluvel.src.XmlMenuParser.xmlparsev3 import XMLMenuParser
from fluvel.core.tools.theme_loader import load_theme, load_style_sheet
from fluvel._user.GlobalConfig import AppConfig

# Exceptions Handler
from fluvel.core.exceptions.exceptions import ContentLoadingError

class ContentHandler:
    """
    Gestiona la carga y el procesamiento de los archivos de contenido.

    Esta clase es responsable de interactuar con el sistema de archivos para
    encontrar, leer y procesar los archivos de contenido.
    """
    MENU_CONTENT: dict = {}
    STATIC_CONTENT: str
    current_lang: str = None

    @classmethod
    def load_content(cls, mode: str, lang: str) -> None:
        """
        Inicializa el manejador de contenido según el entorno (prod/dev) y el idioma.

        :param mode: El modo de ejecución ('production' o 'development').
        :type mode: str
        :param lang: El código del idioma a cargar (e.g. 'es', 'en', etc.)
        :type lang: str
        """

        cls.mode = mode

        if lang != cls.current_lang:

            cls.current_lang = lang

            if mode == "production":

                # en producción, se cargan los archivos .json pre-compilados
                cls.select_mode(("json", "json"), PROD_CONTENT_DIR / cls.current_lang)

            else:

                # en desarrollo, se implementa la carga de archivos .fluml
                cls.select_mode(("fluml", "xml"), CONTENT_DIR / cls.current_lang)

    @classmethod
    def select_mode(cls, extension: str | tuple[str, str], content_folder: Path) -> None:
        """
        Su función es la carga y procesamiento de archivos según la extensión y la ruta.

        :param extension: La extensión del archivo a buscar.
        :type extension: str
        :param content_folder: La carpeta raíz del contenido para un idioma.
        :type content_folder: Path
        """
        menu_files, files = cls.load_files(content_folder, extension)

        # Procesa y almacena los diccionarios de contenido crudo.
        cls.process_menu(menu_files)

        cls.STATIC_CONTENT: dict = cls.process_static(files)

    @classmethod
    def process_menu(cls, menu_files: list[Path]) -> None:
        """
        Parsea el archivo de menú y lo devuelve como un diccionario.

        :param menu_files: La lista de archivos `xml` o `json` de los menus.
        :type menu_files: list[Path]
        """

        if cls.mode == "development":
            
            for file in menu_files:

                cls.MENU_CONTENT[file.stem] = XMLMenuParser(file).parse()
        else:
            for file in menu_files:

                with open(file, "r", encoding="utf-8") as f:

                    cls.MENU_CONTENT = json.load(f)

    @classmethod
    def process_theme(cls) -> str:
        """
        Carga y retorna un tema `qss`.

        :returns: Una cadena con el contenido QSS de los archivos de un tema.
        :rtype: str
        """
        
        theme = AppConfig.ui.theme

        if cls.mode == "development":

            return load_theme(THEMES_DIR, theme)

        return load_style_sheet(PROD_THEMES_DIR / f"{theme}.qss")

    @classmethod
    def process_static(cls, files: list[Path]) -> dict:
        """
        Concatena y parsea todos los archivos de contenido estático.

        :param files: La lista de archivos `fluml` o `json`.
        :type files: list[Path]
        """

        if cls.mode == "development":

            fluml_content = ""

            for file in files:
                fluml_content += "{}\n".format(load_fluml(file))

            return convert_FLUML_to_HTML(fluml_content)
        
        lang_file = PROD_CONTENT_DIR / cls.current_lang / f"{cls.current_lang}.json"
        
        with open(lang_file, "r", encoding="utf-8") as f:

            return json.load(f)


    @staticmethod
    def load_files(content_folder: Path, extension: tuple[str, str]) -> tuple[list[Path], list[Path]]:
        """
        Encuentra los archivos de menú y contenido estático en el disco.

        :param content_folder: La carpeta donde buscar los archivos.
        :type content_folder: Path
        :param extension: La extensión de los archivos a buscar.
        :type extension: str

        :returns: Una tupla que contiene la lista con las rutas de los archivos de menú y otra con los demás archivos de contenido.
        :rtype: tuple[list[Path], list[Path]]
        """
        try:

            # Static Content
            menu_files = [f for f in Path(content_folder / "menus").rglob(f"*.{extension[1]}")]

            files = [  
                file for file in content_folder.rglob(f"*.{extension[0]}")
                if file not in menu_files
            ]

            return menu_files, files

        except StopIteration:

            raise ContentLoadingError(f"Error trying to load {content_folder} JSON/XML files. The folder may not exist.")