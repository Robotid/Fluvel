# Fluvel
from fluvel.core.abstract_models.FluvelLayout import FluvelLayout

# PySide6
from PySide6.QtWidgets import QGridLayout, QWidget, QLayout

class ColumnIndex:
    """
    Clase que provee el funcionamiento para la adición intuitiva
    y automática de widgets en un GridLayout.
    """

    def __init__(self, grid: QGridLayout, column_index: int):

        # Almacenamos la instancia GridLayout
        self.grid = grid

        # Almacenamos el índice de la columna
        self._column_index = column_index

        # Variable de instancia que sirve para indicar al cursor de la fila
        # que al inicio apunte a la primera fila (índice 0)
        self._current_row: int = 0

    def add(
        self, 
        arg__1: QWidget | QLayout, 
        row_span: int = 1, 
        column_span: int = 1
    ) -> None:
        """
        Args:
            arg__1 (QWidget | QLayout): El `Widget` o `Layout` que ocupará la celda.
            row_span (int): El número de celdas hacia abajo que abarcará el objeto. 1 por defecto.
            column_span (int): El número de celdas a la derecha que abarcará el objeto. 1 por defecto.
        """

        # Si existe un elemento en la celda actual
        while (
            self.grid.itemAtPosition(self._current_row, self._column_index) is not None
        ):
            # Se aumenta el cursor de la fila en 1
            # mientras la celda actual esté ocupada por otro Widget o Layout
            self._current_row += 1

        # Se añade el widget o layout con los parametros row, column de la clase
        self.grid.addCell(
            arg__1, self._current_row, self._column_index, row_span, column_span
        )

        # Se aumenta el cursor de la fila según el espacio ocupado por el widget (row_span)
        self._current_row += row_span


class GridLayout(QGridLayout, FluvelLayout):
    """
    Clase base de Fluvel para el manejo de GridLayouts
    """

    def __init__(self):
        super().__init__()

    def Column(self, column_index: int) -> ColumnIndex:
        """
        Obtains a handler for a specific column in the grid.

        This method returns a `ColumnIndex` object that allows widgets to be added
        sequentially to a column, as if it were a vertical layout.

        Args:
            column_index (int): The index of the column to be handled (starting at 0).

        Returns:
            ColumnIndex: A handler object for the specified column.

        Example:
            One of the preferred ways to handle GridLayouts
            .. code-block:: python

                with self.Grid(parent) as grid:
                    c1 = grid.Column(0) # first column
                    c2 = grid.Column(1) # second column

                    # Add widgets to the first column
                    c1.add(FLabel(text="Name:"))
                    c1.add(FLineEdit())

                    # Add widgets to the second column
                    c2.add(FLabel(text="Surname:"))
                    c2.add(FLineEdit())
        """

        return ColumnIndex(self, column_index)

    def Columns(self, n_cols: int) -> list[ColumnIndex]:
        """
        Preferred method for creating `ColumnIndex` objects using
        Python unpacking.

        Args:
            n_cols (int): The number of columns in the Grid.

        Returns:
            list[ColumnIndex]: A list of ColumnIndex objects.

        Example:
            This is the idiomatic method for structuring a Grid in Fluvel.
            
            .. code-block:: python
            
                with self.Grid(parent) as grid:

                    c1, c2 = grid.Columns(2) 
                   
                    # Add widgets to the first column
                    c1.add(FLabel(text="Name:"))
                    c1.add(FLineEdit())

                    # Add widgets to the second column
                    c2.add(FLabel(text="Surname:"))
                    c2.add(FLineEdit())
        """

        return [ColumnIndex(self, index) for index in range(n_cols)]

    def addCell(
        self,
        arg__1: QWidget | QLayout,
        row_index: int,
        column_index: int,
        row_span: int = 1,
        column_span: int = 1,
    ) -> None:
        """
        Método para añadir manualmente un Widget o Layout en 
        una celda de la grilla.
        Args:
            arg__1 (QWidget | QLayout): El `Widget` o `Layout` que ocupará la celda.
            row_index (int): El índice de la fila.
            column_index (int): El índice de la columna.
            row_span (int): El número de celdas hacia abajo que abarcará el objeto. 1 por defecto.
            column_span (int): El número de celdas a la derecha que abarcará el objeto. 1 por defecto.
        ### Uso:
        >>> my_view.Grid(parent) as grid:
                # Añade un botón en la fila=0, columna=0
                grid.addCell(FButton(text="button"), 0, 0, 1, 1)
                # Añade un label en la fila=0, columna=1
                grid.addCell(FLabel(text="label"), 0, 1, 1, 1)
        \nSi bien este método existe, la forma apropiada de gestionar
        un **`GridLayout`** es a través de sus métodos `Column` y `Columns`.
        """
        args: tuple = (arg__1, row_index, column_index, row_span, column_span)

        if isinstance(arg__1, QWidget):
            self.addWidget(*args)

        elif isinstance(arg__1, QLayout):
            self.addLayout(*args)

        else:
            raise TypeError("The 'arg__1' must be an instance of QWidget or QLayout")
