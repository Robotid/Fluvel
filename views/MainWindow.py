# views.MainWindow

from core import AppWindow
from views.Login import LoginPage

class MainWindow(AppWindow):

    def setUpMainWindow(self):
        """ Display the `components` in the Main Window. """

        LoginPage(self.central_widget)
