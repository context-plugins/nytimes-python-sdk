from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Sort(str, Enum):
    BEST = "best"
    NEWEST = "newest"
    OLDEST = "oldest"
    RELEVANCE = "relevance"

    __str__ = str.__str__


SortOrStr: TypeAlias = Annotated[Sort | str, open_enum_validator(Sort)]
