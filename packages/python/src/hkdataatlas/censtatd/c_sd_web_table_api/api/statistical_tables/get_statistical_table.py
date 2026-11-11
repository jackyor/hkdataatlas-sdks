from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_statistical_table_full_series import (
    GetStatisticalTableFullSeries,
)
from ...models.get_statistical_table_lang import (
    GetStatisticalTableLang,
)
from ...models.table_response import TableResponse
from ...types import UNSET, Response


def _get_kwargs(
    *,
    id: str,
    lang: GetStatisticalTableLang,
    full_series: GetStatisticalTableFullSeries,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["id"] = id

    json_lang: str = lang
    params["lang"] = json_lang

    json_full_series: str = full_series
    params["full_series"] = json_full_series

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/get.php",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | TableResponse | None:
    if response.status_code == 200:
        response_200 = TableResponse.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if 400 <= response.status_code <= 499:
        response_4xx = cast(Any, None)
        return response_4xx

    if 500 <= response.status_code <= 599:
        response_5xx = cast(Any, None)
        return response_5xx

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | TableResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    id: str,
    lang: GetStatisticalTableLang,
    full_series: GetStatisticalTableFullSeries,
) -> Response[Any | TableResponse]:
    """Retrieve the statistics for Web Tables

     Returns the requested C&SD Web Tables in JSON format.

    Args:
        id (str):
        lang (GetStatisticalTableLang):
        full_series (GetStatisticalTableFullSeries):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | TableResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        lang=lang,
        full_series=full_series,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    id: str,
    lang: GetStatisticalTableLang,
    full_series: GetStatisticalTableFullSeries,
) -> Any | TableResponse | None:
    """Retrieve the statistics for Web Tables

     Returns the requested C&SD Web Tables in JSON format.

    Args:
        id (str):
        lang (GetStatisticalTableLang):
        full_series (GetStatisticalTableFullSeries):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | TableResponse
    """

    return sync_detailed(
        client=client,
        id=id,
        lang=lang,
        full_series=full_series,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    id: str,
    lang: GetStatisticalTableLang,
    full_series: GetStatisticalTableFullSeries,
) -> Response[Any | TableResponse]:
    """Retrieve the statistics for Web Tables

     Returns the requested C&SD Web Tables in JSON format.

    Args:
        id (str):
        lang (GetStatisticalTableLang):
        full_series (GetStatisticalTableFullSeries):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | TableResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        lang=lang,
        full_series=full_series,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    id: str,
    lang: GetStatisticalTableLang,
    full_series: GetStatisticalTableFullSeries,
) -> Any | TableResponse | None:
    """Retrieve the statistics for Web Tables

     Returns the requested C&SD Web Tables in JSON format.

    Args:
        id (str):
        lang (GetStatisticalTableLang):
        full_series (GetStatisticalTableFullSeries):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | TableResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            lang=lang,
            full_series=full_series,
        )
    ).parsed
