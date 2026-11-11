from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_citybus_route_stops_company_id import (
    GetCitybusRouteStopsCompanyId,
)
from ...models.get_citybus_route_stops_direction import (
    GetCitybusRouteStopsDirection,
)
from ...models.get_citybus_route_stops_response import GetCitybusRouteStopsResponse
from ...types import Response


def _get_kwargs(
    company_id: GetCitybusRouteStopsCompanyId,
    route: str,
    direction: GetCitybusRouteStopsDirection,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/transport/citybus/route-stop/{company_id}/{route}/{direction}".format(
            company_id=quote(str(company_id), safe=""),
            route=quote(str(route), safe=""),
            direction=quote(str(direction), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | GetCitybusRouteStopsResponse | None:
    if response.status_code == 200:
        response_200 = GetCitybusRouteStopsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 422:
        response_422 = response.json()
        return response_422

    if response.status_code == 429:
        response_429 = response.json()
        return response_429

    if response.status_code == 500:
        response_500 = response.json()
        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | GetCitybusRouteStopsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    company_id: GetCitybusRouteStopsCompanyId,
    route: str,
    direction: GetCitybusRouteStopsDirection,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetCitybusRouteStopsResponse]:
    """Route stops

    Args:
        company_id (GetCitybusRouteStopsCompanyId):
        route (str):
        direction (GetCitybusRouteStopsDirection):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetCitybusRouteStopsResponse]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        route=route,
        direction=direction,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    company_id: GetCitybusRouteStopsCompanyId,
    route: str,
    direction: GetCitybusRouteStopsDirection,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetCitybusRouteStopsResponse | None:
    """Route stops

    Args:
        company_id (GetCitybusRouteStopsCompanyId):
        route (str):
        direction (GetCitybusRouteStopsDirection):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetCitybusRouteStopsResponse
    """

    return sync_detailed(
        company_id=company_id,
        route=route,
        direction=direction,
        client=client,
    ).parsed


async def asyncio_detailed(
    company_id: GetCitybusRouteStopsCompanyId,
    route: str,
    direction: GetCitybusRouteStopsDirection,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetCitybusRouteStopsResponse]:
    """Route stops

    Args:
        company_id (GetCitybusRouteStopsCompanyId):
        route (str):
        direction (GetCitybusRouteStopsDirection):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetCitybusRouteStopsResponse]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        route=route,
        direction=direction,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: GetCitybusRouteStopsCompanyId,
    route: str,
    direction: GetCitybusRouteStopsDirection,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetCitybusRouteStopsResponse | None:
    """Route stops

    Args:
        company_id (GetCitybusRouteStopsCompanyId):
        route (str):
        direction (GetCitybusRouteStopsDirection):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetCitybusRouteStopsResponse
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            route=route,
            direction=direction,
            client=client,
        )
    ).parsed
