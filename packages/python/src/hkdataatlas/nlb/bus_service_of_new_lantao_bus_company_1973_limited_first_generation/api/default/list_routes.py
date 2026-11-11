from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_routes_action import ListRoutesAction
from ...models.routes_response import RoutesResponse
from ...types import UNSET, Response


def _get_kwargs(
    *,
    action: ListRoutesAction,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_action: str = action
    params["action"] = json_action

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/route.php",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> RoutesResponse | None:
    if response.status_code == 200:
        response_200 = RoutesResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[RoutesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    action: ListRoutesAction,
) -> Response[RoutesResponse]:
    """Get list of all routes

     The publisher page4 documents POST route.php?action=list with application/json but leaves request
    body and sample body blank. No required object schema is asserted. A source-backed no-body request
    is a separate observation, not a universal body constraint.

    Args:
        action (ListRoutesAction):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RoutesResponse]
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
    action: ListRoutesAction,
) -> RoutesResponse | None:
    """Get list of all routes

     The publisher page4 documents POST route.php?action=list with application/json but leaves request
    body and sample body blank. No required object schema is asserted. A source-backed no-body request
    is a separate observation, not a universal body constraint.

    Args:
        action (ListRoutesAction):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RoutesResponse
    """

    return sync_detailed(
        client=client,
        action=action,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    action: ListRoutesAction,
) -> Response[RoutesResponse]:
    """Get list of all routes

     The publisher page4 documents POST route.php?action=list with application/json but leaves request
    body and sample body blank. No required object schema is asserted. A source-backed no-body request
    is a separate observation, not a universal body constraint.

    Args:
        action (ListRoutesAction):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RoutesResponse]
    """

    kwargs = _get_kwargs(
        action=action,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    action: ListRoutesAction,
) -> RoutesResponse | None:
    """Get list of all routes

     The publisher page4 documents POST route.php?action=list with application/json but leaves request
    body and sample body blank. No required object schema is asserted. A source-backed no-body request
    is a separate observation, not a universal body constraint.

    Args:
        action (ListRoutesAction):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RoutesResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            action=action,
        )
    ).parsed
