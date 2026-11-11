from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ...client import AuthenticatedClient, Client
from ...models.export_prh_income_asset_limits_format import (
    ExportPrhIncomeAssetLimitsFormat,
)
from ...models.export_prh_income_asset_limits_lang import (
    ExportPrhIncomeAssetLimitsLang,
)
from ...models.prh_export_response import PrhExportResponse
from ...types import Response


def _get_kwargs(
    lang: ExportPrhIncomeAssetLimitsLang,
    format_: ExportPrhIncomeAssetLimitsFormat,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/psi/rest/export/prh-inc-ast-lmt/{lang}/{format_}".format(
            lang=quote(str(lang), safe=""),
            format_=quote(str(format_), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | PrhExportResponse:
    if response.status_code == 200:
        response_200 = PrhExportResponse.from_dict(response.json())

        return response_200

    response_default = response.json()
    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | PrhExportResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    lang: ExportPrhIncomeAssetLimitsLang,
    format_: ExportPrhIncomeAssetLimitsFormat,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | PrhExportResponse]:
    """Income and Asset Limits for Public Rental Housing (PRH) Application API

    Args:
        lang (ExportPrhIncomeAssetLimitsLang):
        format_ (ExportPrhIncomeAssetLimitsFormat):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PrhExportResponse]
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
    lang: ExportPrhIncomeAssetLimitsLang,
    format_: ExportPrhIncomeAssetLimitsFormat,
    *,
    client: AuthenticatedClient | Client,
) -> Any | PrhExportResponse | None:
    """Income and Asset Limits for Public Rental Housing (PRH) Application API

    Args:
        lang (ExportPrhIncomeAssetLimitsLang):
        format_ (ExportPrhIncomeAssetLimitsFormat):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PrhExportResponse
    """

    return sync_detailed(
        lang=lang,
        format_=format_,
        client=client,
    ).parsed


async def asyncio_detailed(
    lang: ExportPrhIncomeAssetLimitsLang,
    format_: ExportPrhIncomeAssetLimitsFormat,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | PrhExportResponse]:
    """Income and Asset Limits for Public Rental Housing (PRH) Application API

    Args:
        lang (ExportPrhIncomeAssetLimitsLang):
        format_ (ExportPrhIncomeAssetLimitsFormat):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PrhExportResponse]
    """

    kwargs = _get_kwargs(
        lang=lang,
        format_=format_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    lang: ExportPrhIncomeAssetLimitsLang,
    format_: ExportPrhIncomeAssetLimitsFormat,
    *,
    client: AuthenticatedClient | Client,
) -> Any | PrhExportResponse | None:
    """Income and Asset Limits for Public Rental Housing (PRH) Application API

    Args:
        lang (ExportPrhIncomeAssetLimitsLang):
        format_ (ExportPrhIncomeAssetLimitsFormat):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PrhExportResponse
    """

    return (
        await asyncio_detailed(
            lang=lang,
            format_=format_,
            client=client,
        )
    ).parsed
