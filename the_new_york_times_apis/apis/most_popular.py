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
from ..errors.get_most_emailed_articles_error import (
    GetMostEmailedArticlesErrorBody,
    get_most_emailed_articles_error_mapper,
)
from ..errors.get_most_shared_articles_by_type_error import (
    GetMostSharedArticlesByTypeErrorBody,
    get_most_shared_articles_by_type_error_mapper,
)
from ..errors.get_most_shared_articles_error import (
    GetMostSharedArticlesErrorBody,
    get_most_shared_articles_error_mapper,
)
from ..errors.get_most_viewed_articles_error import (
    GetMostViewedArticlesErrorBody,
    get_most_viewed_articles_error_mapper,
)
from ..models.enums.period import Period, PeriodOrInt
from ..models.enums.share_type import ShareType, ShareTypeOrStr
from ..models.svc_mostpopular_v2_emailed_json_response import SvcMostpopularV2EmailedJsonResponse
from ..models.svc_mostpopular_v2_shared_json_response import SvcMostpopularV2SharedJsonResponse
from ..models.svc_mostpopular_v2_viewed_json_response import SvcMostpopularV2ViewedJsonResponse
from ..server.server import Server


class MostPopular:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = MostPopularWithRawResponse(client, server, auth)

    def get_most_emailed_articles(
        self, *, period: PeriodOrInt = Period.VALUE_1, request_options: RequestOptionsOrDict | None = None
    ) -> SvcMostpopularV2EmailedJsonResponse:
        """Returns an array of the most emailed articles on NYTimes.com for specified period of time (1 day, 7 days, or
        30 days).

        Args:
            period: Time period: 1, 7, or 30 days.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An array of articles.

        Raises:
            ApiError: Unauthorized request. Make sure api-key is set. Too many requests. You reached your per minute or
                per day rate limit. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.get_most_emailed_articles(period=period, request_options=request_options))

    def get_most_shared_articles(
        self, *, period: PeriodOrInt = Period.VALUE_1, request_options: RequestOptionsOrDict | None = None
    ) -> SvcMostpopularV2SharedJsonResponse:
        """Returns an array of the most shared articles on NYTimes.com for specified period of time (1 day, 7 days, or
        30 days).

        Args:
            period: Time period: 1, 7, or 30 days.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An array of articles.

        Raises:
            ApiError: Unauthorized request. Make sure api-key is set. Too many requests. You reached your per minute or
                per day rate limit. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.get_most_shared_articles(period=period, request_options=request_options))

    def get_most_shared_articles_by_type(
        self,
        *,
        period: PeriodOrInt = Period.VALUE_1,
        share_type: ShareTypeOrStr = ShareType.FACEBOOK,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SvcMostpopularV2SharedJsonResponse:
        """Returns an array of the most shared articles by share type on NYTimes.com for specified period of time (1
        day, 7 days, or 30 days).

        Args:
            period: Time period: 1, 7, or 30 days.
            share_type: Share type: facebook.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An array of articles.

        Raises:
            ApiError: Unauthorized request. Make sure api-key is set. Too many requests. You reached your per minute or
                per day rate limit. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.get_most_shared_articles_by_type(
                period=period, share_type=share_type, request_options=request_options
            ),
        )

    def get_most_viewed_articles(
        self, *, period: PeriodOrInt = Period.VALUE_1, request_options: RequestOptionsOrDict | None = None
    ) -> SvcMostpopularV2ViewedJsonResponse:
        """Returns an array of the most viewed articles on NYTimes.com for specified period of time (1 day, 7 days, or
        30 days).

        Args:
            period: Time period: 1, 7, or 30 days.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An array of articles.

        Raises:
            ApiError: Unauthorized request. Make sure api-key is set. Too many requests. You reached your per minute or
                per day rate limit. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.get_most_viewed_articles(period=period, request_options=request_options))

    @property
    def with_raw_response(self) -> MostPopularWithRawResponse:
        return self._with_raw_response


