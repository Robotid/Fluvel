import re
from collections import defaultdict


class StyledTextParser:
    def __init__(self, text: str):

        self.text = text

        self.blocks = defaultdict(list)

        # Estructurar el formato de la información
        self._parse_FLUML()

    def _parse_FLUML(self):
        current_id = None
        for raw_line in self.text.splitlines():
            clean_line = raw_line.strip()
            if not clean_line or clean_line.startswith("#"):
                continue

            _match = re.match(r"\[(.+?)\]:", clean_line)
            if _match:
                current_id = _match.group(1).strip()
                continue

            if current_id and raw_line.startswith(" "):
                self.blocks[current_id].append(raw_line.strip())

    def _apply_styles(self, text):
        """
        Este método encuentra y traduce los patrones escritos en FLUML a la sintaxis HTML correspondiente.\n
        *En caso de coincidir más de un patrón, se anidan las etiquetas `<span>`.*
        """

        # LINK -> {content | href}
        text = re.sub(r"\{(.*?)\s*\|\s*(.*?)\}", r"<a href='\2';'>\1</a>", text)

        # UNDERLINE -> __content__
        text = re.sub(
            r"__([^_]+)__", r"<span style='text-decoration: underline;'>\1</span>", text
        )

        # LINE-THROUG -> --content--
        text = re.sub(
            r"--([^-]+)--",
            r"<span style='text-decoration: line-through;'>\1</span>",
            text,
        )

        # BOLD AND ITALIC -> ***content***
        text = re.sub(
            r"\*\*\*([^\*]+)\*\*\*",
            r"<span style='font-weight: bold; font-style: italic;'>\1</span>",
            text,
        )

        # BOLD -> **content**
        text = re.sub(
            r"\*\*([^\*]+)\*\*", r"<span style='font-weight: bold;'>\1</span>", text
        )

        # ITALIC -> *content*
        text = re.sub(
            r"\*([^\*]+)\*", r"<span style='font-style: italic;'>\1</span>", text
        )

        # VERTICAL ALIGN SUPER -> <sup>content</sup>
        text = re.sub(
            r"<sup>(.*?)</sup>", r"<span style='vertical-align: super;'>\1</span>", text
        )

        # VERTICAL ALIGN SUB -> <sub>content</sub>
        text = re.sub(
            r"<sub>(.*?)</sub>", r"<span style='vertical-align: sub;'>\1</span>", text
        )

        return text

    def render_html(self) -> dict:
        """
        Este método procesa cada bloque de texto,
        aplica los estilos y devuelve el contenido renderizado a HTML.

        Returns:
            dict: Un diccionario con los IDs (claves) referenciando
            a su contenido HTML renderizado (valores).
        """

        result: dict = {}

        for block_id, lines in self.blocks.items():

            full_text = " ".join(lines)

            rendered = self._apply_styles(full_text)

            result[block_id] = rendered

        return result


def convert_FLUML_to_HTML(fluml_content: str) -> dict:

    parser = StyledTextParser(fluml_content)

    return parser.render_html()
