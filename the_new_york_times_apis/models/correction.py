from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Correction(SdkBaseModel):
    text: Optional[str] = UNSET
    correction_date: Optional[str] = UNSET


class CorrectionDict(TypedDict):
    text: NotRequired[str]
    correction_date: NotRequired[str]
