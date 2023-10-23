from typing import Optional
from pythonpackages.sdtmb.message_content import MessageContent
import renpy.character as characterType

from pythonpackages.renpy_utility.flags import get_flags


class Message:
    """Message is a class that represent a message in the phone"""

    def __init__(
        self,
        # Requirement
        character: characterType.ADVCharacter,
        message_content: MessageContent,
        day: Optional[int] = None,
        hour: Optional[int] = None,
        minute: Optional[int] = None,
        second: Optional[int] = None,
    ):
        self.character = character
        self.message_content = message_content
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second

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
    def day(self) -> int:
        if self._day is None:
            return 0
        return self._day

    @day.setter
    def day(self, value: Optional[int]):
        self._day = value

    @property
    def hour(self) -> int:
        if self._hour is None:
            return 0
        return self._hour

    @hour.setter
    def hour(self, value: Optional[int]):
        self._hour = value

    @property
    def minute(self) -> int:
        if self._minute is None:
            return 0
        return self._minute

    @minute.setter
    def minute(self, value: Optional[int]):
        self._minute = value

    @property
    def second(self) -> int:
        if self._second is None:
            return 0
        return self._second

    @second.setter
    def second(self, value: Optional[int]):
        self._second = value
