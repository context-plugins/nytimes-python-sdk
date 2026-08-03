
# Image

*This model accepts additional fields of type Any.*

## Structure

`Image`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `url` | `str` | Optional | - |
| `height` | `int` | Optional | - |
| `width` | `int` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from nytimes.models.image import Image

image = Image(
    url='url0',
    height=120,
    width=228,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

