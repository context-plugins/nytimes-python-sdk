from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Book(SdkBaseModel):
    rank: Optional[int] = UNSET
    """Rank on the list."""

    rank_last_week: Optional[int] = UNSET
    """Rank on list last week."""

    weeks_on_list: Optional[int] = UNSET
    """Number of weeks on list."""

    asterisk: Optional[int] = UNSET
    """Book's sales are barely distinguishable from those of the book above it."""

    dagger: Optional[int] = UNSET
    """Some retailers report receiving bulk orders."""

    primary_isbn13: Optional[str] = UNSET
    """The book's ID, which is usually an ISBN 13."""

    publisher: Optional[str] = UNSET
    """Publisher name."""

    description: Optional[str] = UNSET
    """A short description of the book."""

    title: Optional[str] = UNSET
    """The book title."""

    author: Optional[str] = UNSET
    """The book author."""

    contributor: Optional[str] = UNSET
    """The book author."""

    book_image: Optional[str] = UNSET
    """Book cover image."""

    amazon_product_url: Optional[str] = UNSET
    """A link to the book on Amazon."""

    age_group: Optional[str] = UNSET
    """Book age group."""

    book_review_link: Optional[str] = UNSET
    """Link to NYT book review."""

    sunday_review_link: Optional[str] = UNSET
    """Link to NYT Sunday book review."""


class BookDict(TypedDict):
    rank: NotRequired[int]
    rank_last_week: NotRequired[int]
    weeks_on_list: NotRequired[int]
    asterisk: NotRequired[int]
    dagger: NotRequired[int]
    primary_isbn13: NotRequired[str]
    publisher: NotRequired[str]
    description: NotRequired[str]
    title: NotRequired[str]
    author: NotRequired[str]
    contributor: NotRequired[str]
    book_image: NotRequired[str]
    amazon_product_url: NotRequired[str]
    age_group: NotRequired[str]
    book_review_link: NotRequired[str]
    sunday_review_link: NotRequired[str]
