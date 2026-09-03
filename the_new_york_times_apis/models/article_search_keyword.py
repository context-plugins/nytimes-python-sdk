from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ArticleSearchKeyword(SdkBaseModel):
    name: Optional[str] = UNSET
    value: Optional[str] = UNSET
    rank: Optional[int] = UNSET


class ArticleSearchKeywordDict(TypedDict):
    name: NotRequired[str]
    value: NotRequired[str]
    rank: NotRequired[int]
