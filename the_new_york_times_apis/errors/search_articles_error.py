from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError

SearchArticlesErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _SearchArticlesError:
    def map(self, status_code: int, content: bytes) -> SearchArticlesErrorBody:
        match status_code:
            case 400 | 401 | 429:
                return RawError(status_code, content)
            case _:
                return RawError(status_code, content)


search_articles_error_mapper: Final[ErrorMapper[SearchArticlesErrorBody]] = _SearchArticlesError()
