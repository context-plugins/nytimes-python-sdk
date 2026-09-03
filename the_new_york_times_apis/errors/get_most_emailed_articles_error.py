from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

GetMostEmailedArticlesErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _GetMostEmailedArticlesError:
    def map(self, response: HttpResponse) -> GetMostEmailedArticlesErrorBody:
        match response.status_code:
            case 401 | 429:
                return RawError(response)
            case _:
                return RawError(response)


get_most_emailed_articles_error_mapper: Final[
    ErrorMapper[GetMostEmailedArticlesErrorBody]
] = _GetMostEmailedArticlesError()
