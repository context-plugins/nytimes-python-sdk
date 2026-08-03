
# Response

*This model accepts additional fields of type Any.*

## Structure

`Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `meta` | [`Meta`](../../doc/models/meta.md) | Optional | - |
| `docs` | [`List[Article]`](../../doc/models/article.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from nytimes.models.article import Article
from nytimes.models.meta import Meta
from nytimes.models.response import Response

response = Response(
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
)
```

