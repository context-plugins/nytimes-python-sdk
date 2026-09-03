from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Image1(SdkBaseModel):
    link: Optional[str] = UNSET
    title: Optional[str] = UNSET
    url: Optional[str] = UNSET


class Image1Dict(TypedDict):
    link: NotRequired[str]
    title: NotRequired[str]
    url: NotRequired[str]
