from typing import Optional, Union

from pythonpackages.renpy_utility.flags import get_flags


class TvChannel:
    """TvChannel is a class that represent a tv channel in the tv"""

    def __init__(
        self,
        # Requirement
        id: str,
        image: str,
        label_name: Optional[str] = None,
    ):
        self.id = id
        self.label_name = label_name
        self.image = image

    @property
    def id(self) -> str:
        return self._id

    @id.setter
    def id(self, value: str):
        self._id = value

    @property
    def label_name(self) -> Optional[str]:
        return self._label_name

    @label_name.setter
    def label_name(self, value: Optional[str]):
        self._label_name = value

    @property
    def image(self) -> str:
        return self._image

    @image.setter
    def image(self, value: str):
        self._image = value
