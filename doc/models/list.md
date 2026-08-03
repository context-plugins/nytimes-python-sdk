
# List

*This model accepts additional fields of type Any.*

## Structure

`List`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `display_name` | `str` | Optional | Display name for the list. |
| `list_name_encoded` | `str` | Optional | List name encoded for the URL path. |
| `updated` | `str` | Optional | How often the list is updated (WEEKLY or MONTHLY). |
| `books` | [`List[Book]`](../../doc/models/book.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from nytimes.models.book import Book
from nytimes.models.list import List

list = List(
    display_name='display_name2',
    list_name_encoded='list_name_encoded4',
    updated='updated2',
    books=[
        Book(
            rank=208,
            rank_last_week=38,
            weeks_on_list=242,
            asterisk=168,
            dagger=10,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

