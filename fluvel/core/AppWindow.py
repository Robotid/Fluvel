# fluvel.core.AppWindow

from pathlib import Path
from typing import TypedDict, Unpack, Literal

# Fluvel
from fluvel.core import App
from fluvel.core.MenuBar import MenuBar
from fluvel.core.core_utils.core_process import configure_process

# PySide6
from PySide6.QtWidgets import QMainWindow, QWidget

# Utils
from fluvel.utils.paths import CONTENT_DIR

InitialDisplay = Literal["FullScreen", "Maximized", "Minimized", "Normal"]

class AppWindowKwargs(TypedDict, total=False):

    title: str | None
    geometry: tuple | None
    initial_display: InitialDisplay


class AppWindow(QMainWindow):

    _MAPPING_METHODS = {
        "title": "setWindowTitle",
        "geometry": "setGeometry"
    }

    def __init__(self, root: App) -> None:
        super().__init__()
        
        # Saving the app instance of the QApplication/App()
        self.root = root

        # Se diseña el estado inicial de la UI
        self.init_ui()

        # Se inicializa y muestra UI
        self._init_core_ui()

    # abstract method donde se diseña el estado inicial
    # de la UI a través del método -self.configure- 
    def init_ui(self) -> None: pass
    
    # Abstract method
    def setUpMainWindow(self) -> None: pass

    def configure(self, **kwargs: Unpack[AppWindowKwargs]) -> None:

        configure_process(self, self._MAPPING_METHODS, **kwargs)


    def _init_core_ui(self) -> None:
        """
        This method performs the core configurations of the application's user interface window.
        """

        # Configuring the layout
        self._set_central_widget()

        # Configuring the Top Menu Bar
        self._set_menu_bar()

        # Display views
        self.setUpMainWindow()


    def _set_menu_bar(self) -> None:
        """
        **`IMPORTANT`** Este método inicializa el proceso para la creación del menú dinámico.
        """

        menu_file: Path = CONTENT_DIR / self.root.config.language / "menus" / "menu.fluml"

        # This is not an instance of QMenuBar
        self.menu_bar = MenuBar(parent=self, menu_file=menu_file)

        # Creating the full_menu_options.txt file
        if self.root.config.DEV_MODE:
            self.set_menu_bar_options()

    def clear_layout(self, layout):
        """Elimina todos los widgets de un layout."""
        if layout is not None:
            while layout.count():
                child = layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()

    def update_ui(self):
        """
        Método llamado por el hreloader para actualizar la interfaz.
        """
        print("Actualizando la interfaz de usuario...")

        # Borra el widget central y los layouts
        self.central_widget.deleteLater()

        # Crea uno nuevo
        self._set_central_widget()

        self.setUpMainWindow()

    def _set_central_widget(self) -> None:
        """
        Configuraciones iniciales del layout de la ventana principal.\n
        Por defecto se provee un QWidget() central para implementar los diseños.
        """

        self.central_widget = QWidget()

        self.central_widget.setObjectName("central-widget")

        self.setCentralWidget(self.central_widget)

