# Fluvel
from fluvel.components.widgets import FLabel
from fluvel.components.widgets import FLineEdit
from fluvel.core.abstract_models.FluvelLayout import FluvelLayout

# PySide6
from PySide6.QtWidgets import QFormLayout


class FormLayout(QFormLayout, FluvelLayout):
    def __init__(self):
        super().__init__()

    def add_row(
        self, label: str | list, field: str | list = None
    ) -> tuple[FLabel, FLineEdit]:
        """
        This method adds a row to the form.
        Args:
            label (str): The string identifier that represents the text of the `Label` in `.fluml` file.
            field (str): The string identifier that represents the placeholder of the `LineEdit` in `.fluml` file.
        Returns:
            (tuple[Label, LineEdit]): A tuple with both widgets of the row.
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
