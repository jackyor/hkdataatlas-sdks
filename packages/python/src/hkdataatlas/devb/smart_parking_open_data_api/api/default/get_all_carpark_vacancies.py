from http import HTTPStatus
from typing import Any, cast

import httpx2

from ...client import AuthenticatedClient, Client
from ...models.carpark_list_response import CarparkListResponse
from ...models.get_all_carpark_vacancies_lang import (
    GetAllCarparkVacanciesLang,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    carpark_types: str | Unset = UNSET,
    vehicle_types: str | Unset = UNSET,
    carpark_ids: str | Unset = UNSET,
    extent: str | Unset = UNSET,
    lang: GetAllCarparkVacanciesLang | Unset = "en_US",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["carparkTypes"] = carpark_types

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
        "url": "/getCarparkVacancies",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | CarparkListResponse:
    if response.status_code == 200:
        response_200 = CarparkListResponse.from_dict(response.json())

        return response_200

    response_default = cast(Any, None)
    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | CarparkListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    carpark_types: str | Unset = UNSET,
    vehicle_types: str | Unset = UNSET,
    carpark_ids: str | Unset = UNSET,
    extent: str | Unset = UNSET,
    lang: GetAllCarparkVacanciesLang | Unset = "en_US",
) -> Response[Any | CarparkListResponse]:
    """Get all carpark vacancies

     Gets vacancies for selected carparks in a batch. Current documented carparkIds=12 query succeeded
    anonymously. Historical v1.0 documentation says authentication required but gives no mechanism.

    Args:
        carpark_types (str | Unset):
        vehicle_types (str | Unset):
        carpark_ids (str | Unset):
        extent (str | Unset):
        lang (GetAllCarparkVacanciesLang | Unset):  Default: 'en_US'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CarparkListResponse]
    """

    kwargs = _get_kwargs(
        carpark_types=carpark_types,
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
    carpark_types: str | Unset = UNSET,
    vehicle_types: str | Unset = UNSET,
    carpark_ids: str | Unset = UNSET,
    extent: str | Unset = UNSET,
    lang: GetAllCarparkVacanciesLang | Unset = "en_US",
) -> Any | CarparkListResponse | None:
    """Get all carpark vacancies

     Gets vacancies for selected carparks in a batch. Current documented carparkIds=12 query succeeded
    anonymously. Historical v1.0 documentation says authentication required but gives no mechanism.

    Args:
        carpark_types (str | Unset):
        vehicle_types (str | Unset):
        carpark_ids (str | Unset):
        extent (str | Unset):
        lang (GetAllCarparkVacanciesLang | Unset):  Default: 'en_US'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CarparkListResponse
    """

    return sync_detailed(
        client=client,
        carpark_types=carpark_types,
        vehicle_types=vehicle_types,
        carpark_ids=carpark_ids,
        extent=extent,
        lang=lang,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    carpark_types: str | Unset = UNSET,
    vehicle_types: str | Unset = UNSET,
    carpark_ids: str | Unset = UNSET,
    extent: str | Unset = UNSET,
    lang: GetAllCarparkVacanciesLang | Unset = "en_US",
) -> Response[Any | CarparkListResponse]:
    """Get all carpark vacancies

     Gets vacancies for selected carparks in a batch. Current documented carparkIds=12 query succeeded
    anonymously. Historical v1.0 documentation says authentication required but gives no mechanism.

    Args:
        carpark_types (str | Unset):
        vehicle_types (str | Unset):
        carpark_ids (str | Unset):
        extent (str | Unset):
        lang (GetAllCarparkVacanciesLang | Unset):  Default: 'en_US'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CarparkListResponse]
    """

    kwargs = _get_kwargs(
        carpark_types=carpark_types,
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
    carpark_types: str | Unset = UNSET,
    vehicle_types: str | Unset = UNSET,
    carpark_ids: str | Unset = UNSET,
    extent: str | Unset = UNSET,
    lang: GetAllCarparkVacanciesLang | Unset = "en_US",
) -> Any | CarparkListResponse | None:
    """Get all carpark vacancies

     Gets vacancies for selected carparks in a batch. Current documented carparkIds=12 query succeeded
    anonymously. Historical v1.0 documentation says authentication required but gives no mechanism.

    Args:
        carpark_types (str | Unset):
        vehicle_types (str | Unset):
        carpark_ids (str | Unset):
        extent (str | Unset):
        lang (GetAllCarparkVacanciesLang | Unset):  Default: 'en_US'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CarparkListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            carpark_types=carpark_types,
            vehicle_types=vehicle_types,
            carpark_ids=carpark_ids,
            extent=extent,
            lang=lang,
        )
    ).parsed
