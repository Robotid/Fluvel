def configure_process(obj: object, mapping: dict, **kwargs: any) -> None:
    """
    Configure properties, methods, and signals of a PySide6 object in a generic way.

    This function is a central component of Fluvel that allows dynamic configuration
    of widgets, decoupling the names of the arguments from their
    corresponding methods in PySide6.

    Args:
        obj (object): The PySide6 object instance to be configured (e.g. QWidget, QPushButton).
        mapping (dict): A dictionary that maps argument names to method or signal names.
        **kwargs (any): Configuration arguments that will be processed.
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

        # A TypeError in the call to this function indicates
        # that the object method is being called incorrectly
        # or with incorrect arguments, so in this situation,
        # given the way the algorithm and MAPPING_METHODS are set up, it is inferred that it is a
        # PySide6 signal and an attempt is made to connect it using the obj.signal.connect() method.
        # e.g. button.clicked.connect(slot=value)
        except TypeError:

            # obj.signal = method | line 23
            method.connect(value)

        except KeyError:
            # Ignore keys that do not represent a PySide6 method.
            continue
