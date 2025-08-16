# fluvel.core.MenuBar
# Py
from typing import Literal
from pathlib import Path

# PySide6 Importations
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMenuBar, QMainWindow

# FLUML Parse
from fluvel.src import convert_FLUML_to_JSON

# Utils
from fluvel.core.core_utils import load_file
from fluvel._user.MenuOptions import MenuOptions
from fluvel.core.core_utils.generate_menu_options import set_dynamic_menu_keys

ActionTypes = Literal["triggered", "toggled", "changed", "hovered"]

ActionProperties = Literal[
    "Text",
    "Icon",
    "Shortcut",
    "StatusTip",
    "ToolTip",
    "Enabled",
    "Visible",
    "Checkable",
    "MenuRole",
    "Data",
]

StandardActionShortcut = Literal[
    "AddTab",
    "Back",
    "Bold",
    "Close",
    "Copy",
    ""  # Para la definición del Literal, se pone una cadena vacía en la línea anterior
    "Cut",
    "Delete",
    "Contents",  # Ayuda de contenido
    "Find",
    "FindNext",
    "FindPrevious",
    "Forward",
    "HelpContents",  # Lo mismo que Contents
    "Help",  # Ayuda general
    "InsertParagraphSeparator",
    "InsertLineSeparator",
    "Italic",
    "MoveToNextChar",
    "MoveToPreviousChar",
    "MoveToNextWord",
    "MoveToPreviousWord",
    "MoveToNextLine",
    "MoveToPreviousLine",
    "MoveToNextPage",
    "MoveToPreviousPage",
    "MoveToNextSection",
    "MoveToPreviousSection",
    "MoveToEndOfLine",
    "MoveToEndOfBlock",
    "MoveToEndOfDocument",
    "MoveToStartOfLine",
    "MoveToStartOfBlock",
    "MoveToStartOfDocument",
    "MoveByPage",  # Más general que Next/Previous Page
    "MoveToPreviousWord",
    "MoveToNextWord",
    "MoveMode",  # Para activar/desactivar modo de movimiento
    "NextChild",
    "New",
    "Open",
    "Paste",
    "Preferences",  # Preferencias/Opciones
    "PreviousChild",
    "Print",
    "PrintPreview",
    "Properties",  # Propiedades del elemento actual
    "Redo",
    "Refresh",  # Recargar/Actualizar
    "Replace",
    "Save",
    "SaveAs",
    "SelectAll",
    "SelectNextChar",
    "SelectPreviousChar",
    "SelectNextWord",
    "SelectPreviousWord",
    "SelectNextLine",
    "SelectPreviousLine",
    "SelectNextPage",
    "SelectPreviousPage",
    "SelectNextSection",
    "SelectPreviousSection",
    "SelectToEndOfLine",
    "SelectToEndOfBlock",
    "SelectToEndOfDocument",
    "SelectToStartOfLine",
    "SelectToStartOfBlock",
    "SelectToStartOfDocument",
    "SelectTrailingSpaces",
    "Deselect",  # Deseleccionar todo
    "SetTextDirection",  # Establecer dirección del texto (RTL/LTR)
    "StrikeOut",  # Tachado
    "Subscript",
    "Superscript",
    "Underline",
    "Undo",
    "WhatsThis",  # Qué es esto? (para ayuda contextual)
    "ZoomIn",
    "ZoomOut",
    "Zoom",  # Restablecer zoom
    "DeleteStartOfWord",
    "DeleteEndOfWord",
    "DeleteStartOfLine",
    "DeleteEndOfLine",
    "Copy",  # Duplicado por si acaso, eliminar si ya está
    "Paste",  # Duplicado por si acaso, eliminar si ya está
]


class MenuBar:

    def __init__(self, parent: QMainWindow, menu_file: Path):

        # an instance of the AppWindow Class
        self.app_window = parent

        # The names of all menu options will be added to this list.
        self.all_menu_options: list = []

        # the QMenuBar Widget of the main window
        self.__menu_bar: QMenuBar = self.app_window.menuBar()

        self._MENU_DATA_JSON = None

        # IMPORTANT MAIN PROCESS

        # Step 0
        # The folder where the FLUML and JSON files will be stored
        menus_folder: Path = menu_file.parent
        output_file: Path = menus_folder / f"{menu_file.stem}.json"

        # Step 1
        # Start the conversion process to JSON and provide an output file path
        convert_FLUML_to_JSON(menu_file, output_file)

        # Step 2
        # Getting and load the FLUML file converted to JSON format
        parsed_structure: dict = load_file(output_file)

        # Step 3
        # Decoding and assembling the menu structure
        self._create_menus(parsed_structure)

        # Step 4
        # Generate the literal that contains all menu options
        set_dynamic_menu_keys(self.all_menu_options)

    def _create_menus(self, structure) -> None:
        """
        Inicializa la creación de los menús de nivel superior.\n
        """
        self._structure_menu(self.__menu_bar, structure)

    def _structure_menu(self, parent_menu, items: dict) -> None:
        """
        Función recursiva que forma un menú (o barra de menú) con acciones y submenús de
        acuerdo a la estructura JSON propuesta por el archivo de configuración '**`views/menus/menu.fluml`**'

        Args:
            parent_menu: El QMenu o QMenuBar al que se añadirán los elementos.
            items: Un diccionario con la configuración de los elementos del menú.
        """
        for key, value in items.items():
            if isinstance(value, str):
                # Caso 1: Es una acción o un separador
                if value == "---":
                    parent_menu.addSeparator()
                else:
                    action = QAction(value, self.app_window)
                    parent_menu.addAction(action)
                    # Convirtiendo cada QAction en una instancia de MenuBar
                    setattr(self, key, action)
                    # Guardando sus referencias para usarlas en MenuOptions y MainWindow
                    self.all_menu_options.append(key)

            elif isinstance(value, dict):
                # Caso 2: Es un submenú, llamar recursivamente
                submenu = parent_menu.addMenu(key)
                self._structure_menu(submenu, value)

    def bind(self, menu_option: MenuOptions, action: ActionTypes, controller: any) -> None:
        """
        Args:
            menu_option (str): Option of the Menu Bar
            action (str): Type of action method
            controller (any): Some controller that responds to the action
        """

        getattr(getattr(self, menu_option), action).connect(controller)

    def set_property(self, menu_option: MenuOptions, property_to_change: ActionProperties, new_value: any) -> None:
        """
        Args:
            menu_option (str): Option of the Menu Bar.
            property_to_change (str): Property that will be changed.
            new_value (any): The new value of the property.
        """

        property_method = f"set{property_to_change}"

        getattr(getattr(self, menu_option), property_method)(new_value)

    def add_shortcut(self,menu_option: MenuOptions, new_shortcut: StandardActionShortcut, controller: any) -> None:
        """
        Args:
            menu_option (str): Option of the Menu Bar.
            new_shortcut (str): The new shortcut that will be assigned.
            controller (any): Some controller that responds to the action.
        """

        self.set_property(menu_option, "Shortcut", new_shortcut)

        self.bind(menu_option, "triggered", controller)
