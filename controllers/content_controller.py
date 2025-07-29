from models import GlobalContent

class ContentNotFoundError(Exception):
    """
    Excepción que se lanza cuando se intenta acceder a un contenido
    de la clase GlobalContent con un id erróneo o inexistente.
    """
    def __init__(self, *args):
        super().__init__(*args)

def get_content_by_id(content_id: str) -> str:
    """
    Este controlador se comunica con el modelo `GlobalContent`
    para obtener y retornar el contenido específico relacionado con un id.
    """

    if content_id in GlobalContent.content_map:

        return GlobalContent.content_map[content_id]

    raise ContentNotFoundError(f"No se encontró contenido relacionado al id: '{content_id}'.")