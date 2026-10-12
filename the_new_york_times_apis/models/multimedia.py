from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .legacy import Legacy, LegacyDict


class Multimedia(SdkBaseModel):
    rank: Optional[int] = UNSET
    subtype: Optional[str] = UNSET
    caption: Optional[str] = UNSET
    credit: Optional[str] = UNSET
    type_: Optional[str] = Field(default=UNSET, alias="type")
    url: Optional[str] = UNSET
    height: Optional[int] = UNSET
    width: Optional[int] = UNSET
    legacy: Optional[Legacy] = UNSET
    crop_name: Optional[str] = UNSET


class MultimediaDict(TypedDict):
    rank: NotRequired[int]
    subtype: NotRequired[str]
    caption: NotRequired[str]
    credit: NotRequired[str]
    type_: NotRequired[str]
    url: NotRequired[str]
    height: NotRequired[int]
    width: NotRequired[int]
    legacy: NotRequired[LegacyDict]
    crop_name: NotRequired[str]
