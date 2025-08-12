# Fluvel
from fluvel.core.abstract_models.FluvelLayout import FluvelLayout

# PySide6
from PySide6.QtWidgets import QHBoxLayout, QWidget


class HBoxLayout(QHBoxLayout, FluvelLayout):
    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)
