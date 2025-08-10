from project import GlobalConfig


# NOT USED
def add_global_props_doc(cls):
    # un decorador de clase para añadir la documentación global de la aplicación
    global_doc_content = GlobalConfig.__doc__

    if cls.__doc__:
        cls.__doc__ += f"\n{global_doc_content}"
    else:
        cls.__doc__ = global_doc_content
    return cls


global_props: str = GlobalConfig.__doc__
