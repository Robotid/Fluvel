def get_dynamic_menu_keys(menu_options: list):

    all_options_literal: str = "from typing import Literal \nMenuOptions = Literal["

    for item in menu_options:
        all_options_literal += f"'{item}',\n"
    
    all_options_literal = f"{all_options_literal[:-1]}]"

    with open("project/MenuOptions.py", "w") as f:
        f.writelines(all_options_literal)
