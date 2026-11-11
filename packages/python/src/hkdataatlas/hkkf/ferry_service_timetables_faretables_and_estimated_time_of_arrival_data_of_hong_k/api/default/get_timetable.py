from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_timetable_route_id import (
    GetTimetableRouteId,
)
from ...types import Response


def _get_kwargs(
    route_id: GetTimetableRouteId,
    direction: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/opendata/time_table/{route_id}/{direction}".format(
            route_id=quote(str(route_id), safe=""),
            direction=quote(str(direction), safe=""),
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
    route_id: GetTimetableRouteId,
    direction: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[str]:
    """Get route timetable

     Returns the latest respective route timetable information in CSV format. Documented route IDs are 1
    (Central Pier 4–Sok Kwu Wan), 2 (Central Pier 4–Yung Shue Wan), 3 (Central Pier 6–Peng Chau), and 4
    (Peng Chau–Hei Ling Chau). The direction parameter is required; the specification does not establish
    an exhaustive set of allowed values.

    Args:
        route_id (GetTimetableRouteId):
        direction (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[str]
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
    route_id: GetTimetableRouteId,
    direction: str,
    *,
    client: AuthenticatedClient | Client,
) -> str | None:
    """Get route timetable

     Returns the latest respective route timetable information in CSV format. Documented route IDs are 1
    (Central Pier 4–Sok Kwu Wan), 2 (Central Pier 4–Yung Shue Wan), 3 (Central Pier 6–Peng Chau), and 4
    (Peng Chau–Hei Ling Chau). The direction parameter is required; the specification does not establish
    an exhaustive set of allowed values.

    Args:
        route_id (GetTimetableRouteId):
        direction (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        str
    """

    return sync_detailed(
        route_id=route_id,
        direction=direction,
        client=client,
    ).parsed


async def asyncio_detailed(
    route_id: GetTimetableRouteId,
    direction: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[str]:
    """Get route timetable

     Returns the latest respective route timetable information in CSV format. Documented route IDs are 1
    (Central Pier 4–Sok Kwu Wan), 2 (Central Pier 4–Yung Shue Wan), 3 (Central Pier 6–Peng Chau), and 4
    (Peng Chau–Hei Ling Chau). The direction parameter is required; the specification does not establish
    an exhaustive set of allowed values.

    Args:
        route_id (GetTimetableRouteId):
        direction (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[str]
    """

    kwargs = _get_kwargs(
        route_id=route_id,
        direction=direction,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    route_id: GetTimetableRouteId,
    direction: str,
    *,
    client: AuthenticatedClient | Client,
) -> str | None:
    """Get route timetable

     Returns the latest respective route timetable information in CSV format. Documented route IDs are 1
    (Central Pier 4–Sok Kwu Wan), 2 (Central Pier 4–Yung Shue Wan), 3 (Central Pier 6–Peng Chau), and 4
    (Peng Chau–Hei Ling Chau). The direction parameter is required; the specification does not establish
    an exhaustive set of allowed values.

    Args:
        route_id (GetTimetableRouteId):
        direction (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        str
    """

    return (
        await asyncio_detailed(
            route_id=route_id,
            direction=direction,
            client=client,
        )
    ).parsed
