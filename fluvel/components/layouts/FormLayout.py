# Fluvel
from fluvel.components.widgets import FLabel
from fluvel.components.widgets import FLineEdit
from fluvel.core.abstract_models.FluvelLayout import FluvelLayout

# PySide6
from PySide6.QtWidgets import QFormLayout, QWidget


class FormLayout(QFormLayout, FluvelLayout):
    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)

    def Row(
        self, label: str | list, field: str | list = None
    ) -> tuple[FLabel, FLineEdit]:
        """
        This method adds a row to the form.

        :param label: The string identifier that represetns the text of the `Label` in `.fluml` file.
        :type label: str
        :param field: The string identifier that represents the placeholder of the `LineEdit` in `.fluml` file.
        :type field: str

        :returns: A tuple with both widgets of the row.
        :rtype: tuple[Label, LineEdit]
        """
        if field is None:
            field = f"{label}-behind"

        # el Widget Label
        label_field = FLabel(text=[label])

        # el Widget LineEdit
        input_field = FLineEdit(placeholder_text=[field])

        # Añadiendo la Fila
        self.addRow(label_field, input_field)

        # Retornando los Widgets
        return label_field, input_field
