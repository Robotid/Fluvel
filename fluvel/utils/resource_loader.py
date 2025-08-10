from typing import Literal

_RESOURCE_FOLDERS = {
    "style": "styles",
    "img": "images",
    "ico": "icons",
    "data": "data",
    "template": "templates",
    "font": "fonts",
}

ResourceTypes = Literal["style", "img", "ico", "data", "template", "font"]


def get_resource_path(APP_ROOT, filename: str, resource_type: ResourceTypes) -> str:
    """
    Construye la ruta absoluta a un recurso específico. Ejemplo: *'APP_ROOT/resources/icons/...'*

    Args:
        resource_type (Literal): El tipo de recurso (ej. "style", "img").
        filename (str): El nombre del archivo del recurso.

    Returns:
        str: La ruta absoluta al recurso.
    """
    if resource_type not in _RESOURCE_FOLDERS:
        raise ValueError(
            f"Tipo de recurso '{resource_type}' no soportado. Tipos válidos: {list(_RESOURCE_FOLDERS.keys())}"
        )

    # Construye la ruta completa: APP_ROOT/resources/tipo_de_recurso/filename
    folder_name = _RESOURCE_FOLDERS[resource_type]
    resource_full_path = APP_ROOT / "resources" / folder_name / filename
    return str(resource_full_path)
