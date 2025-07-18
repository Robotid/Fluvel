from utils.helper_functions import get_root_path, filter_by_extension

# para obtener el path raíz de la aplicación desde cualquier directorio
APP_ROOT = get_root_path()

__all__ = [
    "APP_ROOT",
    "get_root_path",
    "filter_by_extension"
]