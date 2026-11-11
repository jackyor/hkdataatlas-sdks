from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.last_update_route_list_response import LastUpdateRouteListResponse
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/last-update/route",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | LastUpdateRouteListResponse | None:
    if response.status_code == 200:
        response_200 = LastUpdateRouteListResponse.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | LastUpdateRouteListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | LastUpdateRouteListResponse]:
    """Retrieve last-update dates for routes

     Documented for GET /last-update/route. The response table describes arrays of route updates under
    data.data_timestamp; the documented examples show this array for route-related listing requests.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | LastUpdateRouteListResponse]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> Any | LastUpdateRouteListResponse | None:
    """Retrieve last-update dates for routes

     Documented for GET /last-update/route. The response table describes arrays of route updates under
    data.data_timestamp; the documented examples show this array for route-related listing requests.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | LastUpdateRouteListResponse
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | LastUpdateRouteListResponse]:
    """Retrieve last-update dates for routes

     Documented for GET /last-update/route. The response table describes arrays of route updates under
    data.data_timestamp; the documented examples show this array for route-related listing requests.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | LastUpdateRouteListResponse]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> Any | LastUpdateRouteListResponse | None:
    """Retrieve last-update dates for routes

     Documented for GET /last-update/route. The response table describes arrays of route updates under
    data.data_timestamp; the documented examples show this array for route-related listing requests.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | LastUpdateRouteListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