class AsyncMostPopular:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncMostPopularWithRawResponse(client, server, auth)

    async def get_most_emailed_articles(
        self, *, period: PeriodOrInt = Period.VALUE_1, request_options: RequestOptionsOrDict | None = None
    ) -> SvcMostpopularV2EmailedJsonResponse:
        """Returns an array of the most emailed articles on NYTimes.com for specified period of time (1 day, 7 days, or
        30 days).

        Args:
            period: Time period: 1, 7, or 30 days.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An array of articles.

        Raises:
            ApiError: Unauthorized request. Make sure api-key is set. Too many requests. You reached your per minute or
                per day rate limit. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.get_most_emailed_articles(period=period, request_options=request_options)
        )

    async def get_most_shared_articles(
        self, *, period: PeriodOrInt = Period.VALUE_1, request_options: RequestOptionsOrDict | None = None
    ) -> SvcMostpopularV2SharedJsonResponse:
        """Returns an array of the most shared articles on NYTimes.com for specified period of time (1 day, 7 days, or
        30 days).

        Args:
            period: Time period: 1, 7, or 30 days.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An array of articles.

        Raises:
            ApiError: Unauthorized request. Make sure api-key is set. Too many requests. You reached your per minute or
                per day rate limit. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.get_most_shared_articles(period=period, request_options=request_options)
        )

    async def get_most_shared_articles_by_type(
        self,
        *,
        period: PeriodOrInt = Period.VALUE_1,
        share_type: ShareTypeOrStr = ShareType.FACEBOOK,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SvcMostpopularV2SharedJsonResponse:
        """Returns an array of the most shared articles by share type on NYTimes.com for specified period of time (1
        day, 7 days, or 30 days).

        Args:
            period: Time period: 1, 7, or 30 days.
            share_type: Share type: facebook.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An array of articles.

        Raises:
            ApiError: Unauthorized request. Make sure api-key is set. Too many requests. You reached your per minute or
                per day rate limit. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.get_most_shared_articles_by_type(
                period=period, share_type=share_type, request_options=request_options
            ),
        )

    async def get_most_viewed_articles(
        self, *, period: PeriodOrInt = Period.VALUE_1, request_options: RequestOptionsOrDict | None = None
    ) -> SvcMostpopularV2ViewedJsonResponse:
        """Returns an array of the most viewed articles on NYTimes.com for specified period of time (1 day, 7 days, or
        30 days).

        Args:
            period: Time period: 1, 7, or 30 days.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An array of articles.

        Raises:
            ApiError: Unauthorized request. Make sure api-key is set. Too many requests. You reached your per minute or
                per day rate limit. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.get_most_viewed_articles(period=period, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> AsyncMostPopularWithRawResponse:
        return self._with_raw_response


class MostPopularWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_most_emailed_articles(
        self, *, period: PeriodOrInt = Period.VALUE_1, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SvcMostpopularV2EmailedJsonResponse, GetMostEmailedArticlesErrorBody]:
        """Returns an array of the most emailed articles on NYTimes.com for specified period of time (1 day, 7 days, or
        30 days).

        Args:
            period: Time period: 1, 7, or 30 days.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/svc/mostpopular/v2/emailed/{period}.json"),
            path_params=[param[PeriodOrInt]("period", period)],
            auth_scheme=self._auth.apikey,
            decoder=json_decoder[SvcMostpopularV2EmailedJsonResponse],
            error_mapper=get_most_emailed_articles_error_mapper,
            request_options=request_options,
        )

    def get_most_shared_articles(
        self, *, period: PeriodOrInt = Period.VALUE_1, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SvcMostpopularV2SharedJsonResponse, GetMostSharedArticlesErrorBody]:
        """Returns an array of the most shared articles on NYTimes.com for specified period of time (1 day, 7 days, or
        30 days).

        Args:
            period: Time period: 1, 7, or 30 days.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/svc/mostpopular/v2/shared/{period}.json"),
            path_params=[param[PeriodOrInt]("period", period)],
            auth_scheme=self._auth.apikey,
            decoder=json_decoder[SvcMostpopularV2SharedJsonResponse],
            error_mapper=get_most_shared_articles_error_mapper,
            request_options=request_options,
        )

    def get_most_shared_articles_by_type(
        self,
        *,
        period: PeriodOrInt = Period.VALUE_1,
        share_type: ShareTypeOrStr = ShareType.FACEBOOK,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SvcMostpopularV2SharedJsonResponse, GetMostSharedArticlesByTypeErrorBody]:
        """Returns an array of the most shared articles by share type on NYTimes.com for specified period of time (1
        day, 7 days, or 30 days).

        Args:
            period: Time period: 1, 7, or 30 days.
            share_type: Share type: facebook.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/svc/mostpopular/v2/shared/{period}/{share_type}.json"),
            path_params=[param[PeriodOrInt]("period", period), param[ShareTypeOrStr]("share_type", share_type)],
            auth_scheme=self._auth.apikey,
            decoder=json_decoder[SvcMostpopularV2SharedJsonResponse],
            error_mapper=get_most_shared_articles_by_type_error_mapper,
            request_options=request_options,
        )

    def get_most_viewed_articles(
        self, *, period: PeriodOrInt = Period.VALUE_1, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SvcMostpopularV2ViewedJsonResponse, GetMostViewedArticlesErrorBody]:
        """Returns an array of the most viewed articles on NYTimes.com for specified period of time (1 day, 7 days, or
        30 days).

        Args:
            period: Time period: 1, 7, or 30 days.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/svc/mostpopular/v2/viewed/{period}.json"),
            path_params=[param[PeriodOrInt]("period", period)],
            auth_scheme=self._auth.apikey,
            decoder=json_decoder[SvcMostpopularV2ViewedJsonResponse],
            error_mapper=get_most_viewed_articles_error_mapper,
            request_options=request_options,
        )


class AsyncMostPopularWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_most_emailed_articles(
        self, *, period: PeriodOrInt = Period.VALUE_1, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SvcMostpopularV2EmailedJsonResponse, GetMostEmailedArticlesErrorBody]:
        """Returns an array of the most emailed articles on NYTimes.com for specified period of time (1 day, 7 days, or
        30 days).

        Args:
            period: Time period: 1, 7, or 30 days.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/svc/mostpopular/v2/emailed/{period}.json"),
            path_params=[param[PeriodOrInt]("period", period)],
            auth_scheme=self._auth.apikey,
            decoder=async_json_decoder[SvcMostpopularV2EmailedJsonResponse],
            error_mapper=get_most_emailed_articles_error_mapper,
            request_options=request_options,
        )

    async def get_most_shared_articles(
        self, *, period: PeriodOrInt = Period.VALUE_1, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SvcMostpopularV2SharedJsonResponse, GetMostSharedArticlesErrorBody]:
        """Returns an array of the most shared articles on NYTimes.com for specified period of time (1 day, 7 days, or
        30 days).

        Args:
            period: Time period: 1, 7, or 30 days.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/svc/mostpopular/v2/shared/{period}.json"),
            path_params=[param[PeriodOrInt]("period", period)],
            auth_scheme=self._auth.apikey,
            decoder=async_json_decoder[SvcMostpopularV2SharedJsonResponse],
            error_mapper=get_most_shared_articles_error_mapper,
            request_options=request_options,
        )

    async def get_most_shared_articles_by_type(
        self,
        *,
        period: PeriodOrInt = Period.VALUE_1,
        share_type: ShareTypeOrStr = ShareType.FACEBOOK,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SvcMostpopularV2SharedJsonResponse, GetMostSharedArticlesByTypeErrorBody]:
        """Returns an array of the most shared articles by share type on NYTimes.com for specified period of time (1
        day, 7 days, or 30 days).

        Args:
            period: Time period: 1, 7, or 30 days.
            share_type: Share type: facebook.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/svc/mostpopular/v2/shared/{period}/{share_type}.json"),
            path_params=[param[PeriodOrInt]("period", period), param[ShareTypeOrStr]("share_type", share_type)],
            auth_scheme=self._auth.apikey,
            decoder=async_json_decoder[SvcMostpopularV2SharedJsonResponse],
            error_mapper=get_most_shared_articles_by_type_error_mapper,
            request_options=request_options,
        )

    async def get_most_viewed_articles(
        self, *, period: PeriodOrInt = Period.VALUE_1, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SvcMostpopularV2ViewedJsonResponse, GetMostViewedArticlesErrorBody]:
        """Returns an array of the most viewed articles on NYTimes.com for specified period of time (1 day, 7 days, or
        30 days).

        Args:
            period: Time period: 1, 7, or 30 days.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/svc/mostpopular/v2/viewed/{period}.json"),
            path_params=[param[PeriodOrInt]("period", period)],
            auth_scheme=self._auth.apikey,
            decoder=async_json_decoder[SvcMostpopularV2ViewedJsonResponse],
            error_mapper=get_most_viewed_articles_error_mapper,
            request_options=request_options,
        )
