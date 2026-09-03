from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Period(int, Enum):
    VALUE_1 = 1
    """The last day."""

    VALUE_7 = 7
    """The last seven days."""

    VALUE_30 = 30
    """The last thirty days."""

    __str__ = str.__str__


PeriodOrInt: TypeAlias = Annotated[Period | int, open_enum_validator(Period)]
