
# Article 2

*This model accepts additional fields of type Any.*

## Structure

`Article2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `section` | `str` | Optional | - |
| `subsection` | `str` | Optional | - |
| `title` | `str` | Optional | - |
| `abstract` | `str` | Optional | - |
| `url` | `str` | Optional | - |
| `uri` | `str` | Optional | - |
| `byline` | `str` | Optional | - |
| `item_type` | `str` | Optional | - |
| `updated_date` | `str` | Optional | - |
| `created_date` | `str` | Optional | - |
| `published_date` | `str` | Optional | - |
| `material_type_facet` | `str` | Optional | - |
| `kicker` | `str` | Optional | - |
| `des_facet` | `List[str]` | Optional | - |
| `org_facet` | `List[str]` | Optional | - |
| `per_facet` | `List[str]` | Optional | - |
| `geo_facet` | `List[str]` | Optional | - |
| `multimedia` | [`List[Multimedium]`](../../doc/models/multimedium.md) | Optional | - |
| `short_url` | `str` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from nytimes.models.article_2 import Article2

article_2 = Article2(
    section='section0',
    subsection='subsection2',
    title='title2',
    abstract='abstract8',
    url='url0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

