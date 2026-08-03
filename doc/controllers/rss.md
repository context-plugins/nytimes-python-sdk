# RSS

```python
rss_api = client.rss
```

## Class Name

`RssApi`


# Returns a List of Articles for a Given Section

Given section name, return lists of articles ranked on the section front.

:information_source: **Note** This endpoint does not require authentication.

```python
def returns_a_list_of_articles_for_a_given_section(self,
                                                  section)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `section` | [`Section`](../../doc/models/section.md) | Template, Required | Section name (Arts, Africa, Americas, ...). |

## Response Type

**200**: A list of articles.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ReturnsAListOfArticlesForAGivenSectionResponse`](../../doc/models/returns-a-list-of-articles-for-a-given-section-response.md).

## Example Usage

```python
section = Section.HOMEPAGE

result = rss_api.returns_a_list_of_articles_for_a_given_section(section)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

