from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_gsh_2019_sale_transactions_dataresource import (
    GetGsh2019SaleTransactionsDataresource,
)
from ...models.get_gsh_2019_sale_transactions_format import (
    GetGsh2019SaleTransactionsFormat,
)
from ...models.get_gsh_2019_sale_transactions_lang import (
    GetGsh2019SaleTransactionsLang,
)
from ...models.transaction_response import TransactionResponse
from ...types import Response


def _get_kwargs(
    dataresource: GetGsh2019SaleTransactionsDataresource,
    lang: GetGsh2019SaleTransactionsLang,
    format_: GetGsh2019SaleTransactionsFormat,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/{dataresource}/{lang}/{format_}".format(
            dataresource=quote(str(dataresource), safe=""),
            lang=quote(str(lang), safe=""),
            format_=quote(str(format_), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | TransactionResponse | None:
    if response.status_code == 200:
        response_200 = TransactionResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | TransactionResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dataresource: GetGsh2019SaleTransactionsDataresource,
    lang: GetGsh2019SaleTransactionsLang,
    format_: GetGsh2019SaleTransactionsFormat,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | TransactionResponse]:
    """Get GSH 2019 sale transactions

     Retrieves transactions in the sale of Green Form Subsidised Home Ownership Scheme flats (GSH) 2019.
    The documented request example is `https://data.housingauthority.gov.hk/psi/rest/export/ssfs-sale-
    transactions-g19/en/json`. The documentation describes Simplified Chinese as a request option, but
    notes that this dataset does not provide Simplified Chinese data and returns Traditional Chinese
    instead.

    Args:
        dataresource (GetGsh2019SaleTransactionsDataresource):
        lang (GetGsh2019SaleTransactionsLang):
        format_ (GetGsh2019SaleTransactionsFormat):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | TransactionResponse]
    """

    kwargs = _get_kwargs(
        dataresource=dataresource,
        lang=lang,
        format_=format_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dataresource: GetGsh2019SaleTransactionsDataresource,
    lang: GetGsh2019SaleTransactionsLang,
    format_: GetGsh2019SaleTransactionsFormat,
    *,
    client: AuthenticatedClient | Client,
) -> Any | TransactionResponse | None:
    """Get GSH 2019 sale transactions

     Retrieves transactions in the sale of Green Form Subsidised Home Ownership Scheme flats (GSH) 2019.
    The documented request example is `https://data.housingauthority.gov.hk/psi/rest/export/ssfs-sale-
    transactions-g19/en/json`. The documentation describes Simplified Chinese as a request option, but
    notes that this dataset does not provide Simplified Chinese data and returns Traditional Chinese
    instead.

    Args:
        dataresource (GetGsh2019SaleTransactionsDataresource):
        lang (GetGsh2019SaleTransactionsLang):
        format_ (GetGsh2019SaleTransactionsFormat):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | TransactionResponse
    """

    return sync_detailed(
        dataresource=dataresource,
        lang=lang,
        format_=format_,
        client=client,
    ).parsed


async def asyncio_detailed(
    dataresource: GetGsh2019SaleTransactionsDataresource,
    lang: GetGsh2019SaleTransactionsLang,
    format_: GetGsh2019SaleTransactionsFormat,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | TransactionResponse]:
    """Get GSH 2019 sale transactions

     Retrieves transactions in the sale of Green Form Subsidised Home Ownership Scheme flats (GSH) 2019.
    The documented request example is `https://data.housingauthority.gov.hk/psi/rest/export/ssfs-sale-
    transactions-g19/en/json`. The documentation describes Simplified Chinese as a request option, but
    notes that this dataset does not provide Simplified Chinese data and returns Traditional Chinese
    instead.

    Args:
        dataresource (GetGsh2019SaleTransactionsDataresource):
        lang (GetGsh2019SaleTransactionsLang):
        format_ (GetGsh2019SaleTransactionsFormat):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | TransactionResponse]
    """

    kwargs = _get_kwargs(
        dataresource=dataresource,
        lang=lang,
        format_=format_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dataresource: GetGsh2019SaleTransactionsDataresource,
    lang: GetGsh2019SaleTransactionsLang,
    format_: GetGsh2019SaleTransactionsFormat,
    *,
    client: AuthenticatedClient | Client,
) -> Any | TransactionResponse | None:
    """Get GSH 2019 sale transactions

     Retrieves transactions in the sale of Green Form Subsidised Home Ownership Scheme flats (GSH) 2019.
    The documented request example is `https://data.housingauthority.gov.hk/psi/rest/export/ssfs-sale-
    transactions-g19/en/json`. The documentation describes Simplified Chinese as a request option, but
    notes that this dataset does not provide Simplified Chinese data and returns Traditional Chinese
    instead.

    Args:
        dataresource (GetGsh2019SaleTransactionsDataresource):
        lang (GetGsh2019SaleTransactionsLang):
        format_ (GetGsh2019SaleTransactionsFormat):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | TransactionResponse
    """

    return (
        await asyncio_detailed(
            dataresource=dataresource,
            lang=lang,
            format_=format_,
            client=client,
        )
    ).parsed
