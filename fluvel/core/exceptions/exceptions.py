class ContentNotFoundError(Exception):
    """
    Excepción que se lanza cuando se intenta acceder a un contenido
    de la clase GlobalContent con un id erróneo o inexistente.
    """

    def __init__(self, *args):
        super().__init__(*args)

class ContentLoadingError(Exception):
    """
    Excepción que se lanza cuando se intenta
    cargar los archivos .json a través del ContentHandler
    """
    def __init__(self, *args):
        super().__init__(*args)