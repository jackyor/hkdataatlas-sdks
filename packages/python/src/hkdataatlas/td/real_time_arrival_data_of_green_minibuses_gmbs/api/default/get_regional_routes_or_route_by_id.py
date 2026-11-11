from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_regional_routes_or_route_by_id_region_type_0 import (
    GetRegionalRoutesOrRouteByIdRegionType0,
)
from ...models.route_response import RouteResponse
from ...models.routes_regional_response import RoutesRegionalResponse
from ...types import Response


def _get_kwargs(
    region: GetRegionalRoutesOrRouteByIdRegionType0 | int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/route/{region}".format(
            region=quote(str(region), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RouteResponse | RoutesRegionalResponse | None:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> RouteResponse | RoutesRegionalResponse:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = RoutesRegionalResponse.from_dict(data)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = RouteResponse.from_dict(data)

            return response_200_type_1

        response_200 = _parse_response_200(response.json())

        return response_200

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RouteResponse | RoutesRegionalResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    region: GetRegionalRoutesOrRouteByIdRegionType0 | int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | RouteResponse | RoutesRegionalResponse]:
    """List regional routes or retrieve route information by ID

     The source documents GET /route/{region} for regional route listing and GET /route/{route_id} for
    route information by ID. OpenAPI cannot distinguish these identical single-segment templates by
    parameter name, so the segment is represented as `region`. Supply a region abbreviation for the
    regional-list form or a route ID for the route-by-ID form. The specification does not explain how
    the service distinguishes the forms beyond the path value.

    Args:
        region (GetRegionalRoutesOrRouteByIdRegionType0 | int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RouteResponse | RoutesRegionalResponse]
    """

    kwargs = _get_kwargs(
        region=region,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    region: GetRegionalRoutesOrRouteByIdRegionType0 | int,
    *,
    client: AuthenticatedClient | Client,
) -> Any | RouteResponse | RoutesRegionalResponse | None:
    """List regional routes or retrieve route information by ID

     The source documents GET /route/{region} for regional route listing and GET /route/{route_id} for
    route information by ID. OpenAPI cannot distinguish these identical single-segment templates by
    parameter name, so the segment is represented as `region`. Supply a region abbreviation for the
    regional-list form or a route ID for the route-by-ID form. The specification does not explain how
    the service distinguishes the forms beyond the path value.

    Args:
        region (GetRegionalRoutesOrRouteByIdRegionType0 | int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RouteResponse | RoutesRegionalResponse
    """

    return sync_detailed(
        region=region,
        client=client,
    ).parsed


async def asyncio_detailed(
    region: GetRegionalRoutesOrRouteByIdRegionType0 | int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | RouteResponse | RoutesRegionalResponse]:
    """List regional routes or retrieve route information by ID

     The source documents GET /route/{region} for regional route listing and GET /route/{route_id} for
    route information by ID. OpenAPI cannot distinguish these identical single-segment templates by
    parameter name, so the segment is represented as `region`. Supply a region abbreviation for the
    regional-list form or a route ID for the route-by-ID form. The specification does not explain how
    the service distinguishes the forms beyond the path value.

    Args:
        region (GetRegionalRoutesOrRouteByIdRegionType0 | int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RouteResponse | RoutesRegionalResponse]
    """

    kwargs = _get_kwargs(
        region=region,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    region: GetRegionalRoutesOrRouteByIdRegionType0 | int,
    *,
    client: AuthenticatedClient | Client,
) -> Any | RouteResponse | RoutesRegionalResponse | None:
    """List regional routes or retrieve route information by ID

     The source documents GET /route/{region} for regional route listing and GET /route/{route_id} for
    route information by ID. OpenAPI cannot distinguish these identical single-segment templates by
    parameter name, so the segment is represented as `region`. Supply a region abbreviation for the
    regional-list form or a route ID for the route-by-ID form. The specification does not explain how
    the service distinguishes the forms beyond the path value.

    Args:
        region (GetRegionalRoutesOrRouteByIdRegionType0 | int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RouteResponse | RoutesRegionalResponse
    """

    return (
        await asyncio_detailed(
            region=region,
            client=client,
        )
    ).parsed
