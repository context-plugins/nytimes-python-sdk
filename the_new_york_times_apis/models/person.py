from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Person(SdkBaseModel):
    firstname: Optional[str] = UNSET
    middlename: Optional[str] = UNSET
    lastname: Optional[str] = UNSET
    qualifier: Optional[str] = UNSET
    title: Optional[str] = UNSET
    role: Optional[str] = UNSET
    organization: Optional[str] = UNSET
    rank: Optional[int] = UNSET


class PersonDict(TypedDict):
    firstname: NotRequired[str]
    middlename: NotRequired[str]
    lastname: NotRequired[str]
    qualifier: NotRequired[str]
    title: NotRequired[str]
    role: NotRequired[str]
    organization: NotRequired[str]
    rank: NotRequired[int]
