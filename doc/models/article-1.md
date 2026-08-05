
# Article 1

*This model accepts additional fields of type Any.*

## Structure

`Article1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `web_url` | `str` | Optional | Article URL. |
| `snippet` | `str` | Optional | - |
| `print_page` | `int` | Optional | Page in print (e.g. 1). |
| `print_section` | `str` | Optional | Section in print (e.g. A). |
| `source` | `str` | Optional | - |
| `multimedia` | [`List[Multimedia]`](../../doc/models/multimedia.md) | Optional | - |
| `headline` | [`Headline`](../../doc/models/headline.md) | Optional | - |
| `keywords` | [`List[Keyword]`](../../doc/models/keyword.md) | Optional | - |
| `pub_date` | `str` | Optional | Publication date. |
| `document_type` | `str` | Optional | Document type (article, multimedia). |
| `news_desk` | `str` | Optional | Desk in the newsroom that worked on the story (Foreign, Metro, Sports, ...). |
| `section_name` | `str` | Optional | Section that the article appeared in (New York, Sports, World, ...). |
| `byline` | [`Byline`](../../doc/models/byline.md) | Optional | - |
| `type_of_material` | `str` | Optional | Type of asset (Correction, News, Op-Ed, Review, Video, ...). |
| `id` | `str` | Optional | - |
| `word_count` | `int` | Optional | Number of words in the article. |
| `uri` | `str` | Optional | Uniquely identifies an asset. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from nytimes.models.article_1 import Article1

article_1 = Article1(
    web_url='web_url8',
    snippet='snippet4',
    print_page=122,
    print_section='print_section6',
    source='source8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

