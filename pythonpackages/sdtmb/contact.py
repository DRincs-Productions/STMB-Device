import renpy as renpy


class Contact:
    """"""

    def __init__(
        self,
        # Requirement
        id: str,
        icon: str,
        character: renpy.character.ADVCharacter,
    ):
        self.id = id
        self.icon = icon
        self.character = character
