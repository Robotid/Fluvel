from controllers import get_content_by_id
import re

from core.exceptions import ContentNotFoundError

class StyledText:
    def __init__(self, content_id: str, *placeholders) -> None:
        """
        Args:
            content_id (str): The string identifier that represents the content block in `.fluml` files
            *placeholders (str): The text that will replace the placeholder in the content block.
        """
        self._id: str = content_id
        self.placeholders: tuple = placeholders
    
    @property
    def text(self) -> str:
        """
        Returns:
            (str): El texto formateado a RichText obtenido de `GlobalContent.content_map`.
        """
        try:
            
            # Load the RichText content from GlobalContent
            content: str = get_content_by_id(content_id=self._id)

            # Check for placeholders in the text
            _match = re.findall(r"\$(\d+)", content)

            if _match:

                for marker in _match:
                    content = content.replace(f"${marker}", self.placeholders[int(marker)])

            return content

        # No se encontró contenido relacionado al ID
        except ContentNotFoundError as e:
            print(f"{type(e).__name__}: {e}")
    
        return ""
