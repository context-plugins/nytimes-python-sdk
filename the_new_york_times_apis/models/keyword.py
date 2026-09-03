from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Keyword(SdkBaseModel):
    name: Optional[str] = UNSET
    value: Optional[str] = UNSET
    rank: Optional[int] = UNSET
    major: Optional[str] = UNSET


class KeywordDict(TypedDict):
    name: NotRequired[str]
    value: NotRequired[str]
    rank: NotRequired[int]
    major: NotRequired[str]
