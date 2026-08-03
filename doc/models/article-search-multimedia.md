
# Article Search Multimedia

*This model accepts additional fields of type Any.*

## Structure

`ArticleSearchMultimedia`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `caption` | `str` | Optional | - |
| `credit` | `str` | Optional | - |
| `default` | [`Image`](../../doc/models/image.md) | Optional | - |
| `thumbnail` | [`Image`](../../doc/models/image.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from nytimes.models.article_search_multimedia import ArticleSearchMultimedia
from nytimes.models.image import Image

article_search_multimedia = ArticleSearchMultimedia(
    caption='caption8',
    credit='credit2',
    default=Image(
        url='url4',
        height=236,
        width=168,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    thumbnail=Image(
        url='url0',
        height=146,
        width=2,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

