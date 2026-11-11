from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_ssfs_sale_transactions_e22_dataresource import (
    GetSsfsSaleTransactionsE22Dataresource,
)
from ...models.get_ssfs_sale_transactions_e22_format import (
    GetSsfsSaleTransactionsE22Format,
)
from ...models.get_ssfs_sale_transactions_e22_lang import (
    GetSsfsSaleTransactionsE22Lang,
)
from ...models.transaction_response import TransactionResponse
from ...types import Response


def _get_kwargs(
    dataresource: GetSsfsSaleTransactionsE22Dataresource,
    lang: GetSsfsSaleTransactionsE22Lang,
    format_: GetSsfsSaleTransactionsE22Format,
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
    dataresource: GetSsfsSaleTransactionsE22Dataresource,
    lang: GetSsfsSaleTransactionsE22Lang,
    format_: GetSsfsSaleTransactionsE22Format,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | TransactionResponse]:
    """Get sales transaction data

     Returns transaction data for the documented dataset. The JSON response is documented with a data
    array. CSV and XML are also listed as supported response formats, but response-body structures for
    those formats are not specified. For simplified Chinese, the source states that this dataset returns
    Traditional Chinese data.

    Args:
        dataresource (GetSsfsSaleTransactionsE22Dataresource):
        lang (GetSsfsSaleTransactionsE22Lang):
        format_ (GetSsfsSaleTransactionsE22Format):

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
    dataresource: GetSsfsSaleTransactionsE22Dataresource,
    lang: GetSsfsSaleTransactionsE22Lang,
    format_: GetSsfsSaleTransactionsE22Format,
    *,
    client: AuthenticatedClient | Client,
) -> Any | TransactionResponse | None:
    """Get sales transaction data

     Returns transaction data for the documented dataset. The JSON response is documented with a data
    array. CSV and XML are also listed as supported response formats, but response-body structures for
    those formats are not specified. For simplified Chinese, the source states that this dataset returns
    Traditional Chinese data.

    Args:
        dataresource (GetSsfsSaleTransactionsE22Dataresource):
        lang (GetSsfsSaleTransactionsE22Lang):
        format_ (GetSsfsSaleTransactionsE22Format):

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
    dataresource: GetSsfsSaleTransactionsE22Dataresource,
    lang: GetSsfsSaleTransactionsE22Lang,
    format_: GetSsfsSaleTransactionsE22Format,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | TransactionResponse]:
    """Get sales transaction data

     Returns transaction data for the documented dataset. The JSON response is documented with a data
    array. CSV and XML are also listed as supported response formats, but response-body structures for
    those formats are not specified. For simplified Chinese, the source states that this dataset returns
    Traditional Chinese data.

    Args:
        dataresource (GetSsfsSaleTransactionsE22Dataresource):
        lang (GetSsfsSaleTransactionsE22Lang):
        format_ (GetSsfsSaleTransactionsE22Format):

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
    dataresource: GetSsfsSaleTransactionsE22Dataresource,
    lang: GetSsfsSaleTransactionsE22Lang,
    format_: GetSsfsSaleTransactionsE22Format,
    *,
    client: AuthenticatedClient | Client,
) -> Any | TransactionResponse | None:
    """Get sales transaction data

     Returns transaction data for the documented dataset. The JSON response is documented with a data
    array. CSV and XML are also listed as supported response formats, but response-body structures for
    those formats are not specified. For simplified Chinese, the source states that this dataset returns
    Traditional Chinese data.

    Args:
        dataresource (GetSsfsSaleTransactionsE22Dataresource):
        lang (GetSsfsSaleTransactionsE22Lang):
        format_ (GetSsfsSaleTransactionsE22Format):

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
