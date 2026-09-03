from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .detail import Detail, DetailDict


class Fault(SdkBaseModel):
    faultstring: Optional[str] = UNSET
    detail: Optional[Detail] = UNSET


class FaultDict(TypedDict):
    faultstring: NotRequired[str]
    detail: NotRequired[Detail | DetailDict]
