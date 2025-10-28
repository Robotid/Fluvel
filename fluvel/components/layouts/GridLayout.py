# Fluvel
from fluvel.core.abstract_models.FluvelLayout import FluvelLayout
from fluvel.components.widgets.FContainer import FContainer

# PySide6
from PySide6.QtWidgets import QGridLayout, QWidget, QLayout


class ColumnIndex:
    """
    Handler for managing a single column in a GridLayout.
    
    This class provides a declarative and intuitive way to add widgets 
    sequentially to a specific column within a grid, emulating a vertical layout (VBoxLayout) for each one.
    
    :ivar grid: The container GridLayout instance.
    :type grid: QGridLayout
    :ivar column_index: The index of the column this handler manages.
    :type column_index: int
    :ivar _current_row: The integer indicating the current position of the row 'cursor' within a column.
    :type _current_row: int
    """

    def __init__(self, grid: QGridLayout, column_index: int):
        """
        Initializer for a ColumnIndex.

        :param grid: The container GridLayout instance.
        :type grid: QGridLayout
        :param column_index: The index of the column this handler manages.
        :type column_index: int
        """

        # Store the GridLayout instance
        self.grid = grid

        # Store the column index
        self._column_index = column_index

        # Instance variable used to indicate to the row cursor
        # that it should initially point to the first row (index 0)
        self._current_row: int = 0

    def add(
        self, 
        widget_or_layout: QWidget | QLayout, 
        row_span: int = 1, 
        column_span: int = 1
    ) -> None:
        """
        Adds a widget or layout to the next available row in the column.

        This method automatically finds the next empty cell in the assigned
        column and adds the given object. The row cursor is then advanced
        by the ``row_span`` value.

        :param widget_or_layout: The :class:`QWidget` or :class:`QLayout` to add to the cell.
        :type widget_or_layout: QWidget or QLayout
        :param row_span: The number of rows the object will span. Defaults to 1.
        :type row_span: int
        :param column_span: The number of columns the object will span. Defaults to 1.
        :type column_span: int
        """

        # If there is an element in the current cell
        while (
            self.grid.itemAtPosition(self._current_row, self._column_index) is not None
        ):
            # Increases the row cursor by 1
            # while the current cell is occupied by another Widget or Layout
            self._current_row += 1

        # Add the widget or layout with the row and column parameters of the class.
        self.grid.addCell(
            widget_or_layout, self._current_row, self._column_index, row_span, column_span
        )

        # The row cursor is increased according to the space occupied by the widget (row_span).
        self._current_row += row_span


class GridLayout(QGridLayout, FluvelLayout):
    """
    Base class for handling GridLayouts in Fluvel.
    
    This class provides the API to manage QGridLayouts, offering
    helper methods to simplify the addition of widgets and layouts.
    """

    def __init__(self, parent: FContainer | None = None):
        super().__init__(parent)

        self.parent = parent

    def Column(self, column_index: int) -> ColumnIndex:
        """
        Obtains a handler for a specific column in the grid.

        This method returns a :class:`ColumnIndex` object that allows widgets to be added
        sequentially to a column, as if it were a vertical layout.

        :param column_index: The index of the column to be handled (starting at 0).
        :type column_index: int
        :returns: A handler object for the specified column.
        :rtype: ColumnIndex

        .. seealso::
            :meth:`~GridLayout.Columns` for the idiomatic way of managing multiple columns.
        
        Example:
        --------
        .. code-block:: python
            ...
            with self.Grid() as grid:
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
        Preferred method for creating a list of :class:``ColumnIndex`` objects.

        This method allows for the idiomatic unpacking of column handlers
        in Python.

        :param n_cols: The number of columns to create in the grid.
        :type n_cols: int
        :returns: A list of :class:``ColumnIndex`` objects.
        :rtype: list
        
        Example:
        --------
        .. code-block:: python
            ...
            with self.Grid() as grid:

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
        widget_or_layout: QWidget | QLayout,
        /,
        row_index: int,
        column_index: int,
        row_span: int = 1,
        column_span: int = 1,
    ) -> None:
        """
        Adds a widget, layout or prefab to a grid cell.

        This method is used to manually place a :class:`QWidget` or :class:`QLayout`
        into a specific cell of the grid.

        :param widget_or_layout: The widget, layout or prefab to add to the cell.
        :type widget_or_layout: QWidget or QLayout or :py:class:`~fluvel.core.abstract_models.ABCAbstractView.AbstractView`
        :param row_index: The row index of the cell.
        :type row_index: int
        :param column_index: The column index of the cell.
        :type column_index: int
        :param row_span: The number of rows the object will span. Defaults to 1.
        :type row_span: int
        :param column_span: The number of columns the object will span. Defaults to 1.
        :type column_span: int
        :raises TypeError: if the provided object is not a QWidget or QLayout.

        .. note::

            While this method exists for manual control, it's recommended to use the
            declarative methods :meth:`~Grid.Column` and :meth:`~Grid.Columns`
            for a cleaner and more organized layout structure.

        .. seealso:: 
            :meth:`~Grid.Column`
            :meth:`~Grid.Columns`
            
        Example:
        --------
        .. code-block:: python
            ...
            with my_view.Grid() as grid:
                # Adds a button to row 0, column 0
                grid.addCell(FButton(text="button"), 0, 0)

                # Adds a label to row 0, column 1
                grid.addCell(FLabel(text="label"), 0, 1)

                # Adds a button that spans 2 columns
                grid.addCell(FButton(text="Spanning Button"), 1, 0, 1, 2)
        """

        args: tuple = (widget_or_layout, row_index, column_index, row_span, column_span)
        
        if isinstance(widget_or_layout, QWidget):
            self.addWidget(*args)

        elif isinstance(widget_or_layout, QLayout):
            self.addLayout(*args)
        
        elif hasattr(widget_or_layout, "container"):
            prefab, *params = args
            self.addWidget(prefab.container, *params)

        else:
            raise TypeError("The 'widget_or_layout' argument must be an instance of QWidget, QLayout or View")
