
# Article Search Byline

*This model accepts additional fields of type Any.*

## Structure

`ArticleSearchByline`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `original` | `str` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from nytimes.models.article_search_byline import ArticleSearchByline

article_search_byline = ArticleSearchByline(
    original='original4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

