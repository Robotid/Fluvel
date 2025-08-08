
# Fluvel
from core.FluvelLayout import FluvelLayout

#PySide6
from PySide6.QtWidgets import QGridLayout, QWidget, QLayout

class ColumnIndex:
        """
        Clase que provee el funcionamiento para la adición intuitiva
        y automática de widgets en un GridLayout.
        """
        _current_row: int = 0

        def __init__(self, grid: QGridLayout, column_index: int):
            
            # Almacenamos la instancia GridLayout
            self.grid = grid
            
            # Almacenamos el índice de la columna
            self._column_index = column_index

        def add(self, arg__1: QWidget | FluvelLayout, row_span: int = 1, column_span: int = 1) -> None:
            """
            Args:
                arg__1 (QWidget | QLayout): El `Widget` o `Layout` que ocupará la celda.
                row_span (int): El número de celdas hacia abajo que abarcará el objeto. 1 por defecto.
                column_span (int): El número de columnas a la derecha que abarcará el objeto. 1 por defecto.
            """
            
            # Si existe un elemento en la celda actual
            while self.grid.itemAtPosition(self._current_row, self._column_index) is not None:
                self._current_row += 1

            # Se añade el widget con los parametros row, column de la clase
            self.grid.addWidget(arg__1, self._current_row, self._column_index, row_span, column_span)

            # se aumenta en 1 la fila actual
            self._current_row += row_span

     
class GridLayout(QGridLayout, FluvelLayout):

    def __init__(self):
        super().__init__()
    
    def Column(self, column_index: int) -> ColumnIndex:

        return ColumnIndex(self, column_index)
    
    def Columns(self, n_cols: int) -> list[ColumnIndex]:
        
        columns: list = []

        for c in range(n_cols):
            columns.append(ColumnIndex(self, c))
        
        return columns