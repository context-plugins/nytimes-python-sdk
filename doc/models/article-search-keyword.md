
# Article Search Keyword

*This model accepts additional fields of type Any.*

## Structure

`ArticleSearchKeyword`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | - |
| `value` | `str` | Optional | - |
| `rank` | `int` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from nytimes.models.article_search_keyword import ArticleSearchKeyword

article_search_keyword = ArticleSearchKeyword(
    name='name8',
    value='value0',
    rank=204,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

