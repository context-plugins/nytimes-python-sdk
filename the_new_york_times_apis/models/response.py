from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .article_search_article import ArticleSearchArticle, ArticleSearchArticleDict
from .meta import Meta, MetaDict


class Response(SdkBaseModel):
    docs: Optional[list[ArticleSearchArticle]] = UNSET
    meta: Optional[Meta] = UNSET


class ResponseDict(TypedDict):
    docs: NotRequired[list[ArticleSearchArticle | ArticleSearchArticleDict]]
    meta: NotRequired[Meta | MetaDict]
