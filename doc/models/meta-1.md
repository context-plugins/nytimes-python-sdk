
# Meta 1

*This model accepts additional fields of type Any.*

## Structure

`Meta1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `hits` | `int` | Optional | - |
| `offset` | `int` | Optional | - |
| `time` | `int` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from nytimes.models.meta_1 import Meta1

meta_1 = Meta1(
    hits=52,
    offset=100,
    time=182,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

