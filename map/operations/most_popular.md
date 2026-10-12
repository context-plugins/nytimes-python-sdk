<!-- Generated file — do not edit; regenerated with the SDK. -->

# MostPopular — operations

Accessor: `client.most_popular` · Source: `the_new_york_times_apis/apis/most_popular.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.most_popular.get_most_emailed_articles

- **Route**: `GET /svc/mostpopular/v2/emailed/{period}.json`
- **Auth**: `apikey`
- **Signature**: `def get_most_emailed_articles(*, period: PeriodOrInt = Period.VALUE_1, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `period` — path
- **Returns (parsed)**: `SvcMostpopularV2EmailedJsonResponse`
- **Returns (raw)**: `ApiResult[SvcMostpopularV2EmailedJsonResponse, GetMostEmailedArticlesErrorBody]`
- **Error**: `GetMostEmailedArticlesErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [401, 429, anything unmapped]

| Type | Source |
| --- | --- |
| `PeriodOrInt` | `the_new_york_times_apis/models/enums/period.py` |
| `SvcMostpopularV2EmailedJsonResponse` | `the_new_york_times_apis/models/svc_mostpopular_v2_emailed_json_response.py` |
| `GetMostEmailedArticlesErrorBody` | `the_new_york_times_apis/errors/get_most_emailed_articles_error.py` |

### client.most_popular.get_most_shared_articles

- **Route**: `GET /svc/mostpopular/v2/shared/{period}.json`
- **Auth**: `apikey`
- **Signature**: `def get_most_shared_articles(*, period: PeriodOrInt = Period.VALUE_1, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `period` — path
- **Returns (parsed)**: `SvcMostpopularV2SharedJsonResponse`
- **Returns (raw)**: `ApiResult[SvcMostpopularV2SharedJsonResponse, GetMostSharedArticlesErrorBody]`
- **Error**: `GetMostSharedArticlesErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [401, 429, anything unmapped]

| Type | Source |
| --- | --- |
| `PeriodOrInt` | `the_new_york_times_apis/models/enums/period.py` |
| `SvcMostpopularV2SharedJsonResponse` | `the_new_york_times_apis/models/svc_mostpopular_v2_shared_json_response.py` |
| `GetMostSharedArticlesErrorBody` | `the_new_york_times_apis/errors/get_most_shared_articles_error.py` |

### client.most_popular.get_most_shared_articles_by_type

- **Route**: `GET /svc/mostpopular/v2/shared/{period}/{share_type}.json`
- **Auth**: `apikey`
- **Signature**: `def get_most_shared_articles_by_type(*, period: PeriodOrInt = Period.VALUE_1, share_type: ShareTypeOrStr = ShareType.FACEBOOK, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `period` — path · `share_type` — path
- **Returns (parsed)**: `SvcMostpopularV2SharedJsonResponse`
- **Returns (raw)**: `ApiResult[SvcMostpopularV2SharedJsonResponse, GetMostSharedArticlesByTypeErrorBody]`
- **Error**: `GetMostSharedArticlesByTypeErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [401, 429, anything unmapped]

| Type | Source |
| --- | --- |
| `PeriodOrInt` | `the_new_york_times_apis/models/enums/period.py` |
| `ShareTypeOrStr` | `the_new_york_times_apis/models/enums/share_type.py` |
| `SvcMostpopularV2SharedJsonResponse` | `the_new_york_times_apis/models/svc_mostpopular_v2_shared_json_response.py` |
| `GetMostSharedArticlesByTypeErrorBody` | `the_new_york_times_apis/errors/get_most_shared_articles_by_type_error.py` |

### client.most_popular.get_most_viewed_articles

- **Route**: `GET /svc/mostpopular/v2/viewed/{period}.json`
- **Auth**: `apikey`
- **Signature**: `def get_most_viewed_articles(*, period: PeriodOrInt = Period.VALUE_1, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `period` — path
- **Returns (parsed)**: `SvcMostpopularV2ViewedJsonResponse`
- **Returns (raw)**: `ApiResult[SvcMostpopularV2ViewedJsonResponse, GetMostViewedArticlesErrorBody]`
- **Error**: `GetMostViewedArticlesErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [401, 429, anything unmapped]

| Type | Source |
| --- | --- |
| `PeriodOrInt` | `the_new_york_times_apis/models/enums/period.py` |
| `SvcMostpopularV2ViewedJsonResponse` | `the_new_york_times_apis/models/svc_mostpopular_v2_viewed_json_response.py` |
| `GetMostViewedArticlesErrorBody` | `the_new_york_times_apis/errors/get_most_viewed_articles_error.py` |

