from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_execution_error import ApiExecutionError
from ...models.error import Error
from ...models.stop_eta_response import StopEtaResponse
from ...types import Response


def _get_kwargs(
    stop_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/transport/kmb/stop-eta/{stop_id}".format(
            stop_id=quote(str(stop_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ApiExecutionError | Error | StopEtaResponse | None:
    if response.status_code == 200:
        response_200 = StopEtaResponse.from_dict(response.json())

        return response_200

    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = ApiExecutionError.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ApiExecutionError | Error | StopEtaResponse]:
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
) -> Response[ApiExecutionError | Error | StopEtaResponse]:
    """Get ETA for all routes at a stop

     Returns ETA information for all routes at the specified stop. Returned ETA information for a
    route/service type may also be included for other service types of the same route number when they
    share the bus stop.

    Args:
        stop_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiExecutionError | Error | StopEtaResponse]
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
) -> ApiExecutionError | Error | StopEtaResponse | None:
    """Get ETA for all routes at a stop

     Returns ETA information for all routes at the specified stop. Returned ETA information for a
    route/service type may also be included for other service types of the same route number when they
    share the bus stop.

    Args:
        stop_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiExecutionError | Error | StopEtaResponse
    """

    return sync_detailed(
        stop_id=stop_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    stop_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ApiExecutionError | Error | StopEtaResponse]:
    """Get ETA for all routes at a stop

     Returns ETA information for all routes at the specified stop. Returned ETA information for a
    route/service type may also be included for other service types of the same route number when they
    share the bus stop.

    Args:
        stop_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiExecutionError | Error | StopEtaResponse]
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
) -> ApiExecutionError | Error | StopEtaResponse | None:
    """Get ETA for all routes at a stop

     Returns ETA information for all routes at the specified stop. Returned ETA information for a
    route/service type may also be included for other service types of the same route number when they
    share the bus stop.

    Args:
        stop_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiExecutionError | Error | StopEtaResponse
    """

    return (
        await asyncio_detailed(
            stop_id=stop_id,
            client=client,
        )
    ).parsed
