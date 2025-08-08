

def configure_process(obj: object, mapping: dict, **kwargs: any) -> None:
    """
    Esta función es un proceso núcleo de Fluvel, permitiendo un enfoque genérico
    ligado a los procesos de configuración de propiedades y métodos de los objetos de PySide6.
    """
    for key, value in kwargs.items():
        try:
            # Get the method name
            method_name = mapping[key]

            # if method is not none
            if method_name:

                # Obtaining the method through its name
                method = getattr(obj, method_name)

                # and Execute
                if isinstance(value, tuple):
                    method(*value)
                else:
                    method(value)
                    
        except KeyError as e:
            # Ignore keys that do not represent a PySide6 method.
            continue