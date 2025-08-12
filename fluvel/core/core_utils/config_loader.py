import toml
import json
from pathlib import Path
from fluvel.utils import APP_ROOT


def get_default_config() -> dict:
    """
    **[`UNUSED]`** `returns` a `dict` with a default configuration format
    if no initial config file is provided or an `Exception` was thrown while trying to load one.
    """
    default_config: dict = {
        "app": {
            "app_name": "Unknown App",
            "version": "N/A",
            "log_level": "INFO",
            "theme": "clean-light",
        },
        "window_size": {"width": 640, "height": 480},
        "database": {
            "host": "localhost",
            "port": 5432,
            "user": "admin",
            "password": "secure_password",
        },
    }

    return default_config


def load_file(file_path: Path | str) -> dict | None:
    """
    **IMPORTANT** Only supports TOML or JSON config files.\n
    This function loads and returns the configuration provided by a JSON or TOML file.\n
    """

    # La extensión del archivo config
    # Deberá ser TOML o JSON
    extension = Path(file_path).suffix

    # Path del archivo de configuración JSON
    config_path = APP_ROOT / file_path

    try:
        # Se intenta abrir el archivo 'config_path'
        with open(config_path, "r", encoding="utf-8") as f:
            if extension == ".toml":
                return toml.load(f)
            if extension == ".json":
                return json.load(f)
            # lanzar ValueError para formatos no soportados
            raise ValueError(
                f"El formato de configuración '{extension}' no es soportado."
            )

    # Si el archivo no fue encontrado
    except FileNotFoundError:
        print(f"Error: El archivo de configuración '{config_path}': no se encontró.")

    # Si hay un fallo al decodificar el JSON
    except (json.JSONDecodeError, toml.TomlDecodeError) as e:
        print(f"Error: El archivo '{config_path}' no es un JSON válido.")

    # Cualquier otro tipo de fallo
    except Exception as e:
        print(f"Error cargando la configuración: {e}.")

    # En caso de excepción, retornar none
    return None


def load_app_config(app_config: Path | str | dict, default_config: dict = {}) -> dict:
    """
    Esta función carga y devuelve la configuración de la aplicación.
    """

    if isinstance(app_config, dict):
        return app_config

    if isinstance(app_config, (str, Path)):

        config = load_file(app_config)

        return default_config if config is None else config
