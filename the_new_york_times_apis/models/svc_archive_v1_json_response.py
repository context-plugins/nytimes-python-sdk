from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .response1 import Response1, Response1Dict


class SvcArchiveV1JsonResponse(SdkBaseModel):
    copyright: Optional[str] = UNSET
    response: Optional[Response1] = UNSET


class SvcArchiveV1JsonResponseDict(TypedDict):
    copyright: NotRequired[str]
    response: NotRequired[Response1 | Response1Dict]
