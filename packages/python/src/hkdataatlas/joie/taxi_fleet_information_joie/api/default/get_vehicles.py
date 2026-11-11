from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.vehicle_collection import VehicleCollection
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/vehicles",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> VehicleCollection | None:
    if response.status_code == 200:
        response_200 = VehicleCollection.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[VehicleCollection]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[VehicleCollection]:
    """Get public taxi fleet data

     Provides public taxi fleet data for data.gov.hk and open data. The endpoint is expected to be behind
    the Transport Department's CDN for caching and shall not be exposed directly to end users. Consumers
    shall not poll it more frequently than once every 30 seconds.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[VehicleCollection]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> VehicleCollection | None:
    """Get public taxi fleet data

     Provides public taxi fleet data for data.gov.hk and open data. The endpoint is expected to be behind
    the Transport Department's CDN for caching and shall not be exposed directly to end users. Consumers
    shall not poll it more frequently than once every 30 seconds.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        VehicleCollection
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[VehicleCollection]:
    """Get public taxi fleet data

     Provides public taxi fleet data for data.gov.hk and open data. The endpoint is expected to be behind
    the Transport Department's CDN for caching and shall not be exposed directly to end users. Consumers
    shall not poll it more frequently than once every 30 seconds.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[VehicleCollection]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> VehicleCollection | None:
    """Get public taxi fleet data

     Provides public taxi fleet data for data.gov.hk and open data. The endpoint is expected to be behind
    the Transport Department's CDN for caching and shall not be exposed directly to end users. Consumers
    shall not poll it more frequently than once every 30 seconds.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        VehicleCollection
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
