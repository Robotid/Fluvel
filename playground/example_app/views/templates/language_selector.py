from functools import partial
from fluvel import Template
from fluvel.composer import Factory

@Factory.compose("FButton")
def Button(text: str, change_to: str):
    return {
        "text": text,
        "style": "dark-outlined font-light rounded-2xl",
        "on_click": partial(Template.app_root.change_language, change_to)
    }

class LanguageSelector(Template):

    def build_ui(self):

        with self.Grid() as grid:
            grid.adjust(spacing=10, margins=(20, 20, 20, 20))

            c1, c2, c3, c4, c5, c6 = grid.Columns(6)

            # First Row
            c1.add(Button("🇪🇦 Spanish", "es"))
            c2.add(Button("🇺🇸 English", "en"))
            c3.add(Button("🇩🇪 Deutsch", "de"))
            c4.add(Button("🇯🇵 Japanese", "ja"))
            c5.add(Button("🇫🇷 French", "fr"))
            c6.add(Button("🇷🇺 Russian", "ru"))

            # Second Row
            c1.add(Button("🇪🇬 Arab", "ar"))
            c2.add(Button("🇮🇳 Hindi", "hi"))
            c3.add(Button("🇰🇷 Korean", "ko"))
            c4.add(Button("🇨🇳 Chinese", "zh"))
            c5.add(Button("🇵🇹 Portuguese", "pt"))
            c6.add(Button("🇮🇳 Telugu", "te"))
