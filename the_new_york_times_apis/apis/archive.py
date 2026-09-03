from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import ApiResult, AsyncRawClient, RawClient, RequestOptionsOrDict, SecuredRawResponse, json_decoder, param
from ..errors.get_archive_by_month_error import GetArchiveByMonthErrorBody, get_archive_by_month_error_mapper
from ..models.svc_archive_v1_json_response import SvcArchiveV1JsonResponse
from ..server.server import Server


class Archive:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ArchiveWithRawResponse(client, server, auth)

    def get_archive_by_month(
        self, *, year: int = 2018, month: int = 9, request_options: RequestOptionsOrDict | None = None
    ) -> SvcArchiveV1JsonResponse:
        """Pass in year and month and get back JSON with all articles for that month. The response can be big (~20
        megabytes) and contain thousands of articles, depending on the year and month.

        Args:
            year: Year: 1851-2019
            month: Year: 1-12
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An array of articles.

        Raises:
            ApiError: Unauthorized request, check api-key is set. Too many requests. You reached your per minute or per
                day rate limit. ``error`` is ``SvcArchiveV1Json401Error1 | RawError``."""
        return self._with_raw_response.get_archive_by_month(
            year=year, month=month, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> ArchiveWithRawResponse:
        return self._with_raw_response


class AsyncArchive:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncArchiveWithRawResponse(client, server, auth)

    async def get_archive_by_month(
        self, *, year: int = 2018, month: int = 9, request_options: RequestOptionsOrDict | None = None
    ) -> SvcArchiveV1JsonResponse:
        """Pass in year and month and get back JSON with all articles for that month. The response can be big (~20
        megabytes) and contain thousands of articles, depending on the year and month.

        Args:
            year: Year: 1851-2019
            month: Year: 1-12
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An array of articles.

        Raises:
            ApiError: Unauthorized request, check api-key is set. Too many requests. You reached your per minute or per
                day rate limit. ``error`` is ``SvcArchiveV1Json401Error1 | RawError``."""
        return (
            await self._with_raw_response.get_archive_by_month(year=year, month=month, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncArchiveWithRawResponse:
        return self._with_raw_response


class ArchiveWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_archive_by_month(
        self, *, year: int = 2018, month: int = 9, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SvcArchiveV1JsonResponse, GetArchiveByMonthErrorBody]:
        """Pass in year and month and get back JSON with all articles for that month. The response can be big (~20
        megabytes) and contain thousands of articles, depending on the year and month.

        Args:
            year: Year: 1851-2019
            month: Year: 1-12
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/svc/archive/v1/{year}/{month}.json"),
            path_params=[param[int]("year", year), param[int]("month", month)],
            auth_scheme=self._auth.apikey,
            decoder=json_decoder[SvcArchiveV1JsonResponse],
            error_mapper=get_archive_by_month_error_mapper,
            request_options=request_options,
        )


class AsyncArchiveWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_archive_by_month(
        self, *, year: int = 2018, month: int = 9, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SvcArchiveV1JsonResponse, GetArchiveByMonthErrorBody]:
        """Pass in year and month and get back JSON with all articles for that month. The response can be big (~20
        megabytes) and contain thousands of articles, depending on the year and month.

        Args:
            year: Year: 1851-2019
            month: Year: 1-12
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/svc/archive/v1/{year}/{month}.json"),
            path_params=[param[int]("year", year), param[int]("month", month)],
            auth_scheme=self._auth.apikey,
            decoder=json_decoder[SvcArchiveV1JsonResponse],
            error_mapper=get_archive_by_month_error_mapper,
            request_options=request_options,
        )
