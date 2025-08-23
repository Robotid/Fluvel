from pathlib import Path
import json
import re


def read_file(file_path: Path | str) -> list[str]:
    """
    Lee un archivo y devuelve una lista de sus líneas con readlines().
    """

    if isinstance(file_path, str):
        file_path = Path(file_path)

    try:

        with open(file_path, "r", encoding="utf-8") as f:
            return f.readlines()

    except Exception as e:
        print(f"Error: Ha ocurrido un error al leer el archivo: {e}")
        return []


def parse_FLUML(file_path: Path | str) -> dict:
    """
    Analiza un archivo `.fluml`, lo formatea a JSON y lo convierte en un diccionario de Python.
    """

    lines = read_file(file_path)
    if not lines:
        return {}

    root = {}
    # La pila (stack) almacenará tuplas de (indentación, diccionario)
    # Empezamos con -1 como indentación base para el diccionario raíz.
    stack = [(-1, root)]
    sep_counter = 1

    for line_num, each_line in enumerate(lines, 1):
        # 1. Limpiar la línea: eliminar comentarios y espacios en blanco
        line = each_line.split("#", 1)[0].rstrip()

        if not line:
            continue

        # 2. Calcular la indentación de la línea actual
        indent = len(line) - len(line.lstrip())
        line = line.lstrip()

        # 3. Volver a la jerarquía correcta basándose en la indentación
        # Si la indentación actual es menor o igual a la del último diccionario en la pila entonces
        # subimos de nivel.
        while indent <= stack[-1][0]:
            stack.pop()

        # El diccionario actual es el último en la pila
        current_dict = stack[-1][1]

        # 4. Procesar la línea según su tipo
        # Separador de sección (@)
        if line.startswith("@"):
            key = f"sep_{sep_counter}"
            current_dict[key] = "---"
            sep_counter += 1
            continue

        # Sección ([Section])
        section_match = re.match(r"\[([^\]]+)\]\:", line)
        if section_match:
            section_name = section_match.group(1).strip()
            new_dict = {}
            current_dict[section_name] = new_dict
            # Añadir la nueva sección y su indentación a la pila
            stack.append((indent, new_dict))
            continue

        # Par entidad clave-valor (key = "value")
        kv_match = re.match(r'([^=\s]+)\s*=\s*"([^"]+)"', line)
        if kv_match:
            key, value = kv_match.groups()
            current_dict[key.strip()] = value.strip()
            continue

        # Si no coincide con ningún patrón, es un error de sintaxis
        raise ValueError(
            f"Error de sintaxis en la línea {line_num}: '{each_line.strip()}'"
        )

    return root


def convert_FLUML_to_JSON(input_file: Path) -> dict:
    """
    Convierte un archivo `.fluml` a `.json.`
    """

    try:

        return parse_FLUML(input_file)

    # Si en el proceso de conversión se detectó una sintaxis errónea
    except ValueError as e:
        print(f"Error durante la conversión: {e}")

    # Cualquier otra excepción
    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")
