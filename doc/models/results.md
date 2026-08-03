
# Results

*This model accepts additional fields of type Any.*

## Structure

`Results`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `display_name` | `str` | Optional | Display name for the list. |
| `list_name_encoded` | `str` | Optional | List name encoded for the URL path. |
| `published_date` | `str` | Optional | When the list was in print. |
| `updated` | `str` | Optional | How often the list is updated (WEEKLY or MONTHLY). |
| `previous_published_date` | `str` | Optional | Date of previous list if exists. |
| `next_published_date` | `str` | Optional | Date of next list if exists. |
| `books` | [`List[Book]`](../../doc/models/book.md) | Optional | - |
| `corrections` | [`List[Correction]`](../../doc/models/correction.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from nytimes.models.results import Results

results = Results(
    display_name='display_name6',
    list_name_encoded='list_name_encoded8',
    published_date='published_date0',
    updated='updated8',
    previous_published_date='previous_published_date0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

