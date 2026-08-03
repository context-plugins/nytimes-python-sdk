
# Results 1

*This model accepts additional fields of type Any.*

## Structure

`Results1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `published_date` | `str` | Optional | When the lists were in print. |
| `previous_published_date` | `str` | Optional | Date of previous overview if exists. |
| `next_published_date` | `str` | Optional | Date of next overview if exists. |
| `lists` | [`List[List]`](../../doc/models/list.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from nytimes.models.book import Book
from nytimes.models.list import List
from nytimes.models.results_1 import Results1

results_1 = Results1(
    published_date='published_date2',
    previous_published_date='previous_published_date8',
    next_published_date='next_published_date8',
    lists=[
        List(
            display_name='display_name4',
            list_name_encoded='list_name_encoded6',
            updated='updated0',
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
                ),
                Book(
                    rank=208,
                    rank_last_week=38,
                    weeks_on_list=242,
                    asterisk=168,
                    dagger=10,
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
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
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

