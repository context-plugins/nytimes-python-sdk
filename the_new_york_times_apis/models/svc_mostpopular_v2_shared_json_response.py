from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .shared_article import SharedArticle, SharedArticleDict


class SvcMostpopularV2SharedJsonResponse(SdkBaseModel):
    status: Optional[str] = UNSET
    """API response status (e.g. OK)."""

    copyright: Optional[str] = UNSET
    """Copyright message."""

    num_results: Optional[int] = UNSET
    """Number of articles in the results (e.g. 20)."""

    results: Optional[list[SharedArticle]] = UNSET
    """Array of articles."""


class SvcMostpopularV2SharedJsonResponseDict(TypedDict):
    status: NotRequired[str]
    copyright: NotRequired[str]
    num_results: NotRequired[int]
    results: NotRequired[list[SharedArticle | SharedArticleDict]]
