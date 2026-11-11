from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.find_nearby_vehicles_unit import (
    FindNearbyVehiclesUnit,
)
from ...models.vehicle_list_response import VehicleListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    lat: float,
    lng: float,
    radius: int | Unset = 5,
    unit: FindNearbyVehiclesUnit | Unset = "km",
    count: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["lat"] = lat

    params["lng"] = lng

    params["radius"] = radius

    json_unit: str | Unset = UNSET
    if not isinstance(unit, Unset):
        json_unit = unit

    params["unit"] = json_unit

    params["count"] = count

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/webx/v1/vehicle/nearby",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | VehicleListResponse | None:
    if response.status_code == 200:
        response_200 = VehicleListResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | VehicleListResponse]:
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
    lng: float,
    radius: int | Unset = 5,
    unit: FindNearbyVehiclesUnit | Unset = "km",
    count: int | Unset = UNSET,
) -> Response[Any | VehicleListResponse]:
    """Find nearby vehicles

     Finds slim vehicles within a geographic radius from a given location. Results are sorted by distance
    ascending. Each record includes a distance field (as a string) indicating distance from the query
    center; the documented TaxiFleetTdSlimRecord schema does not specify that field's exact structure.

    Args:
        lat (float):
        lng (float):
        radius (int | Unset):  Default: 5.
        unit (FindNearbyVehiclesUnit | Unset):  Default: 'km'.
        count (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | VehicleListResponse]
    """

    kwargs = _get_kwargs(
        lat=lat,
        lng=lng,
        radius=radius,
        unit=unit,
        count=count,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    lat: float,
    lng: float,
    radius: int | Unset = 5,
    unit: FindNearbyVehiclesUnit | Unset = "km",
    count: int | Unset = UNSET,
) -> Any | VehicleListResponse | None:
    """Find nearby vehicles

     Finds slim vehicles within a geographic radius from a given location. Results are sorted by distance
    ascending. Each record includes a distance field (as a string) indicating distance from the query
    center; the documented TaxiFleetTdSlimRecord schema does not specify that field's exact structure.

    Args:
        lat (float):
        lng (float):
        radius (int | Unset):  Default: 5.
        unit (FindNearbyVehiclesUnit | Unset):  Default: 'km'.
        count (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | VehicleListResponse
    """

    return sync_detailed(
        client=client,
        lat=lat,
        lng=lng,
        radius=radius,
        unit=unit,
        count=count,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    lat: float,
    lng: float,
    radius: int | Unset = 5,
    unit: FindNearbyVehiclesUnit | Unset = "km",
    count: int | Unset = UNSET,
) -> Response[Any | VehicleListResponse]:
    """Find nearby vehicles

     Finds slim vehicles within a geographic radius from a given location. Results are sorted by distance
    ascending. Each record includes a distance field (as a string) indicating distance from the query
    center; the documented TaxiFleetTdSlimRecord schema does not specify that field's exact structure.

    Args:
        lat (float):
        lng (float):
        radius (int | Unset):  Default: 5.
        unit (FindNearbyVehiclesUnit | Unset):  Default: 'km'.
        count (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | VehicleListResponse]
    """

    kwargs = _get_kwargs(
        lat=lat,
        lng=lng,
        radius=radius,
        unit=unit,
        count=count,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    lat: float,
    lng: float,
    radius: int | Unset = 5,
    unit: FindNearbyVehiclesUnit | Unset = "km",
    count: int | Unset = UNSET,
) -> Any | VehicleListResponse | None:
    """Find nearby vehicles

     Finds slim vehicles within a geographic radius from a given location. Results are sorted by distance
    ascending. Each record includes a distance field (as a string) indicating distance from the query
    center; the documented TaxiFleetTdSlimRecord schema does not specify that field's exact structure.

    Args:
        lat (float):
        lng (float):
        radius (int | Unset):  Default: 5.
        unit (FindNearbyVehiclesUnit | Unset):  Default: 'km'.
        count (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | VehicleListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            lat=lat,
            lng=lng,
            radius=radius,
            unit=unit,
            count=count,
        )
    ).parsed
