from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.taxi_fleet_response import TaxiFleetResponse
from ...models.validation_error import ValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    lat: float,
    long: float,
    range_: int | Unset = 2000,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["lat"] = lat

    params["long"] = long

    params["range"] = range_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/opendata/get_data/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | TaxiFleetResponse | ValidationError | None:
    if response.status_code == 200:
        response_200 = TaxiFleetResponse.from_dict(response.json())

        return response_200

    if response.status_code == 422:
        response_422 = ValidationError.from_dict(response.json())

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
) -> Response[Any | TaxiFleetResponse | ValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    lat: float,
    long: float,
    range_: int | Unset = 2000,
) -> Response[Any | TaxiFleetResponse | ValidationError]:
    """Get vehicles within radius

     Returns vehicles within a specified distance of the given WGS84 coordinate. The range defaults to
    2000 metres when omitted.

    Args:
        lat (float):
        long (float):
        range_ (int | Unset):  Default: 2000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | TaxiFleetResponse | ValidationError]
    """

    kwargs = _get_kwargs(
        lat=lat,
        long=long,
        range_=range_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    lat: float,
    long: float,
    range_: int | Unset = 2000,
) -> Any | TaxiFleetResponse | ValidationError | None:
    """Get vehicles within radius

     Returns vehicles within a specified distance of the given WGS84 coordinate. The range defaults to
    2000 metres when omitted.

    Args:
        lat (float):
        long (float):
        range_ (int | Unset):  Default: 2000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | TaxiFleetResponse | ValidationError
    """

    return sync_detailed(
        client=client,
        lat=lat,
        long=long,
        range_=range_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    lat: float,
    long: float,
    range_: int | Unset = 2000,
) -> Response[Any | TaxiFleetResponse | ValidationError]:
    """Get vehicles within radius

     Returns vehicles within a specified distance of the given WGS84 coordinate. The range defaults to
    2000 metres when omitted.

    Args:
        lat (float):
        long (float):
        range_ (int | Unset):  Default: 2000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | TaxiFleetResponse | ValidationError]
    """

    kwargs = _get_kwargs(
        lat=lat,
        long=long,
        range_=range_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    lat: float,
    long: float,
    range_: int | Unset = 2000,
) -> Any | TaxiFleetResponse | ValidationError | None:
    """Get vehicles within radius

     Returns vehicles within a specified distance of the given WGS84 coordinate. The range defaults to
    2000 metres when omitted.

    Args:
        lat (float):
        long (float):
        range_ (int | Unset):  Default: 2000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | TaxiFleetResponse | ValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            lat=lat,
            long=long,
            range_=range_,
        )
    ).parsed
