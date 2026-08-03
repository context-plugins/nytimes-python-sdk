
# Custom Query Parameter



Documentation for accessing and setting credentials for apikey.

## Auth Credentials

| Name | Type | Description | Getter |
|  --- | --- | --- | --- |
| api-key | `str` | - | `api_key` |



**Note:** Auth credentials can be set using `CustomQueryAuthenticationCredentials` object, passed in as named parameter `custom_query_authentication_credentials` in the client initialization.

## Usage Example

### Client Initialization

You must provide credentials in the client as shown in the following code snippet.

```python
from nytimes.http.auth.custom_query_authentication import CustomQueryAuthenticationCredentials
from nytimes.nytimes_client import NytimesClient

client = NytimesClient(
    custom_query_authentication_credentials=CustomQueryAuthenticationCredentials(
        api_key='api-key'
    )
)
```


