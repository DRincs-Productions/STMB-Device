from typing import Optional
from pythonpackages.sdtmb.message import Message
import renpy.character as characterType


class Messages:
    """Messages is a class that represent a message in the phone"""

    def __init__(
        self,
        chatId: characterType.ADVCharacter,
        messages: list[Message],
    ):
        self.chatId = chatId
        # filter messages by character
        self.messages = list(filter(lambda message: message.chatId == chatId, messages))

    @property
    def chatId(self) -> characterType.ADVCharacter:
        return self._chatId

    @chatId.setter
    def chatId(self, value: characterType.ADVCharacter):
        self._chatId = value

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
    def have_unread_message(self) -> bool:
        for message in self.messages:
            if message.is_unread:
                return True
        return False

    @property
    def have_message(self) -> bool:
        return len(self.messages) > 0

    def add_message(self, message: Message):
        message.is_unread = True
        self.messages.append(message)

    def add_message_read(self, message: Message):
        message.is_unread = False
        self.messages.append(message)
