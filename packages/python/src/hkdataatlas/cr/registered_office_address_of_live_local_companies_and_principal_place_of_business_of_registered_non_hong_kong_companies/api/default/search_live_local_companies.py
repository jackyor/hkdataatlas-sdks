from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.local_company_record import LocalCompanyRecord
from ...models.search_live_local_companies_format import (
    SearchLiveLocalCompaniesFormat,
)
from ...models.search_live_local_companies_query_0_key_1 import (
    SearchLiveLocalCompaniesQuery0Key1,
)
from ...models.search_live_local_companies_query_0_key_2 import (
    SearchLiveLocalCompaniesQuery0Key2,
)
from ...types import UNSET, Response


def _get_kwargs(
    *,
    query0key1: SearchLiveLocalCompaniesQuery0Key1,
    query0key2: SearchLiveLocalCompaniesQuery0Key2,
    query0key3: str,
    format_: SearchLiveLocalCompaniesFormat,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_query0key1: str = query0key1
    params["query[0][key1]"] = json_query0key1

    json_query0key2: str = query0key2
    params["query[0][key2]"] = json_query0key2

    params["query[0][key3]"] = query0key3

    json_format_: str = format_
    params["format"] = json_format_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/local/search",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> list[LocalCompanyRecord] | None:
    if response.status_code == 200:
        media_type = (
            response.headers.get("content-type", "").split(";", 1)[0].strip().lower()
        )
        if media_type != "application/json" and not media_type.endswith("+json"):
            return None
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = LocalCompanyRecord.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[list[LocalCompanyRecord]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    query0key1: SearchLiveLocalCompaniesQuery0Key1,
    query0key2: SearchLiveLocalCompaniesQuery0Key2,
    query0key3: str,
    format_: SearchLiveLocalCompaniesFormat,
) -> Response[list[LocalCompanyRecord]]:
    """Search live local companies

     Searches the registered office address data for live local companies. The dataset is updated daily.
    The API Builder documentation specifies the query parameters and output format; the dictionary
    provides fields but does not specify a complete response envelope.

    Args:
        query0key1 (SearchLiveLocalCompaniesQuery0Key1):
        query0key2 (SearchLiveLocalCompaniesQuery0Key2):
        query0key3 (str):
        format_ (SearchLiveLocalCompaniesFormat):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[LocalCompanyRecord]]
    """

    kwargs = _get_kwargs(
        query0key1=query0key1,
        query0key2=query0key2,
        query0key3=query0key3,
        format_=format_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    query0key1: SearchLiveLocalCompaniesQuery0Key1,
    query0key2: SearchLiveLocalCompaniesQuery0Key2,
    query0key3: str,
    format_: SearchLiveLocalCompaniesFormat,
) -> list[LocalCompanyRecord] | None:
    """Search live local companies

     Searches the registered office address data for live local companies. The dataset is updated daily.
    The API Builder documentation specifies the query parameters and output format; the dictionary
    provides fields but does not specify a complete response envelope.

    Args:
        query0key1 (SearchLiveLocalCompaniesQuery0Key1):
        query0key2 (SearchLiveLocalCompaniesQuery0Key2):
        query0key3 (str):
        format_ (SearchLiveLocalCompaniesFormat):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[LocalCompanyRecord]
    """

    return sync_detailed(
        client=client,
        query0key1=query0key1,
        query0key2=query0key2,
        query0key3=query0key3,
        format_=format_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    query0key1: SearchLiveLocalCompaniesQuery0Key1,
    query0key2: SearchLiveLocalCompaniesQuery0Key2,
    query0key3: str,
    format_: SearchLiveLocalCompaniesFormat,
) -> Response[list[LocalCompanyRecord]]:
    """Search live local companies

     Searches the registered office address data for live local companies. The dataset is updated daily.
    The API Builder documentation specifies the query parameters and output format; the dictionary
    provides fields but does not specify a complete response envelope.

    Args:
        query0key1 (SearchLiveLocalCompaniesQuery0Key1):
        query0key2 (SearchLiveLocalCompaniesQuery0Key2):
        query0key3 (str):
        format_ (SearchLiveLocalCompaniesFormat):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[LocalCompanyRecord]]
    """

    kwargs = _get_kwargs(
        query0key1=query0key1,
        query0key2=query0key2,
        query0key3=query0key3,
        format_=format_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    query0key1: SearchLiveLocalCompaniesQuery0Key1,
    query0key2: SearchLiveLocalCompaniesQuery0Key2,
    query0key3: str,
    format_: SearchLiveLocalCompaniesFormat,
) -> list[LocalCompanyRecord] | None:
    """Search live local companies

     Searches the registered office address data for live local companies. The dataset is updated daily.
    The API Builder documentation specifies the query parameters and output format; the dictionary
    provides fields but does not specify a complete response envelope.

    Args:
        query0key1 (SearchLiveLocalCompaniesQuery0Key1):
        query0key2 (SearchLiveLocalCompaniesQuery0Key2):
        query0key3 (str):
        format_ (SearchLiveLocalCompaniesFormat):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[LocalCompanyRecord]
    """

    return (
        await asyncio_detailed(
            client=client,
            query0key1=query0key1,
            query0key2=query0key2,
            query0key3=query0key3,
            format_=format_,
        )
    ).parsed
