
# Returns an Array of Articles Response

*This model accepts additional fields of type Any.*

## Structure

`ReturnsAnArrayOfArticlesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `str` | Optional | - |
| `copyright` | `str` | Optional | - |
| `response` | [`Response1`](../../doc/models/response-1.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from nytimes.models.article_search_article import ArticleSearchArticle
from nytimes.models.meta_1 import Meta1
from nytimes.models.response_1 import Response1
from nytimes.models.returns_an_array_of_articles_response import ReturnsAnArrayOfArticlesResponse

returns_an_array_of_articles_response = ReturnsAnArrayOfArticlesResponse(
    status='status0',
    copyright='copyright6',
    response=Response1(
        docs=[
            ArticleSearchArticle(
                web_url='web_url8',
                snippet='snippet4',
                print_page=230,
                print_section='print_section6',
                source='source8',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            ArticleSearchArticle(
                web_url='web_url8',
                snippet='snippet4',
                print_page=230,
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
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

