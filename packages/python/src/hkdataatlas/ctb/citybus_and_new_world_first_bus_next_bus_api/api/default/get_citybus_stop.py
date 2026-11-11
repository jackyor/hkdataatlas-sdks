from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_citybus_stop_response import GetCitybusStopResponse
from ...types import Response


def _get_kwargs(
    stop_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/transport/citybus/stop/{stop_id}".format(
            stop_id=quote(str(stop_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | GetCitybusStopResponse | None:
    if response.status_code == 200:
        response_200 = GetCitybusStopResponse.from_dict(response.json())

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
) -> Response[Any | GetCitybusStopResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    stop_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetCitybusStopResponse]:
    """Stop information

    Args:
        stop_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetCitybusStopResponse]
    """

    kwargs = _get_kwargs(
        stop_id=stop_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    stop_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetCitybusStopResponse | None:
    """Stop information

    Args:
        stop_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetCitybusStopResponse
    """

    return sync_detailed(
        stop_id=stop_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    stop_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetCitybusStopResponse]:
    """Stop information

    Args:
        stop_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetCitybusStopResponse]
    """

    kwargs = _get_kwargs(
        stop_id=stop_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    stop_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetCitybusStopResponse | None:
    """Stop information

    Args:
        stop_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetCitybusStopResponse
    """

    return (
        await asyncio_detailed(
            stop_id=stop_id,
            client=client,
        )
    ).parsed
