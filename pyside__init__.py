import sys
import PySide6.QtWidgets as widgets
import PySide6.QtGui as gui
import PySide6.QtCore as core

class MainWindow(widgets.QWidget):
    def __init__(self):
        super().__init__()
        self.title = "App PySide6"
        self.screen_size = {"w" : 1280,"h" : 720}

        # Inicializar UI
        self.inicializarUI()

    def inicializarUI(self):
        """ Configurar la GUI de la aplicación """

        self.setWindowTitle(self.title)
        self.setGeometry(50, 50, self.screen_size["w"], self.screen_size["h"])

        # Display Widgets
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        """ Configurar los Wigets de la aplicación """
        ...

if __name__ == "__main__":
    app = widgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())