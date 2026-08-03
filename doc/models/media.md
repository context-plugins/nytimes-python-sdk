
# Media

*This model accepts additional fields of type Any.*

## Structure

`Media`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `str` | Optional | Asset type (e.g. image). |
| `subtype` | `str` | Optional | Asset subtype (e.g. photo). |
| `caption` | `str` | Optional | Media caption. |
| `copyright` | `str` | Optional | Media credit. |
| `approved_for_syndication` | `bool` | Optional | Whether media is approved for syndication. |
| `media_metadata` | [`List[MediaMetadata]`](../../doc/models/media-metadata.md) | Optional | Media metadata (url, width, height, ...). |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from nytimes.models.media import Media

media = Media(
    mtype='type2',
    subtype='subtype4',
    caption='caption6',
    copyright='copyright0',
    approved_for_syndication=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

