
# Book

*This model accepts additional fields of type Any.*

## Structure

`Book`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `rank` | `int` | Optional | Rank on the list. |
| `rank_last_week` | `int` | Optional | Rank on list last week. |
| `weeks_on_list` | `int` | Optional | Number of weeks on list. |
| `asterisk` | `int` | Optional | Book's sales are barely distinguishable from those of the book above it. |
| `dagger` | `int` | Optional | Some retailers report receiving bulk orders. |
| `primary_isbn_13` | `str` | Optional | The book's ID, which is usually an ISBN 13. |
| `publisher` | `str` | Optional | Publisher name. |
| `description` | `str` | Optional | A short description of the book. |
| `title` | `str` | Optional | The book title. |
| `author` | `str` | Optional | The book author. |
| `contributor` | `str` | Optional | The book author. |
| `book_image` | `str` | Optional | Book cover image. |
| `amazon_product_url` | `str` | Optional | A link to the book on Amazon. |
| `age_group` | `str` | Optional | Book age group. |
| `book_review_link` | `str` | Optional | Link to NYT book review. |
| `sunday_review_link` | `str` | Optional | Link to NYT Sunday book review. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from nytimes.models.book import Book

book = Book(
    rank=50,
    rank_last_week=36,
    weeks_on_list=240,
    asterisk=166,
    dagger=248,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

