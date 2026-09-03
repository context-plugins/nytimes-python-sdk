from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .book import Book, BookDict
from .correction import Correction, CorrectionDict


class Results(SdkBaseModel):
    display_name: Optional[str] = UNSET
    """Display name for the list."""

    list_name_encoded: Optional[str] = UNSET
    """List name encoded for the URL path."""

    published_date: Optional[str] = UNSET
    """When the list was in print."""

    updated: Optional[str] = UNSET
    """How often the list is updated (WEEKLY or MONTHLY)."""

    previous_published_date: Optional[str] = UNSET
    """Date of previous list if exists."""

    next_published_date: Optional[str] = UNSET
    """Date of next list if exists."""

    books: Optional[list[Book]] = UNSET
    corrections: Optional[list[Correction]] = UNSET


class ResultsDict(TypedDict):
    display_name: NotRequired[str]
    list_name_encoded: NotRequired[str]
    published_date: NotRequired[str]
    updated: NotRequired[str]
    previous_published_date: NotRequired[str]
    next_published_date: NotRequired[str]
    books: NotRequired[list[Book | BookDict]]
    corrections: NotRequired[list[Correction | CorrectionDict]]
