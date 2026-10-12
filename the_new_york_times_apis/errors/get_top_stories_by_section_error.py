from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError

GetTopStoriesBySectionErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _GetTopStoriesBySectionError:
    def map(self, status_code: int, content: bytes) -> GetTopStoriesBySectionErrorBody:
        match status_code:
            case 401 | 429:
                return RawError(status_code, content)
            case _:
                return RawError(status_code, content)


get_top_stories_by_section_error_mapper: Final[
    ErrorMapper[GetTopStoriesBySectionErrorBody]
] = _GetTopStoriesBySectionError()
