from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError

GetMostViewedArticlesErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _GetMostViewedArticlesError:
    def map(self, status_code: int, content: bytes) -> GetMostViewedArticlesErrorBody:
        match status_code:
            case 401 | 429:
                return RawError(status_code, content)
            case _:
                return RawError(status_code, content)


get_most_viewed_articles_error_mapper: Final[
    ErrorMapper[GetMostViewedArticlesErrorBody]
] = _GetMostViewedArticlesError()
