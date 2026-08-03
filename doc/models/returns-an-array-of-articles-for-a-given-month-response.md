
# Returns an Array of Articles for a Given Month Response

*This model accepts additional fields of type Any.*

## Structure

`ReturnsAnArrayOfArticlesForAGivenMonthResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `copyright` | `str` | Optional | - |
| `response` | [`Response`](../../doc/models/response.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from nytimes.models.article import Article
from nytimes.models.meta import Meta
from nytimes.models.response import Response
from nytimes.models.returns_an_array_of_articles_for_a_given_month_response import ReturnsAnArrayOfArticlesForAGivenMonthResponse

returns_an_array_of_articles_for_a_given_month_response = ReturnsAnArrayOfArticlesForAGivenMonthResponse(
    copyright='copyright4',
    response=Response(
        meta=Meta(
            hits=186,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        docs=[
            Article(
                web_url='web_url8',
                snippet='snippet4',
                print_page=230,
                print_section='print_section6',
                source='source8',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            Article(
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
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

