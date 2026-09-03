from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

SearchArticlesErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _SearchArticlesError:
    def map(self, response: HttpResponse) -> SearchArticlesErrorBody:
        match response.status_code:
            case 400 | 401 | 429:
                return RawError(response)
            case _:
                return RawError(response)


search_articles_error_mapper: Final[ErrorMapper[SearchArticlesErrorBody]] = _SearchArticlesError()
