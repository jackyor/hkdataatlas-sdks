from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_tps_sale_transactions_dataresource import (
    GetTpsSaleTransactionsDataresource,
)
from ...models.get_tps_sale_transactions_format import (
    GetTpsSaleTransactionsFormat,
)
from ...models.get_tps_sale_transactions_lang import (
    GetTpsSaleTransactionsLang,
)
from ...models.get_tps_sale_transactions_response_200 import (
    GetTpsSaleTransactionsResponse200,
)
from ...types import Response


def _get_kwargs(
    dataresource: GetTpsSaleTransactionsDataresource,
    lang: GetTpsSaleTransactionsLang,
    format_: GetTpsSaleTransactionsFormat,
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
) -> Any | GetTpsSaleTransactionsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetTpsSaleTransactionsResponse200.from_dict(response.json())

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
) -> Response[Any | GetTpsSaleTransactionsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dataresource: GetTpsSaleTransactionsDataresource,
    lang: GetTpsSaleTransactionsLang,
    format_: GetTpsSaleTransactionsFormat,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetTpsSaleTransactionsResponse200]:
    """Get TPS sale transactions

     Returns sales transaction data for the Tenants Purchase Scheme in JSON. The documented resource URL
    is printed with a malformed single slash after `https:`; the example request and documented hostname
    establish the HTTPS server base used here.

    Args:
        dataresource (GetTpsSaleTransactionsDataresource):
        lang (GetTpsSaleTransactionsLang):
        format_ (GetTpsSaleTransactionsFormat):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetTpsSaleTransactionsResponse200]
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
    dataresource: GetTpsSaleTransactionsDataresource,
    lang: GetTpsSaleTransactionsLang,
    format_: GetTpsSaleTransactionsFormat,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetTpsSaleTransactionsResponse200 | None:
    """Get TPS sale transactions

     Returns sales transaction data for the Tenants Purchase Scheme in JSON. The documented resource URL
    is printed with a malformed single slash after `https:`; the example request and documented hostname
    establish the HTTPS server base used here.

    Args:
        dataresource (GetTpsSaleTransactionsDataresource):
        lang (GetTpsSaleTransactionsLang):
        format_ (GetTpsSaleTransactionsFormat):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetTpsSaleTransactionsResponse200
    """

    return sync_detailed(
        dataresource=dataresource,
        lang=lang,
        format_=format_,
        client=client,
    ).parsed


async def asyncio_detailed(
    dataresource: GetTpsSaleTransactionsDataresource,
    lang: GetTpsSaleTransactionsLang,
    format_: GetTpsSaleTransactionsFormat,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetTpsSaleTransactionsResponse200]:
    """Get TPS sale transactions

     Returns sales transaction data for the Tenants Purchase Scheme in JSON. The documented resource URL
    is printed with a malformed single slash after `https:`; the example request and documented hostname
    establish the HTTPS server base used here.

    Args:
        dataresource (GetTpsSaleTransactionsDataresource):
        lang (GetTpsSaleTransactionsLang):
        format_ (GetTpsSaleTransactionsFormat):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetTpsSaleTransactionsResponse200]
    """

    kwargs = _get_kwargs(
        dataresource=dataresource,
        lang=lang,
        format_=format_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dataresource: GetTpsSaleTransactionsDataresource,
    lang: GetTpsSaleTransactionsLang,
    format_: GetTpsSaleTransactionsFormat,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetTpsSaleTransactionsResponse200 | None:
    """Get TPS sale transactions

     Returns sales transaction data for the Tenants Purchase Scheme in JSON. The documented resource URL
    is printed with a malformed single slash after `https:`; the example request and documented hostname
    establish the HTTPS server base used here.

    Args:
        dataresource (GetTpsSaleTransactionsDataresource):
        lang (GetTpsSaleTransactionsLang):
        format_ (GetTpsSaleTransactionsFormat):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetTpsSaleTransactionsResponse200
    """

    return (
        await asyncio_detailed(
            dataresource=dataresource,
            lang=lang,
            format_=format_,
            client=client,
        )
    ).parsed
