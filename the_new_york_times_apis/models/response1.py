from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .article import Article, ArticleDict
from .meta1 import Meta1, Meta1Dict


class Response1(SdkBaseModel):
    meta: Optional[Meta1] = UNSET
    docs: Optional[list[Article]] = UNSET


class Response1Dict(TypedDict):
    meta: NotRequired[Meta1Dict]
    docs: NotRequired[list[ArticleDict]]
