import sys
from pathlib import Path
import os


def get_root_path() -> Path:
    """
     **`ROOT FUNCTION`** This function *returns* the **`APP_ROOT: Path`** of the project.\n
    *Handles both source code execution and packaged executables.*
    """

    if getattr(sys, "frozen", False):
        # Si la app está empaquetada
        return Path(sys.executable).parent
    else:
        # Obtener el directorio de trabajo del usuario
        # Si se ejecuta desde el código fuente, retorna la carpeta del script principal
        # esta forma, en lugar de <return Path(os.getcwd())> hace que se pueda
        # ejecutar el main.py desde cualquier subdirectorio relativo al directorio principal
        return Path(os.getcwd())


def filter_by_extension(dirname: Path | str, suffix: str | tuple) -> list[Path]:
    """
    This function *returns* a *`list`* of files filtered by extension in a given directory.\n
    Args:
        **dirname (Path | str):**
        The abs path of the folder to be filtered.\n
        *example: my_project/resources/styles/themes/theme/*\n
        **suffix (str | tuple):**
        The suffix parameter represents the extension (or a tuple of them) of the files you want to filter.\n
        *example with **str**: '.qss' o '.py'* -> This will only filter out individual '.qss' or '.py' files.\n
        *example with **tuple**: ('.qss', '.py'*) -> This will filter out all '.qss' or '.py' files in the directory.\n
    Returns:
        **list**:
        A list of `pathlib` objects (`WindowsPath` or `PosixPath`) containing the path of the filtered files.\n
    """

    # If the directory is passed as str
    # it is converted to a Path object
    if isinstance(dirname, str):
        dirname = Path(dirname)

    try:

        # Using list comprehension to iterate over
        # the directory and get the list of files
        files = [
            file
            for file in dirname.iterdir()
            if file.suffix in suffix and not file.is_dir()
        ]

    except FileNotFoundError as e:
        print(f"Error: Directory not found at the specified path. {e}")

    except NotADirectoryError as e:
        print(f"The specified path does not point to a directory. {e}")

    finally:
        return files
