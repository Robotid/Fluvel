# Fluvel
from core.FluvelLayout import FluvelLayout

# PySide6
from PySide6.QtWidgets import QVBoxLayout

class VBoxLayout(QVBoxLayout, FluvelLayout):
    def __init__(self):
        super().__init__()
