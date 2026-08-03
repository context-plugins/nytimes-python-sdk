
# Shared Article

*This model accepts additional fields of type Any.*

## Structure

`SharedArticle`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `url` | `str` | Optional | Article's URL. |
| `adx_keywords` | `str` | Optional | Semicolon separated list of keywords. |
| `subsection` | `str` | Optional | Article's subsection (e.g. Politics). Can be empty string. |
| `column` | `str` | Optional | Deprecated. Set to null. |
| `eta_id` | `int` | Optional | Deprecated. Set to 0. |
| `section` | `str` | Optional | Article's section (e.g. Sports). |
| `id` | `int` | Optional | Asset ID number (e.g. 100000007772696). |
| `asset_id` | `int` | Optional | Asset ID number (e.g. 100000007772696). |
| `nytdsection` | `str` | Optional | Article's section (e.g. sports). |
| `byline` | `str` | Optional | Article's byline (e.g. By Thomas L. Friedman). |
| `mtype` | `str` | Optional | Asset type (e.g. Article, Interactive, ...). |
| `title` | `str` | Optional | Article's headline (e.g. When the Cellos Play, the Cows Come Home). |
| `abstract` | `str` | Optional | Brief summary of the article. |
| `published_date` | `str` | Optional | When the article was published on the web (e.g. 2021-04-19). |
| `source` | `str` | Optional | Publisher (e.g. New York Times). |
| `updated` | `str` | Optional | When the article was last updated (e.g. 2021-05-12 06:32:03). |
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

from nytimes.models.shared_article import SharedArticle

shared_article = SharedArticle(
    url='url2',
    adx_keywords='adx_keywords4',
    subsection='subsection0',
    column='column4',
    eta_id=116,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

