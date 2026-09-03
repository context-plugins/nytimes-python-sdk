from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class MediaMetadata(SdkBaseModel):
    url: Optional[str] = UNSET
    """Image's URL."""

    format: Optional[str] = UNSET
    """Image's crop name."""

    height: Optional[int] = UNSET
    """Image's height (e.g. 293)."""

    width: Optional[int] = UNSET
    """Image's width (e.g. 440)."""


class MediaMetadataDict(TypedDict):
    url: NotRequired[str]
    format: NotRequired[str]
    height: NotRequired[int]
    width: NotRequired[int]
