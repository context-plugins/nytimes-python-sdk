<!-- Generated file — do not edit; regenerated with the SDK. -->

# Search — operations

Accessor: `client.search` · Source: `the_new_york_times_apis/apis/search.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.search.search_articles

- **Route**: `GET /svc/search/v2/articlesearch.json`
- **Auth**: `apikey`
- **Signature**: `def search_articles(*, begin_date: str | None = None, end_date: str | None = None, fq: str | None = None, page: int | None = None, q: str | None = None, sort: SortOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `begin_date` — query · `end_date` — query · `fq` — query · `page` — query · `q` — query · `sort` — query
- **Returns (parsed)**: `SvcSearchV2ArticlesearchJsonResponse`
- **Returns (raw)**: `ApiResult[SvcSearchV2ArticlesearchJsonResponse, SearchArticlesErrorBody]`
- **Error**: `SearchArticlesErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 401, 429, anything unmapped]

| Type | Source |
| --- | --- |
| `SortOrStr` | `the_new_york_times_apis/models/enums/sort.py` |
| `SvcSearchV2ArticlesearchJsonResponse` | `the_new_york_times_apis/models/svc_search_v2_articlesearch_json_response.py` |
| `SearchArticlesErrorBody` | `the_new_york_times_apis/errors/search_articles_error.py` |

