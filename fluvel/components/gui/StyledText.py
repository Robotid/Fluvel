import re

# Fluvel
from fluvel.controllers.content_controller import get_content_by_id
from fluvel.components.gui.StringVar import StringVar

# Expect Handler
from fluvel.core.exceptions.expect_handler import expect


class StyledText:
    def __init__(self, content_id: str, *placeholders) -> None:
        """
        Handler for obtaining and formatting static content from .fluml files.

        Args:
            content_id (str): The identifier of the text string in the .fluml files.
            *placeholders (str | StringVar): Variables of type `str` or `StringVars` to replace the placeholders.
        """
        self._id: str = content_id
        self.placeholders: tuple = placeholders

    @property
    @expect.ContentNotFound(stop=False, default_value=StringVar())
    def var(self) -> StringVar:
        """
        Returns:
            (StringVar): The `StringVar` variable related to the ID in `GlobalContent.content_map`.\n
            *The `@Property` Method `StringVar.value` of this instance returns the RichText obtained from the `.fluml` files*
        """
        # Load the RichText content from GlobalContent
        content: StringVar = get_content_by_id(content_id=self._id)

        # Only attempt to match with markers
        # if the tuple has more than 1 element
        if len(self.placeholders) > 0:

            # Save a reference to the text with
            # the original placeholders ($0, $1, etc.)
            if not content._base_text:

                content._base_text = content.value

            # Check for placeholders in the text
            _match = re.findall(r"\$(\d+)", content.base_text)

            if _match:

                # We connect the valueChanged signal to each StringVar in self.placeholder
                # to the replace_markers method of its StringVar container.
                for i, marker in enumerate(self.placeholders):

                    if not isinstance(marker, str):

                        # Connects the signal to the “parent” StringVar
                        marker.valueChanged.connect(lambda: content.replace_markers())

                    # Each StringVar is mapped in relation
                    # to its position
                    content._MAPPING_MARKERS[i] = marker

                # Call the method to set the text
                content.replace_markers()

        return content