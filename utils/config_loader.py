import toml
import json
from pathlib import Path
from utils import APP_ROOT # Aquí ya hago uso de la simplificación con utils/__init__.py

def get_default_config() -> dict:
    """
    `returns` a `dict` with a default configuration format
    if no initial config file is provided or an `Exception` was thrown while trying to load one.
    """
    default_config = {
    "app_name": "Unknown App",
    "version": "N/A",
    "window_size": {
        "width": 640,
        "height": 480
    },
    "theme": "clean-light",
    "database": {
        "host": "localhost",
        "port": 5432,
        "user": "admin",
        "password": "secure_password"
    },
    "log_level": "INFO"
    }

    return default_config

def load_app_config(filename: str) -> dict:
        
        """ 
        **IMPORTANT** Only supports TOML or JSON config files with the ***same*** configuration format.\n
        This function is responsible for loading the application's 
        global configuration provided by a JSON or TOML file.\n
        *If you have or want to create a different configuration style (format), update the **`set_format()`** method of the **`core.Config`** class.*"""

        config: dict # Variable que contendrá la configuración de la aplicación

        hasError: bool = True # Sirve para detectar si ocurrió un error en la carga del archivo

        # La extensión del archivo config
        # Deberá ser TOML o JSON
        cfg_extension = Path(filename).suffix

        # Path del archivo de configuración JSON
        config_path = APP_ROOT / filename

        try:
            # Se intenta abrir el archivo 'config_path'
            with open(config_path, "r", encoding="utf-8") as f:
                if cfg_extension == ".toml":
                    config = toml.load(f)
                else:
                    config = json.load(f)
    
            hasError = False

        # Si el archivo no fue encontrado
        except FileNotFoundError:
            print(f"Error: El archivo de configuración '{config_path}' no se encontró.")

        # Si hay un fallo al decodificar el JSON
        except json.JSONDecodeError:
            print(f"Error: El archivo '{config_path}' no es un JSON válido.")

        # Si hay un fallo al decodificar el TOML
        except toml.TomlDecodeError:
            print(f"Error: El archivo '{config_path} no es un TOML válido.")

        # Cualquier otro tipo de fallo
        except Exception as e:
            print(f"Error cargando la configuración o tema: {e}.")

        finally:
            if hasError:
                config = get_default_config()
            return config