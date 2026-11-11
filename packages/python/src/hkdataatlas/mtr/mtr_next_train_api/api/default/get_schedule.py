from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_schedule_lang import GetScheduleLang
from ...models.get_schedule_line import GetScheduleLine
from ...models.schedule_response import ScheduleResponse
from ...models.service_arrangement_response import ServiceArrangementResponse
from ...models.suspended_station_response import SuspendedStationResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    line: GetScheduleLine,
    sta: str,
    lang: GetScheduleLang | Unset = "EN",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_line: str = line
    params["line"] = json_line

    params["sta"] = sta

    json_lang: str | Unset = UNSET
    if not isinstance(lang, Unset):
        json_lang = lang

    params["lang"] = json_lang

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/getSchedule.php",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> (
    Any
    | ScheduleResponse
    | ServiceArrangementResponse
    | SuspendedStationResponse
    | None
):
    if response.status_code == 200:

        def _parse_response_200(
            data: object,
        ) -> ScheduleResponse | ServiceArrangementResponse | SuspendedStationResponse:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = ScheduleResponse.from_dict(data)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_1 = ServiceArrangementResponse.from_dict(data)

                return response_200_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_2 = SuspendedStationResponse.from_dict(data)

            return response_200_type_2

        response_200 = _parse_response_200(response.json())

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
) -> Response[
    Any | ScheduleResponse | ServiceArrangementResponse | SuspendedStationResponse
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    line: GetScheduleLine,
    sta: str,
    lang: GetScheduleLang | Unset = "EN",
) -> Response[
    Any | ScheduleResponse | ServiceArrangementResponse | SuspendedStationResponse
]:
    """Get train schedule

     Returns train arrival schedule data. A valid result is returned only when the combination of line
    and station is correct. The station availability table in the specification and data dictionary
    differs in some details; the parameter descriptions preserve the documented associations without
    asserting that they are exhaustive. The response may instead describe a special train service
    arrangement, data absence, or a suspended station.

    Args:
        line (GetScheduleLine):
        sta (str):
        lang (GetScheduleLang | Unset):  Default: 'EN'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ScheduleResponse | ServiceArrangementResponse | SuspendedStationResponse]
    """

    kwargs = _get_kwargs(
        line=line,
        sta=sta,
        lang=lang,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    line: GetScheduleLine,
    sta: str,
    lang: GetScheduleLang | Unset = "EN",
) -> (
    Any
    | ScheduleResponse
    | ServiceArrangementResponse
    | SuspendedStationResponse
    | None
):
    """Get train schedule

     Returns train arrival schedule data. A valid result is returned only when the combination of line
    and station is correct. The station availability table in the specification and data dictionary
    differs in some details; the parameter descriptions preserve the documented associations without
    asserting that they are exhaustive. The response may instead describe a special train service
    arrangement, data absence, or a suspended station.

    Args:
        line (GetScheduleLine):
        sta (str):
        lang (GetScheduleLang | Unset):  Default: 'EN'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ScheduleResponse | ServiceArrangementResponse | SuspendedStationResponse
    """

    return sync_detailed(
        client=client,
        line=line,
        sta=sta,
        lang=lang,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    line: GetScheduleLine,
    sta: str,
    lang: GetScheduleLang | Unset = "EN",
) -> Response[
    Any | ScheduleResponse | ServiceArrangementResponse | SuspendedStationResponse
]:
    """Get train schedule

     Returns train arrival schedule data. A valid result is returned only when the combination of line
    and station is correct. The station availability table in the specification and data dictionary
    differs in some details; the parameter descriptions preserve the documented associations without
    asserting that they are exhaustive. The response may instead describe a special train service
    arrangement, data absence, or a suspended station.

    Args:
        line (GetScheduleLine):
        sta (str):
        lang (GetScheduleLang | Unset):  Default: 'EN'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ScheduleResponse | ServiceArrangementResponse | SuspendedStationResponse]
    """

    kwargs = _get_kwargs(
        line=line,
        sta=sta,
        lang=lang,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    line: GetScheduleLine,
    sta: str,
    lang: GetScheduleLang | Unset = "EN",
) -> (
    Any
    | ScheduleResponse
    | ServiceArrangementResponse
    | SuspendedStationResponse
    | None
):
    """Get train schedule

     Returns train arrival schedule data. A valid result is returned only when the combination of line
    and station is correct. The station availability table in the specification and data dictionary
    differs in some details; the parameter descriptions preserve the documented associations without
    asserting that they are exhaustive. The response may instead describe a special train service
    arrangement, data absence, or a suspended station.

    Args:
        line (GetScheduleLine):
        sta (str):
        lang (GetScheduleLang | Unset):  Default: 'EN'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ScheduleResponse | ServiceArrangementResponse | SuspendedStationResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            line=line,
            sta=sta,
            lang=lang,
        )
    ).parsed
