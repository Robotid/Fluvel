from utils import APP_ROOT

_DEFAULT_MENU_OPTIONS = """
# This module updates dynamically depending on your project's menu options.

from typing import Literal
MenuOptions = Literal["nothing yet"]
"""


def set_dynamic_menu_keys(menu_options: list, moduleExists: bool = True) -> None:
    """
    Esta función genera dinámicamente en el módulo `project/MenuOptions.py` el `MenuOptions: Literal`
    """

    menu_file = APP_ROOT / "project" / "MenuOptions.py"

    if moduleExists:

        option_string: str = ",\n\t".join([f"'{option}'" for option in menu_options])

        all_options_literal: str = (
            f"from typing import Literal\nMenuOptions = Literal[{option_string}]"
        )

    else:
        all_options_literal = _DEFAULT_MENU_OPTIONS

    try:
        with open(menu_file, "w", encoding="utf-8") as f:
            f.write(all_options_literal)

    # Si el módulo no existe, se llama recursivamente con el parámetro moduleExists = False
    except ModuleNotFoundError:
        set_dynamic_menu_keys([], moduleExists=False)

    # Cualquier otra excepción
    except Exception as e:
        print(f"Error: an error has ocurred. {e}")
