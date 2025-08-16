from fluvel.controllers.content_controller import get_content_by_id
from fluvel.core.exceptions import ContentNotFoundError
from fluvel.components.gui import StringVar
import re



class StyledText:
    def __init__(self, content_id: str, *placeholders) -> None:
        """
        Args:
            content_id (str): The string identifier that represents the content block in `.fluml` files
            *placeholders (str): The var that will replace the placeholder in the content block.
        """
        self._id: str = content_id
        self.placeholders: tuple = placeholders

    @property
    def var(self) -> str:
        """
        Returns:
            (StringVar): una variable `StringVar` relacionada al ID en `GlobalContent.content_map`.\n
            *El Property Method de esta variable contiene el RichText obtenido de los archivos `.fluml`*
        """
        try:

            # Load the RichText content from GlobalContent
            content: StringVar = get_content_by_id(content_id=self._id)

            # Check for placeholders in the text
            _match = re.findall(r"\$(\d+)", content.value)

            if _match:

                for marker in _match:

                    content.value = content.value.replace(
                        f"${marker}", self.placeholders[int(marker)]
                    )

            return content

        # No se encontró contenido relacionado al ID
        except ContentNotFoundError as e:
            print(f"{type(e).__name__}: {e}")

        return ""
