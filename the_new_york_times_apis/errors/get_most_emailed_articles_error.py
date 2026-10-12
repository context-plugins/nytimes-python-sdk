from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError

GetMostEmailedArticlesErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _GetMostEmailedArticlesError:
    def map(self, status_code: int, content: bytes) -> GetMostEmailedArticlesErrorBody:
        match status_code:
            case 401 | 429:
                return RawError(status_code, content)
            case _:
                return RawError(status_code, content)


get_most_emailed_articles_error_mapper: Final[
    ErrorMapper[GetMostEmailedArticlesErrorBody]
] = _GetMostEmailedArticlesError()
