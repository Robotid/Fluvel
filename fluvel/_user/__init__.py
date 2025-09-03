from pathlib import Path
from fluvel._user.Config import AppConfig

# This folder
USER_FOLDER = Path(__file__).parent

__all__ = [
    "AppConfig",
    "USER_FOLDER"
]