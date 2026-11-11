from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_pier_pier_id import GetPierPierId
from ...models.pier_response import PierResponse
from ...types import Response


def _get_kwargs(
    pier_id: GetPierPierId,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/opendata/pier/{pier_id}".format(
            pier_id=quote(str(pier_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | PierResponse | None:
    if response.status_code == 200:
        response_200 = PierResponse.from_dict(response.json())

        return response_200

    if response.status_code == 422:
        response_422 = cast(Any, None)
        return response_422

    if response.status_code == 429:
        response_429 = cast(Any, None)
        return response_429

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | PierResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    pier_id: GetPierPierId,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | PierResponse]:
    """Get pier information

     Returns the respective pier information for a pier ID. Documented valid pier IDs are 1 (Central Pier
    4), 2 (Central Pier 6), 3 (Yung Shue Wan), 4 (Peng Chau), 5 (Sok Kwu Wan), and 6 (Hei Ling Chau).

    Args:
        pier_id (GetPierPierId):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PierResponse]
    """

    kwargs = _get_kwargs(
        pier_id=pier_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    pier_id: GetPierPierId,
    *,
    client: AuthenticatedClient | Client,
) -> Any | PierResponse | None:
    """Get pier information

     Returns the respective pier information for a pier ID. Documented valid pier IDs are 1 (Central Pier
    4), 2 (Central Pier 6), 3 (Yung Shue Wan), 4 (Peng Chau), 5 (Sok Kwu Wan), and 6 (Hei Ling Chau).

    Args:
        pier_id (GetPierPierId):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PierResponse
    """

    return sync_detailed(
        pier_id=pier_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    pier_id: GetPierPierId,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | PierResponse]:
    """Get pier information

     Returns the respective pier information for a pier ID. Documented valid pier IDs are 1 (Central Pier
    4), 2 (Central Pier 6), 3 (Yung Shue Wan), 4 (Peng Chau), 5 (Sok Kwu Wan), and 6 (Hei Ling Chau).

    Args:
        pier_id (GetPierPierId):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PierResponse]
    """

    kwargs = _get_kwargs(
        pier_id=pier_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    pier_id: GetPierPierId,
    *,
    client: AuthenticatedClient | Client,
) -> Any | PierResponse | None:
    """Get pier information

     Returns the respective pier information for a pier ID. Documented valid pier IDs are 1 (Central Pier
    4), 2 (Central Pier 6), 3 (Yung Shue Wan), 4 (Peng Chau), 5 (Sok Kwu Wan), and 6 (Hei Ling Chau).

    Args:
        pier_id (GetPierPierId):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PierResponse
    """

    return (
        await asyncio_detailed(
            pier_id=pier_id,
            client=client,
        )
    ).parsed
