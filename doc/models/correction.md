
# Correction

*This model accepts additional fields of type Any.*

## Structure

`Correction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `text` | `str` | Optional | - |
| `correction_date` | `str` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from nytimes.models.correction import Correction

correction = Correction(
    text='text8',
    correction_date='correction_date8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

