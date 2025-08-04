# Fluvel
from components import Label
from components.gui import StyledText
from models import GlobalContent

# PySide6
from PySide6.QtWidgets import QFormLayout, QLineEdit

class FormLayout(QFormLayout):
    def __init__(self):
        super().__init__()

    def add_row(self, label: str, field: str | None = None) -> tuple[Label, QLineEdit]:
        """
        This method adds a row to the form.
        Args:
            label (str): The string identifier that represents the text of the `Label` in `.fluml` file.
            field (str): The string identifier that represents the placeholder of the `LineEdit` in `.fluml` file. 
        Returns:
            (tuple[Label, QLineEdit]): A tuple with both widgets of the row.
        """
        if field is None:
            field = f"{label}-behind"
        
        # el Widget Label
        label_field = Label(text=StyledText(label))

        # el Widget QLineEdit
        input_field = QLineEdit(placeholderText=StyledText(field).text)

        # El campo es para una contraseña
        if "password" in field:

            input_field.setEchoMode(QLineEdit.EchoMode.Password)

        # Añadiendo la Fila
        self.addRow(label_field, input_field)

        # Retornando los Widgets
        return label_field, input_field
