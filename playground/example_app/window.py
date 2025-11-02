from fluvel.core import AppWindow

import qtawesome as qta

class MainWindow(AppWindow):

    def init_ui(self):
        """Display the `components` in the Main Window."""

        self.configure(
            size=(920, 605),
            flags=["frameless"],
            attributes=["translucent-background"]
        )
        
        # configure menu options
        self.build_menu_bar()

    def build_menu_bar(self):

        change_theme = self.root.change_theme
        change_language = self.root.change_language

        self.menu_bar.configure(
            controls={
                # -------------- FILE ---------------------
                "quit": {
                    "triggered": self.close,
                    "Shortcut": "Ctrl+Q"
                },
                # -------------- SETTINGS ----------------
                "bootstrap_theme": {
                    "triggered": lambda: change_theme("bootstrap"),
                    "Icon": qta.icon(f"fa5b.github", color="black", options=[{"scale_factor": 0.9}])
                },
                "modern_dark_theme": {
                    "triggered": lambda: change_theme("modern-dark")
                },
                "es_language": {
                    "triggered": lambda: change_language("es")
                },
                "en_language": {
                    "triggered": lambda: change_language("en")
                },
            }
        )

