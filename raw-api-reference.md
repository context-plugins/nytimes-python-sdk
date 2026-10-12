# Raw Reference

**Raw** endpoints, reached through `with_raw_response`, return `ApiResult[T, E]` and never raise for an API error. For the parsed endpoints, see [API Reference](api-reference.md).

> Source: [TheNewYorkTimesApisClient](the_new_york_times_apis/client.py)

## Archive

> Source: [Archive](the_new_york_times_apis/apis/archive.py)

<details>
<summary><code>def get_archive_by_month(*, year: int = 2018, month: int = 9, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SvcArchiveV1JsonResponse, GetArchiveByMonthErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Pass in year and month and get back JSON with all articles for that month. The response can be big (~20 megabytes) and contain thousands of articles, depending on the year and month.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.archive.with_raw_response.get_archive_by_month(year=1, month=1)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SvcArchiveV1JsonResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetArchiveByMonthErrorBody
```

**Async**

```python
result = await async_client.archive.with_raw_response.get_archive_by_month(year=1, month=1)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SvcArchiveV1JsonResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetArchiveByMonthErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>year</code> | <code>int</code> | Year: 1851-2019<br>**Default**: <code>2018</code> |
| <code>month</code> | <code>int</code> | Year: 1-12<br>**Default**: <code>9</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_new_york_times_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_new_york_times_apis/core/results.py)&#91;[SvcArchiveV1JsonResponse](the_new_york_times_apis/models/svc_archive_v1_json_response.py), [GetArchiveByMonthErrorBody](the_new_york_times_apis/errors/get_archive_by_month_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[SvcArchiveV1JsonResponse](the_new_york_times_apis/models/svc_archive_v1_json_response.py)</code> -- An array of articles.

