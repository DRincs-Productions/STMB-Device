from typing import Optional
from pythonpackages.sdtmb.message_content import MessageContent
import renpy.character as characterType
from typing import Optional, Union


class Message:
    """Message is a class that represent a message in the phone"""

    def __init__(
        self,
        # Requirement
        character: characterType.ADVCharacter,
        chatId: Union[str, characterType.ADVCharacter],
        message_content: MessageContent,
        time_description: str,
        is_unread: bool = False,
    ):
        self.character = character
        self.chatId = chatId
        self.message_content = message_content
        self.time_description = time_description
        self.is_unread = is_unread

    @property
    def character(self) -> characterType.ADVCharacter:
        return self._character

    @character.setter
    def character(self, value: characterType.ADVCharacter):
        self._character = value

    @property
    def message_content(self) -> MessageContent:
        return self._message_content

    @message_content.setter
    def message_content(self, value: MessageContent):
        self._message_content = value

    @property
    def chatId(self) -> Union[str, characterType.ADVCharacter]:
        return self._chatId

    @chatId.setter
    def chatId(self, value: Union[str, characterType.ADVCharacter]):
        self._chatId = value

    @property
    def time_description(self) -> str:
        return self._time_description

    @time_description.setter
    def time_description(self, value: str):
        self._time_description = value

    @property
    def is_unread(self) -> bool:
        return self._is_unread

    @is_unread.setter
    def is_unread(self, value: bool):
        self._is_unread = value

    @property
    def text(self) -> Optional[str]:
        return self.message_content.text

    @property
    def image(self) -> Optional[str]:
        return self.message_content.image

    @property
    def icon(self) -> Optional[str]:
        # if ch have a property icon
        if "icon" in self.character.who_args and isinstance(
            self.character.who_args["icon"], str
        ):
            return self.character.who_args["icon"]
        return None
