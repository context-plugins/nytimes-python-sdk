from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .list import List, ListDict


class Results1(SdkBaseModel):
    published_date: Optional[str] = UNSET
    """When the lists were in print."""

    previous_published_date: Optional[str] = UNSET
    """Date of previous overview if exists."""

    next_published_date: Optional[str] = UNSET
    """Date of next overview if exists."""

    lists: Optional[list[List]] = UNSET


class Results1Dict(TypedDict):
    published_date: NotRequired[str]
    previous_published_date: NotRequired[str]
    next_published_date: NotRequired[str]
    lists: NotRequired[list[ListDict]]
