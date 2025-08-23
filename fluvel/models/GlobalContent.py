# core.GlobalContent.py
from pathlib import Path

# Fluvel
from fluvel.utils import filter_by_extension
from fluvel.core.core_utils.content_loader import load_fluml
from fluvel.src import convert_FLUML_to_HTML, convert_FLUML_to_JSON
from fluvel.components.gui import StringVar


class GlobalContent:
    """
    Una clase que almacena como atributos de clase
    estructuras de datos que contienen los recursos estáticos
    del proyecto y sirve como modelo para el acceso a través de controladores.
    """

    content_map: dict[str, StringVar] = {}
    menu_content: dict[str, StringVar] = {}

    menu_counter: int = 0


    @staticmethod
    def initialize(content_path: Path | str) -> None:
        """
        Este método carga y mapea a `ID: str -> CONTENT: StringVar` los
        archivos `.fluml` de la aplicación o actualiza los existentes
        con nuevos valores.

        Args:
            content_path (Path | str): La ruta al directorio con los archivos .fluml.
        """
        # Se carga el contenido de la barra de menú de la aplicación
        GlobalContent._initialize_menu_bar(content_path)

        # Se inicia la carga del contenido estático de la aplicación    
        GlobalContent._initialize_content(content_path)
        

    @staticmethod
    def _initialize_content(content_path: Path | str):

        files = filter_by_extension(content_path, ".fluml")

        fluml_content: str = ""

        for file in files:
            fluml_content += "{}\n".format(load_fluml(file))

        html_content: dict = convert_FLUML_to_HTML(fluml_content)

        # Si el content_map no existe (al momento de la inicialización de la app)
        if not GlobalContent.content_map:

            for _id, text in html_content.items():

                GlobalContent.content_map[_id] = StringVar(text)

        # Si el content_map sí existe, entonces se actualizan los StringVars del 
        else:

            GlobalContent._update_content(html_content, "content_map")


    @staticmethod
    def _initialize_menu_bar(content_path: Path | str) -> None:
        
        # La localización del archivo fluml
        menu_file = content_path / "menus" / "menu.fluml"

        # El diccionario JSON ya parseado
        parsed_structure = convert_FLUML_to_JSON(menu_file)

        # Se genera el map de los menu map
        menu_map: dict = GlobalContent._map_menu(parsed_structure)

        # Si el menu_content no existe (al momento de la inicialización de la app)
        if not GlobalContent.menu_content:

            for _id, text in menu_map.items():

                GlobalContent.menu_content[_id] = StringVar(text)

        # Si el menu_content sí existe, entonces se actualizan los StringVars del menu_content
        else:

            GlobalContent._update_content(menu_map, "menu_content")

            
           
    @staticmethod
    def _map_menu(items: dict) -> dict:
        """
        Construye de forma recursiva un mapa de los menús y actions.
        """

        menu_map: dict = {}

        def create_menu_map(items: dict, counter: int = 0) -> None:
            for key, value in items.items():

                if isinstance(value, str):
                    # Caso 1: Es una acción o un separador
                    if value == "---":
                        continue
                    else:
                        menu_map[key] = value

                elif isinstance(value, dict):
                    
                    menu_key = f"menu_{GlobalContent.menu_counter}"

                    menu_map[menu_key] = key

                    GlobalContent.menu_counter += 1

                    create_menu_map(value, counter)
        
        # Se comienza a crear el menu map
        create_menu_map(items)

        # Se reinicia el contador Global
        GlobalContent.menu_counter = 0
    
        return menu_map


    @staticmethod
    def _update_content(updated_content: dict, map_name: str) -> None:
        """
        Actualiza el valor de los StringVars existentes con nuevos contenidos.

        Args:
            updated_content (dict): Un diccionario con los nuevos IDs y valores.
            map_name (str): El nombre del diccionario en GlobalContent a actualizar.
        """ 

        map_to_update = getattr(GlobalContent, map_name)

        for _id, text in updated_content.items():

            # Actualizamos el texto base del StringVar
            # Lo que desencaden una serie de eventos dentro
            # de la clase StringVar para actualizar el contenido
            map_to_update[_id].base_text = text