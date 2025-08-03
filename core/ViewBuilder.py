import sys

# PySide6
from PySide6.QtWidgets import QWidget, QLayout

# Layouts
from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout, QStackedLayout, QFormLayout

class LayoutBuilder:
    def __init__(self, parent: QLayout | QWidget | None, type_layout):

        # an instance of QHBoxLayout, QVBoxLayout, QGridLayout or QStackedLayout
        self.layout = type_layout

        # Si el layout no tiene padre, se le asigna un contenedor vacío
        if not parent:
            # Se crea el contenedor vacío
            self.container = QWidget()

            # y se le añade el Layout
            self.container.setLayout(self.layout)

        else:
            # Si el padre es un Layout
            if isinstance(parent, QLayout):
                parent.addLayout(self.layout)
            
            # Si el padre es un Widget
            elif isinstance(parent, QWidget):
                parent.setLayout(self.layout)

            else:
                raise TypeError("The parent must be a QLayout or a QWidget.")

    def __enter__(self):
        return self.layout
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        return False

class ViewBuilder:
    """
    Clase núcleo de Fluvel dedicada a la creación de Vistas a través de `manejadores de contexto`.\n
    Los nombres de los métodos ignoran la guía de estilo oficial `PEP 8` para mejorar
    la legibilidad y entendimiento a la hora de codificar.
    """
    def Vertical(self, parent: QLayout | QWidget | None = None) -> QVBoxLayout:
        return LayoutBuilder(parent, QVBoxLayout()) 

    def Horizontal(self, parent: QLayout | QWidget | None = None) -> QHBoxLayout:
        return LayoutBuilder(parent, QHBoxLayout())

    def Form(self, parent: QLayout | QWidget | None = None) -> QFormLayout:
        return LayoutBuilder(parent, QFormLayout())

    def Grid(self, parent: QLayout | QWidget | None = None):
        # Igual que las demás
        ...
    def Stacked(self, parent: QLayout | QWidget | None = None):
        # Igual que las demás
        ...
