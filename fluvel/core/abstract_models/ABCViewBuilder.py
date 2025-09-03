"""
Este módulo contiene la lógica fundamental de Fluvel para la creación
de Layouts.
classes:
    - LayoutBuilder: es la clase usada como context manager
    - ViewBuilder: es el disparador de LayoutBuilder a través de sus
    métodos y sirve como clase abstracta para la creación de Vistas.
"""

from typing import TypeVar, Generic
from abc import ABC, abstractmethod, ABCMeta

# Fluvel
from fluvel.components.layouts import FormLayout, HBoxLayout, VBoxLayout, GridLayout

# PySide6
from PySide6.QtWidgets import QWidget, QLayout
from PySide6.QtCore import QObject

# Definir una variable de tipo para los layouts
TLayout = TypeVar("TLayout", bound=QLayout)


class LayoutBuilder(Generic[TLayout]):

    def __init__(self, parent: QLayout | QWidget, type_layout: type[TLayout]):

        # an instance of HBoxLayout, QVBoxLayout, QGridLayout or QStackedLayout
        self.layout: TLayout = type_layout()

        # the parent is a layout
        if isinstance(parent, QLayout):
            parent.addLayout(self.layout)

        # the parent is a widget
        elif isinstance(parent, QWidget):
            parent.setLayout(self.layout)

        else:
            raise TypeError("The parent must be a QLayout or a QWidget.")

    def __enter__(self) -> TLayout:
        return self.layout

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class VBMeta(type(QObject), ABCMeta):
    """
    Metaclase Unificada que resuelve los conflictos
    entre las clases base QObject y ABCMeta al combinarlas.
    """

    pass


class ViewBuilder(QObject, ABC, metaclass=VBMeta):
    """
    Clase núcleo de Fluvel dedicada a la creación de Vistas a través de `manejadores de contexto`.\n
    Los nombres de los métodos ignoran la guía de estilo oficial `PEP 8` para mejorar
    la legibilidad y entendimiento a la hora de codificar.
    """

    _parent: QWidget

    def __init__(self, parent: QWidget | QLayout) -> None:
        super().__init__()

        self.parent = parent

        self.view()

    @property
    def parent(self) -> QWidget:
        return self._parent

    @parent.setter
    def parent(self, parent: QWidget | QLayout) -> None:

        if isinstance(parent, QWidget):
            self._parent = parent

        # El padre es un Layout, por lo que se crea
        # un contenedor en blanco QWidget
        elif isinstance(parent, QLayout):
            blank_container = QWidget()
            parent.addWidget(blank_container)
            self._parent = blank_container

    def Vertical(self, parent: QLayout | QWidget) -> LayoutBuilder[VBoxLayout]:
        return LayoutBuilder(parent, VBoxLayout)

    def Horizontal(self, parent: QLayout | QWidget) -> LayoutBuilder[HBoxLayout]:
        return LayoutBuilder(parent, HBoxLayout)

    def Form(self, parent: QLayout | QWidget) -> LayoutBuilder[FormLayout]:
        return LayoutBuilder(parent, FormLayout)

    def Grid(self, parent: QLayout | QWidget) -> LayoutBuilder[GridLayout]:
        return LayoutBuilder(parent, GridLayout)

    def Stacked(self, parent: QLayout | QWidget): ...

    @abstractmethod
    def view(self) -> None:
        pass
