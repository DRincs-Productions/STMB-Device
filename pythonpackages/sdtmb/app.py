from typing import Optional, Union

from pythonpackages.renpy_utility.flags import get_flags


class App:
    """App is a class that represent a app in the phone"""

    def __init__(
        self,
        # Requirement
        id: str,
        name: str,
        icon: str,
        label_name: Optional[str] = None,
        disabled: Union[bool, str] = False,
        hidden: Union[bool, str] = False,
    ):
        self.id = id
        self.name = name
        self.icon = icon
        self.disabled = disabled
        self.hidden = hidden
        self.label_name = label_name

    @property
    def id(self) -> str:
        return self._id

    @id.setter
    def id(self, value: str):
        self._id = value

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def icon(self) -> str:
        return self._icon

    @icon.setter
    def icon(self, value: str):
        self._icon = value

    @property
    def disabled(self) -> Union[bool, str]:
        return self._disabled

    @disabled.setter
    def disabled(self, value: Union[bool, str]):
        self._disabled = value

    @property
    def hidden(self) -> Union[bool, str]:
        return self._hidden

    @hidden.setter
    def hidden(self, value: Union[bool, str]):
        self._hidden = value

    @property
    def label_name(self) -> Optional[str]:
        return self._label_name

    @label_name.setter
    def label_name(self, value: Optional[str]):
        self._label_name = value

    def is_disabled(self, flags: dict[str, bool] = {}) -> bool:
        """ "If disabled is a string: get the value of the flags system"""
        if isinstance(self.disabled, str):
            return get_flags(self.disabled, flags)
        else:
            return self.disabled

    def is_hidden(self, flags: dict[str, bool] = {}) -> bool:
        """ "If hidden is a string: get the value of the flags system"""
        if isinstance(self.hidden, str):
            return get_flags(self.hidden, flags)
        else:
            return self.hidden
