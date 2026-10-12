<!-- Generated file — do not edit; regenerated with the SDK. -->

# Stories — operations

Accessor: `client.stories` · Source: `the_new_york_times_apis/apis/stories.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.stories.get_top_stories_by_section

- **Route**: `GET /svc/topstories/v2/{section}.json`
- **Auth**: `apikey`
- **Signature**: `def get_top_stories_by_section(*, section: SectionOrStr = Section.HOME, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `section` — path
- **Returns (parsed)**: `SvcTopstoriesV2JsonResponse`
- **Returns (raw)**: `ApiResult[SvcTopstoriesV2JsonResponse, GetTopStoriesBySectionErrorBody]`
- **Error**: `GetTopStoriesBySectionErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [401, 429, anything unmapped]

| Type | Source |
| --- | --- |
| `SectionOrStr` | `the_new_york_times_apis/models/enums/section.py` |
| `SvcTopstoriesV2JsonResponse` | `the_new_york_times_apis/models/svc_topstories_v2_json_response.py` |
| `GetTopStoriesBySectionErrorBody` | `the_new_york_times_apis/errors/get_top_stories_by_section_error.py` |

