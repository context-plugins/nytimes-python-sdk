from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .media import Media, MediaDict


class ViewedArticle(SdkBaseModel):
    url: Optional[str] = UNSET
    """Article's URL."""

    adx_keywords: Optional[str] = UNSET
    """Semicolon separated list of keywords."""

    column: OptionalNullable[str] = UNSET
    """Deprecated. Always returned as null."""

    section: Optional[str] = UNSET
    """Article's section (e.g. Sports)."""

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

    id: Optional[int] = UNSET
    """Asset ID number (e.g. 100000007772696)."""

    asset_id: Optional[int] = UNSET
    """Asset ID number (e.g. 100000007772696)."""

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


class ViewedArticleDict(TypedDict):
    url: NotRequired[str]
    adx_keywords: NotRequired[str]
    column: NotRequired[str | None]
    section: NotRequired[str]
    byline: NotRequired[str]
    type_: NotRequired[str]
    title: NotRequired[str]
    abstract: NotRequired[str]
    published_date: NotRequired[str]
    source: NotRequired[str]
    id: NotRequired[int]
    asset_id: NotRequired[int]
    des_facet: NotRequired[list[str]]
    org_facet: NotRequired[list[str]]
    per_facet: NotRequired[list[str]]
    geo_facet: NotRequired[list[str]]
    media: NotRequired[list[MediaDict]]
    uri: NotRequired[str]
