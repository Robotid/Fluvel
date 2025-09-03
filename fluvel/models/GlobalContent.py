# Fluvel
from fluvel.components.gui import StringVar


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

        Args:
            menu_content (dict): Diccionario con los datos 'crudos' del menú.
            static_content (dict): Diccionario con los datos 'crudos' del contenido estático.
        """
        # Se carga el contenido de la barra de menú de la aplicación
        cls._load_menu(menu_content)

        # Se inicia la carga del contenido estático de la aplicación
        cls._load_static(static_content)

    @classmethod
    def _load_static(cls, static_content: dict) -> None:
        """
        Carga el contenido estático en el mapa de estado `content_map`.
        """

        cls._load_structure(static_content, "content_map")

    @classmethod
    def _load_menu(cls, menu_content: dict) -> None:
        """
        Transforma y carga el contenido del menú en `menu_content`.
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

        Args:
            structure (dict): El diccionario de datos a cargar.
            map_name (str): El nombre del atributo de clase a modificar.
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

        Esta función recorre recursivamente el diccionario del menú para asignar
        IDs únicos a los submenús (QMenu) (ej. 'menu_0', 'menu_1') y mantener los IDs
        originales para las acciones (QAction).

        Args:
            items (dict): El diccionario anidado que representa la estructura del menú.

        Returns:
            dict: Un diccionario plano donde cada clave es un ID único y cada valor
                  es el texto a mostrar.
        """

        menu_map: dict = {}

        def create_menu_map(items: dict, counter: int) -> int:
            """
            Función anidada recursiva para gestionar el estado del contador.
            """

            for key, value in items.items():

                if isinstance(value, str):

                    # Es una acción de menú o un separador.
                    if value != "---":
                        menu_map[key] = value

                elif isinstance(value, dict):

                    # Es un submenú, por lo que se genera una clave única.
                    menu_key = f"menu_{counter}"

                    # El valor es el título del submenú
                    menu_map[menu_key] = key

                    counter += 1

                    # Llamada recursiva, pasando el contador actualizado.
                    counter = create_menu_map(value, counter)

            return counter

        # Se comienza a crear el menu map
        create_menu_map(items, 0)

        return menu_map

    @classmethod
    def _update_content(cls, updated_content: dict, map_name: str) -> None:
        """
        Actualiza la UI con un nuevo contenido `updated_content` al modificar
        el atributo `base_text` de un `StringVar`.

        Args:
            updated_content (dict): Un diccionario con los nuevos IDs y valores de texto..
            map_name (str): El nombre del diccionario en GlobalContent a actualizar.
        """

        map_to_update = getattr(cls, map_name)

        for _id, text in updated_content.items():

            # Actualizamos el texto base del StringVar
            # Lo que desencaden una serie de eventos dentro
            # de la clase StringVar para actualizar el contenido
            map_to_update[_id].base_text = text
