from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

GetMostViewedArticlesErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _GetMostViewedArticlesError:
    def map(self, response: HttpResponse) -> GetMostViewedArticlesErrorBody:
        match response.status_code:
            case 401 | 429:
                return RawError(response)
            case _:
                return RawError(response)


get_most_viewed_articles_error_mapper: Final[
    ErrorMapper[GetMostViewedArticlesErrorBody]
] = _GetMostViewedArticlesError()
