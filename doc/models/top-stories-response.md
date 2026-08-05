
# Top Stories Response

*This model accepts additional fields of type Any.*

## Structure

`TopStoriesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `str` | Optional | - |
| `copyright` | `str` | Optional | - |
| `section` | `str` | Optional | - |
| `last_updated` | `str` | Optional | - |
| `num_results` | `int` | Optional | - |
| `results` | [`List[Article2]`](../../doc/models/article-2.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from nytimes.models.top_stories_response import TopStoriesResponse

top_stories_response = TopStoriesResponse(
    status='status0',
    copyright='copyright6',
    section='section2',
    last_updated='last_updated0',
    num_results=44,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

