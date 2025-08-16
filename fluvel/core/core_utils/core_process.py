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

        # Un TypeError en la llamada de esta función indica
        # que el método del objeto está siendo llamado de forma errónea
        # o con argumentos incorrectos, por lo que en esta situación, 
        # por como está planteado el algoritmo y los MAPPING_METHODS, se infiere que es una 
        # señal de PySide6 y se intenta conectarla usando el método obj.signal.connect().
        # e.g. button.clicked.connect(slot=value)
        except TypeError:
                
                signal = getattr(obj, method_name)

                signal.connect(value)

        except KeyError:
            # Ignore keys that do not represent a PySide6 method.
            continue