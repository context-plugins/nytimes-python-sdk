
# Media Metadata

*This model accepts additional fields of type Any.*

## Structure

`MediaMetadata`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `url` | `str` | Optional | Image's URL. |
| `format` | `str` | Optional | Image's crop name. |
| `height` | `int` | Optional | Image's height (e.g. 293). |
| `width` | `int` | Optional | Image's width (e.g. 440). |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from nytimes.models.media_metadata import MediaMetadata

media_metadata = MediaMetadata(
    url='url2',
    format='format6',
    height=156,
    width=248,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

