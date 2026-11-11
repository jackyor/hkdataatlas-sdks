from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.eta_response import ETAResponse
from ...models.get_eta_direction import GetEtaDirection
from ...models.get_eta_route_id import GetEtaRouteId
from ...types import Response


def _get_kwargs(
    route_id: GetEtaRouteId,
    direction: GetEtaDirection,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/opendata/eta/{route_id}/{direction}".format(
            route_id=quote(str(route_id), safe=""),
            direction=quote(str(direction), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | ETAResponse | None:
    if response.status_code == 200:
        response_200 = ETAResponse.from_dict(response.json())

        return response_200

    if response.status_code == 422:
        response_422 = cast(Any, None)
        return response_422

    if response.status_code == 429:
        response_429 = cast(Any, None)
        return response_429

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | ETAResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    route_id: GetEtaRouteId,
    direction: GetEtaDirection,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | ETAResponse]:
    """Get estimated arrival times

     Returns estimated arrival time and direction information for running ferries on the specified route.
    Documented route IDs are 1 (Central Pier 4–Sok Kwu Wan), 2 (Central Pier 4–Yung Shue Wan), 3
    (Central Pier 6–Peng Chau), and 4 (Peng Chau–Hei Ling Chau). Valid directions are inbound (towards
    the origin; for example, Yung Shue Wan to Central Pier 4) and outbound (towards the destination).
    The companion dictionary declares data.route_id as a string, while the primary API sample represents
    it as a number; the schema permits either representation.

    Args:
        route_id (GetEtaRouteId):
        direction (GetEtaDirection):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ETAResponse]
    """

    kwargs = _get_kwargs(
        route_id=route_id,
        direction=direction,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    route_id: GetEtaRouteId,
    direction: GetEtaDirection,
    *,
    client: AuthenticatedClient | Client,
) -> Any | ETAResponse | None:
    """Get estimated arrival times

     Returns estimated arrival time and direction information for running ferries on the specified route.
    Documented route IDs are 1 (Central Pier 4–Sok Kwu Wan), 2 (Central Pier 4–Yung Shue Wan), 3
    (Central Pier 6–Peng Chau), and 4 (Peng Chau–Hei Ling Chau). Valid directions are inbound (towards
    the origin; for example, Yung Shue Wan to Central Pier 4) and outbound (towards the destination).
    The companion dictionary declares data.route_id as a string, while the primary API sample represents
    it as a number; the schema permits either representation.

    Args:
        route_id (GetEtaRouteId):
        direction (GetEtaDirection):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ETAResponse
    """

    return sync_detailed(
        route_id=route_id,
        direction=direction,
        client=client,
    ).parsed


async def asyncio_detailed(
    route_id: GetEtaRouteId,
    direction: GetEtaDirection,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | ETAResponse]:
    """Get estimated arrival times

     Returns estimated arrival time and direction information for running ferries on the specified route.
    Documented route IDs are 1 (Central Pier 4–Sok Kwu Wan), 2 (Central Pier 4–Yung Shue Wan), 3
    (Central Pier 6–Peng Chau), and 4 (Peng Chau–Hei Ling Chau). Valid directions are inbound (towards
    the origin; for example, Yung Shue Wan to Central Pier 4) and outbound (towards the destination).
    The companion dictionary declares data.route_id as a string, while the primary API sample represents
    it as a number; the schema permits either representation.

    Args:
        route_id (GetEtaRouteId):
        direction (GetEtaDirection):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ETAResponse]
    """

    kwargs = _get_kwargs(
        route_id=route_id,
        direction=direction,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    route_id: GetEtaRouteId,
    direction: GetEtaDirection,
    *,
    client: AuthenticatedClient | Client,
) -> Any | ETAResponse | None:
    """Get estimated arrival times

     Returns estimated arrival time and direction information for running ferries on the specified route.
    Documented route IDs are 1 (Central Pier 4–Sok Kwu Wan), 2 (Central Pier 4–Yung Shue Wan), 3
    (Central Pier 6–Peng Chau), and 4 (Peng Chau–Hei Ling Chau). Valid directions are inbound (towards
    the origin; for example, Yung Shue Wan to Central Pier 4) and outbound (towards the destination).
    The companion dictionary declares data.route_id as a string, while the primary API sample represents
    it as a number; the schema permits either representation.

    Args:
        route_id (GetEtaRouteId):
        direction (GetEtaDirection):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ETAResponse
    """

    return (
        await asyncio_detailed(
            route_id=route_id,
            direction=direction,
            client=client,
        )
    ).parsed
