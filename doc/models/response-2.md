
# Response 2

*This model accepts additional fields of type Any.*

## Structure

`Response2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `docs` | [`List[ArticleSearchArticle1]`](../../doc/models/article-search-article-1.md) | Optional | - |
| `meta` | [`Meta1`](../../doc/models/meta-1.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from nytimes.models.article_search_article_1 import ArticleSearchArticle1
from nytimes.models.meta_1 import Meta1
from nytimes.models.response_2 import Response2

response_2 = Response2(
    docs=[
        ArticleSearchArticle1(
            web_url='web_url8',
            snippet='snippet4',
            print_page='print_page2',
            print_section='print_section6',
            source='source8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    meta=Meta1(
        hits=186,
        offset=222,
        time=60,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

