from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_light_rail_next_train_schedule_with_special_type_0 import (
    GetLightRailNextTrainScheduleWithSpecialType0,
)
from ...models.get_light_rail_next_train_schedule_with_special_type_1 import (
    GetLightRailNextTrainScheduleWithSpecialType1,
)
from ...models.schedule_response import ScheduleResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    station_id: int,
    with_special: GetLightRailNextTrainScheduleWithSpecialType0
    | GetLightRailNextTrainScheduleWithSpecialType1
    | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["station_id"] = station_id

    json_with_special: int | Unset
    if isinstance(with_special, Unset):
        json_with_special = UNSET
    elif isinstance(with_special, int):
        json_with_special = with_special
    else:
        json_with_special = with_special

    params["with_special"] = json_with_special

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/getSchedule",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | ScheduleResponse | None:
    if response.status_code == 200:
        response_200 = ScheduleResponse.from_dict(response.json())

        return response_200

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
) -> Response[Any | ScheduleResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    station_id: int,
    with_special: GetLightRailNextTrainScheduleWithSpecialType0
    | GetLightRailNextTrainScheduleWithSpecialType1
    | Unset = UNSET,
) -> Response[Any | ScheduleResponse]:
    """Get Light Rail next train schedule

     Returns train arrival schedule information for the selected Light Rail station. When with_special is
    omitted, only regular routes are returned.

    Args:
        station_id (int):
        with_special (GetLightRailNextTrainScheduleWithSpecialType0 |
            GetLightRailNextTrainScheduleWithSpecialType1 | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ScheduleResponse]
    """

    kwargs = _get_kwargs(
        station_id=station_id,
        with_special=with_special,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    station_id: int,
    with_special: GetLightRailNextTrainScheduleWithSpecialType0
    | GetLightRailNextTrainScheduleWithSpecialType1
    | Unset = UNSET,
) -> Any | ScheduleResponse | None:
    """Get Light Rail next train schedule

     Returns train arrival schedule information for the selected Light Rail station. When with_special is
    omitted, only regular routes are returned.

    Args:
        station_id (int):
        with_special (GetLightRailNextTrainScheduleWithSpecialType0 |
            GetLightRailNextTrainScheduleWithSpecialType1 | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ScheduleResponse
    """

    return sync_detailed(
        client=client,
        station_id=station_id,
        with_special=with_special,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    station_id: int,
    with_special: GetLightRailNextTrainScheduleWithSpecialType0
    | GetLightRailNextTrainScheduleWithSpecialType1
    | Unset = UNSET,
) -> Response[Any | ScheduleResponse]:
    """Get Light Rail next train schedule

     Returns train arrival schedule information for the selected Light Rail station. When with_special is
    omitted, only regular routes are returned.

    Args:
        station_id (int):
        with_special (GetLightRailNextTrainScheduleWithSpecialType0 |
            GetLightRailNextTrainScheduleWithSpecialType1 | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ScheduleResponse]
    """

    kwargs = _get_kwargs(
        station_id=station_id,
        with_special=with_special,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    station_id: int,
    with_special: GetLightRailNextTrainScheduleWithSpecialType0
    | GetLightRailNextTrainScheduleWithSpecialType1
    | Unset = UNSET,
) -> Any | ScheduleResponse | None:
    """Get Light Rail next train schedule

     Returns train arrival schedule information for the selected Light Rail station. When with_special is
    omitted, only regular routes are returned.

    Args:
        station_id (int):
        with_special (GetLightRailNextTrainScheduleWithSpecialType0 |
            GetLightRailNextTrainScheduleWithSpecialType1 | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ScheduleResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            station_id=station_id,
            with_special=with_special,
        )
    ).parsed
