import toml, json
from pathlib import Path
from fluvel.utils import APP_ROOT


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
                f"The configuration format ‘{extension}’ is not supported."
            )

    # Si el archivo no fue encontrado
    except FileNotFoundError:
        print(f"Error: Configuration file ‘{config_path}’: not found.")

    # Si hay un fallo al decodificar el JSON
    except (json.JSONDecodeError, toml.TomlDecodeError) as e:
        print(f"Error: The file ‘{config_path}’ is not valid JSON/TOML.")

    # Cualquier otro tipo de fallo
    except Exception as e:
        print(f"Error loading configuration: {e}.")

    # En caso de excepción, retornar none
    return None