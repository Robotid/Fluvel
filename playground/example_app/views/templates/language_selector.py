from functools import partial
from fluvel import Template
from fluvel.composer import Factory

@Factory.compose("FButton")
def Button(text: str, change_to: str):
    return {
        "text": text.capitalize(),
        "on_click": partial(Template.app_root.change_language, change_to)
    }


class LanguageSelector(Template):

    def build_ui(self):

        with self.Grid(self.container) as grid:
            grid.adjust(spacing=10, margins=(20, 20, 20, 20))

            c1, c2, c3, c4, c5, c6 = grid.Columns(6)

            # First Row
            c1.add(Button("spanish", "es"))
            c2.add(Button("english", "en"))
            c3.add(Button("deutsch", "de"))
            c4.add(Button("japanese", "ja"))
            c5.add(Button("french", "fr"))
            c6.add(Button("russian", "ru"))

            # Second Row
            c1.add(Button("arab", "ar"))
            c2.add(Button("hindi", "hi"))
            c3.add(Button("korean", "ko"))
            c4.add(Button("chinese", "zh"))
            c5.add(Button("portuguese", "pt"))
            c6.add(Button("telugu", "te"))
