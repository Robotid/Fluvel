from pathlib import Path
import xml.etree.ElementTree as ET

# Expect Handler
from fluvel.core.exceptions.expect_handler import expect

class XMLMenuParser:

    @expect.FileNotFound(stop=True)
    def __init__(self, xml_path: Path):
        """
        Inicializa el parser, cargando el archivo XML.

        Args:
            xml_path (Path): La ruta al archivo XML a parsear.
        """
        self.tree = ET.parse(xml_path)
        self.root = self.tree.getroot()

    def parse(self) -> dict:
        """
        Inicia el proceso de parseo y devuelve la estructura del menú completa.

        Returns:
            dict: Un diccionario que representa la jerarquía del menú.
        """
        menus_dict = {}
        for menu_element in self.root.findall("menu"):
            menu_id = menu_element.get("id")
            if menu_id:
                # Llama a la función recursiva para construir cada menú principal
                menus_dict[menu_id] = self._build_dict_from_element(menu_element)
        return menus_dict

    def _build_dict_from_element(self, element: ET.Element) -> dict:
        """
        Función recursiva que convierte un elemento XML y sus hijos en un diccionario.
        """
        # Caso base para los separadores
        if element.tag == "sep":
            return {"text": "---"}

        # Construye el diccionario para el elemento actual
        node_dict = {
            "id": element.get("id"),
            "text": element.get("text", element.text),
            "icon": element.get("icon"),
            "checkable": element.get("checkable") == "true",
            # Prepara el diccionario de elementos solo si el nodo tiene hijos
            "elements": {} if len(element) > 0 else None
        }

        # Si el diccionario de elementos no es None, lo poblamos recursivamente
        if node_dict["elements"] is not None:
            for child in element:
                
                child_id = child.get("id", f"sep_{id(child)}")

                # Llamada recursiva para cada hijo
                node_dict["elements"][child_id] = self._build_dict_from_element(child)
        
        return node_dict