
# Headline

*This model accepts additional fields of type Any.*

## Structure

`Headline`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `main` | `str` | Optional | - |
| `kicker` | `str` | Optional | - |
| `content_kicker` | `str` | Optional | - |
| `print_headline` | `str` | Optional | - |
| `name` | `str` | Optional | - |
| `seo` | `str` | Optional | - |
| `sub` | `str` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from nytimes.models.headline import Headline

headline = Headline(
    main='main4',
    kicker='kicker8',
    content_kicker='content_kicker4',
    print_headline='print_headline4',
    name='name0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

