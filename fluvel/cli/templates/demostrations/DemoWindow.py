from fluvel.core import AppWindow
from fluvel.cli.templates.demostrations.DemoView import Demo


class DemoWindow(AppWindow):

    def setUpMainWindow(self):
        """Display the `components` in the Main Window."""

        self.demo_view = Demo(self.central_widget)

    def init_ui(self) -> None:

        screen_geometry = self.root.primaryScreen().availableGeometry()
        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()
        x = (screen_width - self.root.config.window_width) // 2
        y = (screen_height - self.root.config.window_height) // 2

        self.configure(
            title="Demo Widgets",
            geometry=(
                x,
                y,
                self.root.config.window_width,
                self.root.config.window_height,
            ),
        )
