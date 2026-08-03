
# Image 1

*This model accepts additional fields of type Any.*

## Structure

`Image1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `link` | `str` | Optional | - |
| `title` | `str` | Optional | - |
| `url` | `str` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from nytimes.models.image_1 import Image1

image_1 = Image1(
    link='link0',
    title='title4',
    url='url4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

