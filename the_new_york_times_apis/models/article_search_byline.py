from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ArticleSearchByline(SdkBaseModel):
    original: Optional[str] = UNSET


class ArticleSearchBylineDict(TypedDict):
    original: NotRequired[str]
