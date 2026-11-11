from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_route_by_region_and_code_region import (
    GetRouteByRegionAndCodeRegion,
)
from ...models.route_response import RouteResponse
from ...types import Response


def _get_kwargs(
    region: GetRouteByRegionAndCodeRegion,
    route_code: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/route/{region}/{route_code}".format(
            region=quote(str(region), safe=""),
            route_code=quote(str(route_code), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> RouteResponse | None:
    if response.status_code == 200:
        response_200 = RouteResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[RouteResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    region: GetRouteByRegionAndCodeRegion,
    route_code: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RouteResponse]:
    """Retrieve route information by region and route code

     Accepts a region and route code and returns the respective route information. Route codes are unique
    within a region, but not across all regions.

    Args:
        region (GetRouteByRegionAndCodeRegion):
        route_code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RouteResponse]
    """

    kwargs = _get_kwargs(
        region=region,
        route_code=route_code,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    region: GetRouteByRegionAndCodeRegion,
    route_code: str,
    *,
    client: AuthenticatedClient | Client,
) -> RouteResponse | None:
    """Retrieve route information by region and route code

     Accepts a region and route code and returns the respective route information. Route codes are unique
    within a region, but not across all regions.

    Args:
        region (GetRouteByRegionAndCodeRegion):
        route_code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RouteResponse
    """

    return sync_detailed(
        region=region,
        route_code=route_code,
        client=client,
    ).parsed


async def asyncio_detailed(
    region: GetRouteByRegionAndCodeRegion,
    route_code: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RouteResponse]:
    """Retrieve route information by region and route code

     Accepts a region and route code and returns the respective route information. Route codes are unique
    within a region, but not across all regions.

    Args:
        region (GetRouteByRegionAndCodeRegion):
        route_code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RouteResponse]
    """

    kwargs = _get_kwargs(
        region=region,
        route_code=route_code,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    region: GetRouteByRegionAndCodeRegion,
    route_code: str,
    *,
    client: AuthenticatedClient | Client,
) -> RouteResponse | None:
    """Retrieve route information by region and route code

     Accepts a region and route code and returns the respective route information. Route codes are unique
    within a region, but not across all regions.

    Args:
        region (GetRouteByRegionAndCodeRegion):
        route_code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RouteResponse
    """

    return (
        await asyncio_detailed(
            region=region,
            route_code=route_code,
            client=client,
        )
    ).parsed
