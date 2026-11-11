from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_hos_2018_sale_transactions_dataresource import (
    GetHos2018SaleTransactionsDataresource,
)
from ...models.get_hos_2018_sale_transactions_lang import (
    GetHos2018SaleTransactionsLang,
)
from ...models.get_hos_2018_sale_transactions_sc import (
    GetHos2018SaleTransactionsSc,
)
from ...models.transactions_response import TransactionsResponse
from ...types import Response


def _get_kwargs(
    dataresource: GetHos2018SaleTransactionsDataresource,
    lang: GetHos2018SaleTransactionsLang,
    sc: GetHos2018SaleTransactionsSc,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/psi/rest/export/{dataresource}/{lang}/{sc}".format(
            dataresource=quote(str(dataresource), safe=""),
            lang=quote(str(lang), safe=""),
            sc=quote(str(sc), safe=""),
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
    dataresource: GetHos2018SaleTransactionsDataresource,
    lang: GetHos2018SaleTransactionsLang,
    sc: GetHos2018SaleTransactionsSc,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | TransactionsResponse]:
    """Get HOS flats 2018 sale transactions

     Returns sales transaction data. The documented example requests JSON and shows a top-level data
    array. Although resource information lists JSON, CSV, and XML, the dictionary describes the web
    service response as JSON. The documented Simplified Chinese language selection returns Traditional
    Chinese data for this dataset.

    Args:
        dataresource (GetHos2018SaleTransactionsDataresource):
        lang (GetHos2018SaleTransactionsLang):
        sc (GetHos2018SaleTransactionsSc):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | TransactionsResponse]
    """

    kwargs = _get_kwargs(
        dataresource=dataresource,
        lang=lang,
        sc=sc,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dataresource: GetHos2018SaleTransactionsDataresource,
    lang: GetHos2018SaleTransactionsLang,
    sc: GetHos2018SaleTransactionsSc,
    *,
    client: AuthenticatedClient | Client,
) -> Any | TransactionsResponse | None:
    """Get HOS flats 2018 sale transactions

     Returns sales transaction data. The documented example requests JSON and shows a top-level data
    array. Although resource information lists JSON, CSV, and XML, the dictionary describes the web
    service response as JSON. The documented Simplified Chinese language selection returns Traditional
    Chinese data for this dataset.

    Args:
        dataresource (GetHos2018SaleTransactionsDataresource):
        lang (GetHos2018SaleTransactionsLang):
        sc (GetHos2018SaleTransactionsSc):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | TransactionsResponse
    """

    return sync_detailed(
        dataresource=dataresource,
        lang=lang,
        sc=sc,
        client=client,
    ).parsed


async def asyncio_detailed(
    dataresource: GetHos2018SaleTransactionsDataresource,
    lang: GetHos2018SaleTransactionsLang,
    sc: GetHos2018SaleTransactionsSc,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | TransactionsResponse]:
    """Get HOS flats 2018 sale transactions

     Returns sales transaction data. The documented example requests JSON and shows a top-level data
    array. Although resource information lists JSON, CSV, and XML, the dictionary describes the web
    service response as JSON. The documented Simplified Chinese language selection returns Traditional
    Chinese data for this dataset.

    Args:
        dataresource (GetHos2018SaleTransactionsDataresource):
        lang (GetHos2018SaleTransactionsLang):
        sc (GetHos2018SaleTransactionsSc):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | TransactionsResponse]
    """

    kwargs = _get_kwargs(
        dataresource=dataresource,
        lang=lang,
        sc=sc,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dataresource: GetHos2018SaleTransactionsDataresource,
    lang: GetHos2018SaleTransactionsLang,
    sc: GetHos2018SaleTransactionsSc,
    *,
    client: AuthenticatedClient | Client,
) -> Any | TransactionsResponse | None:
    """Get HOS flats 2018 sale transactions

     Returns sales transaction data. The documented example requests JSON and shows a top-level data
    array. Although resource information lists JSON, CSV, and XML, the dictionary describes the web
    service response as JSON. The documented Simplified Chinese language selection returns Traditional
    Chinese data for this dataset.

    Args:
        dataresource (GetHos2018SaleTransactionsDataresource):
        lang (GetHos2018SaleTransactionsLang):
        sc (GetHos2018SaleTransactionsSc):

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
            sc=sc,
            client=client,
        )
    ).parsed
