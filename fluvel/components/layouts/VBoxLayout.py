# Fluvel
from fluvel.core.abstract_models.FluvelLayout import FluvelLayout
from fluvel.components.widgets.FContainer import FContainer

# PySide6
from PySide6.QtWidgets import QVBoxLayout


class VBoxLayout(QVBoxLayout, FluvelLayout):
    def __init__(self, parent: FContainer | None = None):
        super().__init__(parent)
