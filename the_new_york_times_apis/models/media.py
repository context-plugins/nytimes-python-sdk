from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .media_metadata import MediaMetadata, MediaMetadataDict


class Media(SdkBaseModel):
    type_: Optional[str] = Field(default=UNSET, alias="type")
    """Asset type (e.g. image)."""

    subtype: Optional[str] = UNSET
    """Asset subtype (e.g. photo)."""

    caption: Optional[str] = UNSET
    """Media caption."""

    copyright: Optional[str] = UNSET
    """Media credit."""

    approved_for_syndication: Optional[int] = UNSET
    """Whether media is approved for syndication. Returned as an integer flag (1 = approved, 0 = not approved), not a
    JSON boolean."""

    media_metadata: Optional[list[MediaMetadata]] = Field(default=UNSET, alias="media-metadata")
    """Media metadata (url, width, height, ...)."""


class MediaDict(TypedDict):
    type_: NotRequired[str]
    subtype: NotRequired[str]
    caption: NotRequired[str]
    copyright: NotRequired[str]
    approved_for_syndication: NotRequired[int]
    media_metadata: NotRequired[list[MediaMetadata | MediaMetadataDict]]