**On `Failure`**: `error` is <code>[GetArchiveByMonthErrorBody](the_new_york_times_apis/errors/get_archive_by_month_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401 | <code>[SvcArchiveV1Json401Error1](the_new_york_times_apis/models/svc_archive_v1_json401_error1.py)</code> |
| 429 | <code>[RawError](the_new_york_times_apis/core/results.py)</code> |
| anything unmapped | <code>[RawError](the_new_york_times_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Books

> Source: [Books](the_new_york_times_apis/apis/books.py)

<details>
<summary><code>def get_lists_date_list_json(date: str, list_: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListResponse, GetListsDateListJsonErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get Best Sellers data for a given list name and date.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.books.with_raw_response.get_lists_date_list_json("some example string", "some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetListsDateListJsonErrorBody
```

**Async**

```python
result = await async_client.books.with_raw_response.get_lists_date_list_json(
    "some example string", "some example string"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetListsDateListJsonErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>date</code> | <code>str</code> | YYYY-MM-DD or "current"<br><br>The date the best sellers list was in the print [The New York Times Book Review](https://www.nytimes.com/section/books/review).  Use "current" to get latest list. |
| <code>list_</code> | <code>str</code> | Name of the Best Sellers List (e.g. hardcover-fiction). You can get the  list of names from the /lists/overview.json service. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_new_york_times_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_new_york_times_apis/core/results.py)&#91;[ListResponse](the_new_york_times_apis/models/list_response.py), [GetListsDateListJsonErrorBody](the_new_york_times_apis/errors/get_lists_date_list_json_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListResponse](the_new_york_times_apis/models/list_response.py)</code> -- Best Sellers list books.

**On `Failure`**: `error` is <code>[GetListsDateListJsonErrorBody](the_new_york_times_apis/errors/get_lists_date_list_json_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401, 429 | <code>[RawError](the_new_york_times_apis/core/results.py)</code> |
| anything unmapped | <code>[RawError](the_new_york_times_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_lists_overview_json(*, published_date: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[OverviewResponse, GetListsOverviewJsonErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get all books for all the Best Sellers lists for specified print date.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.books.with_raw_response.get_lists_overview_json()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type OverviewResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetListsOverviewJsonErrorBody
```

**Async**

```python
result = await async_client.books.with_raw_response.get_lists_overview_json()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type OverviewResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetListsOverviewJsonErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>published_date</code> | <code>str \| None</code> | YYYY-MM-DD<br><br>The overview published date when the list was or will be in the print [The New York Times Book Review](https://www.nytimes.com/section/books/review).<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_new_york_times_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_new_york_times_apis/core/results.py)&#91;[OverviewResponse](the_new_york_times_apis/models/overview_response.py), [GetListsOverviewJsonErrorBody](the_new_york_times_apis/errors/get_lists_overview_json_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[OverviewResponse](the_new_york_times_apis/models/overview_response.py)</code> -- Overview of Best Sellers lists.

**On `Failure`**: `error` is <code>[GetListsOverviewJsonErrorBody](the_new_york_times_apis/errors/get_lists_overview_json_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401, 429 | <code>[RawError](the_new_york_times_apis/core/results.py)</code> |
| anything unmapped | <code>[RawError](the_new_york_times_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## MostPopular

> Source: [MostPopular](the_new_york_times_apis/apis/most_popular.py)

<details>
<summary><code>def get_most_emailed_articles(*, period: PeriodOrInt = Period.VALUE_1, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SvcMostpopularV2EmailedJsonResponse, GetMostEmailedArticlesErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns an array of the most emailed articles on NYTimes.com for specified period of time (1 day, 7 days, or 30 days).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.most_popular.with_raw_response.get_most_emailed_articles(period=Period.VALUE_1)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SvcMostpopularV2EmailedJsonResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetMostEmailedArticlesErrorBody
```

**Async**

```python
result = await async_client.most_popular.with_raw_response.get_most_emailed_articles(period=Period.VALUE_1)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SvcMostpopularV2EmailedJsonResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetMostEmailedArticlesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>period</code> | <code>[PeriodOrInt](the_new_york_times_apis/models/enums/period.py)</code> | Time period: 1, 7, or 30 days.<br>**Default**: <code>Period.VALUE_1</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_new_york_times_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_new_york_times_apis/core/results.py)&#91;[SvcMostpopularV2EmailedJsonResponse](the_new_york_times_apis/models/svc_mostpopular_v2_emailed_json_response.py), [GetMostEmailedArticlesErrorBody](the_new_york_times_apis/errors/get_most_emailed_articles_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[SvcMostpopularV2EmailedJsonResponse](the_new_york_times_apis/models/svc_mostpopular_v2_emailed_json_response.py)</code> -- An array of articles.

**On `Failure`**: `error` is <code>[GetMostEmailedArticlesErrorBody](the_new_york_times_apis/errors/get_most_emailed_articles_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401, 429 | <code>[RawError](the_new_york_times_apis/core/results.py)</code> |
| anything unmapped | <code>[RawError](the_new_york_times_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_most_shared_articles(*, period: PeriodOrInt = Period.VALUE_1, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SvcMostpopularV2SharedJsonResponse, GetMostSharedArticlesErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns an array of the most shared articles on NYTimes.com for specified period of time (1 day, 7 days, or 30 days).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.most_popular.with_raw_response.get_most_shared_articles(period=Period.VALUE_1)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SvcMostpopularV2SharedJsonResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetMostSharedArticlesErrorBody
```

**Async**

```python
result = await async_client.most_popular.with_raw_response.get_most_shared_articles(period=Period.VALUE_1)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SvcMostpopularV2SharedJsonResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetMostSharedArticlesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>period</code> | <code>[PeriodOrInt](the_new_york_times_apis/models/enums/period.py)</code> | Time period: 1, 7, or 30 days.<br>**Default**: <code>Period.VALUE_1</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_new_york_times_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_new_york_times_apis/core/results.py)&#91;[SvcMostpopularV2SharedJsonResponse](the_new_york_times_apis/models/svc_mostpopular_v2_shared_json_response.py), [GetMostSharedArticlesErrorBody](the_new_york_times_apis/errors/get_most_shared_articles_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[SvcMostpopularV2SharedJsonResponse](the_new_york_times_apis/models/svc_mostpopular_v2_shared_json_response.py)</code> -- An array of articles.

**On `Failure`**: `error` is <code>[GetMostSharedArticlesErrorBody](the_new_york_times_apis/errors/get_most_shared_articles_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401, 429 | <code>[RawError](the_new_york_times_apis/core/results.py)</code> |
| anything unmapped | <code>[RawError](the_new_york_times_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_most_shared_articles_by_type(*, period: PeriodOrInt = Period.VALUE_1, share_type: ShareTypeOrStr = ShareType.FACEBOOK, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SvcMostpopularV2SharedJsonResponse, GetMostSharedArticlesByTypeErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns an array of the most shared articles by share type on NYTimes.com for specified period of time (1 day, 7 days, or 30 days).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.most_popular.with_raw_response.get_most_shared_articles_by_type(
    period=Period.VALUE_1, share_type=ShareType.FACEBOOK
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SvcMostpopularV2SharedJsonResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetMostSharedArticlesByTypeErrorBody
```

**Async**

```python
result = await async_client.most_popular.with_raw_response.get_most_shared_articles_by_type(
    period=Period.VALUE_1, share_type=ShareType.FACEBOOK
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SvcMostpopularV2SharedJsonResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetMostSharedArticlesByTypeErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>period</code> | <code>[PeriodOrInt](the_new_york_times_apis/models/enums/period.py)</code> | Time period: 1, 7, or 30 days.<br>**Default**: <code>Period.VALUE_1</code> |
| <code>share_type</code> | <code>[ShareTypeOrStr](the_new_york_times_apis/models/enums/share_type.py)</code> | Share type: facebook.<br>**Default**: <code>ShareType.FACEBOOK</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_new_york_times_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_new_york_times_apis/core/results.py)&#91;[SvcMostpopularV2SharedJsonResponse](the_new_york_times_apis/models/svc_mostpopular_v2_shared_json_response.py), [GetMostSharedArticlesByTypeErrorBody](the_new_york_times_apis/errors/get_most_shared_articles_by_type_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[SvcMostpopularV2SharedJsonResponse](the_new_york_times_apis/models/svc_mostpopular_v2_shared_json_response.py)</code> -- An array of articles.

**On `Failure`**: `error` is <code>[GetMostSharedArticlesByTypeErrorBody](the_new_york_times_apis/errors/get_most_shared_articles_by_type_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401, 429 | <code>[RawError](the_new_york_times_apis/core/results.py)</code> |
| anything unmapped | <code>[RawError](the_new_york_times_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_most_viewed_articles(*, period: PeriodOrInt = Period.VALUE_1, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SvcMostpopularV2ViewedJsonResponse, GetMostViewedArticlesErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns an array of the most viewed articles on NYTimes.com for specified period of time (1 day, 7 days, or 30 days).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.most_popular.with_raw_response.get_most_viewed_articles(period=Period.VALUE_1)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SvcMostpopularV2ViewedJsonResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetMostViewedArticlesErrorBody
```

**Async**

```python
result = await async_client.most_popular.with_raw_response.get_most_viewed_articles(period=Period.VALUE_1)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SvcMostpopularV2ViewedJsonResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetMostViewedArticlesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>period</code> | <code>[PeriodOrInt](the_new_york_times_apis/models/enums/period.py)</code> | Time period: 1, 7, or 30 days.<br>**Default**: <code>Period.VALUE_1</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_new_york_times_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_new_york_times_apis/core/results.py)&#91;[SvcMostpopularV2ViewedJsonResponse](the_new_york_times_apis/models/svc_mostpopular_v2_viewed_json_response.py), [GetMostViewedArticlesErrorBody](the_new_york_times_apis/errors/get_most_viewed_articles_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[SvcMostpopularV2ViewedJsonResponse](the_new_york_times_apis/models/svc_mostpopular_v2_viewed_json_response.py)</code> -- An array of articles.

**On `Failure`**: `error` is <code>[GetMostViewedArticlesErrorBody](the_new_york_times_apis/errors/get_most_viewed_articles_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401, 429 | <code>[RawError](the_new_york_times_apis/core/results.py)</code> |
| anything unmapped | <code>[RawError](the_new_york_times_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Rss

> Source: [Rss](the_new_york_times_apis/apis/rss.py)

<details>
<summary><code>def get_section_feed(*, section: Section1OrStr = Section1.HOME_PAGE, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Given section name, return lists of articles ranked on the section front.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.rss.with_raw_response.get_section_feed(section=Section1.AFRICA)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.rss.with_raw_response.get_section_feed(section=Section1.AFRICA)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>section</code> | <code>[Section1OrStr](the_new_york_times_apis/models/enums/section1.py)</code> | Section name (Arts, Africa, Americas, ...).<br>**Default**: <code>Section1.HOME_PAGE</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_new_york_times_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_new_york_times_apis/core/results.py)&#91;None, [RawError](the_new_york_times_apis/core/results.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[RawError](the_new_york_times_apis/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Search

> Source: [Search](the_new_york_times_apis/apis/search.py)

<details>
<summary><code>def search_articles(*, begin_date: str | None = None, end_date: str | None = None, fq: str | None = None, page: int | None = None, q: str | None = None, sort: SortOrStr | None = Sort.BEST, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SvcSearchV2ArticlesearchJsonResponse, SearchArticlesErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Search for NYT articles by keywords and filters.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.search.with_raw_response.search_articles()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SvcSearchV2ArticlesearchJsonResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SearchArticlesErrorBody
```

**Async**

```python
result = await async_client.search.with_raw_response.search_articles()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SvcSearchV2ArticlesearchJsonResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SearchArticlesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>begin_date</code> | <code>str \| None</code> | Begin date (e.g. 20120101)<br>**Default**: <code>None</code> |
| <code>end_date</code> | <code>str \| None</code> | End date (e.g. 20121231)<br>**Default**: <code>None</code> |
| <code>fq</code> | <code>str \| None</code> | Filter query<br>**Default**: <code>None</code> |
| <code>page</code> | <code>int \| None</code> | Page number (0, 1, ...)<br>**Default**: <code>None</code> |
| <code>q</code> | <code>str \| None</code> | Query<br>**Default**: <code>None</code> |
| <code>sort</code> | <code>[SortOrStr](the_new_york_times_apis/models/enums/sort.py) \| None</code> | Sort order<br>**Default**: <code>Sort.BEST</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_new_york_times_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_new_york_times_apis/core/results.py)&#91;[SvcSearchV2ArticlesearchJsonResponse](the_new_york_times_apis/models/svc_search_v2_articlesearch_json_response.py), [SearchArticlesErrorBody](the_new_york_times_apis/errors/search_articles_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[SvcSearchV2ArticlesearchJsonResponse](the_new_york_times_apis/models/svc_search_v2_articlesearch_json_response.py)</code> -- An array of articles.

**On `Failure`**: `error` is <code>[SearchArticlesErrorBody](the_new_york_times_apis/errors/search_articles_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 429 | <code>[RawError](the_new_york_times_apis/core/results.py)</code> |
| anything unmapped | <code>[RawError](the_new_york_times_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Stories

> Source: [Stories](the_new_york_times_apis/apis/stories.py)

<details>
<summary><code>def get_top_stories_by_section(*, section: SectionOrStr = Section.HOME, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SvcTopstoriesV2JsonResponse, GetTopStoriesBySectionErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The Top Stories API returns an array of articles currently on the specified section.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.stories.with_raw_response.get_top_stories_by_section(section=Section.ARTS)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SvcTopstoriesV2JsonResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetTopStoriesBySectionErrorBody
```

**Async**

```python
result = await async_client.stories.with_raw_response.get_top_stories_by_section(section=Section.ARTS)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SvcTopstoriesV2JsonResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetTopStoriesBySectionErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>section</code> | <code>[SectionOrStr](the_new_york_times_apis/models/enums/section.py)</code> | The section the story appears in.<br>**Default**: <code>Section.HOME</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](the_new_york_times_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](the_new_york_times_apis/core/results.py)&#91;[SvcTopstoriesV2JsonResponse](the_new_york_times_apis/models/svc_topstories_v2_json_response.py), [GetTopStoriesBySectionErrorBody](the_new_york_times_apis/errors/get_top_stories_by_section_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[SvcTopstoriesV2JsonResponse](the_new_york_times_apis/models/svc_topstories_v2_json_response.py)</code> -- An array of articles.

**On `Failure`**: `error` is <code>[GetTopStoriesBySectionErrorBody](the_new_york_times_apis/errors/get_top_stories_by_section_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 401, 429 | <code>[RawError](the_new_york_times_apis/core/results.py)</code> |
| anything unmapped | <code>[RawError](the_new_york_times_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

