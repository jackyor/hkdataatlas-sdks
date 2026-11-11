from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.route_stop_eta_by_stop_id_response import RouteStopEtaByStopIdResponse
from ...types import Response


def _get_kwargs(
    route_id: int,
    stop_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/eta/route-stop/{route_id}/{stop_id}".format(
            route_id=quote(str(route_id), safe=""),
            stop_id=quote(str(stop_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RouteStopEtaByStopIdResponse | None:
    if response.status_code == 200:
        response_200 = RouteStopEtaByStopIdResponse.from_dict(response.json())

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
) -> Response[Any | RouteStopEtaByStopIdResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    route_id: int,
    stop_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | RouteStopEtaByStopIdResponse]:
    """Retrieve ETA for a route and stop ID

     Returns ETA information for occurrences of the specified stop ID along the route. This is distinct
    from the documented form that identifies a stop by stop sequence.

    Args:
        route_id (int):
        stop_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RouteStopEtaByStopIdResponse]
    """

    kwargs = _get_kwargs(
        route_id=route_id,
        stop_id=stop_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    route_id: int,
    stop_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Any | RouteStopEtaByStopIdResponse | None:
    """Retrieve ETA for a route and stop ID

     Returns ETA information for occurrences of the specified stop ID along the route. This is distinct
    from the documented form that identifies a stop by stop sequence.

    Args:
        route_id (int):
        stop_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RouteStopEtaByStopIdResponse
    """

    return sync_detailed(
        route_id=route_id,
        stop_id=stop_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    route_id: int,
    stop_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | RouteStopEtaByStopIdResponse]:
    """Retrieve ETA for a route and stop ID

     Returns ETA information for occurrences of the specified stop ID along the route. This is distinct
    from the documented form that identifies a stop by stop sequence.

    Args:
        route_id (int):
        stop_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RouteStopEtaByStopIdResponse]
    """

    kwargs = _get_kwargs(
        route_id=route_id,
        stop_id=stop_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    route_id: int,
    stop_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Any | RouteStopEtaByStopIdResponse | None:
    """Retrieve ETA for a route and stop ID

     Returns ETA information for occurrences of the specified stop ID along the route. This is distinct
    from the documented form that identifies a stop by stop sequence.

    Args:
        route_id (int):
        stop_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RouteStopEtaByStopIdResponse
    """

    return (
        await asyncio_detailed(
            route_id=route_id,
            stop_id=stop_id,
            client=client,
        )
    ).parsed
