from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError

GetListsDateListJsonErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _GetListsDateListJsonError:
    def map(self, status_code: int, content: bytes) -> GetListsDateListJsonErrorBody:
        match status_code:
            case 401 | 429:
                return RawError(status_code, content)
            case _:
                return RawError(status_code, content)


get_lists_date_list_json_error_mapper: Final[ErrorMapper[GetListsDateListJsonErrorBody]] = _GetListsDateListJsonError()
