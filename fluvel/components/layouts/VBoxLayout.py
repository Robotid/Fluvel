# Fluvel
from fluvel.core.abstract_models.FluvelLayout import FluvelLayout

# PySide6
from PySide6.QtWidgets import QVBoxLayout, QWidget


class VBoxLayout(QVBoxLayout, FluvelLayout):
    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)

