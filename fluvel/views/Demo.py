from core import ViewBuilder
from components import Button

from PySide6.QtCore import Slot

class Demo(ViewBuilder):

    def view(self):

        with self.Grid(self.parent) as main:
            main.adjust(margins=(50, 50, 50, 50), alignment=main.CENTER)

            c1, c2 = main.Columns(2)

            btn = Button(text="Dark Button Outlined", style="dark-outlined")
            btn.clicked.connect(self.saludar)

            # Normal
            c1.add(Button(text="Primary Button", style="primary"))
            c1.add(Button(text="Secondary Button", style="secondary"))
            c1.add(Button(text="Success Button", style="success"))
            c1.add(Button(text="Info Button", style="info"))
            c1.add(Button(text="Warning Button", style="warning"))
            c1.add(Button(text="Danger Button", style="danger"))
            c1.add(Button(text="Dark Button", style="dark"))
            c1.add(Button(text="Light Button", style="light"))

            # Outlined
            c2.add(Button(text="Primary Button Outlined", style="primary-outlined"))
            c2.add(Button(text="Secondary Button Outlined", style="secondary-outlined"))
            c2.add(Button(text="Success Button Outlined", style="success-outlined"))
            c2.add(Button(text="Info Button Outlined", style="info-outlined"))
            c2.add(Button(text="Warning Button Outlined", style="warning-outlined"))
            c2.add(Button(text="Danger Button Outlined", style="danger-outlined"))
            c2.add(btn)
            c2.add(Button(text="Light Button Outlined", style="light-outlined"))

    @Slot()
    def saludar(self):
        print("Hola!")