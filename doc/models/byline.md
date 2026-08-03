
# Byline

*This model accepts additional fields of type Any.*

## Structure

`Byline`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `original` | `str` | Optional | - |
| `person` | [`List[Person]`](../../doc/models/person.md) | Optional | - |
| `organization` | `str` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from nytimes.models.byline import Byline
from nytimes.models.person import Person

byline = Byline(
    original='original2',
    person=[
        Person(
            firstname='firstname6',
            middlename='middlename4',
            lastname='lastname8',
            qualifier='qualifier6',
            title='title6',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    organization='organization6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

