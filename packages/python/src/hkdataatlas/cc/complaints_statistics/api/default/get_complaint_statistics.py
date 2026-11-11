from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.complaint_statistics_response import ComplaintStatisticsResponse
from ...models.get_complaint_statistics_lang import (
    GetComplaintStatisticsLang,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    year: None | str | Unset = UNSET,
    lang: GetComplaintStatisticsLang | Unset = "tc",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_year: None | str | Unset
    if isinstance(year, Unset):
        json_year = UNSET
    else:
        json_year = year
    params["year"] = json_year

    json_lang: str | Unset = UNSET
    if not isinstance(lang, Unset):
        json_lang = lang

    params["lang"] = json_lang

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/node/32290/export-complaints/json",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | ComplaintStatisticsResponse | None:
    if response.status_code == 200:
        response_200 = ComplaintStatisticsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if response.status_code == 503:
        response_503 = cast(Any, None)
        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | ComplaintStatisticsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    year: None | str | Unset = UNSET,
    lang: GetComplaintStatisticsLang | Unset = "tc",
) -> Response[Any | ComplaintStatisticsResponse]:
    """Get complaint statistics

     Returns complaint statistics. The API documentation says the data covers the recent three years.

    Args:
        year (None | str | Unset):
        lang (GetComplaintStatisticsLang | Unset):  Default: 'tc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ComplaintStatisticsResponse]
    """

    kwargs = _get_kwargs(
        year=year,
        lang=lang,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    year: None | str | Unset = UNSET,
    lang: GetComplaintStatisticsLang | Unset = "tc",
) -> Any | ComplaintStatisticsResponse | None:
    """Get complaint statistics

     Returns complaint statistics. The API documentation says the data covers the recent three years.

    Args:
        year (None | str | Unset):
        lang (GetComplaintStatisticsLang | Unset):  Default: 'tc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ComplaintStatisticsResponse
    """

    return sync_detailed(
        client=client,
        year=year,
        lang=lang,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    year: None | str | Unset = UNSET,
    lang: GetComplaintStatisticsLang | Unset = "tc",
) -> Response[Any | ComplaintStatisticsResponse]:
    """Get complaint statistics

     Returns complaint statistics. The API documentation says the data covers the recent three years.

    Args:
        year (None | str | Unset):
        lang (GetComplaintStatisticsLang | Unset):  Default: 'tc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ComplaintStatisticsResponse]
    """

    kwargs = _get_kwargs(
        year=year,
        lang=lang,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    year: None | str | Unset = UNSET,
    lang: GetComplaintStatisticsLang | Unset = "tc",
) -> Any | ComplaintStatisticsResponse | None:
    """Get complaint statistics

     Returns complaint statistics. The API documentation says the data covers the recent three years.

    Args:
        year (None | str | Unset):
        lang (GetComplaintStatisticsLang | Unset):  Default: 'tc'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ComplaintStatisticsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            year=year,
            lang=lang,
        )
    ).parsed
