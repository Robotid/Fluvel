from typing import TYPE_CHECKING

# Fluvel
from fluvel.core.abstract_models.FluvelLayout import FluvelLayout
from fluvel.components.widgets.FContainer import FContainer

# PySide6
from PySide6.QtWidgets import QVBoxLayout

# Esto es necesario
from fluvel.core.abstract_models.Builder import Builder

class VBoxLayout(QVBoxLayout, FluvelLayout, Builder):
    def __init__(self, parent: FContainer | None = None):
        super().__init__(parent)
