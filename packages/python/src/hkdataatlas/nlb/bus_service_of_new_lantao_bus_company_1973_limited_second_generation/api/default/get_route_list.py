from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_route_list_action import (
    GetRouteListAction,
)
from ...models.get_route_list_response_200 import GetRouteListResponse200
from ...types import UNSET, Response


def _get_kwargs(
    *,
    action: GetRouteListAction,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_action: str = action
    params["action"] = json_action

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/route.php",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> GetRouteListResponse200 | None:
    if response.status_code == 200:
        response_200 = GetRouteListResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[GetRouteListResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    action: GetRouteListAction,
) -> Response[GetRouteListResponse200]:
    """Get list of all routes

    Args:
        action (GetRouteListAction):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetRouteListResponse200]
    """

    kwargs = _get_kwargs(
        action=action,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    action: GetRouteListAction,
) -> GetRouteListResponse200 | None:
    """Get list of all routes

    Args:
        action (GetRouteListAction):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetRouteListResponse200
    """

    return sync_detailed(
        client=client,
        action=action,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    action: GetRouteListAction,
) -> Response[GetRouteListResponse200]:
    """Get list of all routes

    Args:
        action (GetRouteListAction):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetRouteListResponse200]
    """

    kwargs = _get_kwargs(
        action=action,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    action: GetRouteListAction,
) -> GetRouteListResponse200 | None:
    """Get list of all routes

    Args:
        action (GetRouteListAction):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetRouteListResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            action=action,
        )
    ).parsed
