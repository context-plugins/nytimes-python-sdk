from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Legacy(SdkBaseModel):
    xlarge: Optional[str] = UNSET
    xlargewidth: Optional[int] = UNSET
    xlargeheight: Optional[int] = UNSET


class LegacyDict(TypedDict):
    xlarge: NotRequired[str]
    xlargewidth: NotRequired[int]
    xlargeheight: NotRequired[int]
