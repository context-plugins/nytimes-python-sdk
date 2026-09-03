from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .person import Person, PersonDict


class Byline(SdkBaseModel):
    original: Optional[str] = UNSET
    person: Optional[list[Person]] = UNSET
    organization: Optional[str] = UNSET


class BylineDict(TypedDict):
    original: NotRequired[str]
    person: NotRequired[list[Person | PersonDict]]
    organization: NotRequired[str]
