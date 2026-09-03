from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import ApiResult, AsyncRawClient, RawClient, RequestOptionsOrDict, SecuredRawResponse, json_decoder, param
from ..errors.search_articles_error import SearchArticlesErrorBody, search_articles_error_mapper
from ..models.enums.sort import SortOrStr
from ..models.svc_search_v2_articlesearch_json_response import SvcSearchV2ArticlesearchJsonResponse
from ..server.server import Server


class Search:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SearchWithRawResponse(client, server, auth)

    def search_articles(
        self,
        *,
        begin_date: str | None = None,
        end_date: str | None = None,
        fq: str | None = None,
        page: int | None = None,
        q: str | None = None,
        sort: SortOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SvcSearchV2ArticlesearchJsonResponse:
        """Search for NYT articles by keywords and filters.

        Args:
            begin_date: Begin date (e.g. 20120101)
            end_date: End date (e.g. 20121231)
            fq: Filter query
            page: Page number (0, 1, ...)
            q: Query
            sort: Sort order
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An array of articles.

        Raises:
            ApiError: Bad request. Check your query parameters. Unauthorized request. Make sure api-key is set. Too many
                requests. You reached your per minute or per day rate limit. ``error`` is ``RawError``."""
        return self._with_raw_response.search_articles(
            begin_date=begin_date, end_date=end_date, fq=fq, page=page, q=q, sort=sort, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> SearchWithRawResponse:
        return self._with_raw_response


class AsyncSearch:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSearchWithRawResponse(client, server, auth)

    async def search_articles(
        self,
        *,
        begin_date: str | None = None,
        end_date: str | None = None,
        fq: str | None = None,
        page: int | None = None,
        q: str | None = None,
        sort: SortOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SvcSearchV2ArticlesearchJsonResponse:
        """Search for NYT articles by keywords and filters.

        Args:
            begin_date: Begin date (e.g. 20120101)
            end_date: End date (e.g. 20121231)
            fq: Filter query
            page: Page number (0, 1, ...)
            q: Query
            sort: Sort order
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An array of articles.

        Raises:
            ApiError: Bad request. Check your query parameters. Unauthorized request. Make sure api-key is set. Too many
                requests. You reached your per minute or per day rate limit. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.search_articles(
                begin_date=begin_date,
                end_date=end_date,
                fq=fq,
                page=page,
                q=q,
                sort=sort,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncSearchWithRawResponse:
        return self._with_raw_response


class SearchWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def search_articles(
        self,
        *,
        begin_date: str | None = None,
        end_date: str | None = None,
        fq: str | None = None,
        page: int | None = None,
        q: str | None = None,
        sort: SortOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SvcSearchV2ArticlesearchJsonResponse, SearchArticlesErrorBody]:
        """Search for NYT articles by keywords and filters.

        Args:
            begin_date: Begin date (e.g. 20120101)
            end_date: End date (e.g. 20121231)
            fq: Filter query
            page: Page number (0, 1, ...)
            q: Query
            sort: Sort order
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/svc/search/v2/articlesearch.json"),
            query_params=[
                param[str | None]("begin_date", begin_date),
                param[str | None]("end_date", end_date),
                param[str | None]("fq", fq),
                param[int | None]("page", page),
                param[str | None]("q", q),
                param[SortOrStr | None]("sort", sort),
            ],
            auth_scheme=self._auth.apikey,
            decoder=json_decoder[SvcSearchV2ArticlesearchJsonResponse],
            error_mapper=search_articles_error_mapper,
            request_options=request_options,
        )


class AsyncSearchWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def search_articles(
        self,
        *,
        begin_date: str | None = None,
        end_date: str | None = None,
        fq: str | None = None,
        page: int | None = None,
        q: str | None = None,
        sort: SortOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SvcSearchV2ArticlesearchJsonResponse, SearchArticlesErrorBody]:
        """Search for NYT articles by keywords and filters.

        Args:
            begin_date: Begin date (e.g. 20120101)
            end_date: End date (e.g. 20121231)
            fq: Filter query
            page: Page number (0, 1, ...)
            q: Query
            sort: Sort order
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/svc/search/v2/articlesearch.json"),
            query_params=[
                param[str | None]("begin_date", begin_date),
                param[str | None]("end_date", end_date),
                param[str | None]("fq", fq),
                param[int | None]("page", page),
                param[str | None]("q", q),
                param[SortOrStr | None]("sort", sort),
            ],
            auth_scheme=self._auth.apikey,
            decoder=json_decoder[SvcSearchV2ArticlesearchJsonResponse],
            error_mapper=search_articles_error_mapper,
            request_options=request_options,
        )
