from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .results import Results, ResultsDict


class ListResponse(SdkBaseModel):
    status: Optional[str] = UNSET
    copyright: Optional[str] = UNSET
    num_results: Optional[int] = UNSET
    results: Optional[Results] = UNSET


class ListResponseDict(TypedDict):
    status: NotRequired[str]
    copyright: NotRequired[str]
    num_results: NotRequired[int]
    results: NotRequired[ResultsDict]
