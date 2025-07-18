# fluvel.core.App

from project import GlobalConfig
from PySide6.QtWidgets import QApplication
from core.core_utils.theme_loader import load_style_sheet
from core.core_utils.doc_utils import add_global_props_doc

class App(QApplication, GlobalConfig):
    def __init__(self, argv: list):
        super().__init__(argv)
        
    def load(self, filename: str):
        """ 
        **IMPORTANT** Only supports TOML or JSON config files with the ***same*** configuration format.\n
        This method is responsible for loading the application's 
        global configuration provided by a JSON or TOML file.\n
        *If you have or want to create a different configuration style (format), 
        update the **`set_config_format()`** method of the **`project.GlobalConfig`** class.*
        """

        # Se aplican los atributos globales del proyecto
        self.set_config_format(filename)

        # Aplicando los temas y estilos a los componentes
        self.set_theme()    

    def set_theme(self):
        """
        This method *loads* the *global theme* and *component styles* to be used in the application.
        """
        label_content = load_style_sheet("Label.qss", self.theme)
        push_button_content = load_style_sheet("PushButton.qss", self.theme)
        check_button_content = load_style_sheet("CheckButton.qss", self.theme)
        full_content = f"{label_content}{push_button_content}{check_button_content}"
        self.setStyleSheet(full_content)

    