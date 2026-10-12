from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .media import Media, MediaDict


class EmailedArticle(SdkBaseModel):
    url: Optional[str] = UNSET
    """Article's URL."""

    adx_keywords: Optional[str] = UNSET
    """Semicolon separated list of keywords."""

    subsection: Optional[str] = UNSET
    """Article's subsection (e.g. Politics). Can be empty string."""

    column: OptionalNullable[str] = UNSET
    """Deprecated. Always returned as null."""

    eta_id: Optional[int] = UNSET
    """Deprecated. Set to 0."""

    section: Optional[str] = UNSET
    """Article's section (e.g. Sports)."""

    id: Optional[int] = UNSET
    """Asset ID number (e.g. 100000007772696)."""

    asset_id: Optional[int] = UNSET
    """Asset ID number (e.g. 100000007772696)."""

    nytdsection: Optional[str] = UNSET
    """Article's section (e.g. sports)."""

    byline: Optional[str] = UNSET
    """Article's byline (e.g. By Thomas L. Friedman)."""

    type_: Optional[str] = Field(default=UNSET, alias="type")
    """Asset type (e.g. Article, Interactive, ...)."""

    title: Optional[str] = UNSET
    """Article's headline (e.g. When the Cellos Play, the Cows Come Home)."""

    abstract: Optional[str] = UNSET
    """Brief summary of the article."""

    published_date: Optional[str] = UNSET
    """When the article was published on the web (e.g. 2021-04-19)."""

    source: Optional[str] = UNSET
    """Publisher (e.g. New York Times)."""

    updated: Optional[str] = UNSET
    """When the article was last updated (e.g. 2021-05-12 06:32:03)."""

    des_facet: Optional[list[str]] = UNSET
    """Array of description facets (e.g. Quarantine (Life and Culture))."""

    org_facet: Optional[list[str]] = UNSET
    """Array of organization facets (e.g. Sullivan Street Bakery)."""

    per_facet: Optional[list[str]] = UNSET
    """Array of person facets (e.g. Bittman, Mark)."""

    geo_facet: Optional[list[str]] = UNSET
    """Array of geographic facets (e.g. Canada)."""

    media: Optional[list[Media]] = UNSET
    """Array of images."""

    uri: Optional[str] = UNSET
    """An article's globally unique identifier."""


class EmailedArticleDict(TypedDict):
    url: NotRequired[str]
    adx_keywords: NotRequired[str]
    subsection: NotRequired[str]
    column: NotRequired[str | None]
    eta_id: NotRequired[int]
    section: NotRequired[str]
    id: NotRequired[int]
    asset_id: NotRequired[int]
    nytdsection: NotRequired[str]
    byline: NotRequired[str]
    type_: NotRequired[str]
    title: NotRequired[str]
    abstract: NotRequired[str]
    published_date: NotRequired[str]
    source: NotRequired[str]
    updated: NotRequired[str]
    des_facet: NotRequired[list[str]]
    org_facet: NotRequired[list[str]]
    per_facet: NotRequired[list[str]]
    geo_facet: NotRequired[list[str]]
    media: NotRequired[list[MediaDict]]
    uri: NotRequired[str]
