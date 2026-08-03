
# Article Search Headline

*This model accepts additional fields of type Any.*

## Structure

`ArticleSearchHeadline`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `main` | `str` | Optional | - |
| `kicker` | `str` | Optional | - |
| `print_headline` | `str` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from nytimes.models.article_search_headline import ArticleSearchHeadline

article_search_headline = ArticleSearchHeadline(
    main='main2',
    kicker='kicker8',
    print_headline='print_headline2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

