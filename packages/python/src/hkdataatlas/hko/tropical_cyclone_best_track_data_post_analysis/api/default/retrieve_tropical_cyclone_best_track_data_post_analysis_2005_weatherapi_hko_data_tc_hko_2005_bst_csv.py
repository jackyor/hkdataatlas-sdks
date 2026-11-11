from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/weatherAPI/hko_data/tc/HKO2005BST.csv",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> str | None:
    if response.status_code == 200:
        response_200 = response.text
        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[str]:
    """Retrieve Tropical cyclone best track data (post analysis) (2005)

     Read-only retrieval of the exact publisher-listed CSV resource
    https://data.weather.gov.hk/weatherAPI/hko_data/tc/HKO2005BST.csv. This is a published data-file
    link; no additional hosted API or URL template is asserted. Dictionary components describe
    contextual record fields without establishing the complete payload shape. Authentication is
    unspecified.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[str]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> str | None:
    """Retrieve Tropical cyclone best track data (post analysis) (2005)

     Read-only retrieval of the exact publisher-listed CSV resource
    https://data.weather.gov.hk/weatherAPI/hko_data/tc/HKO2005BST.csv. This is a published data-file
    link; no additional hosted API or URL template is asserted. Dictionary components describe
    contextual record fields without establishing the complete payload shape. Authentication is
    unspecified.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        str
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[str]:
    """Retrieve Tropical cyclone best track data (post analysis) (2005)

     Read-only retrieval of the exact publisher-listed CSV resource
    https://data.weather.gov.hk/weatherAPI/hko_data/tc/HKO2005BST.csv. This is a published data-file
    link; no additional hosted API or URL template is asserted. Dictionary components describe
    contextual record fields without establishing the complete payload shape. Authentication is
    unspecified.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[str]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> str | None:
    """Retrieve Tropical cyclone best track data (post analysis) (2005)

     Read-only retrieval of the exact publisher-listed CSV resource
    https://data.weather.gov.hk/weatherAPI/hko_data/tc/HKO2005BST.csv. This is a published data-file
    link; no additional hosted API or URL template is asserted. Dictionary components describe
    contextual record fields without establishing the complete payload shape. Authentication is
    unspecified.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        str
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
