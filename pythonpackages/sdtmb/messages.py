from typing import Optional
from pythonpackages.sdtmb.message import Message
import renpy.character as characterType


class Messages:
    """Messages is a class that represent a message in the phone"""

    def __init__(
        self,
        character: characterType.ADVCharacter,
        messages: list[Message],
    ):
        self.character = character
        self.messages = messages

    @property
    def character(self) -> characterType.ADVCharacter:
        return self._character

    @character.setter
    def character(self, value: characterType.ADVCharacter):
        self._character = value

    @property
    def messages(self) -> list[Message]:
        # TODO: order messages by date
        return self._messages

    @messages.setter
    def messages(self, value: list[Message]):
        self._messages = value

    @property
    def last_message(self) -> Optional[Message]:
        if len(self.messages) == 0:
            return None
        return self.messages[-1]

    @property
    def is_unread_message(self) -> bool:
        for message in self.messages:
            if message.is_unread:
                return True
        return False

    @property
    def have_message(self) -> bool:
        return len(self.messages) > 0

    def add_message(self, message: Message):
        self.messages.append(message)
