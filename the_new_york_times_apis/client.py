from __future__ import annotations

from functools import cached_property
from types import TracebackType

from typing_extensions import Self

from .apis.archive import Archive
from .apis.books import Books
from .apis.most_popular import MostPopular
from .apis.rss import Rss
from .apis.search import Search
from .apis.stories import Stories
from .auth import AuthSchemes
from .base_client import DEFAULT_TIMEOUT, BaseTheNewYorkTimesApisClient
from .core import (
    OPERATING_SYSTEM,
    PYTHON_RUNTIME,
    ApiKeyQueryScheme,
    HttpClient,
    Httpx2Client,
    RawClient,
    RetryOptionsOrDict,
    no_auth,
    param,
)


class TheNewYorkTimesApisClient(BaseTheNewYorkTimesApisClient[RawClient]):
    def __init__(
        self,
        *,
        base_url: str | None = None,
        timeout: float = DEFAULT_TIMEOUT,
        retry_options: int | RetryOptionsOrDict | None = None,
        custom_http_client: HttpClient | None = None,
        apikey: str | None = None,
    ) -> None:
        super().__init__(base_url=base_url, timeout=timeout, retry_options=retry_options)
        self._raw_client = RawClient(
            http_client=custom_http_client if custom_http_client is not None else Httpx2Client(timeout=timeout),
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
        self._auth = AuthSchemes(apikey=ApiKeyQueryScheme("api-key", apikey) if apikey is not None else no_auth)

    @cached_property
    def archive(self) -> Archive:
        return Archive(self._raw_client, self._server, self._auth)

    @cached_property
    def books(self) -> Books:
        return Books(self._raw_client, self._server, self._auth)

    @cached_property
    def most_popular(self) -> MostPopular:
        return MostPopular(self._raw_client, self._server, self._auth)

    @cached_property
    def rss(self) -> Rss:
        return Rss(self._raw_client, self._server)

    @cached_property
    def search(self) -> Search:
        return Search(self._raw_client, self._server, self._auth)

    @cached_property
    def stories(self) -> Stories:
        return Stories(self._raw_client, self._server, self._auth)

    def close(self) -> None:
        self._raw_client.http_client.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        self.close()


Client = TheNewYorkTimesApisClient
