import sys
from pathlib import Path

def get_root_path() -> Path:
    """
     **`ROOT FUNCTION`** This function *returns* the **`APP_ROOT: Path`** of the project.\n
    *Handles both source code execution and packaged executables.*
    """

    APP_ROOT: Path

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
    Minimizes a QSS string by removing whitespace and comments.\n
    perhaps useful when running the *`fluvel build`* command
    """
    ...

def get_files_from_directory(dirname: str) -> list:
    """
    This function *returns* a *`list`* of ***all files*** in a specified directory except the *`__init__.py`* file.\n
    """ 
    
    return Path(dirname).iterdir() # Is just the 'iterdir()' method of the pathlib.Path Class

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
    
    if isinstance(dirname, str):
        dirname = Path(dirname)

    files: list = []

    try:
        for _file in dirname.iterdir():
            # compares the file extension with the suffix parameter
            if _file.suffix in suffix and not _file.is_dir(): 
                files.append(_file)

    except FileNotFoundError as e:
        print(f"Error: Directory not found at the specified path. {e}")
    
    except NotADirectoryError as e:
        print(f"The specified path does not point to a directory. {e}")
    
    finally:
        return files
