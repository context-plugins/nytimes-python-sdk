from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .image1 import Image1, Image1Dict
from .item import Item, ItemDict


class Channel(SdkBaseModel):
    copyright: Optional[str] = UNSET
    description: Optional[str] = UNSET
    image: Optional[Image1] = UNSET
    item: Optional[list[Item]] = UNSET
    language: Optional[str] = UNSET
    last_build_date: Optional[str] = Field(default=UNSET, alias="lastBuildDate")
    link: Optional[str] = UNSET
    title: Optional[str] = UNSET


class ChannelDict(TypedDict):
    copyright: NotRequired[str]
    description: NotRequired[str]
    image: NotRequired[Image1Dict]
    item: NotRequired[list[ItemDict]]
    language: NotRequired[str]
    last_build_date: NotRequired[str]
    link: NotRequired[str]
    title: NotRequired[str]
