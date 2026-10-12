from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .byline import Byline, BylineDict
from .headline import Headline, HeadlineDict
from .keyword import Keyword, KeywordDict
from .multimedia import Multimedia, MultimediaDict


class Article(SdkBaseModel):
    web_url: Optional[str] = UNSET
    """Article URL."""

    snippet: Optional[str] = UNSET
    print_page: Optional[str] = UNSET
    """Page in print (e.g. "1"). Empty string when not applicable."""

    print_section: Optional[str] = UNSET
    """Section in print (e.g. A)."""

    source: Optional[str] = UNSET
    multimedia: Optional[list[Multimedia]] = UNSET
    headline: Optional[Headline] = UNSET
    keywords: Optional[list[Keyword]] = UNSET
    pub_date: Optional[str] = UNSET
    """Publication date."""

    document_type: Optional[str] = UNSET
    """Document type (article, multimedia)."""

    news_desk: Optional[str] = UNSET
    """Desk in the newsroom that worked on the story (Foreign, Metro, Sports, ...)."""

    section_name: Optional[str] = UNSET
    """Section that the article appeared in (New York, Sports, World, ...)."""

    byline: Optional[Byline] = UNSET
    type_of_material: Optional[str] = UNSET
    """Type of asset (Correction, News, Op-Ed, Review, Video, ...)."""

    id: Optional[str] = Field(default=UNSET, alias="_id")
    word_count: Optional[int] = UNSET
    """Number of words in the article."""

    uri: Optional[str] = UNSET
    """Uniquely identifies an asset."""


class ArticleDict(TypedDict):
    web_url: NotRequired[str]
    snippet: NotRequired[str]
    print_page: NotRequired[str]
    print_section: NotRequired[str]
    source: NotRequired[str]
    multimedia: NotRequired[list[MultimediaDict]]
    headline: NotRequired[HeadlineDict]
    keywords: NotRequired[list[KeywordDict]]
    pub_date: NotRequired[str]
    document_type: NotRequired[str]
    news_desk: NotRequired[str]
    section_name: NotRequired[str]
    byline: NotRequired[BylineDict]
    type_of_material: NotRequired[str]
    id: NotRequired[str]
    word_count: NotRequired[int]
    uri: NotRequired[str]
