from fluvel.core import AppWindow
from fluvel.cli.templates.demostrations.DemoView import Demo


class MainWindow(AppWindow):

    def setUpMainWindow(self):
        """Display the `components` in the Main Window."""

        self.demo_view = Demo(self.central_widget)
