from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Item(SdkBaseModel):
    category: Optional[str] = UNSET
    description: Optional[str] = UNSET
    dc_creator: Optional[str] = Field(default=UNSET, alias="dcCreator")
    guid: Optional[str] = UNSET
    link: Optional[str] = UNSET
    media_content: Optional[str] = Field(default=UNSET, alias="mediaContent")
    media_credit: Optional[str] = Field(default=UNSET, alias="mediaCredit")
    pub_date: Optional[str] = Field(default=UNSET, alias="pubDate")
    title: Optional[str] = UNSET


class ItemDict(TypedDict):
    category: NotRequired[str]
    description: NotRequired[str]
    dc_creator: NotRequired[str]
    guid: NotRequired[str]
    link: NotRequired[str]
    media_content: NotRequired[str]
    media_credit: NotRequired[str]
    pub_date: NotRequired[str]
    title: NotRequired[str]
