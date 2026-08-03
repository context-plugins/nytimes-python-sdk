
# Person

*This model accepts additional fields of type Any.*

## Structure

`Person`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `firstname` | `str` | Optional | - |
| `middlename` | `str` | Optional | - |
| `lastname` | `str` | Optional | - |
| `qualifier` | `str` | Optional | - |
| `title` | `str` | Optional | - |
| `role` | `str` | Optional | - |
| `organization` | `str` | Optional | - |
| `rank` | `int` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from nytimes.models.person import Person

person = Person(
    firstname='firstname6',
    middlename='middlename4',
    lastname='lastname8',
    qualifier='qualifier6',
    title='title6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

