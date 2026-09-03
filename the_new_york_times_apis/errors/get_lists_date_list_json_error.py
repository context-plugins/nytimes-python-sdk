from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError

GetListsDateListJsonErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _GetListsDateListJsonError:
    def map(self, response: HttpResponse) -> GetListsDateListJsonErrorBody:
        match response.status_code:
            case 401 | 429:
                return RawError(response)
            case _:
                return RawError(response)


get_lists_date_list_json_error_mapper: Final[ErrorMapper[GetListsDateListJsonErrorBody]] = _GetListsDateListJsonError()
