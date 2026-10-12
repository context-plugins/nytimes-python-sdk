from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    async_json_decoder,
    json_decoder,
    param,
    unwrap,
)
from ..errors.get_lists_date_list_json_error import GetListsDateListJsonErrorBody, get_lists_date_list_json_error_mapper
from ..errors.get_lists_overview_json_error import GetListsOverviewJsonErrorBody, get_lists_overview_json_error_mapper
from ..models.list_response import ListResponse
from ..models.overview_response import OverviewResponse
from ..server.server import Server


class Books:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = BooksWithRawResponse(client, server, auth)

    def get_lists_date_list_json(
        self, date: str, list_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ListResponse:
        """Get Best Sellers data for a given list name and date.

        Args:
            date: YYYY-MM-DD or "current" The date the best sellers list was in the print `The New York Times Book
                Review <https://www.nytimes.com/section/books/review>`__. Use "current" to get latest list.
            list_: Name of the Best Sellers List (e.g. hardcover-fiction). You can get the list of names from the
                /lists/overview.json service.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Best Sellers list books.

        Raises:
            ApiError: Unauthorized request. Make sure api-key is set. Too many requests. You reached your per minute or
                per day rate limit. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.get_lists_date_list_json(date, list_, request_options=request_options))

    def get_lists_overview_json(
        self, *, published_date: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> OverviewResponse:
        """Get all books for all the Best Sellers lists for specified print date.

        Args:
            published_date: YYYY-MM-DD The overview published date when the list was or will be in the print `The New
                York Times Book Review <https://www.nytimes.com/section/books/review>`__.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Overview of Best Sellers lists.

        Raises:
            ApiError: Unauthorized request. Make sure api-key is set. Too many requests. You reached your per minute or
                per day rate limit. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.get_lists_overview_json(
                published_date=published_date, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> BooksWithRawResponse:
        return self._with_raw_response


class AsyncBooks:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncBooksWithRawResponse(client, server, auth)

    async def get_lists_date_list_json(
        self, date: str, list_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ListResponse:
        """Get Best Sellers data for a given list name and date.

        Args:
            date: YYYY-MM-DD or "current" The date the best sellers list was in the print `The New York Times Book
                Review <https://www.nytimes.com/section/books/review>`__. Use "current" to get latest list.
            list_: Name of the Best Sellers List (e.g. hardcover-fiction). You can get the list of names from the
                /lists/overview.json service.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Best Sellers list books.

        Raises:
            ApiError: Unauthorized request. Make sure api-key is set. Too many requests. You reached your per minute or
                per day rate limit. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.get_lists_date_list_json(date, list_, request_options=request_options)
        )

    async def get_lists_overview_json(
        self, *, published_date: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> OverviewResponse:
        """Get all books for all the Best Sellers lists for specified print date.

        Args:
            published_date: YYYY-MM-DD The overview published date when the list was or will be in the print `The New
                York Times Book Review <https://www.nytimes.com/section/books/review>`__.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Overview of Best Sellers lists.

        Raises:
            ApiError: Unauthorized request. Make sure api-key is set. Too many requests. You reached your per minute or
                per day rate limit. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.get_lists_overview_json(
                published_date=published_date, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncBooksWithRawResponse:
        return self._with_raw_response


class BooksWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_lists_date_list_json(
        self, date: str, list_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ListResponse, GetListsDateListJsonErrorBody]:
        """Get Best Sellers data for a given list name and date.

        Args:
            date: YYYY-MM-DD or "current" The date the best sellers list was in the print `The New York Times Book
                Review <https://www.nytimes.com/section/books/review>`__. Use "current" to get latest list.
            list_: Name of the Best Sellers List (e.g. hardcover-fiction). You can get the list of names from the
                /lists/overview.json service.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/svc/books/v3/lists/{date}/{list}.json"),
            path_params=[param[str]("date", date), param[str]("list", list_)],
            auth_scheme=self._auth.apikey,
            decoder=json_decoder[ListResponse],
            error_mapper=get_lists_date_list_json_error_mapper,
            request_options=request_options,
        )

    def get_lists_overview_json(
        self, *, published_date: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[OverviewResponse, GetListsOverviewJsonErrorBody]:
        """Get all books for all the Best Sellers lists for specified print date.

        Args:
            published_date: YYYY-MM-DD The overview published date when the list was or will be in the print `The New
                York Times Book Review <https://www.nytimes.com/section/books/review>`__.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/svc/books/v3/lists/overview.json"),
            query_params=[param[str | None]("published_date", published_date)],
            auth_scheme=self._auth.apikey,
            decoder=json_decoder[OverviewResponse],
            error_mapper=get_lists_overview_json_error_mapper,
            request_options=request_options,
        )


class AsyncBooksWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_lists_date_list_json(
        self, date: str, list_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ListResponse, GetListsDateListJsonErrorBody]:
        """Get Best Sellers data for a given list name and date.

        Args:
            date: YYYY-MM-DD or "current" The date the best sellers list was in the print `The New York Times Book
                Review <https://www.nytimes.com/section/books/review>`__. Use "current" to get latest list.
            list_: Name of the Best Sellers List (e.g. hardcover-fiction). You can get the list of names from the
                /lists/overview.json service.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/svc/books/v3/lists/{date}/{list}.json"),
            path_params=[param[str]("date", date), param[str]("list", list_)],
            auth_scheme=self._auth.apikey,
            decoder=async_json_decoder[ListResponse],
            error_mapper=get_lists_date_list_json_error_mapper,
            request_options=request_options,
        )

    async def get_lists_overview_json(
        self, *, published_date: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[OverviewResponse, GetListsOverviewJsonErrorBody]:
        """Get all books for all the Best Sellers lists for specified print date.

        Args:
            published_date: YYYY-MM-DD The overview published date when the list was or will be in the print `The New
                York Times Book Review <https://www.nytimes.com/section/books/review>`__.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/svc/books/v3/lists/overview.json"),
            query_params=[param[str | None]("published_date", published_date)],
            auth_scheme=self._auth.apikey,
            decoder=async_json_decoder[OverviewResponse],
            error_mapper=get_lists_overview_json_error_mapper,
            request_options=request_options,
        )
