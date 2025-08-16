from fluvel.core.exceptions import ContentNotFoundError


def get_content_by_id(content_id: str) -> str:
    """
    Este controlador se comunica con el modelo `GlobalContent`
    para obtener y retornar el contenido específico relacionado con un id.
    """
    from fluvel.models.GlobalContent import GlobalContent
    

    if content_id in GlobalContent.content_map:
        
        # La instancia de
        return GlobalContent.content_map[content_id]

    raise ContentNotFoundError(
        f"No content related to the id '{content_id}' has been found, is misspelled or does not exist."
    )
