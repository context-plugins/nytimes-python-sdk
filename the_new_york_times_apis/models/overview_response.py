from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .results1 import Results1, Results1Dict


class OverviewResponse(SdkBaseModel):
    status: Optional[str] = UNSET
    copyright: Optional[str] = UNSET
    num_results: Optional[int] = UNSET
    results: Optional[Results1] = UNSET


class OverviewResponseDict(TypedDict):
    status: NotRequired[str]
    copyright: NotRequired[str]
    num_results: NotRequired[int]
    results: NotRequired[Results1Dict]
