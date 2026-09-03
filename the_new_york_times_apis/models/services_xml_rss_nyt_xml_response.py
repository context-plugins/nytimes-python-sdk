from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .channel import Channel, ChannelDict


class ServicesXmlRssNytXmlResponse(SdkBaseModel):
    channel: Optional[Channel] = UNSET


class ServicesXmlRssNytXmlResponseDict(TypedDict):
    channel: NotRequired[Channel | ChannelDict]
