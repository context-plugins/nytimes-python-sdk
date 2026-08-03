
# Most Emailed Articles on Ny Times Com Response

*This model accepts additional fields of type Any.*

## Structure

`MostEmailedArticlesOnNyTimesComResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `str` | Optional | API response status (e.g. OK). |
| `copyright` | `str` | Optional | Copyright message. |
| `num_results` | `int` | Optional | Number of articles in the results (e.g. 20). |
| `results` | [`List[EmailedArticle]`](../../doc/models/emailed-article.md) | Optional | Array of articles. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from nytimes.models.emailed_article import EmailedArticle
from nytimes.models.most_emailed_articles_on_ny_times_com_response import MostEmailedArticlesOnNyTimesComResponse

most_emailed_articles_on_ny_times_com_response = MostEmailedArticlesOnNyTimesComResponse(
    status='status8',
    copyright='copyright4',
    num_results=48,
    results=[
        EmailedArticle(
            url='url0',
            adx_keywords='adx_keywords2',
            subsection='subsection2',
            column='column2',
            eta_id=192,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        EmailedArticle(
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

