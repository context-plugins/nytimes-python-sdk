from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ShareType(str, Enum):
    FACEBOOK = "facebook"

    __str__ = str.__str__


ShareTypeOrStr: TypeAlias = Annotated[ShareType | str, open_enum_validator(ShareType)]
