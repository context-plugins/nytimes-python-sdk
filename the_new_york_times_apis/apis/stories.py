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
from ..errors.get_top_stories_by_section_error import (
    GetTopStoriesBySectionErrorBody,
    get_top_stories_by_section_error_mapper,
)
from ..models.enums.section import Section, SectionOrStr
from ..models.svc_topstories_v2_json_response import SvcTopstoriesV2JsonResponse
from ..server.server import Server


class Stories:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = StoriesWithRawResponse(client, server, auth)

    def get_top_stories_by_section(
        self, *, section: SectionOrStr = Section.HOME, request_options: RequestOptionsOrDict | None = None
    ) -> SvcTopstoriesV2JsonResponse:
        """The Top Stories API returns an array of articles currently on the specified section.

        Args:
            section: The section the story appears in.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An array of articles.

        Raises:
            ApiError: Unauthorized request. Make sure api-key is set. Too many requests. You reached your per minute or
                per day rate limit. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.get_top_stories_by_section(section=section, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> StoriesWithRawResponse:
        return self._with_raw_response


class AsyncStories:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncStoriesWithRawResponse(client, server, auth)

    async def get_top_stories_by_section(
        self, *, section: SectionOrStr = Section.HOME, request_options: RequestOptionsOrDict | None = None
    ) -> SvcTopstoriesV2JsonResponse:
        """The Top Stories API returns an array of articles currently on the specified section.

        Args:
            section: The section the story appears in.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An array of articles.

        Raises:
            ApiError: Unauthorized request. Make sure api-key is set. Too many requests. You reached your per minute or
                per day rate limit. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.get_top_stories_by_section(section=section, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> AsyncStoriesWithRawResponse:
        return self._with_raw_response


class StoriesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_top_stories_by_section(
        self, *, section: SectionOrStr = Section.HOME, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SvcTopstoriesV2JsonResponse, GetTopStoriesBySectionErrorBody]:
        """The Top Stories API returns an array of articles currently on the specified section.

        Args:
            section: The section the story appears in.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/svc/topstories/v2/{section}.json"),
            path_params=[param[SectionOrStr]("section", section)],
            auth_scheme=self._auth.apikey,
            decoder=json_decoder[SvcTopstoriesV2JsonResponse],
            error_mapper=get_top_stories_by_section_error_mapper,
            request_options=request_options,
        )


class AsyncStoriesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_top_stories_by_section(
        self, *, section: SectionOrStr = Section.HOME, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SvcTopstoriesV2JsonResponse, GetTopStoriesBySectionErrorBody]:
        """The Top Stories API returns an array of articles currently on the specified section.

        Args:
            section: The section the story appears in.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/svc/topstories/v2/{section}.json"),
            path_params=[param[SectionOrStr]("section", section)],
            auth_scheme=self._auth.apikey,
            decoder=async_json_decoder[SvcTopstoriesV2JsonResponse],
            error_mapper=get_top_stories_by_section_error_mapper,
            request_options=request_options,
        )
