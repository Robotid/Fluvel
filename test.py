from typing import TypedDict, Literal, Union

# --- Definimos cada caso por separado ---

class PropiedadTexto(TypedDict):
    text: Literal["text"]
    value: str


# --- Magia en el análisis de tipos ---

def procesar_propiedad(p: PropiedadTexto):
    # El analizador sabe que 'property' es la clave discriminadora
    if p["property"] == "text":
        # OK: Sabe que 'p' es PropiedadTexto
        # y por lo tanto 'p['value']' es un 'str'
        print(p["value"].upper()) 
    
    elif p["property"] == "font-size":
        # OK: Sabe que 'p' es PropiedadTamaño
        # y por lo tanto 'p['value']' es un 'int'
        print(p["value"] + 10)
    
    elif p["property"] == "color":
        # OK: Sabe que 'p' es PropiedadColor
        # y 'p['value']' es Literal["red", "green", "blue"]
        print(f"Color elegido: {p['value']}")

# --- Ejemplos de uso ---

# Válido:
procesar_propiedad({"property": "text", "value": "Hola"})