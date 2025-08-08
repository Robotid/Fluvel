from typing import TypeVar, Generic
from abc import ABC, abstractmethod

# Fluvel
from components.layouts import FormLayout, HBoxLayout, VBoxLayout, GridLayout

# PySide6
from PySide6.QtWidgets import QWidget, QLayout
from PySide6.QtWidgets import QGridLayout, QStackedLayout

# Definir una variable de tipo para los layouts
TLayout = TypeVar('TLayout', bound=QLayout)

class LayoutBuilder(Generic[TLayout]):
    
    def __init__(self, parent: QLayout | QWidget | None, type_layout: type[TLayout]):

        # an instance of HBoxLayout, QVBoxLayout, QGridLayout or QStackedLayout
        self.layout: TLayout = type_layout()

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

    def __enter__(self) -> TLayout:
        return self.layout
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        return False

class ViewBuilder(ABC):
    """
    Clase núcleo de Fluvel dedicada a la creación de Vistas a través de `manejadores de contexto`.\n
    Los nombres de los métodos ignoran la guía de estilo oficial `PEP 8` para mejorar
    la legibilidad y entendimiento a la hora de codificar.
    """
    def __init__(self, parent: QLayout | QWidget) -> None:

        self.parent = parent

        self.view()

    def Vertical(self, parent: QLayout | QWidget | None = None) -> LayoutBuilder[VBoxLayout]:
        return LayoutBuilder(parent, VBoxLayout) 

    def Horizontal(self, parent: QLayout | QWidget | None = None) -> LayoutBuilder[HBoxLayout]:
        return LayoutBuilder(parent, HBoxLayout)

    def Form(self, parent: QLayout | QWidget | None = None) -> LayoutBuilder[FormLayout]:
        return LayoutBuilder(parent, FormLayout)

    def Grid(self, parent: QLayout | QWidget | None = None) -> LayoutBuilder[GridLayout]:
        # Igual que las demás
        return LayoutBuilder(parent, GridLayout)

    def Stacked(self, parent: QLayout | QWidget | None = None):
        # Igual que las demás
        ...

    @abstractmethod
    def view(self) -> None: ...