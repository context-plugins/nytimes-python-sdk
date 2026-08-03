
# Most Viewed Articles on Ny Times Com Response

*This model accepts additional fields of type Any.*

## Structure

`MostViewedArticlesOnNyTimesComResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `str` | Optional | API response status (e.g. OK). |
| `copyright` | `str` | Optional | Copyright message. |
| `num_results` | `int` | Optional | Number of articles in the results (e.g. 20). |
| `results` | [`List[ViewedArticle]`](../../doc/models/viewed-article.md) | Optional | Array of articles. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from nytimes.models.most_viewed_articles_on_ny_times_com_response import MostViewedArticlesOnNyTimesComResponse
from nytimes.models.viewed_article import ViewedArticle

most_viewed_articles_on_ny_times_com_response = MostViewedArticlesOnNyTimesComResponse(
    status='status8',
    copyright='copyright4',
    num_results=194,
    results=[
        ViewedArticle(
            url='url0',
            adx_keywords='adx_keywords2',
            column='column2',
            section='section0',
            byline='byline8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        ViewedArticle(
            url='url0',
            adx_keywords='adx_keywords2',
            column='column2',
            section='section0',
            byline='byline8',
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

