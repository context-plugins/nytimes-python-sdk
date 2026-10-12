from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .fault import Fault, FaultDict


class SvcArchiveV1Json401Error(SdkBaseModel):
    fault: Optional[Fault] = UNSET


class SvcArchiveV1Json401ErrorDict(TypedDict):
    fault: NotRequired[FaultDict]
