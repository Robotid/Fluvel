from utils import APP_ROOT

class StyledText:
    def __init__(self, id: str) -> None:

        self.content: str = self.get_content_by_id(id)

    def get_content_by_id(self):
        pass

    def write(self, content: str):
        self.content = content