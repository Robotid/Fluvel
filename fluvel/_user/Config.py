from pathlib import Path

# Fluvel utils
from fluvel.core.core_utils.config_loader import load_file

class DataSection:
    """
    Un objeto contenedor simple utilizado para representar una sección anidada en el archivo de configuración.
    Permite acceder a las configuraciones como atributos, e.g.: `AppConfig.app.name`.
    """
    pass

class AppConfig:
    """
    Una clase de utilidad que carga, procesa y expone la configuración
    de la aplicación desde un archivo.

    La configuración se carga de forma recursiva, y las secciones anidadas  
    se representan como objetos de `DataSection`, lo que permite un acceso    
    estructurado y de fácil lectura.
    """

    @classmethod
    def init_config(cls, filename: str) -> None:
        """
        Inicializa la configuración de la aplicación a partir de un archivo.

        Este método carga el archivo de configuración y procesa su contenido
        para establecer los atributos de la calse `AppConfig`.

        Args:
            filename (str): El nombre del archivo de configuración (e.g. 'appconfig.toml')
        """

        # Getting the abs path to the file
        filepath = Path(filename).resolve()
        
        # Loading the file
        config: dict = load_file(filepath)

        # Start auto-configuration process
        structure_config(cls, config)


def structure_config(obj: AppConfig | DataSection, config: dict) -> None:
    """
    Procesa un diccionario de configuración y lo estructura en atributos.

    Esta es una función auxiliar recursiva que itera sobre el diccionario
    de configuración y crea atributos dinámicamente. Las secciones
    anidadas se convierten en objetos `DataSection`.

    Args:
        obj: (AppConfig | DataSection): El objeto actual donde se establecerán los atributos.
        config: (dict): El diccionario de configuración que se va a procesar.
    """
    for varname, value in config.items():

        if not isinstance(value, dict):
            setattr(obj, varname, value)
        else:
            data_sec = DataSection()
            setattr(obj, varname, data_sec)
            structure_config(data_sec, value)