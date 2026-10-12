from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .image import Image, ImageDict


class ArticleSearchMultimedia(SdkBaseModel):
    caption: Optional[str] = UNSET
    credit: Optional[str] = UNSET
    default: Optional[Image] = UNSET
    thumbnail: Optional[Image] = UNSET


class ArticleSearchMultimediaDict(TypedDict):
    caption: NotRequired[str]
    credit: NotRequired[str]
    default: NotRequired[ImageDict]
    thumbnail: NotRequired[ImageDict]
