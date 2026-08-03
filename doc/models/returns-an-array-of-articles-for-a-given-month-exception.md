
# Returns an Array of Articles for a Given Month Exception

*This model accepts additional fields of type Any.*

## Structure

`ReturnsAnArrayOfArticlesForAGivenMonthException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `fault` | [`Fault`](../../doc/models/fault.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
try:
    # make the API call
except ReturnsAnArrayOfArticlesForAGivenMonthException as e:
    print(e)
except ApiException as e:
    print(e)
```

