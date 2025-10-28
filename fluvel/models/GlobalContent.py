# Fluvel
from fluvel.components.gui.StringVar import StringVar

class GlobalContent:
    """
    Gestor del contenido de texto dinámico de la aplicación obtenidos de arhivos
    `FLUML` o `JSON`

    Almacena todo el contenido de la UI (texto general y menús) en diccionarios
    estáticos (atributos de clase). Cada pieza de contenido se envuelve en un
    objeto `StringVar` para permitir la reactividad en toda la aplicación.

    Esta clase utiliza únicamente métodos estáticos, ya que no necesita ser
    instanciada.
    """

    content_map: dict[str, StringVar] = {}
    menu_content: dict[str, StringVar] = {}

    @classmethod
    def initialize(cls, menu_content: dict, static_content: dict) -> None:
        """
        Inicializa o actualiza el estado del contenido global de la aplicación.

        :param menu_content: El diccionario con la estructura de cada menú de la aplicación.
        :type menu_content: dict
        :param static_content: El diccionario con los datos del contenido de texto general.
        :type static_content: dict
        """
        # Se carga el contenido de la barra de menú de la aplicación
        cls._load_menu(menu_content)

        # Se inicia la carga del contenido estático de la aplicación
        cls._load_static(static_content)

    @classmethod
    def _load_static(cls, static_content: dict) -> None:
        """
        Carga el contenido estático en el mapa de estado `content_map`.

        :param static_content: El diccionario con los datos del contenido de texto general.
        :type static_content: dict
        """

        cls._load_structure(static_content, "content_map")

    @classmethod
    def _load_menu(cls, menu_content: dict) -> None:
        """
        Transforma y carga el contenido del menú en `menu_content`.

        :param menu_content: El diccionario con la estructura de cada menú de la aplicación.
        :type menu_content: dict
        """

        # se 'aplana' el diccionario con la estructura del menú
        menu_map: dict = cls._map_menu(menu_content)

        # se carga o actualiza el contenido de 'GlobalContent.menu_content'
        cls._load_structure(menu_map, "menu_content")

    @classmethod
    def _load_structure(cls, structure: dict, map_name: str) -> None:
        """
        Puebla o actualiza un mapa de estado (`content_map` o `menu_content`).

        Distingue entre la carga inicial (creando nuevos StringVars) y las
        cargas posteriores (actualizando los existentes).

        :param structure: El diccionario de datos a cargar.
        :type structure: dict
        :param map_name: El nombre del atributo de clase a modificar
        :type map_name: str
        """
        map_to_modify: dict = getattr(cls, map_name)

        if not map_to_modify:

            for _id, text in structure.items():

                map_to_modify[_id] = StringVar(text)

        else:

            cls._update_content(structure, map_name)
    
    @staticmethod
    def _map_menu(items: dict) -> dict:
        """
        Transforma una estructura de menú anidada en un mapa plano (diccionario).

        :param: items: El diccionario anidado que representa la estructura del menú.
        :type items: dict

        :returns: Un diccionario plano donde cada clave es un ID único y cada valor es
                  el texto a mostrar.
        :rtype: dict
        """

        menu_map: dict = {}

        def create_menu_map(items: dict):
            """
            Función anidada recursiva para mapear las opciones de menú en un diccionario.

            Esta función recorre recursivamente el diccionario del menú para crear
            uno nuevo en formato plano, donde cada opción se mapea con su ID que apunta a su 
            TEXTO.
            """

            for _id, menu_dict in items.items():

                text = menu_dict.get("text")
                elements = menu_dict.get("elements")

                if text != "---":
                    menu_map[_id] = text

                if elements:

                    create_menu_map(elements)

        for structure in items.values():

            create_menu_map(structure)

        return menu_map

    @classmethod
    def _update_content(cls, updated_content: dict, map_name: str) -> None:
        """
        Actualiza la UI con un nuevo contenido `updated_content` al modificar
        el atributo `base_text` de un `StringVar`.

        :param updated_content: El diccionario con los nuevos IDs y valores de texto.
        :type updated_content: dict
        :param map_name: El nombre del diccionario en `GlobalContent` a actualizar.
        :type map_name: str
        """

        map_to_update = getattr(cls, map_name)

        for _id, text in updated_content.items():

            # Actualizamos el texto base del StringVar
            # Lo que desencaden una serie de eventos dentro
            # de la clase StringVar para actualizar el contenido
            map_to_update[_id].base_text = text
