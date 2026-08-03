# Stories

```python
stories_api = client.stories
```

## Class Name

`StoriesApi`


# Top Stories

The Top Stories API returns an array of articles currently on the specified section.

```python
def top_stories(self,
               section)
```

## Authentication

This endpoint requires [apikey](../../doc/auth/custom-query-parameter.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `section` | [`Section1`](../../doc/models/section-1.md) | Template, Required | The section the story appears in. |

## Response Type

**200**: An array of articles.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TopStoriesResponse`](../../doc/models/top-stories-response.md).

## Example Usage

```python
section = Section1.HOME

result = stories_api.top_stories(section)

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

