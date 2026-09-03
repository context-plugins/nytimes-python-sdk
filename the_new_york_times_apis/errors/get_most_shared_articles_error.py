from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

GetMostSharedArticlesErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _GetMostSharedArticlesError:
    def map(self, response: HttpResponse) -> GetMostSharedArticlesErrorBody:
        match response.status_code:
            case 401 | 429:
                return RawError(response)
            case _:
                return RawError(response)


get_most_shared_articles_error_mapper: Final[
    ErrorMapper[GetMostSharedArticlesErrorBody]
] = _GetMostSharedArticlesError()
