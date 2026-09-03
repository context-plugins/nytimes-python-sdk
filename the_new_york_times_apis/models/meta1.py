from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Meta1(SdkBaseModel):
    hits: Optional[int] = UNSET


class Meta1Dict(TypedDict):
    hits: NotRequired[int]
