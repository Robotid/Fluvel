import importlib

try:
    global_config = importlib.import_module("project.GlobalConfig")
    USER_CONFIG = global_config.GlobalConfig
except ModuleNotFoundError:
    global_config: str = "ModuleNotFound"
