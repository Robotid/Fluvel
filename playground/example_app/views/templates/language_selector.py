from functools import partial
from fluvel import Template
from fluvel.composer import Factory

@Factory.compose("FButton")
def LangButton(text: str, change_to: str):
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
            c1.add(LangButton("áéñ Spanish", "es"))
            c2.add(LangButton("ABC English", "en"))
            c3.add(LangButton("ÄÖÜ Deutsch", "de"))
            c4.add(LangButton("あ Japanese", "ja"))
            c5.add(LangButton("éèç French", "fr"))
            c6.add(LangButton("Я Russian", "ru"))

            # Second Row
            c1.add(LangButton("ا Arab", "ar"))
            c2.add(LangButton("द Hindi", "hi"))
            c3.add(LangButton("한 Korean", "ko"))
            c4.add(LangButton("汉 Chinese", "cn"))
            c5.add(LangButton("ãõç Portuguese", "pt"))
            c6.add(LangButton("త Telugu", "te")) 
