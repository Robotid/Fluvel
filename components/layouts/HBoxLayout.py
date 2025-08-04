# Fluvel
from core.FluvelLayout import FluvelLayout

# PySide6
from PySide6.QtWidgets import QHBoxLayout

class HBoxLayout(QHBoxLayout, FluvelLayout):
    def __init__(self):
        super().__init__()
