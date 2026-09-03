from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ArticleSearchHeadline(SdkBaseModel):
    main: Optional[str] = UNSET
    kicker: Optional[str] = UNSET
    print_headline: Optional[str] = UNSET


class ArticleSearchHeadlineDict(TypedDict):
    main: NotRequired[str]
    kicker: NotRequired[str]
    print_headline: NotRequired[str]
