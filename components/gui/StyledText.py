from controllers import get_content_by_id
import re

class StyledText:
    def __init__(self, content_id: str, placeholders: list = None) -> None:
        self._id = content_id
        self.placeholders = placeholders
    
    @property
    def text(self) -> str:

        try:
            
            # Load the RichText content from GlobalContent
            content = get_content_by_id(content_id=self._id)

            # Checks for markers for dynamic text in the string.
            _match = re.findall(r"\$(\d+)", content)

            if _match:

                for marker in _match:
                    content = content.replace(f"${marker}", self.placeholders[int(marker)])

            return content
    
        except Exception as e:
            print(e)
    
        return ""
