from typing import Literal

# PySide6 - Fluvel
from fluvel.components.gui.StyledText import StyledText
from fluvel.components.widgets import Label, Button
from PySide6.QtWidgets import QHBoxLayout, QFrame, QSizePolicy

# Utils
from fluvel.utils import APP_ROOT


AlertTypes = Literal["Infocard", "WarningCard", "SuccessCard", "DangerCard"]

IconsPath = APP_ROOT / "resources" / "icons" / "bootstrap-icons"


class FluvelCard(QFrame):
    """
    Clase base de **`Fluvel`** para etiquetas de aviso estilizadas. Las subclases deben definir el atributo **`_card_type`**.
    """

    _card_type: AlertTypes
    _icon: str

    def __init__(self, text: str | StyledText = None) -> None:
        super().__init__()

        self.setObjectName(self._card_type)
        self.setProperty("type", "card-container")
        self.setContentsMargins(5, 5, 5, 5)

        # Body layout Container
        self.hbox = QHBoxLayout(self)

        # self.icon_label = Label()
        # self.icon = QIcon(self._icon).pixmap(36, 36)
        # self.icon_label.setPixmap(self.icon)
        # self.icon_label.setFixedWidth(65)
        # self.icon_label.setProperty("type", "card-description")

        self.description_label = Label(text=text)
        self.description_label.setProperty("type", "card-description")
        self.description_label.setWordWrap(True)
        self.description_label.setSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred
        )

        self.close_btn = Button(text="")
        self.close_btn.setFixedSize(22, 12)
        self.close_btn.setProperty("type", "card-description")

        # self.hbox.addWidget(self.icon_label)
        self.hbox.addWidget(self.description_label)
        self.hbox.addWidget(self.close_btn)

        self.hbox.setContentsMargins(0, 0, 0, 0)
        self.setContentsMargins(0, 0, 0, 0)


class InfoCard(FluvelCard):
    _icon = str(IconsPath / "info.png")
    _card_type = "InfoCard"


class DangerCard(FluvelCard):
    _icon = str(IconsPath / "danger.png")
    _card_type = "DangerCard"


class WarningCard(FluvelCard):
    _icon = str(IconsPath / "warning.png")
    _card_type = "WarningCard"


class SuccessCard(FluvelCard):
    _icon = str(IconsPath / "success.png")
    _card_type = "SuccessCard"
