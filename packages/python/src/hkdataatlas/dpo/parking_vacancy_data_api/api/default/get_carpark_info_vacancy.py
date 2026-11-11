from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_carpark_info_vacancy_data import (
    GetCarparkInfoVacancyData,
)
from ...models.get_carpark_info_vacancy_lang import (
    GetCarparkInfoVacancyLang,
)
from ...models.get_carpark_info_vacancy_response_200 import (
    GetCarparkInfoVacancyResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    data: GetCarparkInfoVacancyData | Unset = "info",
    vehicle_types: str | Unset = UNSET,
    carpark_ids: str | Unset = UNSET,
    extent: str | Unset = UNSET,
    lang: GetCarparkInfoVacancyLang | Unset = "en_US",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_data: str | Unset = UNSET
    if not isinstance(data, Unset):
        json_data = data

    params["data"] = json_data

    params["vehicleTypes"] = vehicle_types

    params["carparkIds"] = carpark_ids

    params["extent"] = extent

    json_lang: str | Unset = UNSET
    if not isinstance(lang, Unset):
        json_lang = lang

    params["lang"] = json_lang

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/carpark-info-vacancy",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | GetCarparkInfoVacancyResponse200 | None:
    if response.status_code == 200:
        media_type = (
            response.headers.get("content-type", "").split(";", 1)[0].strip().lower()
        )
        if media_type != "application/json" and not media_type.endswith("+json"):
            return None
        response_200 = GetCarparkInfoVacancyResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if response.status_code == 503:
        response_503 = cast(Any, None)
        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | GetCarparkInfoVacancyResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    data: GetCarparkInfoVacancyData | Unset = "info",
    vehicle_types: str | Unset = UNSET,
    carpark_ids: str | Unset = UNSET,
    extent: str | Unset = UNSET,
    lang: GetCarparkInfoVacancyLang | Unset = "en_US",
) -> Response[Any | GetCarparkInfoVacancyResponse200]:
    """Get car park information and vacancy data

     Gets all published car parks' basic information and vacancy data. The `data` parameter selects basic
    information or parking vacancy data. Response examples and dictionaries are representative
    documentation and do not establish that every listed property is present in every response.

    Args:
        data (GetCarparkInfoVacancyData | Unset):  Default: 'info'.
        vehicle_types (str | Unset):
        carpark_ids (str | Unset):
        extent (str | Unset):
        lang (GetCarparkInfoVacancyLang | Unset):  Default: 'en_US'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetCarparkInfoVacancyResponse200]
    """

    kwargs = _get_kwargs(
        data=data,
        vehicle_types=vehicle_types,
        carpark_ids=carpark_ids,
        extent=extent,
        lang=lang,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    data: GetCarparkInfoVacancyData | Unset = "info",
    vehicle_types: str | Unset = UNSET,
    carpark_ids: str | Unset = UNSET,
    extent: str | Unset = UNSET,
    lang: GetCarparkInfoVacancyLang | Unset = "en_US",
) -> Any | GetCarparkInfoVacancyResponse200 | None:
    """Get car park information and vacancy data

     Gets all published car parks' basic information and vacancy data. The `data` parameter selects basic
    information or parking vacancy data. Response examples and dictionaries are representative
    documentation and do not establish that every listed property is present in every response.

    Args:
        data (GetCarparkInfoVacancyData | Unset):  Default: 'info'.
        vehicle_types (str | Unset):
        carpark_ids (str | Unset):
        extent (str | Unset):
        lang (GetCarparkInfoVacancyLang | Unset):  Default: 'en_US'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetCarparkInfoVacancyResponse200
    """

    return sync_detailed(
        client=client,
        data=data,
        vehicle_types=vehicle_types,
        carpark_ids=carpark_ids,
        extent=extent,
        lang=lang,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    data: GetCarparkInfoVacancyData | Unset = "info",
    vehicle_types: str | Unset = UNSET,
    carpark_ids: str | Unset = UNSET,
    extent: str | Unset = UNSET,
    lang: GetCarparkInfoVacancyLang | Unset = "en_US",
) -> Response[Any | GetCarparkInfoVacancyResponse200]:
    """Get car park information and vacancy data

     Gets all published car parks' basic information and vacancy data. The `data` parameter selects basic
    information or parking vacancy data. Response examples and dictionaries are representative
    documentation and do not establish that every listed property is present in every response.

    Args:
        data (GetCarparkInfoVacancyData | Unset):  Default: 'info'.
        vehicle_types (str | Unset):
        carpark_ids (str | Unset):
        extent (str | Unset):
        lang (GetCarparkInfoVacancyLang | Unset):  Default: 'en_US'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetCarparkInfoVacancyResponse200]
    """

    kwargs = _get_kwargs(
        data=data,
        vehicle_types=vehicle_types,
        carpark_ids=carpark_ids,
        extent=extent,
        lang=lang,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    data: GetCarparkInfoVacancyData | Unset = "info",
    vehicle_types: str | Unset = UNSET,
    carpark_ids: str | Unset = UNSET,
    extent: str | Unset = UNSET,
    lang: GetCarparkInfoVacancyLang | Unset = "en_US",
) -> Any | GetCarparkInfoVacancyResponse200 | None:
    """Get car park information and vacancy data

     Gets all published car parks' basic information and vacancy data. The `data` parameter selects basic
    information or parking vacancy data. Response examples and dictionaries are representative
    documentation and do not establish that every listed property is present in every response.

    Args:
        data (GetCarparkInfoVacancyData | Unset):  Default: 'info'.
        vehicle_types (str | Unset):
        carpark_ids (str | Unset):
        extent (str | Unset):
        lang (GetCarparkInfoVacancyLang | Unset):  Default: 'en_US'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetCarparkInfoVacancyResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            data=data,
            vehicle_types=vehicle_types,
            carpark_ids=carpark_ids,
            extent=extent,
            lang=lang,
        )
    ).parsed
