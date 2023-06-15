import renpy.exports as renpy


class Contact:
    """"""

    def __init__(
        self,
        # Requirement
        id: str,
        icon: str,
        character: renpy.Character,
    ):
        self.id = id
        self.icon = icon
        self.character = character
