from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.route_stop_eta_sequence_response import RouteStopEtaSequenceResponse
from ...types import Response


def _get_kwargs(
    route_id: int,
    route_seq: int,
    stop_seq: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/eta/route-stop/{route_id}/{route_seq}/{stop_seq}".format(
            route_id=quote(str(route_id), safe=""),
            route_seq=quote(str(route_seq), safe=""),
            stop_seq=quote(str(stop_seq), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RouteStopEtaSequenceResponse | None:
    if response.status_code == 200:
        response_200 = RouteStopEtaSequenceResponse.from_dict(response.json())

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
) -> Response[Any | RouteStopEtaSequenceResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    route_id: int,
    route_seq: int,
    stop_seq: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | RouteStopEtaSequenceResponse]:
    """Retrieve ETA for a route stop by sequence

     Returns the ETA information for the specified route ID, route sequence, and stop sequence. The
    documented data structure differs according to whether ETA service is enabled.

    Args:
        route_id (int):
        route_seq (int):
        stop_seq (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RouteStopEtaSequenceResponse]
    """

    kwargs = _get_kwargs(
        route_id=route_id,
        route_seq=route_seq,
        stop_seq=stop_seq,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    route_id: int,
    route_seq: int,
    stop_seq: int,
    *,
    client: AuthenticatedClient | Client,
) -> Any | RouteStopEtaSequenceResponse | None:
    """Retrieve ETA for a route stop by sequence

     Returns the ETA information for the specified route ID, route sequence, and stop sequence. The
    documented data structure differs according to whether ETA service is enabled.

    Args:
        route_id (int):
        route_seq (int):
        stop_seq (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RouteStopEtaSequenceResponse
    """

    return sync_detailed(
        route_id=route_id,
        route_seq=route_seq,
        stop_seq=stop_seq,
        client=client,
    ).parsed


async def asyncio_detailed(
    route_id: int,
    route_seq: int,
    stop_seq: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | RouteStopEtaSequenceResponse]:
    """Retrieve ETA for a route stop by sequence

     Returns the ETA information for the specified route ID, route sequence, and stop sequence. The
    documented data structure differs according to whether ETA service is enabled.

    Args:
        route_id (int):
        route_seq (int):
        stop_seq (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RouteStopEtaSequenceResponse]
    """

    kwargs = _get_kwargs(
        route_id=route_id,
        route_seq=route_seq,
        stop_seq=stop_seq,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    route_id: int,
    route_seq: int,
    stop_seq: int,
    *,
    client: AuthenticatedClient | Client,
) -> Any | RouteStopEtaSequenceResponse | None:
    """Retrieve ETA for a route stop by sequence

     Returns the ETA information for the specified route ID, route sequence, and stop sequence. The
    documented data structure differs according to whether ETA service is enabled.

    Args:
        route_id (int):
        route_seq (int):
        stop_seq (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RouteStopEtaSequenceResponse
    """

    return (
        await asyncio_detailed(
            route_id=route_id,
            route_seq=route_seq,
            stop_seq=stop_seq,
            client=client,
        )
    ).parsed
