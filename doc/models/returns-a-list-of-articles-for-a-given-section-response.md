
# Returns a List of Articles for a Given Section Response

*This model accepts additional fields of type Any.*

## Structure

`ReturnsAListOfArticlesForAGivenSectionResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `channel` | [`Channel`](../../doc/models/channel.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from nytimes.models.channel import Channel
from nytimes.models.image_1 import Image1
from nytimes.models.item import Item
from nytimes.models.returns_a_list_of_articles_for_a_given_section_response import ReturnsAListOfArticlesForAGivenSectionResponse

returns_a_list_of_articles_for_a_given_section_response = ReturnsAListOfArticlesForAGivenSectionResponse(
    channel=Channel(
        atom_link='atom:link0',
        copyright='copyright2',
        description='description4',
        image=Image1(
            link='link6',
            title='title2',
            url='url0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        item=[
            Item(
                atom_link='atom:link8',
                category='category0',
                description='description2',
                dc_creator='dc:creator2',
                guid='guid6',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            Item(
                atom_link='atom:link8',
                category='category0',
                description='description2',
                dc_creator='dc:creator2',
                guid='guid6',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            Item(
                atom_link='atom:link8',
                category='category0',
                description='description2',
                dc_creator='dc:creator2',
                guid='guid6',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            )
        ],
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

