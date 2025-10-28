from typing import Unpack

# Fluvel
from fluvel.components.widgets.FButton import FButton, FButtonKwargs

# PySide6
from PySide6.QtCore import QUrl
from PySide6.QtGui import QDesktopServices

class FLinkButton(FButton):
    def __init__(self, url: str, **kwargs: Unpack[FButtonKwargs]):
        super().__init__(**kwargs)

        self._set_defaults()

        self.url = url
        
        self.clicked.connect(self.open_link)

    def open_link(self):
        QDesktopServices.openUrl(QUrl(self.url))
