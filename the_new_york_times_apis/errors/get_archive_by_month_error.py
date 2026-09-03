from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.svc_archive_v1_json401_error1 import SvcArchiveV1Json401Error1

GetArchiveByMonthErrorBody: TypeAlias = SvcArchiveV1Json401Error1 | RawError


@dataclass(frozen=True, slots=True)
class _GetArchiveByMonthError:
    def map(self, response: HttpResponse) -> GetArchiveByMonthErrorBody:
        match response.status_code:
            case 401:
                return decode_json[SvcArchiveV1Json401Error1](response)
            case 429:
                return RawError(response)
            case _:
                return RawError(response)


get_archive_by_month_error_mapper: Final[ErrorMapper[GetArchiveByMonthErrorBody]] = _GetArchiveByMonthError()
