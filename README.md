# The New York Times APIs SDK

[![Built with APIMatic][apimatic-badge]][apimatic-url] [![License: MIT][license-badge]][license-url] [![Python 3.10+][python-badge]][python-url]

The The New York Times APIs SDK for Python provides access to the [The New York Times APIs REST APIs](https://developer.nytimes.com/apis) from Python applications.

> [!TIP]
> **Looking for a specific signature, model, enum, or error type?** This SDK ships a generated
> **[SDK map](sdk-map.md)** -- a lookup index of the SDK's entire Python surface. Consult it before
> scanning the source tree; details under [SDK map](#sdk-map).

The New York Times developer platform is made up of several independent APIs. This document is the
entry point for all of them: it declares the shared server, the shared API-key security scheme and
the tags that group the endpoints, and then links every operation with a JSON Reference (`$ref`) to
the specification file that owns it. No endpoint is duplicated here - the individual API files stay
the single source of truth.

| API | Version | Base path | Specification file |
| --- | --- | --- | --- |
| Article Search | 2.0.0 | `/svc/search/v2` | [`articlesearch/articlesearch-product.yaml`](./articlesearch/articlesearch-product.yaml) |
| Archive | 2.0.0 | `/svc/archive/v1` | [`archive/archive-product.yaml`](./archive/archive-product.yaml) |
| Top Stories | 2.0.0 | `/svc/topstories/v2` | [`top-stories/top-stories-product.yaml`](./top-stories/top-stories-product.yaml) |
| Most Popular | 2.0.0 | `/svc/mostpopular/v2` | [`most-popular/most-popular-product.yaml`](./most-popular/most-popular-product.yaml) |
| Books | 3.0.0 | `/svc/books/v3` | [`books/books-product.yaml`](./books/books-product.yaml) |
| RSS | 2.0.0 | `/services/xml/rss/nyt` | [`rss/rss-api.yaml`](./rss/rss-api.yaml) |

## Authentication

Every API except the RSS feeds requires an API key, passed as the `api-key` query parameter. Create
one at <https://developer.nytimes.com/my-apps>. Rate limits are enforced per key and per API.


---

## Installation

Install the Python SDK from PyPI, with whichever package manager your project uses:

```bash
pip install the-new-york-times-apis
```

```bash
uv add the-new-york-times-apis
```

```bash
poetry add the-new-york-times-apis
```

---

## Quick Start

### Synchronous client

Construct `TheNewYorkTimesApisClient` with keyword arguments, and call `close()` when you are done. Every argument is optional; the full list is in the [SDK map](sdk-map.md).

```python
from the_new_york_times_apis import TheNewYorkTimesApisClient

client = TheNewYorkTimesApisClient(apikey="YOUR_API_KEY")

# TODO: call endpoints here -- see api-reference.md

client.close()
```

Alternatively, scope it -- `with TheNewYorkTimesApisClient(...) as client:` closes the pool on exit; see [Best Practices](#best-practices).

`Client` is exported as an alias of `TheNewYorkTimesApisClient`, so `from the_new_york_times_apis import Client` also works.

The SDK accepts every model-typed input in two interchangeable spellings, both type-checked: the typed model, or a plain dict with the same keys -- the `OrDict` and `Model | ModelDict` unions in the [SDK map](sdk-map.md). Pick whichever suits the call site: the dict form needs no import, while the model form adds a keyword-checked constructor and editor completion.

### Asynchronous client

`AsyncTheNewYorkTimesApisClient` mirrors `TheNewYorkTimesApisClient` with **identical method names**, and every endpoint method is a coroutine. It takes the same arguments, with some differences -- for example, the transport argument is `custom_async_http_client`.

```python
from asyncio import run

from the_new_york_times_apis import AsyncTheNewYorkTimesApisClient


async def main() -> None:
    client = AsyncTheNewYorkTimesApisClient(apikey="YOUR_API_KEY")
    # TODO: call endpoints here, awaiting each -- see api-reference.md
    await client.aclose()


run(main())
```

Alternatively, scope it -- `async with AsyncTheNewYorkTimesApisClient(...) as client:` closes the pool on exit. Only the async spelling is `aclose`, matching httpx; see [Best Practices](#best-practices).

`AsyncClient` is the exported alias. Each client accepts **only** its own transport argument; passing the other's is a `TypeError` at runtime and an error under mypy.

---

## Usage

Two generated references cover the SDK; each answers a different question:

| Reference | For |
| --- | --- |
| **[API Reference](api-reference.md)** | Usage guidance for a single **parsed** operation: `client.<group>.<operation>(...)` returns the typed payload and raises `ApiError` on any non-2xx, with `.error` the typed error body, or `RawError` for a status the operation does not document. |
| **[Raw API Reference](raw-api-reference.md)** | The same for the **raw** variant: `client.<group>.with_raw_response.<operation>(...)` returns `ApiResult[T, E]` and never raises for an API error. |

Both API references carry every one of the 10 operations, with a sync and an async sample and a parameter table each.

## SDK map

This SDK ships a generated **SDK map** -- [`sdk-map.md`](sdk-map.md) -- a deterministic, lookup-oriented table of contents of the SDK's Python surface, generated by APIMatic alongside this SDK.

Consult the map before scanning or grepping the source: it answers call-level contract questions by lookup, and for anything it does not carry -- model shapes, enum values, an endpoint's route or behavioural prose -- it names the one source file to read. How to read the map itself, including the SDK-wide defaults its rows rely on, is stated at the top of [`sdk-map.md`](sdk-map.md).

## Best Practices

> [!TIP]
> Use a **single `TheNewYorkTimesApisClient` instance** for the lifetime of your application and reuse it across
> all requests. Each instance owns its own connection pool, so an instance per request forfeits
> connection reuse and leaks pools that are never closed.

Match the disposal to the client's lifetime: an application-lifetime client is closed once at shutdown with `close()` / `aclose()`; where the lifetime fits a block, `with TheNewYorkTimesApisClient() as client:` / `async with AsyncTheNewYorkTimesApisClient() as client:` releases it automatically. Both are idempotent, but a closed client is not reusable: the next call raises. The client closes **whatever transport it holds**, including one you supplied via `custom_http_client` / `custom_async_http_client`; if you intend to reuse your own transport across clients, don't hand its lifetime to a `with` block.

## License

This SDK is distributed under the [MIT License][license-url].

---

## Support

Refer to the [API reference](api-reference.md) for detailed information on available operations with code samples.

For further assistance, please contact support at code@nytimes.com.

---

[license-url]: LICENSE
[license-badge]: https://img.shields.io/badge/License-MIT-blue.svg
[apimatic-url]: https://www.apimatic.io
[apimatic-badge]: https://www.apimatic.io/hubfs/Built-with-APIMatic-badge.svg
[python-url]: https://www.python.org/downloads/
[python-badge]: https://img.shields.io/badge/python-3.10%2B-blue.svg
