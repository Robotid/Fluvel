import importlib

global_config = importlib.import_module("project.GlobalConfig")

USER_CONFIG = global_config.GlobalConfig
