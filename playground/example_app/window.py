from fluvel.core import AppWindow

class MainWindow(AppWindow):

    def init_ui(self):
        """Display the `components` in the Main Window."""

        # # configure menu options
        self.build_menu_bar()

    def build_menu_bar(self):

        change_theme = self.root.change_theme
        change_language = self.root.change_language

        self.menu_bar.config(
            shortcuts=[
                ("quit", "Ctrl+Q", self.close)
            ],
            on_triggered=[
                # -------------- Menu Settings ---------------------
                # Themes
                ("bootstrap_theme", change_theme, "bootstrap"),
                ("modern_dark_theme", change_theme, "modern-dark"),
                # Languages
                ("es_language", change_language, "es"),
                ("en_language", change_language, "en"),
            ]
        )