
# Most Shared Articles on Ny Times Com Response

*This model accepts additional fields of type Any.*

## Structure

`MostSharedArticlesOnNyTimesComResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `str` | Optional | API response status (e.g. OK). |
| `copyright` | `str` | Optional | Copyright message. |
| `num_results` | `int` | Optional | Number of articles in the results (e.g. 20). |
| `results` | [`List[SharedArticle]`](../../doc/models/shared-article.md) | Optional | Array of articles. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from nytimes.models.most_shared_articles_on_ny_times_com_response import MostSharedArticlesOnNyTimesComResponse
from nytimes.models.shared_article import SharedArticle

most_shared_articles_on_ny_times_com_response = MostSharedArticlesOnNyTimesComResponse(
    status='status6',
    copyright='copyright0',
    num_results=84,
    results=[
        SharedArticle(
            url='url0',
            adx_keywords='adx_keywords2',
            subsection='subsection2',
            column='column2',
            eta_id=192,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        SharedArticle(
            url='url0',
            adx_keywords='adx_keywords2',
            subsection='subsection2',
            column='column2',
            eta_id=192,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        SharedArticle(
            url='url0',
            adx_keywords='adx_keywords2',
            subsection='subsection2',
            column='column2',
            eta_id=192,
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

