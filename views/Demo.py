from core import ViewBuilder

from components import LineEdit

class Demo(ViewBuilder):

    def view(self):

        with self.Vertical(self.parent) as v:
            v.adjust(alignment=v.CENTER, margins=(50, 50, 50, 50))

            input_field = LineEdit(
                text="hola!"
            )

            v.addWidget(input_field)