from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_hourly_rainfall_lang import (
    GetHourlyRainfallLang,
)
from ...models.hourly_rainfall_report import HourlyRainfallReport
from ...types import UNSET, Response


def _get_kwargs(
    *,
    lang: GetHourlyRainfallLang = "en",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_lang: str = lang
    params["lang"] = json_lang

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/hourlyRainfall.php",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> HourlyRainfallReport | None:
    if response.status_code == 200:
        response_200 = HourlyRainfallReport.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[HourlyRainfallReport]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    lang: GetHourlyRainfallLang = "en",
) -> Response[HourlyRainfallReport]:
    """Rainfall in the past hour from automatic weather stations

     Rainfall measured during the one-hour period ending at observation time. Data are provisional and
    have undergone only limited validation. Rainfall for the Hong Kong Observatory station in this
    dataset differs from the official climatological database and other weather bulletins.

    Args:
        lang (GetHourlyRainfallLang):  Default: 'en'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HourlyRainfallReport]
    """

    kwargs = _get_kwargs(
        lang=lang,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    lang: GetHourlyRainfallLang = "en",
) -> HourlyRainfallReport | None:
    """Rainfall in the past hour from automatic weather stations

     Rainfall measured during the one-hour period ending at observation time. Data are provisional and
    have undergone only limited validation. Rainfall for the Hong Kong Observatory station in this
    dataset differs from the official climatological database and other weather bulletins.

    Args:
        lang (GetHourlyRainfallLang):  Default: 'en'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HourlyRainfallReport
    """

    return sync_detailed(
        client=client,
        lang=lang,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    lang: GetHourlyRainfallLang = "en",
) -> Response[HourlyRainfallReport]:
    """Rainfall in the past hour from automatic weather stations

     Rainfall measured during the one-hour period ending at observation time. Data are provisional and
    have undergone only limited validation. Rainfall for the Hong Kong Observatory station in this
    dataset differs from the official climatological database and other weather bulletins.

    Args:
        lang (GetHourlyRainfallLang):  Default: 'en'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HourlyRainfallReport]
    """

    kwargs = _get_kwargs(
        lang=lang,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    lang: GetHourlyRainfallLang = "en",
) -> HourlyRainfallReport | None:
    """Rainfall in the past hour from automatic weather stations

     Rainfall measured during the one-hour period ending at observation time. Data are provisional and
    have undergone only limited validation. Rainfall for the Hong Kong Observatory station in this
    dataset differs from the official climatological database and other weather bulletins.

    Args:
        lang (GetHourlyRainfallLang):  Default: 'en'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HourlyRainfallReport
    """

    return (
        await asyncio_detailed(
            client=client,
            lang=lang,
        )
    ).parsed
