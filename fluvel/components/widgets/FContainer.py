from typing import TypedDict, Unpack

# Fluvel
from fluvel.core.abstract_models.FluvelWidget import FluvelWidget

# PySide6
from PySide6.QtWidgets import QFrame
from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QMouseEvent

class FContainerKwargs(TypedDict, total=False):

    style: str
    movable: bool

class FContainer(QFrame, FluvelWidget):

    WIDGET_TYPE: str = "QFrame"

    def __init__(self, **kwargs: Unpack[FContainerKwargs]):
        super().__init__()

        # FluvelWidget Defaults
        self._set_widget_base_defaults()
        
        # Movable functionality
        self.isMovable = kwargs.get("movable", False)
        self.dragging = False
        self.offset = QPoint()

        self.configure(**kwargs)

    def configure(self, **kwargs: Unpack[FContainerKwargs]) -> None:

        kwargs = self._apply_styles(**kwargs)

    def mousePressEvent(self, event: QMouseEvent):

        if self.isMovable and event.button() == Qt.MouseButton.LeftButton:

            self.dragging = True

            # Calcular la posición del cursor respecto a la ventana principal
            parent_window = self.window() # Obtiene la QMainWindow principal

            self.offset = event.globalPosition().toPoint() - parent_window.frameGeometry().topLeft()
            event.accept()
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event: QMouseEvent):

        if self.isMovable and self.dragging:
            parent_window = self.window()

            # Mueve la ventana principal (MainWindow)
            parent_window.move(event.globalPosition().toPoint() - self.offset)
            event.accept()
        else:
            super().mousePressEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent):
        
        if self.isMovable and event.button() == Qt.MouseButton.LeftButton:
            self.dragging = False
            event.accept()
        else:
            super().mousePressEvent(event)