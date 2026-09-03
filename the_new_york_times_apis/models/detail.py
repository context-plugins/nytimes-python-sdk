from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Detail(SdkBaseModel):
    errorcode: Optional[str] = UNSET


class DetailDict(TypedDict):
    errorcode: NotRequired[str]
