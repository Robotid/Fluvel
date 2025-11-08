# Fluvel
from fluvel.components.widgets import FLabel
from fluvel.components.widgets import FInput
from fluvel.core.abstract_models.FluvelLayout import FluvelLayout
from fluvel.components.widgets.FContainer import FContainer
from fluvel.core.abstract_models.Builder import Builder

# PySide6
from PySide6.QtWidgets import QFormLayout


class FormLayout(QFormLayout, FluvelLayout, Builder):
    def __init__(self, parent: FContainer | None = None):
        super().__init__(parent)

    def Row(
        self, label: str | list, field: str | list = None
    ) -> tuple[FLabel, FInput]:
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
        input_field = FInput(placeholder_text=[field])

        # Añadiendo la Fila
        self.addRow(label_field, input_field)

        # Retornando los Widgets
        return label_field, input_field
