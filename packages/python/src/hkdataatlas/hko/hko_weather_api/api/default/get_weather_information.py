from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.current_weather_report import CurrentWeatherReport
from ...models.get_weather_information_data_type import (
    GetWeatherInformationDataType,
)
from ...models.get_weather_information_lang import (
    GetWeatherInformationLang,
)
from ...models.local_weather_forecast import LocalWeatherForecast
from ...models.nine_day_forecast import NineDayForecast
from ...models.special_weather_tips import SpecialWeatherTips
from ...models.weather_warning_information import WeatherWarningInformation
from ...models.weather_warning_summary import WeatherWarningSummary
from ...types import UNSET, Response


def _get_kwargs(
    *,
    data_type: GetWeatherInformationDataType,
    lang: GetWeatherInformationLang = "en",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_data_type: str = data_type
    params["dataType"] = json_data_type

    json_lang: str = lang
    params["lang"] = json_lang

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/weather.php",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> (
    CurrentWeatherReport
    | LocalWeatherForecast
    | NineDayForecast
    | SpecialWeatherTips
    | WeatherWarningInformation
    | WeatherWarningSummary
    | None
):
    if response.status_code == 200:

        def _parse_response_200(
            data: object,
        ) -> (
            CurrentWeatherReport
            | LocalWeatherForecast
            | NineDayForecast
            | SpecialWeatherTips
            | WeatherWarningInformation
            | WeatherWarningSummary
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = LocalWeatherForecast.from_dict(data)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_1 = NineDayForecast.from_dict(data)

                return response_200_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_2 = CurrentWeatherReport.from_dict(data)

                return response_200_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_3 = WeatherWarningSummary.from_dict(data)

                return response_200_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_4 = WeatherWarningInformation.from_dict(data)

                return response_200_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_5 = SpecialWeatherTips.from_dict(data)

            return response_200_type_5

        response_200 = _parse_response_200(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[
    CurrentWeatherReport
    | LocalWeatherForecast
    | NineDayForecast
    | SpecialWeatherTips
    | WeatherWarningInformation
    | WeatherWarningSummary
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
    data_type: GetWeatherInformationDataType,
    lang: GetWeatherInformationLang = "en",
) -> Response[
    CurrentWeatherReport
    | LocalWeatherForecast
    | NineDayForecast
    | SpecialWeatherTips
    | WeatherWarningInformation
    | WeatherWarningSummary
]:
    """Weather information

     Returns one of the documented weather datasets selected by dataType. Documented fields may be
    missing when null or unavailable; the Current Weather Report may return an empty string for UV index
    when no data is available.

    Args:
        data_type (GetWeatherInformationDataType):
        lang (GetWeatherInformationLang):  Default: 'en'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CurrentWeatherReport | LocalWeatherForecast | NineDayForecast | SpecialWeatherTips | WeatherWarningInformation | WeatherWarningSummary]
    """

    kwargs = _get_kwargs(
        data_type=data_type,
        lang=lang,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    data_type: GetWeatherInformationDataType,
    lang: GetWeatherInformationLang = "en",
) -> (
    CurrentWeatherReport
    | LocalWeatherForecast
    | NineDayForecast
    | SpecialWeatherTips
    | WeatherWarningInformation
    | WeatherWarningSummary
    | None
):
    """Weather information

     Returns one of the documented weather datasets selected by dataType. Documented fields may be
    missing when null or unavailable; the Current Weather Report may return an empty string for UV index
    when no data is available.

    Args:
        data_type (GetWeatherInformationDataType):
        lang (GetWeatherInformationLang):  Default: 'en'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CurrentWeatherReport | LocalWeatherForecast | NineDayForecast | SpecialWeatherTips | WeatherWarningInformation | WeatherWarningSummary
    """

    return sync_detailed(
        client=client,
        data_type=data_type,
        lang=lang,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    data_type: GetWeatherInformationDataType,
    lang: GetWeatherInformationLang = "en",
) -> Response[
    CurrentWeatherReport
    | LocalWeatherForecast
    | NineDayForecast
    | SpecialWeatherTips
    | WeatherWarningInformation
    | WeatherWarningSummary
]:
    """Weather information

     Returns one of the documented weather datasets selected by dataType. Documented fields may be
    missing when null or unavailable; the Current Weather Report may return an empty string for UV index
    when no data is available.

    Args:
        data_type (GetWeatherInformationDataType):
        lang (GetWeatherInformationLang):  Default: 'en'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CurrentWeatherReport | LocalWeatherForecast | NineDayForecast | SpecialWeatherTips | WeatherWarningInformation | WeatherWarningSummary]
    """

    kwargs = _get_kwargs(
        data_type=data_type,
        lang=lang,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    data_type: GetWeatherInformationDataType,
    lang: GetWeatherInformationLang = "en",
) -> (
    CurrentWeatherReport
    | LocalWeatherForecast
    | NineDayForecast
    | SpecialWeatherTips
    | WeatherWarningInformation
    | WeatherWarningSummary
    | None
):
    """Weather information

     Returns one of the documented weather datasets selected by dataType. Documented fields may be
    missing when null or unavailable; the Current Weather Report may return an empty string for UV index
    when no data is available.

    Args:
        data_type (GetWeatherInformationDataType):
        lang (GetWeatherInformationLang):  Default: 'en'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CurrentWeatherReport | LocalWeatherForecast | NineDayForecast | SpecialWeatherTips | WeatherWarningInformation | WeatherWarningSummary
    """

    return (
        await asyncio_detailed(
            client=client,
            data_type=data_type,
            lang=lang,
        )
    ).parsed
