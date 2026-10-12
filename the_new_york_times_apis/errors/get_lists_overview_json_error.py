from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError

GetListsOverviewJsonErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _GetListsOverviewJsonError:
    def map(self, status_code: int, content: bytes) -> GetListsOverviewJsonErrorBody:
        match status_code:
            case 401 | 429:
                return RawError(status_code, content)
            case _:
                return RawError(status_code, content)


get_lists_overview_json_error_mapper: Final[ErrorMapper[GetListsOverviewJsonErrorBody]] = _GetListsOverviewJsonError()
