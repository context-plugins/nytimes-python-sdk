from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Headline(SdkBaseModel):
    main: Optional[str] = UNSET
    kicker: Optional[str] = UNSET
    content_kicker: Optional[str] = UNSET
    print_headline: Optional[str] = UNSET
    name: Optional[str] = UNSET
    seo: Optional[str] = UNSET
    sub: Optional[str] = UNSET


class HeadlineDict(TypedDict):
    main: NotRequired[str]
    kicker: NotRequired[str]
    content_kicker: NotRequired[str]
    print_headline: NotRequired[str]
    name: NotRequired[str]
    seo: NotRequired[str]
    sub: NotRequired[str]
