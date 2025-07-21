# fluvel.core.App

from project import GlobalConfig
from PySide6.QtWidgets import QApplication
from core.core_utils.theme_loader import load_style_sheet, get_theme_path
from utils.helper_functions import filter_by_extension

class App(QApplication, GlobalConfig):
    def __init__(self, argv: list) -> None:
        super().__init__(argv)
        
    def load(self, filename: str) -> None:
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


    def set_theme(self) -> None:
        """
        This method *loads* the *global theme* and *component styles* to be used in the application.
        """

        # Directorio donde se encuentran los archivos qss de los componentes
        theme_path = get_theme_path(self.theme)

        # Lista con los archivos .qss
        qss_files: list = filter_by_extension(theme_path, ".qss")
        
        # Contenido que se cargará a la app
        qss_content: str = ""

        for qss_file in qss_files:
            qss_content += load_style_sheet(qss_file)

        # Cargando el tema a la app
        self.setStyleSheet(qss_content)

    