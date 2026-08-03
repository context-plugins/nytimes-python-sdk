
# Keyword

*This model accepts additional fields of type Any.*

## Structure

`Keyword`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | - |
| `value` | `str` | Optional | - |
| `rank` | `int` | Optional | - |
| `major` | `str` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from nytimes.models.keyword import Keyword

keyword = Keyword(
    name='name6',
    value='value8',
    rank=228,
    major='major0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

