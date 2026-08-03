
# Fault

*This model accepts additional fields of type Any.*

## Structure

`Fault`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `faultstring` | `str` | Optional | - |
| `detail` | [`Detail`](../../doc/models/detail.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from nytimes.models.detail import Detail
from nytimes.models.fault import Fault

fault = Fault(
    faultstring='faultstring2',
    detail=Detail(
        errorcode='errorcode6',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

