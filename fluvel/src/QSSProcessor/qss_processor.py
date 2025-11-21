import re
from typing import Dict, List

class QSSProcessor:
    """
    QSS style preprocessing engine for Silk Framework.

    This class is responsible for translating Silk's simplified and utilitarian syntax 
    (e.g., ``bg[red]``, ``h::f-size[14px]``) into native QSS stylesheets that are valid for Qt.

    It implements a system of tokens and regular expressions to parse standard properties,
    interactive pseudo-states (hover, pressed, etc.), and generate complex gradients.
    """
    
    TEMPLATES = {
        "common": "{widget_name}#{id} {{\n\t{properties}\n}}\n",
        "h": "{widget_name}#{id}:hover {{\n\t{properties}\n}}\n",
        "p": "{widget_name}#{id}:pressed {{\n\t{properties}\n}}\n",
        "d": "{widget_name}#{id}:disabled {{\n\t{properties}\n}}\n",
        "c": "{widget_name}#{id}:checked {{\n\t{properties}\n}}\n"
    }

    BASE_PATTERN = re.compile(r"""
        (?:^|\s)                      # Inicio de string o espacio (Non-capturing)
        (?:                           # Inicio de Prefijo Interactivo Opcional (Non-capturing)
            (?P<state>[a-z])          # Grupo 'state': Captura 'h', 'p', 'd', etc.
            ::                        # Literal '::'
        )?                            # Fin de Prefijo Interactivo Opcional
        (?P<token>[a-z-]+)            # Grupo 'token': Captura 'bg', 'f-size', etc.
        \[                            
        (?P<value>.*?)                # Grupo 'value': Captura el contenido.
        \]
    """, re.VERBOSE)

    GRADIENT_PREFIX = "bg-lgradient"

    STYLE_TOKENS = {
        "bg": "background-color: {value};",
        "bg-img": "background-image: url(\"{value}\");",
        "bg-repeat": "background-repeat: {value};",
        "bg-position": "background-position: {value};",
        "bg-origin": "background-origin: {value};",
        "bg-lgradient-v": "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, {value});",
        "bg-lgradient-rv": "background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, {value});", # reversed vertical gradient
        "bg-lgradient-h": "background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, {value});",
        "bg-lgradient-rh": "background-color: qlineargradient(x1: 1, y1: 0, x2: 0, y2: 0, {value});", # reversed horizontal gradient

        "b": "border: {value};",
        "b-color": "border-color: {value};",
        "b-style": "border-style: {value};",
        "b-width": "border-width: {value};",
        "br": "border-radius: {value};",
        
        "b-left": "border-left: {value};",
        "b-top": "border-top: {value};",
        "b-right": "border-right: {value};",
        "b-bottom": "border-bottom: {value};",

        "br-tl": "border-top-left-radius: {value};",  
        "br-tr": "border-top-right-radius: {value};",  
        "br-bl": "border-bottom-left-radius: {value};",  
        "br-br": "border-bottom-right-radius: {value};", 

        "f-size": "font-size: {value};",
        "f-color": "color: {value};",
        "f-weight": "font-weight: {value};",
        "f-align": "text-align: {value};",
        "f-family": "font-family: {value};",
        "f-style": "font-style: {value};",
        "f-decoration": "text-decoration: {value};",
        
        "m": "margin: {value};",
        "m-top": "margin-top: {value};",
        "m-bottom": "margin-bottom: {value};",
        "m-left": "margin-left: {value};",
        "m-right": "margin-right: {value};",
        
        "p": "padding: {value};",
        "p-top": "padding-top: {value};",
        "p-bottom": "padding-bottom: {value};",
        "p-left": "padding-left: {value};",
        "p-right": "padding-right: {value};",
        
        "w": "width: {value};",
        "h": "height: {value};",
        "min-w": "min-width: {value};",
        "min-h": "min-height: {value};",
        "max-w": "max-width: {value};",
        "max-h": "max-height: {value};",
    }

    @classmethod
    def process(cls, styles: str, widget_name: str, widget_id: str) -> str:
        """
        Processes a Silk style string and generates the final QSS code.

        This method parses the input string for normal and interactive style patterns,
        resolves tokens using :attr:`STYLE_TOKENS`, and constructs the complete CSS style block
        applied to the specific widget ID.

        :param styles: The style string in Silk syntax (e.g., ``“bg[#333] :h:bg[#555]”``).
        :type styles: str
        :param widget_name: The name of the widget class (e.g., ``“QPushButton”``).
        :type widget_name: str
        :param widget_id: The unique ID of the object (e.g., ``“12345678”``) used as the ID selector in QSS.
        :type widget_id: str
        :return: The complete, formatted QSS code ready for use in ``setStyleSheet``.
        :rtype: str

        .. note::
            Interactive properties are automatically grouped by state to generate
            efficient pseudo-selector blocks.
        """

        # Variable that serves as an accumulator
        # for processed QSS styles
        final_qss: str = ""

        parsed_qss_lines: Dict[str, List] = {}

        # We search for matches and groups in the string
        # ‘styles’ based on the regular expression ‘cls.BASE_PATTERN’
        matches = cls.BASE_PATTERN.findall(styles)

        # If matches were found
        # in the ‘matches’ list
        if matches:
            
            # We iterate through each match found
            # and obtain the ‘state’, ‘token’, and ‘value’ groups
            for state, token, value in matches:

                # If ‘state’ is an empty group, it is assigned the value “common”
                # (this is the case for common properties, e.g. ‘f-color[red]’ 'bg[white]', etc.)
                state = "common" if not state else state

                # We create the corresponding QSS string through its ‘token’ and ‘value’
                qss_line = cls._resolve_token(token, value)

                # If nothing was obtained because the token is not mapped
                # in ‘cls.STYLE_TOKENS’, we continue to the next property
                if not qss_line:
                    continue
                
                # If ‘state’ is not in the ‘parsed_qss_lines’ dictionary
                # the state is mapped and assigned an empty list to
                # store the Processed QSS strings for that ‘state’
                if state not in parsed_qss_lines:
                    parsed_qss_lines[state] = []

                # Finally, the Processed QSS string is added
                # to the ‘state’ list
                parsed_qss_lines[state].append (qss_line)

        # Now, for each ‘state’ and ‘properties’ (i.e., the list of processed QSS strings)
        # in the ‘parsed_qss_lines’ dictionary, we fill in the ‘cls.TEMPLATES’ templates
        # and concatenate them with ‘final_qss’.
        for state, properties in parsed_qss_lines.items():

            template_to_fill = cls.TEMPLATES.get(state)

            if not template_to_fill:
                print(f"Unknown QSS template state: '{state}'")
                continue

            final_qss += cls._fill_template(template_to_fill, widget_name, widget_id, properties)

        return final_qss
    
    @classmethod
    def _fill_template(cls, template: str, widget_name: str, widget_id: str, properties: List)  -> str:
        """Fill in the QSS template with the widget name, ID, and formatted properties."""
        
        filled_template = template.format(
            widget_name=widget_name,
            id=widget_id,
            properties="\n\t".join(properties)
        )

        return filled_template

    @classmethod
    def _resolve_token(cls, property_name: str, value: str) -> str | None:
        """
        Resolves a Silk property token to its equivalent QSS line.

        Searches for the token in the :attr:`STYLE_TOKENS` dictionary. If it is a gradient,
        processes the value through :meth:`generate_qss_stops` before substitution.

        :param property_name: The name of the property token (e.g., ``"bg"``, ``"bg-lgradient-v"``).
        :type property_name: str
        :param value: The value assigned to the property.
        :type value: str
        :return: The complete QSS line (e.g., ``"background-color: #fff;"``) or ``None`` if the token does not exist.
        :rtype: str | None
        """
        
        token_template = cls.STYLE_TOKENS.get(property_name)
        
        if not token_template:
            print(f"Unmapped QSS property: '{property_name}'")
            return None

        # Procesamiento para gradientes
        if property_name.startswith(cls.GRADIENT_PREFIX):
            value = cls.generate_qss_stops(value)

        return token_template.format(value=value)

    @classmethod
    def generate_qss_stops(cls, colors: str) -> str:
        """
        Generates the string of 'stops' for a QSS gradient from a list of colors.

        Converts a string of colors separated by ``|`` into the ``stop`` syntax required
        by ``qlineargradient``. Automatically calculates the positions of the intermediate colors
        to distribute them evenly between 0.0 and 1.0.

        Example:
        
            Input: "#f00|#0f0|#00f"
            Output: "stop: 0.00 #f00, stop: 0.50 #0f0, stop: 1.00 #00f"

        :param colors: String with color codes separated by ``|``.
        :type colors: str
        :return: Formatted string of stops for QSS.
        :rtype: str
        """
        colors_list = colors.split("|")
        num_colors = len(colors_list)
        
        if num_colors == 0: return ""
        if num_colors == 1: return f"stop: 0 {colors_list[0]}, stop: 1 {colors_list[0]}"

        stops = []
        for i, color in enumerate(colors_list):
            pos = i / (num_colors - 1)
            stops.append(f"stop: {pos:.3f} {color}")
            
        return ", ".join(stops) 