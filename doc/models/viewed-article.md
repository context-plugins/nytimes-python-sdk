
# Viewed Article

*This model accepts additional fields of type Any.*

## Structure

`ViewedArticle`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `url` | `str` | Optional | Article's URL. |
| `adx_keywords` | `str` | Optional | Semicolon separated list of keywords. |
| `column` | `str` | Optional | Deprecated. Set to null. |
| `section` | `str` | Optional | Article's section (e.g. Sports). |
| `byline` | `str` | Optional | Article's byline (e.g. By Thomas L. Friedman). |
| `mtype` | `str` | Optional | Asset type (e.g. Article, Interactive, ...). |
| `title` | `str` | Optional | Article's headline (e.g. When the Cellos Play, the Cows Come Home). |
| `abstract` | `str` | Optional | Brief summary of the article. |
| `published_date` | `str` | Optional | When the article was published on the web (e.g. 2021-04-19). |
| `source` | `str` | Optional | Publisher (e.g. New York Times). |
| `id` | `int` | Optional | Asset ID number (e.g. 100000007772696). |
| `asset_id` | `int` | Optional | Asset ID number (e.g. 100000007772696). |
| `des_facet` | `List[str]` | Optional | Array of description facets (e.g. Quarantine (Life and Culture)). |
| `org_facet` | `List[str]` | Optional | Array of organization facets (e.g. Sullivan Street Bakery). |
| `per_facet` | `List[str]` | Optional | Array of person facets (e.g. Bittman, Mark). |
| `geo_facet` | `List[str]` | Optional | Array of geographic facets (e.g. Canada). |
| `media` | [`List[Media]`](../../doc/models/media.md) | Optional | Array of images. |
| `uri` | `str` | Optional | An article's globally unique identifier. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from nytimes.models.viewed_article import ViewedArticle

viewed_article = ViewedArticle(
    url='url8',
    adx_keywords='adx_keywords0',
    column='column0',
    section='section8',
    byline='byline6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

