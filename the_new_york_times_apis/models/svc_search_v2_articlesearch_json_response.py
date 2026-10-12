from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .response import Response, ResponseDict


class SvcSearchV2ArticlesearchJsonResponse(SdkBaseModel):
    status: Optional[str] = UNSET
    copyright: Optional[str] = UNSET
    response: Optional[Response] = UNSET


class SvcSearchV2ArticlesearchJsonResponseDict(TypedDict):
    status: NotRequired[str]
    copyright: NotRequired[str]
    response: NotRequired[ResponseDict]
