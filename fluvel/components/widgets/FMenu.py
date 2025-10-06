from typing import TypedDict, Unpack

# Fluvel
from fluvel.components.gui.StringVar import StringVar
from fluvel.components.gui.FAction import FAction
from fluvel.models.GlobalContent import GlobalContent

# PySide6
from PySide6.QtWidgets import QMenu, QMenuBar
from PySide6.QtGui import QIcon


class FMenuKwargs(TypedDict, total=False):

    title: str | StringVar
    menu_structure: dict

class FMenu(QMenu):

    def __init__(self, parent: QMenu | QMenuBar | None = None, **kwargs: Unpack[FMenuKwargs]) -> None:
        super().__init__(parent)

        self.all_menu_options: list = []

        self.configure(**kwargs)

        if "menu_structure" in kwargs:

            self._create_menu(parent, kwargs["menu_structure"])

    def configure(self, **kwargs: Unpack[FMenuKwargs]) -> None:

        if "title" in kwargs:

            string_var = kwargs["title"]

            string_var.valueChanged.connect(self.setTitle)

            self.setTitle(string_var.value)

    def _create_menu(self, parent, structure: dict):
        
        parent_menu = self if not parent else parent

        self.origin_object = parent

        self._structure_menu(parent_menu, structure)

    def _structure_menu(self, parent_menu: QMenu, menu_structure: dict):
        # Itera sobre la lista de elementos en un submenú o menú principal
        for _id, element_dict in menu_structure.items():

            text = element_dict.get("text")
            elements = element_dict.get("elements")

            if text == "---":
                # Caso base: es un separador
                parent_menu.addSeparator()

            elif elements:
                # Es un submenú, crea un FMenu
                new_menu = self._add_menu(parent_menu, _id, element_dict)
                setattr(self.origin_object, _id, new_menu)

                # Llama recursivamente para construir el submenú
                self._structure_menu(new_menu, elements)
            else:
                # Es una acción
                action = self._add_action(parent_menu, _id, element_dict)
                setattr(self.origin_object, _id, action)


    def _add_menu(self, parent_menu: QMenu, element_id, element_dict: dict) -> QMenu:
        text = GlobalContent.menu_content[element_id]
        menu = FMenu(parent_menu, title=text)
        parent_menu.addMenu(menu)

        return menu

    def _add_action(self, parent_menu: QMenu, element_id: str, element_dict: dict) -> FAction:
        """Método auxiliar para crear y añadir una QAction."""
        text = GlobalContent.menu_content[element_id]
        action = FAction(parent=parent_menu, text=text)

        # Opcional: añade icono si existe
        icon_path = element_dict.get("icon")

        if icon_path:
            action.setIcon(QIcon(icon_path))
            
        # Opcional: setea checkable si existe
        checkable = element_dict.get("checkable")
        if checkable:
            action.setCheckable(checkable)

        parent_menu.addAction(action)

        self.all_menu_options.append(element_id)

        return action