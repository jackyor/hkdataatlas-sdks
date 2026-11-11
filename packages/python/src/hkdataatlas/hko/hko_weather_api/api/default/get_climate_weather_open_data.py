from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_climate_weather_open_data_data_type import (
    GetClimateWeatherOpenDataDataType,
)
from ...models.get_climate_weather_open_data_lang import (
    GetClimateWeatherOpenDataLang,
)
from ...models.get_climate_weather_open_data_rformat import (
    GetClimateWeatherOpenDataRformat,
)
from ...models.tabular_open_data import TabularOpenData
from ...models.weather_radiation_report import WeatherRadiationReport
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    data_type: GetClimateWeatherOpenDataDataType,
    rformat: GetClimateWeatherOpenDataRformat | Unset = "csv",
    station: str | Unset = UNSET,
    year: int | Unset = UNSET,
    month: int | Unset = UNSET,
    day: int | Unset = UNSET,
    hour: int | Unset = UNSET,
    lang: GetClimateWeatherOpenDataLang | Unset = "en",
    date: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_data_type: str = data_type
    params["dataType"] = json_data_type

    json_rformat: str | Unset = UNSET
    if not isinstance(rformat, Unset):
        json_rformat = rformat

    params["rformat"] = json_rformat

    params["station"] = station

    params["year"] = year

    params["month"] = month

    params["day"] = day

    params["hour"] = hour

    json_lang: str | Unset = UNSET
    if not isinstance(lang, Unset):
        json_lang = lang

    params["lang"] = json_lang

    params["date"] = date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/opendata.php",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> TabularOpenData | WeatherRadiationReport | None:
    if response.status_code == 200:

        def _parse_response_200(
            data: object,
        ) -> TabularOpenData | WeatherRadiationReport:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = TabularOpenData.from_dict(data)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = WeatherRadiationReport.from_dict(data)

            return response_200_type_1

        response_200 = _parse_response_200(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[TabularOpenData | WeatherRadiationReport]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    data_type: GetClimateWeatherOpenDataDataType,
    rformat: GetClimateWeatherOpenDataRformat | Unset = "csv",
    station: str | Unset = UNSET,
    year: int | Unset = UNSET,
    month: int | Unset = UNSET,
    day: int | Unset = UNSET,
    hour: int | Unset = UNSET,
    lang: GetClimateWeatherOpenDataLang | Unset = "en",
    date: str | Unset = UNSET,
) -> Response[TabularOpenData | WeatherRadiationReport]:
    """Climate and weather open data

     Returns a documented climate and weather dataset. JSON or CSV is documented for applicable
    selectors. Parameter applicability, station assignments, and year ranges depend on dataType. The
    associated predicted hourly astronomical tides CSV file layout is described in the text/csv response
    and is not a universal CSV contract.

    Args:
        data_type (GetClimateWeatherOpenDataDataType):
        rformat (GetClimateWeatherOpenDataRformat | Unset):  Default: 'csv'.
        station (str | Unset): Accepted codes depend on dataType. See the dataset-specific station
            descriptions.
        year (int | Unset):
        month (int | Unset):
        day (int | Unset):
        hour (int | Unset):
        lang (GetClimateWeatherOpenDataLang | Unset):  Default: 'en'.
        date (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TabularOpenData | WeatherRadiationReport]
    """

    kwargs = _get_kwargs(
        data_type=data_type,
        rformat=rformat,
        station=station,
        year=year,
        month=month,
        day=day,
        hour=hour,
        lang=lang,
        date=date,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    data_type: GetClimateWeatherOpenDataDataType,
    rformat: GetClimateWeatherOpenDataRformat | Unset = "csv",
    station: str | Unset = UNSET,
    year: int | Unset = UNSET,
    month: int | Unset = UNSET,
    day: int | Unset = UNSET,
    hour: int | Unset = UNSET,
    lang: GetClimateWeatherOpenDataLang | Unset = "en",
    date: str | Unset = UNSET,
) -> TabularOpenData | WeatherRadiationReport | None:
    """Climate and weather open data

     Returns a documented climate and weather dataset. JSON or CSV is documented for applicable
    selectors. Parameter applicability, station assignments, and year ranges depend on dataType. The
    associated predicted hourly astronomical tides CSV file layout is described in the text/csv response
    and is not a universal CSV contract.

    Args:
        data_type (GetClimateWeatherOpenDataDataType):
        rformat (GetClimateWeatherOpenDataRformat | Unset):  Default: 'csv'.
        station (str | Unset): Accepted codes depend on dataType. See the dataset-specific station
            descriptions.
        year (int | Unset):
        month (int | Unset):
        day (int | Unset):
        hour (int | Unset):
        lang (GetClimateWeatherOpenDataLang | Unset):  Default: 'en'.
        date (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TabularOpenData | WeatherRadiationReport
    """

    return sync_detailed(
        client=client,
        data_type=data_type,
        rformat=rformat,
        station=station,
        year=year,
        month=month,
        day=day,
        hour=hour,
        lang=lang,
        date=date,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    data_type: GetClimateWeatherOpenDataDataType,
    rformat: GetClimateWeatherOpenDataRformat | Unset = "csv",
    station: str | Unset = UNSET,
    year: int | Unset = UNSET,
    month: int | Unset = UNSET,
    day: int | Unset = UNSET,
    hour: int | Unset = UNSET,
    lang: GetClimateWeatherOpenDataLang | Unset = "en",
    date: str | Unset = UNSET,
) -> Response[TabularOpenData | WeatherRadiationReport]:
    """Climate and weather open data

     Returns a documented climate and weather dataset. JSON or CSV is documented for applicable
    selectors. Parameter applicability, station assignments, and year ranges depend on dataType. The
    associated predicted hourly astronomical tides CSV file layout is described in the text/csv response
    and is not a universal CSV contract.

    Args:
        data_type (GetClimateWeatherOpenDataDataType):
        rformat (GetClimateWeatherOpenDataRformat | Unset):  Default: 'csv'.
        station (str | Unset): Accepted codes depend on dataType. See the dataset-specific station
            descriptions.
        year (int | Unset):
        month (int | Unset):
        day (int | Unset):
        hour (int | Unset):
        lang (GetClimateWeatherOpenDataLang | Unset):  Default: 'en'.
        date (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TabularOpenData | WeatherRadiationReport]
    """

    kwargs = _get_kwargs(
        data_type=data_type,
        rformat=rformat,
        station=station,
        year=year,
        month=month,
        day=day,
        hour=hour,
        lang=lang,
        date=date,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    data_type: GetClimateWeatherOpenDataDataType,
    rformat: GetClimateWeatherOpenDataRformat | Unset = "csv",
    station: str | Unset = UNSET,
    year: int | Unset = UNSET,
    month: int | Unset = UNSET,
    day: int | Unset = UNSET,
    hour: int | Unset = UNSET,
    lang: GetClimateWeatherOpenDataLang | Unset = "en",
    date: str | Unset = UNSET,
) -> TabularOpenData | WeatherRadiationReport | None:
    """Climate and weather open data

     Returns a documented climate and weather dataset. JSON or CSV is documented for applicable
    selectors. Parameter applicability, station assignments, and year ranges depend on dataType. The
    associated predicted hourly astronomical tides CSV file layout is described in the text/csv response
    and is not a universal CSV contract.

    Args:
        data_type (GetClimateWeatherOpenDataDataType):
        rformat (GetClimateWeatherOpenDataRformat | Unset):  Default: 'csv'.
        station (str | Unset): Accepted codes depend on dataType. See the dataset-specific station
            descriptions.
        year (int | Unset):
        month (int | Unset):
        day (int | Unset):
        hour (int | Unset):
        lang (GetClimateWeatherOpenDataLang | Unset):  Default: 'en'.
        date (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TabularOpenData | WeatherRadiationReport
    """

    return (
        await asyncio_detailed(
            client=client,
            data_type=data_type,
            rformat=rformat,
            station=station,
            year=year,
            month=month,
            day=day,
            hour=hour,
            lang=lang,
            date=date,
        )
    ).parsed
