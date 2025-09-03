import os

# Fluvel
from fluvel.controllers.ContentHandler import ContentHandler
from fluvel.models.GlobalContent import GlobalContent
from fluvel._user.Config import AppConfig


def init_content(lang: str) -> None:
    """
    Punto de entrada para inicializar o actualizar el contenido de la aplicación.

    1. Determina el modo de ejecución (desarrollo/producción) para definir qué tipo de archivos
    (fluml/json) y qué carpeta se usará (CONTENT_DIR/PROD_CONTENT_DIR).
    2. Usa `ContentHandler` para cargar y parsear los datos desde los archivos.
    3. Entrega los diccionarios de datos limpios a `GlobalContent` para que
    actualice el estado reactivo de la aplicación (`StringVars`).

    Args:
        lang (str): El código del idioma a cargar.
    """

    mode = "development" if AppConfig.fluvel.DEV_MODE else "production"

    ContentHandler.load_content(mode, lang)

    GlobalContent.initialize(
        ContentHandler.MENU_CONTENT, ContentHandler.STATIC_CONTENT
    )