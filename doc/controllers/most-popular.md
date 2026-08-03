# Most Popular

```python
most_popular_api = client.most_popular
```

## Class Name

`MostPopularApi`

## Methods

* [Most Emailed Articles on NY Times Com](../../doc/controllers/most-popular.md#most-emailed-articles-on-ny-times-com)
* [Most Shared Articles on NY Times Com](../../doc/controllers/most-popular.md#most-shared-articles-on-ny-times-com)
* [Most Shared Articles on NY Times Com of Specified Share Type](../../doc/controllers/most-popular.md#most-shared-articles-on-ny-times-com-of-specified-share-type)
* [Most Viewed Articles on NY Times Com](../../doc/controllers/most-popular.md#most-viewed-articles-on-ny-times-com)


# Most Emailed Articles on NY Times Com

Returns an array of the most emailed articles on NYTimes.com for specified period of time (1 day, 7 days, or 30 days).

```python
def most_emailed_articles_on_ny_times_com(self,
                                         period)
```

## Authentication

This endpoint requires [apikey](../../doc/auth/custom-query-parameter.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `period` | [`Period`](../../doc/models/period.md) | Template, Required | Time period: 1, 7, or 30 days. |

## Response Type

**200**: An array of articles.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`MostEmailedArticlesOnNyTimesComResponse`](../../doc/models/most-emailed-articles-on-ny-times-com-response.md).

## Example Usage

```python
period = Period.ENUM_1

result = most_popular_api.most_emailed_articles_on_ny_times_com(period)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized request. Make sure api-key is set. | `ApiException` |
| 429 | Too many requests. You reached your per minute or per day rate limit. | `ApiException` |


# Most Shared Articles on NY Times Com

Returns an array of the most shared articles on NYTimes.com for specified period of time (1 day, 7 days, or 30 days).

```python
def most_shared_articles_on_ny_times_com(self,
                                        period)
```

## Authentication

This endpoint requires [apikey](../../doc/auth/custom-query-parameter.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `period` | [`Period`](../../doc/models/period.md) | Template, Required | Time period: 1, 7, or 30 days. |

## Response Type

**200**: An array of articles.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`MostSharedArticlesOnNyTimesComResponse`](../../doc/models/most-shared-articles-on-ny-times-com-response.md).

## Example Usage

```python
period = Period.ENUM_1

result = most_popular_api.most_shared_articles_on_ny_times_com(period)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized request.  Make sure api-key is set. | `ApiException` |
| 429 | Too many requests.  You reached your per minute or per day rate limit. | `ApiException` |


# Most Shared Articles on NY Times Com of Specified Share Type

Returns an array of the most shared articles by share type on NYTimes.com for specified period of time (1 day, 7 days, or 30 days).

```python
def most_shared_articles_on_ny_times_com_of_specified_share_type(self,
                                                                period)
```

## Authentication

This endpoint requires [apikey](../../doc/auth/custom-query-parameter.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `period` | [`Period`](../../doc/models/period.md) | Template, Required | Time period: 1, 7, or 30 days. |

## Response Type

**200**: An array of articles.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`MostSharedArticlesOnNyTimesComOfSpecifiedShareTypeResponse`](../../doc/models/most-shared-articles-on-ny-times-com-of-specified-share-type-response.md).

## Example Usage

```python
period = Period.ENUM_1

result = most_popular_api.most_shared_articles_on_ny_times_com_of_specified_share_type(period)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized request.  Make sure api-key is set. | `ApiException` |
| 429 | Too many requests.  You reached your per minute or per day rate limit. | `ApiException` |


# Most Viewed Articles on NY Times Com

Returns an array of the most viewed articles on NYTimes.com for specified period of time (1 day, 7 days, or 30 days).

```python
def most_viewed_articles_on_ny_times_com(self,
                                        period)
```

## Authentication

This endpoint requires [apikey](../../doc/auth/custom-query-parameter.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `period` | [`Period`](../../doc/models/period.md) | Template, Required | Time period: 1, 7, or 30 days. |

## Response Type

**200**: An array of articles.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`MostViewedArticlesOnNyTimesComResponse`](../../doc/models/most-viewed-articles-on-ny-times-com-response.md).

## Example Usage

```python
period = Period.ENUM_1

result = most_popular_api.most_viewed_articles_on_ny_times_com(period)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized request.  Make sure api-key is set. | `ApiException` |
| 429 | Too many requests.  You reached your per minute or per day rate limit. | `ApiException` |

