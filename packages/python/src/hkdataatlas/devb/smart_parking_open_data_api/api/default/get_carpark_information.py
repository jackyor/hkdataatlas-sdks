from http import HTTPStatus
from typing import Any, cast

import httpx2

from ...client import AuthenticatedClient, Client
from ...models.carpark_info_response import CarparkInfoResponse
from ...models.get_carpark_information_lang import (
    GetCarparkInformationLang,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    carpark_id: int,
    lang: GetCarparkInformationLang | Unset = "en_US",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["carparkId"] = carpark_id

    json_lang: str | Unset = UNSET
    if not isinstance(lang, Unset):
        json_lang = lang

    params["lang"] = json_lang

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/getCarparkInfo",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | CarparkInfoResponse:
    if response.status_code == 200:
        response_200 = CarparkInfoResponse.from_dict(response.json())

        return response_200

    response_default = cast(Any, None)
    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | CarparkInfoResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    carpark_id: int,
    lang: GetCarparkInformationLang | Unset = "en_US",
) -> Response[Any | CarparkInfoResponse]:
    """Get carpark information

     Gets detailed information for one carpark without vacancy. Supports gzip/deflate compression and
    ETag.

    Args:
        carpark_id (int):
        lang (GetCarparkInformationLang | Unset):  Default: 'en_US'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CarparkInfoResponse]
    """

    kwargs = _get_kwargs(
        carpark_id=carpark_id,
        lang=lang,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    carpark_id: int,
    lang: GetCarparkInformationLang | Unset = "en_US",
) -> Any | CarparkInfoResponse | None:
    """Get carpark information

     Gets detailed information for one carpark without vacancy. Supports gzip/deflate compression and
    ETag.

    Args:
        carpark_id (int):
        lang (GetCarparkInformationLang | Unset):  Default: 'en_US'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CarparkInfoResponse
    """

    return sync_detailed(
        client=client,
        carpark_id=carpark_id,
        lang=lang,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    carpark_id: int,
    lang: GetCarparkInformationLang | Unset = "en_US",
) -> Response[Any | CarparkInfoResponse]:
    """Get carpark information

     Gets detailed information for one carpark without vacancy. Supports gzip/deflate compression and
    ETag.

    Args:
        carpark_id (int):
        lang (GetCarparkInformationLang | Unset):  Default: 'en_US'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CarparkInfoResponse]
    """

    kwargs = _get_kwargs(
        carpark_id=carpark_id,
        lang=lang,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    carpark_id: int,
    lang: GetCarparkInformationLang | Unset = "en_US",
) -> Any | CarparkInfoResponse | None:
    """Get carpark information

     Gets detailed information for one carpark without vacancy. Supports gzip/deflate compression and
    ETag.

    Args:
        carpark_id (int):
        lang (GetCarparkInformationLang | Unset):  Default: 'en_US'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CarparkInfoResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            carpark_id=carpark_id,
            lang=lang,
        )
    ).parsed
