
# List Response

*This model accepts additional fields of type Any.*

## Structure

`ListResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `str` | Optional | - |
| `copyright` | `str` | Optional | - |
| `num_results` | `int` | Optional | - |
| `results` | [`Results`](../../doc/models/results.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from nytimes.models.list_response import ListResponse
from nytimes.models.results import Results

list_response = ListResponse(
    status='status0',
    copyright='copyright6',
    num_results=22,
    results=Results(
        display_name='display_name6',
        list_name_encoded='list_name_encoded8',
        published_date='published_date0',
        updated='updated8',
        previous_published_date='previous_published_date0',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

