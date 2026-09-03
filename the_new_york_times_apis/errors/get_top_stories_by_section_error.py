from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

GetTopStoriesBySectionErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _GetTopStoriesBySectionError:
    def map(self, response: HttpResponse) -> GetTopStoriesBySectionErrorBody:
        match response.status_code:
            case 401 | 429:
                return RawError(response)
            case _:
                return RawError(response)


get_top_stories_by_section_error_mapper: Final[
    ErrorMapper[GetTopStoriesBySectionErrorBody]
] = _GetTopStoriesBySectionError()
