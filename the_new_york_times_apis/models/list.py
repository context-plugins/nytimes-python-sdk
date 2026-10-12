from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .book import Book, BookDict


class List(SdkBaseModel):
    display_name: Optional[str] = UNSET
    """Display name for the list."""

    list_name_encoded: Optional[str] = UNSET
    """List name encoded for the URL path."""

    updated: Optional[str] = UNSET
    """How often the list is updated (WEEKLY or MONTHLY)."""

    books: Optional[list[Book]] = UNSET


class ListDict(TypedDict):
    display_name: NotRequired[str]
    list_name_encoded: NotRequired[str]
    updated: NotRequired[str]
    books: NotRequired[list[BookDict]]
