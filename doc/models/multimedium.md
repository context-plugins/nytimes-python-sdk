
# Multimedium

*This model accepts additional fields of type Any.*

## Structure

`Multimedium`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `url` | `str` | Optional | - |
| `format` | `str` | Optional | - |
| `height` | `int` | Optional | - |
| `width` | `int` | Optional | - |
| `mtype` | `str` | Optional | - |
| `subtype` | `str` | Optional | - |
| `caption` | `str` | Optional | - |
| `copyright` | `str` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from nytimes.models.multimedium import Multimedium

multimedium = Multimedium(
    url='url2',
    format='format4',
    height=6,
    width=114,
    mtype='type8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

