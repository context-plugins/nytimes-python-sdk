from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError

GetMostSharedArticlesByTypeErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _GetMostSharedArticlesByTypeError:
    def map(self, status_code: int, content: bytes) -> GetMostSharedArticlesByTypeErrorBody:
        match status_code:
            case 401 | 429:
                return RawError(status_code, content)
            case _:
                return RawError(status_code, content)


get_most_shared_articles_by_type_error_mapper: Final[
    ErrorMapper[GetMostSharedArticlesByTypeErrorBody]
] = _GetMostSharedArticlesByTypeError()
