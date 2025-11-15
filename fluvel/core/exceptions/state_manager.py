
class SilkBindingError(ValueError):
    """Excepción lanzada cuando la sintaxis del Data Binding es inválida."""
    pass

class SilkStateError(RuntimeError):
    """Excepción lanzada por errores relacionados con el StateManager."""
    pass