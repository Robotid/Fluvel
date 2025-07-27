import re
from collections import defaultdict
from pathlib import Path

class StyledTextParser:
    def __init__(self, text: str):

        self.text = text

        self.blocks = defaultdict(list)

        # Estructurar el formato de la información
        self._parse_FLUML()

    def _parse_FLUML(self):
        current_id = None
        for line in self.text.splitlines():
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue 

            match = re.match(r"\[(.+?)\]:", stripped)
            if match:
                current_id = match.group(1).strip()
                continue

            if current_id and line.startswith(" "):
                self.blocks[current_id].append(line.strip())

    def _apply_styles(self, text):
        """
        Este método encuentra y traduce los patrones a la sintaxis HTML correspondiente.\n
        En caso de coincidir más de un patrón, se anidan las etiquetas `<span>`.
        """

        # Patrones Single
        
        # LINK {content | href}
        text = re.sub(r"\{(.*?)\s*\|\s*(.*?)\}", r"<a href='\2';'>\1</a>", text)

        # UNDERLINE __content__
        text = re.sub(r"__([^_]+)__", r"<span style='text-decoration: underline;'>\1</span>", text)

        # LINE-THROUG -> --content--
        text = re.sub(r"--([^-]+)--", r"<span style='text-decoration: line-through;'>\1</span>", text)

        # BOLD AND ITALIC
        text = re.sub(r"\*\*\*([^\*]+)\*\*\*", r"<span style='font-weight: bold; font-style: italic;'>\1</span>", text)

        # BOLD -> **content**
        text = re.sub(r"\*\*([^\*]+)\*\*", r"<span style='font-weight: bold;'>\1</span>", text)

        # ITALIC -> *content*
        text = re.sub(r"\*([^\*]+)\*", r"<span style='font-style: italic;'>\1</span>", text)

        # VERTICAL ALIGN SUPER -> <<content>>
        text = re.sub(r"<sup>(.*?)</sup>", r"<span style='vertical-align: sub;'>\1</span>", text)

        # VERTICAL ALIGN SUB -> <<<content>>>
        text = re.sub(r"<sub>(.*?)</sub>", r"<span style='vertical-align: super;'>\1</span>", text)

        # if __name__ == "__main__":
        #     print(f"text: {text}")

        return text

    def render_html(self):

        result: dict = {}

        for block_id, lines in self.blocks.items():
            
            full_text = " ".join(lines)

            rendered = self._apply_styles(full_text)

            result[block_id] = rendered

        return result

input_text = """
[solicitud_no1]:
    ***Hi!***, this *is* an demostration our <sup>hola</sup> {Youtube | https://www.youtube.com} channel.
    Genial --hola--.

[solicitud_no2]:
    __n__o soy yo.
"""

def style_FLUML_CONTENT(content: dict) -> dict:

    parser = StyledTextParser(content)

    content_dict: dict = parser.render_html()

