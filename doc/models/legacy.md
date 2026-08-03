
# Legacy

*This model accepts additional fields of type Any.*

## Structure

`Legacy`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `xlarge` | `str` | Optional | - |
| `xlargewidth` | `int` | Optional | - |
| `xlargeheight` | `int` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from nytimes.models.legacy import Legacy

legacy = Legacy(
    xlarge='xlarge0',
    xlargewidth=156,
    xlargeheight=10,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

