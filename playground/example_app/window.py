from fluvel.core import AppWindow
from functools import partial

from fluvel._user import AppConfig
from playground.example_app.views.LoginPage import LoginPage


class MainWindow(AppWindow):

    def setUpMainWindow(self):
        """Display the `components` in the Main Window."""

        self.demo_view = LoginPage(self.central_widget)

        # configure menu options
        self.config_menu()

    def config_menu(self) -> None:

        # Menu Config Example
        bind = self.menu_bar.bind
        add_shortcut = self.menu_bar.add_shortcut
        change_theme = self.root.change_theme
        change_language = self.root.change_language

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
        bind("en_language", "triggered", lambda: change_language("en"))
        bind("es_language", "triggered", lambda: change_language("es"))

    def change_language(self, language) -> None:

        self.root.change_language(language)

    def init_ui(self):
        """
        Aplica las configuraciones principales en la Ventana Principal
        """

        # Screen size
        screen_geometry = self.root.primaryScreen().availableGeometry()
        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()
        x = (screen_width - AppConfig.window.width) // 2
        y = (screen_height - AppConfig.window.height) // 2

        self.configure(
            title=f"{AppConfig.app.name} - {AppConfig.app.version}",
            geometry=(
                x,
                y,
                AppConfig.window.width,
                AppConfig.window.height,
            ),
        )
