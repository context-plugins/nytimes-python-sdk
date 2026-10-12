from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.svc_archive_v1_json401_error1 import SvcArchiveV1Json401Error1

GetArchiveByMonthErrorBody: TypeAlias = SvcArchiveV1Json401Error1 | RawError


@dataclass(frozen=True, slots=True)
class _GetArchiveByMonthError:
    def map(self, status_code: int, content: bytes) -> GetArchiveByMonthErrorBody:
        match status_code:
            case 401:
                return decode_json[SvcArchiveV1Json401Error1](content)
            case 429:
                return RawError(status_code, content)
            case _:
                return RawError(status_code, content)


get_archive_by_month_error_mapper: Final[ErrorMapper[GetArchiveByMonthErrorBody]] = _GetArchiveByMonthError()
