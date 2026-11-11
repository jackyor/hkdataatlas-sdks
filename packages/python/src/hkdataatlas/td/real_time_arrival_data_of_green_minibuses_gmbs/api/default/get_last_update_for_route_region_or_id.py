from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_last_update_for_route_region_or_id_region_type_0 import (
    GetLastUpdateForRouteRegionOrIdRegionType0,
)
from ...models.last_update_single_response import LastUpdateSingleResponse
from ...types import Response


def _get_kwargs(
    region: GetLastUpdateForRouteRegionOrIdRegionType0 | int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/last-update/route/{region}".format(
            region=quote(str(region), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | LastUpdateSingleResponse | None:
    if response.status_code == 200:
        response_200 = LastUpdateSingleResponse.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | LastUpdateSingleResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    region: GetLastUpdateForRouteRegionOrIdRegionType0 | int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | LastUpdateSingleResponse]:
    """Retrieve last-update date by region or route ID

     The source documents both /last-update/route/{region} and /last-update/route/{route_id}. These have
    the same path hierarchy and are represented with one required segment. Supply a region abbreviation
    for the region form, or a route ID for the route-ID form; the source does not specify the mechanism
    that distinguishes them.

    Args:
        region (GetLastUpdateForRouteRegionOrIdRegionType0 | int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | LastUpdateSingleResponse]
    """

    kwargs = _get_kwargs(
        region=region,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    region: GetLastUpdateForRouteRegionOrIdRegionType0 | int,
    *,
    client: AuthenticatedClient | Client,
) -> Any | LastUpdateSingleResponse | None:
    """Retrieve last-update date by region or route ID

     The source documents both /last-update/route/{region} and /last-update/route/{route_id}. These have
    the same path hierarchy and are represented with one required segment. Supply a region abbreviation
    for the region form, or a route ID for the route-ID form; the source does not specify the mechanism
    that distinguishes them.

    Args:
        region (GetLastUpdateForRouteRegionOrIdRegionType0 | int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | LastUpdateSingleResponse
    """

    return sync_detailed(
        region=region,
        client=client,
    ).parsed


async def asyncio_detailed(
    region: GetLastUpdateForRouteRegionOrIdRegionType0 | int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | LastUpdateSingleResponse]:
    """Retrieve last-update date by region or route ID

     The source documents both /last-update/route/{region} and /last-update/route/{route_id}. These have
    the same path hierarchy and are represented with one required segment. Supply a region abbreviation
    for the region form, or a route ID for the route-ID form; the source does not specify the mechanism
    that distinguishes them.

    Args:
        region (GetLastUpdateForRouteRegionOrIdRegionType0 | int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | LastUpdateSingleResponse]
    """

    kwargs = _get_kwargs(
        region=region,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    region: GetLastUpdateForRouteRegionOrIdRegionType0 | int,
    *,
    client: AuthenticatedClient | Client,
) -> Any | LastUpdateSingleResponse | None:
    """Retrieve last-update date by region or route ID

     The source documents both /last-update/route/{region} and /last-update/route/{route_id}. These have
    the same path hierarchy and are represented with one required segment. Supply a region abbreviation
    for the region form, or a route ID for the route-ID form; the source does not specify the mechanism
    that distinguishes them.

    Args:
        region (GetLastUpdateForRouteRegionOrIdRegionType0 | int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | LastUpdateSingleResponse
    """

    return (
        await asyncio_detailed(
            region=region,
            client=client,
        )
    ).parsed
