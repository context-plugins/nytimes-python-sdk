from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Multimedia1(SdkBaseModel):
    url: Optional[str] = UNSET
    format: Optional[str] = UNSET
    height: Optional[int] = UNSET
    width: Optional[int] = UNSET
    type_: Optional[str] = Field(default=UNSET, alias="type")
    subtype: Optional[str] = UNSET
    caption: Optional[str] = UNSET
    copyright: Optional[str] = UNSET


class Multimedia1Dict(TypedDict):
    url: NotRequired[str]
    format: NotRequired[str]
    height: NotRequired[int]
    width: NotRequired[int]
    type_: NotRequired[str]
    subtype: NotRequired[str]
    caption: NotRequired[str]
    copyright: NotRequired[str]
