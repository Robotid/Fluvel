import sys
from pathlib import Path

def get_root_path() -> str:
    """
    This function *returns* the **`APP_ROOT: Path`** of the project.
    """

    APP_ROOT: str

    if getattr(sys, "frozen", False):
        # Si la app está empaquetada
        APP_ROOT = Path(sys.executable).parent
    else:
        # Si se ejecuta desde el código fuente
        # Path desde este archivo. 
        # parent 1 -> .../utils/
        # parent 2 -> .../App  <root folder of the app>
        APP_ROOT = Path(__file__).parent.parent

    return APP_ROOT


def minify_qss(qss_content: str) -> str:
    """
    -> **TO DO** <-\n
    Minimiza una cadena QSS eliminando espacios en blanco y comentarios.
    """
    ...


def get_files_from_directory(dirname: str) -> list:
    """
    This function *returns* a *`list`* of ***all files*** in a specified directory except the *`__init__.py`* file.\n
    """ 
    
    return Path(dirname).iterdir() # Is just the 'iterdir()' method of the pathlib.Path Class


def filter_by_extension(dirname: Path | str, suffix: str | tuple) -> list:
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
    
    if isinstance(dirname, str):
        dirname = Path(dirname)

    files: list = []
    
    for _file in dirname.iterdir():
        # compares the file extension with the suffix parameter
        if _file.suffix in suffix: 
            files.append(_file)
        else:
            pass
    
    return files

# archivos_qss = filter_by_extension()