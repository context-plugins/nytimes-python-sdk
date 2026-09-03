from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

GetMostSharedArticlesByTypeErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _GetMostSharedArticlesByTypeError:
    def map(self, response: HttpResponse) -> GetMostSharedArticlesByTypeErrorBody:
        match response.status_code:
            case 401 | 429:
                return RawError(response)
            case _:
                return RawError(response)


get_most_shared_articles_by_type_error_mapper: Final[
    ErrorMapper[GetMostSharedArticlesByTypeErrorBody]
] = _GetMostSharedArticlesByTypeError()
