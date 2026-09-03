<!-- Generated file — do not edit; regenerated with the SDK. -->

# Archive — operations

Accessor: `client.archive` · Source: `the_new_york_times_apis/apis/archive.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.archive.get_archive_by_month

- **Route**: `GET /svc/archive/v1/{year}/{month}.json`
- **Auth**: `apikey`
- **Signature**: `def get_archive_by_month(*, year: int = 2018, month: int = 9, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `year` — path · `month` — path
- **Returns (parsed)**: `SvcArchiveV1JsonResponse`
- **Returns (raw)**: `ApiResult[SvcArchiveV1JsonResponse, GetArchiveByMonthErrorBody]`
- **Error**: `GetArchiveByMonthErrorBody` — **Case A (typed)**
- **Error arms**: `SvcArchiveV1Json401Error1` [401] · `RawError` [429, anything unmapped]

| Type | Source |
| --- | --- |
| `SvcArchiveV1JsonResponse` | `the_new_york_times_apis/models/svc_archive_v1_json_response.py` |
| `GetArchiveByMonthErrorBody` | `the_new_york_times_apis/errors/get_archive_by_month_error.py` |
| `SvcArchiveV1Json401Error1` | `the_new_york_times_apis/models/svc_archive_v1_json401_error1.py` |

