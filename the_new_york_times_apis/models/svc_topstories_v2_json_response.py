from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .article1 import Article1, Article1Dict


class SvcTopstoriesV2JsonResponse(SdkBaseModel):
    status: Optional[str] = UNSET
    copyright: Optional[str] = UNSET
    section: Optional[str] = UNSET
    last_updated: Optional[str] = UNSET
    num_results: Optional[int] = UNSET
    results: Optional[list[Article1]] = UNSET


class SvcTopstoriesV2JsonResponseDict(TypedDict):
    status: NotRequired[str]
    copyright: NotRequired[str]
    section: NotRequired[str]
    last_updated: NotRequired[str]
    num_results: NotRequired[int]
    results: NotRequired[list[Article1Dict]]
