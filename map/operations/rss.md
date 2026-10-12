<!-- Generated file — do not edit; regenerated with the SDK. -->

# Rss — operations

Accessor: `client.rss` · Source: `the_new_york_times_apis/apis/rss.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.rss.get_section_feed

- **Route**: `GET /services/xml/rss/nyt/{section}.xml`
- **Signature**: `def get_section_feed(*, section: Section1OrStr = Section1.HOME_PAGE, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `section` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Section1OrStr` | `the_new_york_times_apis/models/enums/section1.py` |

