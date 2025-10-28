from typing import Unpack

# Fluvel
from fluvel.components.widgets.FContainer import FContainer, FContainerKwargs

# PySide6
from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QMouseEvent

class FMovableContainer(FContainer):
    """
    Un contenedor personalizado que implementa la lógica de arrastre para su padre.
    """
    def __init__(self, **kwargs: Unpack[FContainerKwargs]):
        super().__init__(**kwargs)
        self.dragging = False
        self.offset = QPoint()

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.dragging = True
            # Calcular la posición del cursor respecto a la ventana principal
            parent_window = self.window() # Obtiene la QMainWindow principal
            self.offset = event.globalPosition().toPoint() - parent_window.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event: QMouseEvent):
        if self.dragging:
            parent_window = self.window()
            # Mueve la ventana principal (MainWindow)
            parent_window.move(event.globalPosition().toPoint() - self.offset)
            event.accept()

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.dragging = False
            event.accept()