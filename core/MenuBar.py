# fluvel.core.MenuBar

from PySide6.QtWidgets import QMenuBar, QMainWindow
from core.core_utils import load_file, APP_ROOT
from typing import Literal
from core.core_utils.generate_menu_options import set_dynamic_menu_keys
from project.MenuOptions import MenuOptions
from PySide6.QtGui import QAction
from src.flumlparse.flumlmain import convert_FLUML_to_JSON

ActionTypes = Literal["triggered", "toggled", "changed", "hovered"]

ActionProperties = Literal["Text", "Icon", "Shortcut", "StatusTip",
                           "ToolTip", "Enabled", "Visible", "Checkable",
                           "MenuRole", "Data"]

class MenuBar:
    def __init__(self, parent: QMainWindow, menu_file: str):

        self.main_window = parent

        self.all_menu_options: list = []

        # the QMenuBar Widget
        self.menu_bar: QMenuBar = parent.menuBar()

        # IMPORTANT PROCESS

        # Step 0
        # The folder where the FLUML and JSON files will be stored
        menus_folder = APP_ROOT / "views" / "menus" 
        fluml_file = menus_folder / "menu.fluml" # or f"{GlobalConfig.menu_config_path}.fluml"
        output_file = menus_folder / f"{fluml_file.stem}.json"

        # Step 1
        # read the JSON generated in step 2
        convert_FLUML_to_JSON(fluml_file, output_file)
        
        # Step 2
        # Getting the FLUML file converted to JSON format
        parsed_structure: dict = load_file(output_file)

        # Step 3
        # Decoding and assembling the menu structure
        self._create_menus(parsed_structure)

        # Step 4
        # Generate the literal that contains all menu options
        set_dynamic_menu_keys(self.all_menu_options)

    def _decode_menu_config(self):
        """
        **`UNUSED`** 1st Semi-failed and obsolete attempt
        """

        all_menu_options: list = []

        self.options = {}

        option_dict = {}

        for top_menu, medium_menu in self.menu_info.items():

            set_top_option = self.__menu.addMenu(top_menu)

            sub_option = {}

            for sub_menu, value in medium_menu.items():

                if isinstance(value, dict):

                    set_top_option.addSeparator() # Añadiendo separador

                    for sub, val in value.items():

                        set_sub_option = set_top_option.addAction(val)

                        sub_option.update({sub: set_sub_option})

                        all_menu_options.append(sub)

                        setattr(self, sub, set_sub_option)

                else:

                    set_sub_option = set_top_option.addAction(value)

                    sub_option.update({sub_menu: set_sub_option})

                    all_menu_options.append(sub_menu)

                    setattr(self, sub_menu, set_sub_option)

                option_dict.update({top_menu.lower(): sub_option})

            self.options.update(option_dict)

            # Generando el Literal con todas las opciones de Menú
            set_dynamic_menu_keys(all_menu_options)

    def _parse_menu_config(self):
        """
        **`UNUSED`** 2nd Semi-failed and obsolete attempt
        """
        
        self.all_menu_options: list = []

        self.options: dict = {}

        lista_desplegable: list = []

        def add_menu_option(parent_name, menu_header, option, value):
            action_object = menu_header.addAction(value)
            setattr(self, option, action_object)

            self.all_menu_options.append(option)
            self.options.update({parent_name: {option: value}})
        
        def add_desplegable_menu(lista_acciones):
            ...

        for header_parent, submenu_variables in self.menu_info.items():
            # header_parent es el padre
            menu_header = self.__menu.addMenu(header_parent)

            for submenu_var, submenu_value in submenu_variables.items():

                evaluate: bool = isinstance(submenu_value, dict)
                match evaluate:
                    case True:
                        
                        menu_header.addSeparator()
                        for after_separated_var, after_separated_value in submenu_value.items():
                            match after_separated_var:
                                case "Advanced":

                                    for desplegable_var, desplegable_value in after_separated_value.items():
                                        ...
                                        # AGRHH!!!!

                                case _:
                                    add_menu_option(header_parent, menu_header, after_separated_var, after_separated_value)

                    case _:
                        add_menu_option(header_parent, menu_header, submenu_var, submenu_value)
    
    def _create_menus(self, structure):
        """Inicializa la creación de los menús de nivel superior."""
        self._structure_menu(self.menu_bar, structure)

    def _structure_menu(self, parent_menu, items: dict):
        """
        Función recursiva que forma un menú (o barra de menú) con acciones y submenús de
        acuerdo a la estructura propuesta por el archivo de configuración '**`views/menus/menu.fluml`**'
        
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
                    action = QAction(value, self.main_window)
                    parent_menu.addAction(action)
                    # self.main_window.actions[key] = action # Guardar la acción usando su clave TOML
                    # FluvelOption.options = action # Maybe
                    setattr(self, key, action) # convirtiendo cada QAction en una instancia de MenuBar
                    self.all_menu_options.append(key) # Guardando sus referencias para usarlas en MenuOptions y MainWindow
            
            elif isinstance(value, dict):
                # Caso 2: Es un submenú, llamar recursivamente
                # El título del submenú es la propia clave, formateada.
                submenu_title = key.replace('_', ' ').capitalize()
                submenu = parent_menu.addMenu(submenu_title)
                self._structure_menu(submenu, value)

    def bind(self, menu_option: MenuOptions, action: ActionTypes, controller: any) -> None:
        """
        Args:
            menu_option (Literal): Option of the Menu Bar
            action (Literal): Type of action method
            controller (any): Some controller that responds to the action
        """

        getattr(getattr(self, menu_option), action).connect(controller)

    def set_property(self, menu_option: MenuOptions, property_to_change: ActionProperties, new_value: any) -> None:
        """
        Args:
            menu_option (Literal): Option of the Menu Bar.
            property_to_change (Literal): Property that will be changed.
            new_value (any): The new value of the property.
        """
        
        property_method = f"set{property_to_change}"

        getattr(getattr(self, menu_option), f"{property_method}")(new_value)

    def add_shortcut(self, menu_option: MenuOptions, new_shortcut: str, controller: any) -> None:
        """
        Args:
            menu_option (Literal): Option of the Menu Bar.
            new_shortcut (str): The new shortcut that will be assigned.
            controller (any): Some controller that responds to the action.
        """

        self.set_property(menu_option, "Shortcut", new_shortcut)

        self.bind(menu_option, "triggered", controller)