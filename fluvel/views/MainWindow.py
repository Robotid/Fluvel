# views.MainWindow

from core import AppWindow
from views.LoginDemo import LoginPage

class MainWindow(AppWindow):

    def setUpMainWindow(self):
        """ Display the `components` in the Main Window. """
        
        # View Example
        LoginPage(self.central_widget)

        # configure menu options
        self.config_menu()

    def config_menu(self) -> None:

        # Menu Config Example
        bind = self.menu_bar.bind
        add_shortcut = self.menu_bar.add_shortcut
        theme = self.root.change_theme

        # Add a shortcut
        add_shortcut("quit", "Ctrl+Q", self.close)

        # configure theme switching
        bind("bootstrap_theme", "triggered", lambda: theme("bootstrap"))
        bind("modern_dark_theme", "triggered", lambda: theme("modern-dark"))
        bind("clean_light_theme", "triggered", lambda: theme("clean-light"))