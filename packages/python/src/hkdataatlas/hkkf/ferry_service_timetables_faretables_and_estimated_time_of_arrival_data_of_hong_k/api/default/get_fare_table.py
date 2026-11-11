from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_fare_table_route_id import (
    GetFareTableRouteId,
)
from ...types import Response


def _get_kwargs(
    route_id: GetFareTableRouteId,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/opendata/fare_table/{route_id}".format(
            route_id=quote(str(route_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> str | None:
    if response.status_code == 200:
        response_200 = response.text
        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    route_id: GetFareTableRouteId,
    *,
    client: AuthenticatedClient | Client,
) -> Response[str]:
    """Get route fare table

     Returns the corresponding fare table for Monday to Saturday and public holidays in CSV format.
    Documented route IDs are 1 (Central Pier 4–Sok Kwu Wan), 2 (Central Pier 4–Yung Shue Wan), 3
    (Central Pier 6–Peng Chau), and 4 (Peng Chau–Hei Ling Chau). The companion dictionary identifies
    ticket types and fare values but does not provide a complete CSV layout.

    Args:
        route_id (GetFareTableRouteId):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[str]
    """

    kwargs = _get_kwargs(
        route_id=route_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    route_id: GetFareTableRouteId,
    *,
    client: AuthenticatedClient | Client,
) -> str | None:
    """Get route fare table

     Returns the corresponding fare table for Monday to Saturday and public holidays in CSV format.
    Documented route IDs are 1 (Central Pier 4–Sok Kwu Wan), 2 (Central Pier 4–Yung Shue Wan), 3
    (Central Pier 6–Peng Chau), and 4 (Peng Chau–Hei Ling Chau). The companion dictionary identifies
    ticket types and fare values but does not provide a complete CSV layout.

    Args:
        route_id (GetFareTableRouteId):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        str
    """

    return sync_detailed(
        route_id=route_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    route_id: GetFareTableRouteId,
    *,
    client: AuthenticatedClient | Client,
) -> Response[str]:
    """Get route fare table

     Returns the corresponding fare table for Monday to Saturday and public holidays in CSV format.
    Documented route IDs are 1 (Central Pier 4–Sok Kwu Wan), 2 (Central Pier 4–Yung Shue Wan), 3
    (Central Pier 6–Peng Chau), and 4 (Peng Chau–Hei Ling Chau). The companion dictionary identifies
    ticket types and fare values but does not provide a complete CSV layout.

    Args:
        route_id (GetFareTableRouteId):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[str]
    """

    kwargs = _get_kwargs(
        route_id=route_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    route_id: GetFareTableRouteId,
    *,
    client: AuthenticatedClient | Client,
) -> str | None:
    """Get route fare table

     Returns the corresponding fare table for Monday to Saturday and public holidays in CSV format.
    Documented route IDs are 1 (Central Pier 4–Sok Kwu Wan), 2 (Central Pier 4–Yung Shue Wan), 3
    (Central Pier 6–Peng Chau), and 4 (Peng Chau–Hei Ling Chau). The companion dictionary identifies
    ticket types and fare values but does not provide a complete CSV layout.

    Args:
        route_id (GetFareTableRouteId):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        str
    """

    return (
        await asyncio_detailed(
            route_id=route_id,
            client=client,
        )
    ).parsed
