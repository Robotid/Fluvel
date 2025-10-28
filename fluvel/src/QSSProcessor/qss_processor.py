import re

class QSSProcessor:

    STYLE_TOKENS = {
        # --- Fondo
        "bg": "background-color: $value;",
        "bg-img": "background-image: url(\"$value\");",
        "bg-repeat": "background-repeat: $value;",
        "bg-position": "background-position: $value;",
        "bg-origin": "background-origin: $value;",

        # --- Borde
        "b": "border: $value;",
        "b-color": "border-color: $value;",
        "b-style": "border-style: $value;",
        "b-width": "border-width: $value;",
        "b-radius": "border-radius: $value;",
        
        # Bordes por lado
        "b-left": "border-left: $value;",
        "b-top": "border-top: $value;",
        "b-right": "border-right: $value;",
        "b-bottom": "border-bottom: $value;",

        # Corners
        "br-tl": "border-top-left-radius: $value;",  
        "br-tr": "border-top-right-radius: $value;",  
        "br-bl": "border-bottom-left-radius: $value;",  
        "br-br": "border-bottom-right-radius: $value;", 

        # Sides
        "br-top": "border-top-left-radius: $value; border-top-right-radius: $value;", 
        "br-bottom": "border-bottom-left-radius: $value; border-bottom-right-radius: $value;",
        "br-left": "border-top-left-radius: $value; border-bottom-left-radius: $value;",
        "br-right": "border-top-right-radius: $value; border-bottom-right-radius: $value;",
        
        # --- Fuente
        "f-size": "font-size: $value;",
        "f-color": "color: $value;",
        "f-weight": "font-weight: $value;",
        "f-align": "text-align: $value;",
        "f-family": "font-family: $value;",
        "f-style": "font-style: $value;",
        "f-decoration": "text-decoration: $value;",
        
        # --- Espaciado y Dimensión
        "m": "margin: $value;",
        "m-top": "margin-top: $value;",
        "m-bottom": "margin-bottom: $value;",
        "m-left": "margin-left: $value;",
        "m-right": "margin-right: $value;",
        
        "p": "padding: $value;",
        "p-top": "padding-top: $value;",
        "p-bottom": "padding-bottom: $value;",
        "p-left": "padding-left: $value;",
        "p-right": "padding-right: $value;",
        "p-left-right": "padding-left: $value; padding-right: $value;",
        "p-top-bottom": "padding-top: $value; padding-bottom: $value;",
        
        "min-w": "min-width: $value;",
        "min-h": "min-height: $value;",
        "max-w": "max-width: $value;",
        "max-h": "max-height: $value;",
    }

    @classmethod
    def process(cls, styles: str, widget_name: str, widget_id: str) -> str:

        qss_string: str = ""

        matches = re.findall(r"([\w-]+)\[(.*?)\]", styles)

        for property_name, value in matches:

            # Obtener el token QSS
            style_token = cls.STYLE_TOKENS.get(property_name)

            if style_token:
                # Reemplazar el marcador $value
                qss_string += f"\n\t{style_token.replace('$value', value)}"
            else:
                print(f"QSSError: Propiedad '{property_name}' Errónea o no mapeada.")
        
        return QSSProcessor.get_full_qss(widget_name, widget_id, qss_string)

    @staticmethod
    def get_full_qss(widget_name: str, _id: str, full_properties: str) -> str:

        qss_style = "$widget_name#$id {\n $full_properties \n}"

        return qss_style\
            .replace("$widget_name", widget_name) \
                .replace("$id", _id)\
                    .replace("$full_properties", full_properties)