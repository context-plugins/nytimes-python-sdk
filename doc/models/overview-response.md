
# Overview Response

*This model accepts additional fields of type Any.*

## Structure

`OverviewResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `str` | Optional | - |
| `copyright` | `str` | Optional | - |
| `num_results` | `int` | Optional | - |
| `results` | [`Results1`](../../doc/models/results-1.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from nytimes.models.book import Book
from nytimes.models.list import List
from nytimes.models.overview_response import OverviewResponse
from nytimes.models.results_1 import Results1

overview_response = OverviewResponse(
    status='status2',
    copyright='copyright8',
    num_results=54,
    results=Results1(
        published_date='published_date0',
        previous_published_date='previous_published_date0',
        next_published_date='next_published_date0',
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
            ),
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
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

