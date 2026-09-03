from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Image(SdkBaseModel):
    url: Optional[str] = UNSET
    height: Optional[int] = UNSET
    width: Optional[int] = UNSET


class ImageDict(TypedDict):
    url: NotRequired[str]
    height: NotRequired[int]
    width: NotRequired[int]
