# Search

```python
search_api = client.search
```

## Class Name

`SearchApi`


# Returns an Array of Articles

Search for NYT articles by keywords and filters.

```python
def returns_an_array_of_articles(self,
                                begin_date=None,
                                end_date=None,
                                fq=None,
                                page=None,
                                q=None,
                                sort="best")
```

## Authentication

This endpoint requires [apikey](../../doc/auth/custom-query-parameter.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `begin_date` | `str` | Query, Optional | Begin date (e.g. 20120101)<br><br>**Constraints**: *Pattern*: `^\d{8}$` |
| `end_date` | `str` | Query, Optional | End date (e.g. 20121231)<br><br>**Constraints**: *Pattern*: `^\d{8}$` |
| `fq` | `str` | Query, Optional | Filter query |
| `page` | `int` | Query, Optional | Page number (0, 1, ...)<br><br>**Constraints**: `>= 0`, `<= 100` |
| `q` | `str` | Query, Optional | Query |
| `sort` | [`Sort`](../../doc/models/sort.md) | Query, Optional | Sort order<br><br>**Default**: `"best"` |

## Response Type

**200**: An array of articles.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ReturnsAnArrayOfArticlesResponse`](../../doc/models/returns-an-array-of-articles-response.md).

## Example Usage

```python
sort = Sort.BEST

result = search_api.returns_an_array_of_articles(
    sort=sort
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request. Check your query parameters. | `ApiException` |
| 401 | Unauthorized request. Make sure api-key is set. | `ApiException` |
| 429 | Too many requests. You reached your per minute or per day rate limit. | `ApiException` |

