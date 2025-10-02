from pathlib import Path

# Expect Handler
from fluvel.core.exceptions.expect_handler import expect

@expect.FileNotFound(stop=True, default_value="")
def load_fluml(file_path: Path | str) -> str:
    """
    Loads and returns the contents of a ``.fluml`` file.

    :param file_path: The path to the .fluml file
    :type file_path: Path | str
    :returns: A string with fluml content.
    :rtype: str
    """

    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

