
# Item

*This model accepts additional fields of type Any.*

## Structure

`Item`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `atom_link` | `str` | Optional | - |
| `category` | `str` | Optional | - |
| `description` | `str` | Optional | - |
| `dc_creator` | `str` | Optional | - |
| `guid` | `str` | Optional | - |
| `link` | `str` | Optional | - |
| `media_content` | `str` | Optional | - |
| `media_credit` | `str` | Optional | - |
| `media_description` | `str` | Optional | - |
| `pub_date` | `str` | Optional | - |
| `title` | `str` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from nytimes.models.item import Item

item = Item(
    atom_link='atom:link8',
    category='category0',
    description='description2',
    dc_creator='dc:creator2',
    guid='guid6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

