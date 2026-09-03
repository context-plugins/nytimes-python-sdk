from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .article_search_byline import ArticleSearchByline, ArticleSearchBylineDict
from .article_search_headline import ArticleSearchHeadline, ArticleSearchHeadlineDict
from .article_search_keyword import ArticleSearchKeyword, ArticleSearchKeywordDict
from .article_search_multimedia import ArticleSearchMultimedia, ArticleSearchMultimediaDict


class ArticleSearchArticle(SdkBaseModel):
    web_url: Optional[str] = UNSET
    """Article URL."""

    snippet: Optional[str] = UNSET
    print_page: Optional[str] = UNSET
    """Page in print (e.g. "1"). Empty string when not applicable."""

    print_section: Optional[str] = UNSET
    """Section in print (e.g. A)."""

    source: Optional[str] = UNSET
    multimedia: Optional[ArticleSearchMultimedia] = UNSET
    headline: Optional[ArticleSearchHeadline] = UNSET
    keywords: Optional[list[ArticleSearchKeyword]] = UNSET
    pub_date: Optional[str] = UNSET
    """Publication date."""

    document_type: Optional[str] = UNSET
    """Document type (article, multimedia)."""

    desk: Optional[str] = UNSET
    """Desk in the newsroom that worked on the story (Business, Foreign, Metro, ...)."""

    section_name: Optional[str] = UNSET
    """Section that the article appeared in (Arts, New York, World, ...)."""

    byline: Optional[ArticleSearchByline] = UNSET
    type_of_material: Optional[str] = UNSET
    """Type of asset (Correction, News, Op-Ed, Review, Video, ...)."""

    word_count: Optional[int] = UNSET
    """Number of words in the article."""

    uri: Optional[str] = UNSET
    """Uniquely identifies an asset."""


class ArticleSearchArticleDict(TypedDict):
    web_url: NotRequired[str]
    snippet: NotRequired[str]
    print_page: NotRequired[str]
    print_section: NotRequired[str]
    source: NotRequired[str]
    multimedia: NotRequired[ArticleSearchMultimedia | ArticleSearchMultimediaDict]
    headline: NotRequired[ArticleSearchHeadline | ArticleSearchHeadlineDict]
    keywords: NotRequired[list[ArticleSearchKeyword | ArticleSearchKeywordDict]]
    pub_date: NotRequired[str]
    document_type: NotRequired[str]
    desk: NotRequired[str]
    section_name: NotRequired[str]
    byline: NotRequired[ArticleSearchByline | ArticleSearchBylineDict]
    type_of_material: NotRequired[str]
    word_count: NotRequired[int]
    uri: NotRequired[str]
