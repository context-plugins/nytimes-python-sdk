<!-- Generated file — do not edit; regenerated with the SDK. -->

# Books — operations

Accessor: `client.books` · Source: `the_new_york_times_apis/apis/books.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.books.get_lists_date_list_json

- **Route**: `GET /svc/books/v3/lists/{date}/{list}.json`
- **Auth**: `apikey`
- **Signature**: `def get_lists_date_list_json(date: str, list_: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `date`, `list_`
- **Params**: `date` — path · `list_` — path `list`
- **Returns (parsed)**: `ListResponse`
- **Returns (raw)**: `ApiResult[ListResponse, GetListsDateListJsonErrorBody]`
- **Error**: `GetListsDateListJsonErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [401, 429, anything unmapped]

| Type | Source |
| --- | --- |
| `ListResponse` | `the_new_york_times_apis/models/list_response.py` |
| `GetListsDateListJsonErrorBody` | `the_new_york_times_apis/errors/get_lists_date_list_json_error.py` |

### client.books.get_lists_overview_json

- **Route**: `GET /svc/books/v3/lists/overview.json`
- **Auth**: `apikey`
- **Signature**: `def get_lists_overview_json(*, published_date: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `published_date` — query
- **Returns (parsed)**: `OverviewResponse`
- **Returns (raw)**: `ApiResult[OverviewResponse, GetListsOverviewJsonErrorBody]`
- **Error**: `GetListsOverviewJsonErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [401, 429, anything unmapped]

| Type | Source |
| --- | --- |
| `OverviewResponse` | `the_new_york_times_apis/models/overview_response.py` |
| `GetListsOverviewJsonErrorBody` | `the_new_york_times_apis/errors/get_lists_overview_json_error.py` |

