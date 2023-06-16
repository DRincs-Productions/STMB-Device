from typing import Union
import renpy as renpy

from pythonpackages.renpy_utility.flags import get_flags


class Contact:
    """"""

    def __init__(
        self,
        # Requirement
        id: str,
        icon: str,
        character: renpy.character.ADVCharacter,
        hidden: Union[bool, str] = False,
    ):
        self.id = id
        self.icon = icon
        self.character = character
        self.hidden = hidden

    @property
    def name(self):
        return self.character.name

    @property
    def id(self) -> str:
        return self._id

    @id.setter
    def id(self, value: str):
        self._id = value

    @property
    def icon(self) -> str:
        return self._icon

    @icon.setter
    def icon(self, value: str):
        self._icon = value

    @property
    def character(self) -> renpy.character.ADVCharacter:
        return self._character

    @character.setter
    def character(self, value: renpy.character.ADVCharacter):
        self._character = value

    @property
    def hidden(self) -> Union[bool, str]:
        return self._hidden

    @hidden.setter
    def hidden(self, value: Union[bool, str]):
        self._hidden = value

    def is_hidden(self, flags: dict[str, bool] = {}) -> bool:
        """ "If hidden is a string: get the value of the flags system"""
        if isinstance(self.hidden, str):
            return get_flags(self.hidden, flags)
        else:
            return self.hidden
