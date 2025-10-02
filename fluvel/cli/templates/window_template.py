WINDOW_TEMPLATE = """from fluvel.core import AppWindow

class MainWindow(AppWindow):

    def init_ui(self):
        \"\"\" Make the main settings of the window\"\"\"

        # These settings replace those made in appconfig.toml
        self.configure(
            title="FluvelApp",
            size=[720, 500]
        )
"""