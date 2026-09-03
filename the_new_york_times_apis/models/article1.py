from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .multimedia1 import Multimedia1, Multimedia1Dict


class Article1(SdkBaseModel):
    section: Optional[str] = UNSET
    subsection: Optional[str] = UNSET
    title: Optional[str] = UNSET
    abstract: Optional[str] = UNSET
    url: Optional[str] = UNSET
    uri: Optional[str] = UNSET
    byline: Optional[str] = UNSET
    item_type: Optional[str] = UNSET
    updated_date: Optional[str] = UNSET
    created_date: Optional[str] = UNSET
    published_date: Optional[str] = UNSET
    material_type_facet: Optional[str] = UNSET
    kicker: Optional[str] = UNSET
    des_facet: Optional[list[str]] = UNSET
    org_facet: Optional[list[str]] = UNSET
    per_facet: Optional[list[str]] = UNSET
    geo_facet: Optional[list[str]] = UNSET
    multimedia: Optional[list[Multimedia1]] = UNSET
    short_url: Optional[str] = UNSET


class Article1Dict(TypedDict):
    section: NotRequired[str]
    subsection: NotRequired[str]
    title: NotRequired[str]
    abstract: NotRequired[str]
    url: NotRequired[str]
    uri: NotRequired[str]
    byline: NotRequired[str]
    item_type: NotRequired[str]
    updated_date: NotRequired[str]
    created_date: NotRequired[str]
    published_date: NotRequired[str]
    material_type_facet: NotRequired[str]
    kicker: NotRequired[str]
    des_facet: NotRequired[list[str]]
    org_facet: NotRequired[list[str]]
    per_facet: NotRequired[list[str]]
    geo_facet: NotRequired[list[str]]
    multimedia: NotRequired[list[Multimedia1 | Multimedia1Dict]]
    short_url: NotRequired[str]
