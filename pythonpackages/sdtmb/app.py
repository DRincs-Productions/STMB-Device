from typing import Union


class App():
    """"""

    def __init__(
        self,
        # Requirement
        id: str,
        name: str,
        icon: str,
        label_name: str,
        disabled: Union[bool, str] = False,
        hidden: Union[bool, str] = False,
    ):
        self.id = id
        self.name = name
        self.icon = icon
        self.disabled = disabled
        self.hidden = hidden
        self.label_name = label_name
