# API

```python
client_api = client.client
```

## Class Name

`Api`

## Methods

* [GET Lists-Date-List-Json](../../doc/controllers/api.md#get-lists-date-list-json)
* [GET Lists-Overview-Json](../../doc/controllers/api.md#get-lists-overview-json)


# GET Lists-Date-List-Json

Get Best Sellers data for a given list name and date.

```python
def get_lists_date_list_json(self,
                            date,
                            list)
```

## Authentication

This endpoint requires [apikey](../../doc/auth/custom-query-parameter.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `date` | `str` | Template, Required | YYYY-MM-DD or "current"<br><br>The date the best sellers list was in the print [The New York Times Book Review](https://www.nytimes.com/section/books/review).  Use "current" to get latest list.<br><br>**Constraints**: *Pattern*: `^(\d{4}-\d{2}-\d{2}\|current)$` |
| `list` | `str` | Template, Required | Name of the Best Sellers List (e.g. hardcover-fiction). You can get the  list of names from the /lists/overview.json service. |

## Response Type

**200**: Best Sellers list books.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ListResponse`](../../doc/models/list-response.md).

## Example Usage

```python
date = 'date4'

list = 'list2'

result = client_api.get_lists_date_list_json(
    date,
    list
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "status": "OK",
  "copyright": "Copyright (c) 2025 The New York Times Company. All Rights Reserved.",
  "num_results": 15,
  "results": {
    "list_name": "Hardcover Fiction",
    "list_name_encoded": "hardcover-fiction",
    "display_name": "Hardcover Fiction",
    "bestsellers_date": "2025-05-04",
    "previous_published_date": "2025-05-11",
    "published_date": "2025-05-18",
    "next_published_date": "2025-05-25",
    "normal_list_ends_at": 15,
    "updated": "WEEKLY",
    "books": [
      {
        "rank": 1,
        "rank_last_week": 1,
        "weeks_on_list": 2,
        "asterisk": 0,
        "dagger": 0,
        "primary_isbn13": "9780593441299",
        "publisher": "Berkley",
        "description": "A writer looking for her big break competes against a Pulitzer winner to tell the story of an octogenarian with a storied past.",
        "title": "Great Big Beautiful Life",
        "author": "Emily Henry",
        "contributor": "Emily Henry",
        "contributor_note": "",
        "book_image": "https://static01.nyt.com/bestsellers/images/9780593441299.jpg",
        "amazon_product_url": "https://www.amazon.com/dp/059344129X?tag=thenewyorktim-20",
        "age_group": "",
        "book_review_link": "",
        "sunday_review_link": ""
      }
    ],
    "corrections": []
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized request. Make sure api-key is set. | `ApiException` |
| 429 | Too many requests. You reached your per minute or per day rate limit. | `ApiException` |


# GET Lists-Overview-Json

Get all books for all the Best Sellers lists for specified print date.

```python
def get_lists_overview_json(self,
                           published_date=None)
```

## Authentication

This endpoint requires [apikey](../../doc/auth/custom-query-parameter.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `published_date` | `str` | Query, Optional | YYYY-MM-DD<br><br>The overview published date when the list was or will be in the print [The New York Times Book Review](https://www.nytimes.com/section/books/review).<br><br>**Constraints**: *Pattern*: `^\d{4}-\d{2}-\d{2}$` |

## Response Type

**200**: Overview of Best Sellers lists.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`OverviewResponse`](../../doc/models/overview-response.md).

## Example Usage

```python
result = client_api.get_lists_overview_json()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "status": "OK",
  "copyright": "Copyright (c) 2025 The New York Times Company. All Rights Reserved.",
  "num_results": 250,
  "results": {
    "bestsellers_date": "2025-05-04",
    "previous_published_date": "2025-05-11",
    "published_date": "2025-05-18",
    "next_published_date": "2025-05-25",
    "lists": [
      {
        "list_id": 1,
        "list_name": "Hardcover Fiction",
        "list_name_encoded": "hardcover-fiction",
        "display_name": "Hardcover Fiction",
        "updated": "WEEKLY",
        "books": [
          {
            "rank": 1,
            "rank_last_week": 1,
            "weeks_on_list": 2,
            "asterisk": 0,
            "dagger": 0,
            "primary_isbn13": "9780593441299",
            "publisher": "Berkley",
            "description": "A writer looking for her big break competes against a Pulitzer winner to tell the story of an octogenarian with a storied past.",
            "title": "Great Big Beautiful Life",
            "author": "Emily Henry",
            "contributor": "Emily Henry",
            "contributor_note": "",
            "book_image": "https://static01.nyt.com/bestsellers/images/9780593441299.jpg",
            "amazon_product_url": "https://www.amazon.com/dp/059344129X?tag=thenewyorktim-20",
            "age_group": "",
            "book_review_link": "",
            "sunday_review_link": ""
          }
        ]
      }
    ]
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized request. Make sure api-key is set. | `ApiException` |
| 429 | Too many requests. You reached your per minute or per day rate limit. | `ApiException` |

