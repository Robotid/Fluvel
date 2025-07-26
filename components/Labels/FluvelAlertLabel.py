from typing import Literal
from PySide6.QtWidgets import QLabel, QHBoxLayout, QFrame, QVBoxLayout, QSizePolicy, QPushButton, QWidget
from PySide6.QtGui import QIcon, Qt, QPixmap
from PySide6.QtCore import Signal
from utils import APP_ROOT

AlertTypes = Literal["FluvelInfoAlert", "FluvelDangerAlert", "FluvelWarningAlert", "FluvelSuccessAlert"]

IconsPath = APP_ROOT / "resources" / "icons" / "bootstrap-icons"

class FluvelAlertLabel(QFrame):
    """
    Clase base de **`Fluvel`** para etiquetas de alerta estilizadas. Las subclases deben definir el atributo **`_alert_type`**.
    """
    closed = Signal(QWidget) # <--- Here it is!

    _alert_type: AlertTypes
    _icon: str
    _close_icon_path: str = str(IconsPath / "close.png")

    def __init__(self, text: str) -> None:
        super().__init__()
        self.setObjectName(self._alert_type)
        self.setProperty("type", "frame-container")

        # *** CORRECTED LINE ***
        # Assign self.body as the main layout for the QFrame (self)
        self.body = QVBoxLayout(self) # This correctly sets the layout for 'self'
        
        # *** CORRECTED LINE ***
        # Create top_layout WITHOUT assigning it directly to 'self'.
        # It will be added to 'self.body' later.
        self.top_layout = QHBoxLayout() # No 'self' argument here!

        # Título de la alerta 
        self.title = QLabel(text)
        self.title.setProperty("type", "title-label")
        self.title.setObjectName(f"{self._alert_type}Title")
        self.title.setMaximumHeight(40) # Consider removing this if you want auto-height adjustment

          # 3. Botón de cierre
        self.close_button = QPushButton()
        self.close_button.setProperty("type", "close-btn")
        self.close_button.setObjectName("CloseButton")
        self.close_button.setFixedSize(24, 24) # Tamaño del botón de cierre
        self.close_button.setMinimumWidth(50)
        self.close_button.setIcon(QIcon(self._close_icon_path)) # Establece el ícono
        self.close_button.setIconSize(self.close_button.size()) # El ícono ocupa todo el botón
        self.close_button.setFlat(True) # Para un aspecto de ícono puro (sin borde 3D)

        # Conectar la señal clicked del botón a un slot que emitirá nuestra señal custom 'closed'
        self.close_button.clicked.connect(self._emit_closed_signal)

        # Ícono en el título
        # self.label_icon = QLabel()
        # self.label_icon.setObjectName("LabelIcon")
        # self.label_icon.setFixedSize(32, 32)
        # # Ensure self._icon is a valid path to an image before loading
        # pixmap = QPixmap(self._icon)
        # if pixmap.isNull():
        #     print(f"Warning: Could not load icon from {self._icon}. Check path and file integrity.")
        #     # Optionally, set a default pixmap or hide the label_icon
        #     self.label_icon.hide() 
        # else:
        #     self.pixmap_icon = pixmap.scaled(24, 24, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        #     self.label_icon.setPixmap(self.pixmap_icon)
        
        # Texto de la alerta
        self.description = QLabel("Alguna Descripción")
        self.description.setObjectName(f"{self._alert_type}Description")
        self.description.setProperty("type", "description-label")
        self.description.setWordWrap(True)

        # *** CORRECTED LAYOUT STRUCTURE ***
        # Add the icon to the top_layout first
        # self.top_layout.addWidget(self.label_icon) 
        # Then add the title to the top_layout
        self.top_layout.addWidget(self.title)
        # Add a stretch to push icon and title to the left
        self.top_layout.addStretch()
        self.top_layout.addWidget(self.close_button)

        # Add the top_layout (which contains icon and title) to the body layout
        self.body.addLayout(self.top_layout)
        # Add the description to the body layout
        self.body.addWidget(self.description)
        
        # --- Estilo del QFrame (para visibilidad) ---
        self.body.setContentsMargins(0, 0, 0, 0)
        self.setFrameShape(QFrame.StyledPanel)
        self.setLineWidth(1)
    
    def _emit_closed_signal(self):
        self.closed.emit(self)


class FluvelInfoAlert(FluvelAlertLabel):
    _icon = str(IconsPath / "info.png")
    _alert_type = "FluvelInfoAlert"

class FluvelDangerAlert(FluvelAlertLabel):
    _icon = str(IconsPath / "danger.png")
    _alert_type = "FluvelDangerAlert"

class FluvelWarningAlert(FluvelAlertLabel):
    _icon = str(IconsPath / "danger.png")
    _alert_type = "FluvelWarningAlert"

class FluvelSuccessAlert(FluvelAlertLabel):
    _icon = str(IconsPath / "success.png")
    _alert_type = "FluvelSuccessAlert"