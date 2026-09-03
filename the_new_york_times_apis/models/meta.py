from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Meta(SdkBaseModel):
    hits: Optional[int] = UNSET
    offset: Optional[int] = UNSET
    time: Optional[int] = UNSET


class MetaDict(TypedDict):
    hits: NotRequired[int]
    offset: NotRequired[int]
    time: NotRequired[int]
