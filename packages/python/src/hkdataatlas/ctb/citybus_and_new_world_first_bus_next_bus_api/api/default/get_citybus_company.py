from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_citybus_company_company_id import (
    GetCitybusCompanyCompanyId,
)
from ...models.get_citybus_company_response import GetCitybusCompanyResponse
from ...types import Response


def _get_kwargs(
    company_id: GetCitybusCompanyCompanyId,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/transport/citybus/company/{company_id}".format(
            company_id=quote(str(company_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | GetCitybusCompanyResponse | None:
    if response.status_code == 200:
        response_200 = GetCitybusCompanyResponse.from_dict(response.json())

        return response_200

    if response.status_code == 422:
        response_422 = response.json()
        return response_422

    if response.status_code == 429:
        response_429 = response.json()
        return response_429

    if response.status_code == 500:
        response_500 = response.json()
        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | GetCitybusCompanyResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    company_id: GetCitybusCompanyCompanyId,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetCitybusCompanyResponse]:
    """Company information

    Args:
        company_id (GetCitybusCompanyCompanyId):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetCitybusCompanyResponse]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    company_id: GetCitybusCompanyCompanyId,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetCitybusCompanyResponse | None:
    """Company information

    Args:
        company_id (GetCitybusCompanyCompanyId):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetCitybusCompanyResponse
    """

    return sync_detailed(
        company_id=company_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    company_id: GetCitybusCompanyCompanyId,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetCitybusCompanyResponse]:
    """Company information

    Args:
        company_id (GetCitybusCompanyCompanyId):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetCitybusCompanyResponse]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: GetCitybusCompanyCompanyId,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetCitybusCompanyResponse | None:
    """Company information

    Args:
        company_id (GetCitybusCompanyCompanyId):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetCitybusCompanyResponse
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            client=client,
        )
    ).parsed
