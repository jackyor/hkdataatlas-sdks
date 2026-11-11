from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_gsh_2024_sale_transactions_dataresource import (
    GetGsh2024SaleTransactionsDataresource,
)
from ...models.get_gsh_2024_sale_transactions_format import (
    GetGsh2024SaleTransactionsFormat,
)
from ...models.get_gsh_2024_sale_transactions_lang import (
    GetGsh2024SaleTransactionsLang,
)
from ...models.transactions_response import TransactionsResponse
from ...types import Response


def _get_kwargs(
    dataresource: GetGsh2024SaleTransactionsDataresource,
    lang: GetGsh2024SaleTransactionsLang,
    format_: GetGsh2024SaleTransactionsFormat,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/psi/rest/export/{dataresource}/{lang}/{format_}".format(
            dataresource=quote(str(dataresource), safe=""),
            lang=quote(str(lang), safe=""),
            format_=quote(str(format_), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | TransactionsResponse | None:
    if response.status_code == 200:
        response_200 = TransactionsResponse.from_dict(response.json())

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
) -> Response[Any | TransactionsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dataresource: GetGsh2024SaleTransactionsDataresource,
    lang: GetGsh2024SaleTransactionsLang,
    format_: GetGsh2024SaleTransactionsFormat,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | TransactionsResponse]:
    """Get GSH Flats 2024 sale transactions

     Returns sales transaction data for the 2024 GSH flats dataset. The documentation lists JSON, CSV,
    and XML response formats and UTF-8 encoding. The example documents a JSON response envelope
    containing a data array. The companion dataset page is https://data.gov.hk/en-data/dataset/hk-
    housing-gsh2024-ssfs-sale-transactions-g24.

    Args:
        dataresource (GetGsh2024SaleTransactionsDataresource):
        lang (GetGsh2024SaleTransactionsLang):
        format_ (GetGsh2024SaleTransactionsFormat):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | TransactionsResponse]
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
    dataresource: GetGsh2024SaleTransactionsDataresource,
    lang: GetGsh2024SaleTransactionsLang,
    format_: GetGsh2024SaleTransactionsFormat,
    *,
    client: AuthenticatedClient | Client,
) -> Any | TransactionsResponse | None:
    """Get GSH Flats 2024 sale transactions

     Returns sales transaction data for the 2024 GSH flats dataset. The documentation lists JSON, CSV,
    and XML response formats and UTF-8 encoding. The example documents a JSON response envelope
    containing a data array. The companion dataset page is https://data.gov.hk/en-data/dataset/hk-
    housing-gsh2024-ssfs-sale-transactions-g24.

    Args:
        dataresource (GetGsh2024SaleTransactionsDataresource):
        lang (GetGsh2024SaleTransactionsLang):
        format_ (GetGsh2024SaleTransactionsFormat):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | TransactionsResponse
    """

    return sync_detailed(
        dataresource=dataresource,
        lang=lang,
        format_=format_,
        client=client,
    ).parsed


async def asyncio_detailed(
    dataresource: GetGsh2024SaleTransactionsDataresource,
    lang: GetGsh2024SaleTransactionsLang,
    format_: GetGsh2024SaleTransactionsFormat,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | TransactionsResponse]:
    """Get GSH Flats 2024 sale transactions

     Returns sales transaction data for the 2024 GSH flats dataset. The documentation lists JSON, CSV,
    and XML response formats and UTF-8 encoding. The example documents a JSON response envelope
    containing a data array. The companion dataset page is https://data.gov.hk/en-data/dataset/hk-
    housing-gsh2024-ssfs-sale-transactions-g24.

    Args:
        dataresource (GetGsh2024SaleTransactionsDataresource):
        lang (GetGsh2024SaleTransactionsLang):
        format_ (GetGsh2024SaleTransactionsFormat):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | TransactionsResponse]
    """

    kwargs = _get_kwargs(
        dataresource=dataresource,
        lang=lang,
        format_=format_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dataresource: GetGsh2024SaleTransactionsDataresource,
    lang: GetGsh2024SaleTransactionsLang,
    format_: GetGsh2024SaleTransactionsFormat,
    *,
    client: AuthenticatedClient | Client,
) -> Any | TransactionsResponse | None:
    """Get GSH Flats 2024 sale transactions

     Returns sales transaction data for the 2024 GSH flats dataset. The documentation lists JSON, CSV,
    and XML response formats and UTF-8 encoding. The example documents a JSON response envelope
    containing a data array. The companion dataset page is https://data.gov.hk/en-data/dataset/hk-
    housing-gsh2024-ssfs-sale-transactions-g24.

    Args:
        dataresource (GetGsh2024SaleTransactionsDataresource):
        lang (GetGsh2024SaleTransactionsLang):
        format_ (GetGsh2024SaleTransactionsFormat):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | TransactionsResponse
    """

    return (
        await asyncio_detailed(
            dataresource=dataresource,
            lang=lang,
            format_=format_,
            client=client,
        )
    ).parsed
