from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_execution_error import ApiExecutionError
from ...models.error import Error
from ...models.get_route_stops_direction import (
    GetRouteStopsDirection,
)
from ...models.route_stop_response import RouteStopResponse
from ...types import Response


def _get_kwargs(
    route: str,
    direction: GetRouteStopsDirection,
    service_type: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/transport/kmb/route-stop/{route}/{direction}/{service_type}".format(
            route=quote(str(route), safe=""),
            direction=quote(str(direction), safe=""),
            service_type=quote(str(service_type), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ApiExecutionError | Error | RouteStopResponse | None:
    if response.status_code == 200:
        response_200 = RouteStopResponse.from_dict(response.json())

        return response_200

    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = ApiExecutionError.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ApiExecutionError | Error | RouteStopResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    route: str,
    direction: GetRouteStopsDirection,
    service_type: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ApiExecutionError | Error | RouteStopResponse]:
    """Get stops for a route

     Returns stop information for the specified route, direction, and service type. Updated daily at
    05:00. Route number and direction are case-sensitive.

    Args:
        route (str):
        direction (GetRouteStopsDirection):
        service_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiExecutionError | Error | RouteStopResponse]
    """

    kwargs = _get_kwargs(
        route=route,
        direction=direction,
        service_type=service_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    route: str,
    direction: GetRouteStopsDirection,
    service_type: str,
    *,
    client: AuthenticatedClient | Client,
) -> ApiExecutionError | Error | RouteStopResponse | None:
    """Get stops for a route

     Returns stop information for the specified route, direction, and service type. Updated daily at
    05:00. Route number and direction are case-sensitive.

    Args:
        route (str):
        direction (GetRouteStopsDirection):
        service_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiExecutionError | Error | RouteStopResponse
    """

    return sync_detailed(
        route=route,
        direction=direction,
        service_type=service_type,
        client=client,
    ).parsed


async def asyncio_detailed(
    route: str,
    direction: GetRouteStopsDirection,
    service_type: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ApiExecutionError | Error | RouteStopResponse]:
    """Get stops for a route

     Returns stop information for the specified route, direction, and service type. Updated daily at
    05:00. Route number and direction are case-sensitive.

    Args:
        route (str):
        direction (GetRouteStopsDirection):
        service_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiExecutionError | Error | RouteStopResponse]
    """

    kwargs = _get_kwargs(
        route=route,
        direction=direction,
        service_type=service_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    route: str,
    direction: GetRouteStopsDirection,
    service_type: str,
    *,
    client: AuthenticatedClient | Client,
) -> ApiExecutionError | Error | RouteStopResponse | None:
    """Get stops for a route

     Returns stop information for the specified route, direction, and service type. Updated daily at
    05:00. Route number and direction are case-sensitive.

    Args:
        route (str):
        direction (GetRouteStopsDirection):
        service_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiExecutionError | Error | RouteStopResponse
    """

    return (
        await asyncio_detailed(
            route=route,
            direction=direction,
            service_type=service_type,
            client=client,
        )
    ).parsed
