# views.MainWindow

from core import AppWindow
from functools import partial

from views.LoginDemo import LoginPage
from fluvel.views.Demo import Demo


class MainWindow(AppWindow):

    def setUpMainWindow(self):
        """Display the `components` in the Main Window."""

        self.demo_view = Demo(self.central_widget)

        # configure menu options
        self.config_menu()

    def config_menu(self) -> None:

        # Menu Config Example
        bind = self.menu_bar.bind
        add_shortcut = self.menu_bar.add_shortcut
        change_theme = self.root.change_theme

        # Add a shortcut
        add_shortcut("quit", "Ctrl+Q", self.close)

        themes: tuple[tuple[str, str]] = (
            ("bootstrap", "bootstrap_theme"),
            ("modern-dark", "modern_dark_theme"),
            ("clean-light", "clean_light_theme"),
        )

        for theme in themes:

            name, option = theme

            controller = partial(change_theme, name)

            bind(option, "triggered", controller)