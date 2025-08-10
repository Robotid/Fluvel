from pathlib import Path


def load_fluml(file_path: Path | str) -> str:

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()

    except FileNotFoundError as e:
        print(f"El archivo .fluml no se encontró: {e}")

    return ""
