
# Multimedia

*This model accepts additional fields of type Any.*

## Structure

`Multimedia`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `rank` | `int` | Optional | - |
| `subtype` | `str` | Optional | - |
| `caption` | `str` | Optional | - |
| `credit` | `str` | Optional | - |
| `mtype` | `str` | Optional | - |
| `url` | `str` | Optional | - |
| `height` | `int` | Optional | - |
| `width` | `int` | Optional | - |
| `legacy` | [`Legacy`](../../doc/models/legacy.md) | Optional | - |
| `crop_name` | `str` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from nytimes.models.multimedia import Multimedia

multimedia = Multimedia(
    rank=38,
    subtype='subtype6',
    caption='caption8',
    credit='credit2',
    mtype='type6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

