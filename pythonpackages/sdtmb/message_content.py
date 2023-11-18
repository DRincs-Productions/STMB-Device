from typing import Optional


class MessageContent:
    """MessageContent is a class that represent a message content"""

    def __init__(
        self,
        # Requirement
        text: Optional[str] = None,
        image: Optional[str] = None,
    ):
        self.text = text
        self.image = image

    @property
    def text(self) -> Optional[str]:
        return self._text

    @text.setter
    def text(self, value: Optional[str]):
        self._text = value

    @property
    def image(self) -> Optional[str]:
        return self._image

    @image.setter
    def image(self, value: Optional[str]):
        self._image = value
