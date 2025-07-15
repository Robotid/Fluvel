import os
import toml
import json
from pathlib import Path
from utils.helper_functions import get_root_path

APP_ROOT = get_root_path()

def get_default_config() -> dict:
    default_config = {
    "app_name": "Mi Aplicación PySide6 - POR DEFECTO",
    "version": "1.0.0",
    "window_size": {
        "width": 800,
        "height": 600
    },
    "theme": "light",
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
        Only supports TOML or JSON config files.\n
        Este método se encarga de cargar la configuración 
        global de la aplicación a través de un archivo JSON o TOML"""

        # La extensión del archivo config
        # Deberá ser TOML o JSON
        cfg_extension = Path(filename).suffix

        # Path del archivo de configuración JSON
        config_path = APP_ROOT / filename
        config: dict

        try:
            # Se intenta abrir el archivo 'config_path'
            with open(config_path, "r", encoding="utf-8") as f:

                if cfg_extension == ".toml":
                    config = toml.load(f)
                else:
                    config = json.load(f)

        # Si el archivo no se encuentra se retorna una configuración por defecto 'default_config'
        except FileNotFoundError:
            print(f"Error: El archivo de configuración '{config_path}' no se encontró.")
            
            # Estableciendo una configuración por defecto
            config = get_default_config()

        # Si hay un fallo al decodificar el JSON, se retorna un diccionario vacío
        except json.JSONDecodeError:
            print(f"Error: El archivo '{config_path}' no es un JSON válido.")

            # Estableciendo una configuración por defecto
            config = get_default_config()

        # Usar una configuración vacía por si falla
        except Exception as e:
            print(f"Error cargando la configuración o tema: {e}")

            # Estableciendo una configuración por defecto
            config = get_default_config()

        finally:
            return config