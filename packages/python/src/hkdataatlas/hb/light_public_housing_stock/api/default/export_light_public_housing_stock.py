from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...models.export_light_public_housing_stock_format import (
    ExportLightPublicHousingStockFormat,
)
from ...models.export_light_public_housing_stock_lang import (
    ExportLightPublicHousingStockLang,
)
from ...models.light_public_housing_response import LightPublicHousingResponse
from ...types import Response


def _get_kwargs(
    lang: ExportLightPublicHousingStockLang,
    format_: ExportLightPublicHousingStockFormat,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/psi/rest/export/lph/{lang}/{format_}".format(
            lang=quote(str(lang), safe=""),
            format_=quote(str(format_), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | LightPublicHousingResponse:
    if response.status_code == 200:
        response_200 = LightPublicHousingResponse.from_dict(response.json())

        return response_200

    response_default = response.json()
    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | LightPublicHousingResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    lang: ExportLightPublicHousingStockLang,
    format_: ExportLightPublicHousingStockFormat,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | LightPublicHousingResponse]:
    """Light Public Housing Stock API

    Args:
        lang (ExportLightPublicHousingStockLang):
        format_ (ExportLightPublicHousingStockFormat):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | LightPublicHousingResponse]
    """

    kwargs = _get_kwargs(
        lang=lang,
        format_=format_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    lang: ExportLightPublicHousingStockLang,
    format_: ExportLightPublicHousingStockFormat,
    *,
    client: AuthenticatedClient | Client,
) -> Any | LightPublicHousingResponse | None:
    """Light Public Housing Stock API

    Args:
        lang (ExportLightPublicHousingStockLang):
        format_ (ExportLightPublicHousingStockFormat):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | LightPublicHousingResponse
    """

    return sync_detailed(
        lang=lang,
        format_=format_,
        client=client,
    ).parsed


async def asyncio_detailed(
    lang: ExportLightPublicHousingStockLang,
    format_: ExportLightPublicHousingStockFormat,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | LightPublicHousingResponse]:
    """Light Public Housing Stock API

    Args:
        lang (ExportLightPublicHousingStockLang):
        format_ (ExportLightPublicHousingStockFormat):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | LightPublicHousingResponse]
    """

    kwargs = _get_kwargs(
        lang=lang,
        format_=format_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    lang: ExportLightPublicHousingStockLang,
    format_: ExportLightPublicHousingStockFormat,
    *,
    client: AuthenticatedClient | Client,
) -> Any | LightPublicHousingResponse | None:
    """Light Public Housing Stock API

    Args:
        lang (ExportLightPublicHousingStockLang):
        format_ (ExportLightPublicHousingStockFormat):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | LightPublicHousingResponse
    """

    return (
        await asyncio_detailed(
            lang=lang,
            format_=format_,
            client=client,
        )
    ).parsed
