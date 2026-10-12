from __future__ import annotations

from functools import cached_property
from types import TracebackType

from typing_extensions import Self

from .apis.archive import AsyncArchive
from .apis.books import AsyncBooks
from .apis.most_popular import AsyncMostPopular
from .apis.rss import AsyncRss
from .apis.search import AsyncSearch
from .apis.stories import AsyncStories
from .auth import AsyncAuthSchemes
from .base_client import DEFAULT_TIMEOUT, BaseTheNewYorkTimesApisClient
from .core import (
    OPERATING_SYSTEM,
    PYTHON_RUNTIME,
    ApiKeyQueryScheme,
    AsyncHttpClient,
    AsyncHttpx2Client,
    AsyncRawClient,
    RetryOptionsOrDict,
    no_auth,
    param,
)


class AsyncTheNewYorkTimesApisClient(BaseTheNewYorkTimesApisClient[AsyncRawClient]):
    def __init__(
        self,
        *,
        base_url: str | None = None,
        timeout: float = DEFAULT_TIMEOUT,
        retry_options: int | RetryOptionsOrDict | None = None,
        custom_async_http_client: AsyncHttpClient | None = None,
        apikey: str | None = None,
    ) -> None:
        super().__init__(base_url=base_url, timeout=timeout, retry_options=retry_options)
        self._raw_client = AsyncRawClient(
            http_client=(
                custom_async_http_client if custom_async_http_client is not None else AsyncHttpx2Client(timeout=timeout)
            ),
            retry_options=self._retry_options,
            global_headers=[
                param[str]("User-Agent", "TheNewYorkTimesApisClient/1.0.0 Python"),
                param[str]("X-APIMatic-Lang", "Python"),
                param[str]("X-APIMatic-Package-Version", "1.0.0"),
                param[str]("X-APIMatic-Gen-Version", "4.0.0"),
                param[str]("X-APIMatic-OS", OPERATING_SYSTEM),
                param[str]("X-APIMatic-Runtime", PYTHON_RUNTIME),
            ],
        )
        self._auth = AsyncAuthSchemes(apikey=ApiKeyQueryScheme("api-key", apikey) if apikey is not None else no_auth)

    @cached_property
    def archive(self) -> AsyncArchive:
        return AsyncArchive(self._raw_client, self._server, self._auth)

    @cached_property
    def books(self) -> AsyncBooks:
        return AsyncBooks(self._raw_client, self._server, self._auth)

    @cached_property
    def most_popular(self) -> AsyncMostPopular:
        return AsyncMostPopular(self._raw_client, self._server, self._auth)

    @cached_property
    def rss(self) -> AsyncRss:
        return AsyncRss(self._raw_client, self._server)

    @cached_property
    def search(self) -> AsyncSearch:
        return AsyncSearch(self._raw_client, self._server, self._auth)

    @cached_property
    def stories(self) -> AsyncStories:
        return AsyncStories(self._raw_client, self._server, self._auth)

    async def aclose(self) -> None:
        await self._raw_client.http_client.aclose()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        await self.aclose()


AsyncClient = AsyncTheNewYorkTimesApisClient
