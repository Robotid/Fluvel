from pathlib import Path

def get_theme_path(folder: Path, theme: str) -> Path:
    """
    Esta función retorna la ruta absoluta de un tema qss determinado.
    """

    return folder / theme

def load_theme(folder: Path, theme_name: str) -> str:

    qss_files = get_theme_path(folder, theme_name).rglob("*.qss")
    
    qss_content: str = ""

    # Iterando y concatenando el contenido QSS de los archivos
    for qss_file in qss_files:

        qss_content += load_style_sheet(qss_file)

    return qss_content  

def load_style_sheet(file_path: str | Path) -> str:
    """
    Esta función carga y devuelve en forma de *`string`* el contenido de un archivo de hoja de estilos (QSS).
    """

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            style_content = f.read()

        return style_content

    except FileNotFoundError:
        print(
            f"Error: No se encontró el archivo {file_path.name} en la ruta {file_path}."
        )

    except Exception as e:
        print(f"Error al leer el archivo de hoja de estilos '{file_path.name}': {e}.")

    # En caso de alguna excepción
    return ""
