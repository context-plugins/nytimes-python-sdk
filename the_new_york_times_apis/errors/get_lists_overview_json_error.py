from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

GetListsOverviewJsonErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _GetListsOverviewJsonError:
    def map(self, response: HttpResponse) -> GetListsOverviewJsonErrorBody:
        match response.status_code:
            case 401 | 429:
                return RawError(response)
            case _:
                return RawError(response)


get_lists_overview_json_error_mapper: Final[ErrorMapper[GetListsOverviewJsonErrorBody]] = _GetListsOverviewJsonError()
