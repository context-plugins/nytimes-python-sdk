from __future__ import annotations

from ..core import (
    ApiResult,
    AsyncRawClient,
    BaseRawResponse,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    async_empty_response,
    empty_response,
    param,
    raw_error_response,
    unwrap,
)
from ..models.enums.section1 import Section1, Section1OrStr
from ..server.server import Server


class Rss:
    def __init__(self, client: RawClient, server: Server) -> None:
        self._with_raw_response = RssWithRawResponse(client, server)

    def get_section_feed(
        self, *, section: Section1OrStr = Section1.HOME_PAGE, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Given section name, return lists of articles ranked on the section front.

        Args:
            section: Section name (Arts, Africa, Americas, ...).
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A list of articles.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.get_section_feed(section=section, request_options=request_options))

    @property
    def with_raw_response(self) -> RssWithRawResponse:
        return self._with_raw_response


class AsyncRss:
    def __init__(self, client: AsyncRawClient, server: Server) -> None:
        self._with_raw_response = AsyncRssWithRawResponse(client, server)

    async def get_section_feed(
        self, *, section: Section1OrStr = Section1.HOME_PAGE, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Given section name, return lists of articles ranked on the section front.

        Args:
            section: Section name (Arts, Africa, Americas, ...).
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A list of articles.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.get_section_feed(section=section, request_options=request_options))

    @property
    def with_raw_response(self) -> AsyncRssWithRawResponse:
        return self._with_raw_response


class RssWithRawResponse(BaseRawResponse[RawClient, Server]):
    def get_section_feed(
        self, *, section: Section1OrStr = Section1.HOME_PAGE, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Given section name, return lists of articles ranked on the section front.

        Args:
            section: Section name (Arts, Africa, Americas, ...).
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/services/xml/rss/nyt/{section}.xml"),
            path_params=[param[Section1OrStr]("section", section)],
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncRssWithRawResponse(BaseRawResponse[AsyncRawClient, Server]):
    async def get_section_feed(
        self, *, section: Section1OrStr = Section1.HOME_PAGE, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, RawError]:
        """Given section name, return lists of articles ranked on the section front.

        Args:
            section: Section name (Arts, Africa, Americas, ...).
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/services/xml/rss/nyt/{section}.xml"),
            path_params=[param[Section1OrStr]("section", section)],
            decoder=async_empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )
