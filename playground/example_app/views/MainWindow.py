# views.MainWindow

from fluvel.core import AppWindow
from functools import partial

from views.LoginDemo import LoginPage


class MainWindow(AppWindow):

    def setUpMainWindow(self):
        """Display the `components` in the Main Window."""

        # self.demo_view = Demo(self.central_widget)
        self.demo_view = LoginPage(self.central_widget)

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

        # Manejando el cambio de idioma
        bind("en_language", "triggered", lambda: self.change_language("en"))
        bind("es_language", "triggered", lambda: self.change_language("es"))

    def change_language(self, language) -> None:

        self.root.change_language(language)

        # self._init_core_ui()

    def init_ui(self):
        # Screen size

        screen_geometry = self.root.primaryScreen().availableGeometry()
        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()
        x = (screen_width - self.root.config.window_width) // 2
        y = (screen_height - self.root.config.window_height) // 2

        self.configure(
            title=f"{self.root.config.app_name} - {self.root.config.version}",
            geometry=(
                x,
                y,
                self.root.config.window_width,
                self.root.config.window_height,
            ),
        )
