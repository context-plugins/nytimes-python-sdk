
# Response 1

*This model accepts additional fields of type Any.*

## Structure

`Response1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `docs` | [`List[ArticleSearchArticle]`](../../doc/models/article-search-article.md) | Optional | - |
| `meta` | [`Meta1`](../../doc/models/meta-1.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from nytimes.models.article_search_article import ArticleSearchArticle
from nytimes.models.meta_1 import Meta1
from nytimes.models.response_1 import Response1

response_1 = Response1(
    docs=[
        ArticleSearchArticle(
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

