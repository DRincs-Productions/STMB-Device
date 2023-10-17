from typing import Optional, Union
import renpy.character as characterType

from pythonpackages.renpy_utility.flags import get_flags


class Contact:
    """"""

    def __init__(
        self,
        # Requirement
        character: characterType.ADVCharacter,
        hidden: Union[bool, str] = False,
    ):
        self.character = character
        self.hidden = hidden

    @property
    def name(self):
        return self.character.name

    @property
    def icon(self) -> Optional[str]:
        # if ch have a property icon
        if "icon" in self.character.who_args and isinstance(
            self.character.who_args["icon"], str
        ):
            return self.character.who_args["icon"]
        return None

    @property
    def character(self) -> characterType.ADVCharacter:
        return self._character

    @character.setter
    def character(self, value: characterType.ADVCharacter):
        self._character = value

    @property
    def hidden(self) -> Union[bool, str]:
        return self._hidden

    @hidden.setter
    def hidden(self, value: Union[bool, str]):
        self._hidden = value

    def is_hidden(self, flags: dict[str, bool] = {}) -> bool:
        """If hidden is a string: get the value of the flags system"""
        if isinstance(self.hidden, str):
            return get_flags(self.hidden, flags)
        else:
            return self.hidden
