
# Article Search Article 1

*This model accepts additional fields of type Any.*

## Structure

`ArticleSearchArticle1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `web_url` | `str` | Optional | Article URL. |
| `snippet` | `str` | Optional | - |
| `print_page` | `str` | Optional | Page in print (e.g. "1"). Empty string when not applicable. |
| `print_section` | `str` | Optional | Section in print (e.g. A). |
| `source` | `str` | Optional | - |
| `multimedia` | [`ArticleSearchMultimedia`](../../doc/models/article-search-multimedia.md) | Optional | - |
| `headline` | [`ArticleSearchHeadline`](../../doc/models/article-search-headline.md) | Optional | - |
| `keywords` | [`List[ArticleSearchKeyword]`](../../doc/models/article-search-keyword.md) | Optional | - |
| `pub_date` | `str` | Optional | Publication date. |
| `document_type` | `str` | Optional | Document type (article, multimedia). |
| `desk` | `str` | Optional | Desk in the newsroom that worked on the story (Business, Foreign, Metro, ...). |
| `section_name` | `str` | Optional | Section that the article appeared in (Arts, New York, World, ...). |
| `byline` | [`ArticleSearchByline`](../../doc/models/article-search-byline.md) | Optional | - |
| `type_of_material` | `str` | Optional | Type of asset (Correction, News, Op-Ed, Review, Video, ...). |
| `word_count` | `int` | Optional | Number of words in the article. |
| `uri` | `str` | Optional | Uniquely identifies an asset. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from nytimes.models.article_search_article_1 import ArticleSearchArticle1

article_search_article_1 = ArticleSearchArticle1(
    web_url='web_url8',
    snippet='snippet6',
    print_page='print_page8',
    print_section='print_section4',
    source='source2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

