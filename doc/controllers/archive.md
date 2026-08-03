# Archive

```python
archive_api = client.archive
```

## Class Name

`ArchiveApi`


# Returns an Array of Articles for a Given Month

Pass in year and month and get back JSON with all articles for that month. The response can be big (~20 megabytes) and contain thousands of articles, depending on the year and month.

```python
def returns_an_array_of_articles_for_a_given_month(self,
                                                  year,
                                                  month)
```

## Authentication

This endpoint requires [apikey](../../doc/auth/custom-query-parameter.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `year` | `int` | Template, Required | Year: 1851-2019 |
| `month` | `int` | Template, Required | Year: 1-12 |

## Response Type

**200**: An array of articles.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ReturnsAnArrayOfArticlesForAGivenMonthResponse`](../../doc/models/returns-an-array-of-articles-for-a-given-month-response.md).

## Example Usage

```python
year = 2018

month = 9

result = archive_api.returns_an_array_of_articles_for_a_given_month(
    year,
    month
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized request, check api-key is set. | [`ReturnsAnArrayOfArticlesForAGivenMonthException`](../../doc/models/returns-an-array-of-articles-for-a-given-month-exception.md) |
| 429 | Too many requests.  You reached your per minute or per day rate limit. | `ApiException` |

