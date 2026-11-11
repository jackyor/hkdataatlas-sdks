from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_execution_error import ApiExecutionError
from ...models.error import Error
from ...models.eta_response import EtaResponse
from ...types import Response


def _get_kwargs(
    stop_id: str,
    route: str,
    service_type: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/transport/kmb/eta/{stop_id}/{route}/{service_type}".format(
            stop_id=quote(str(stop_id), safe=""),
            route=quote(str(route), safe=""),
            service_type=quote(str(service_type), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ApiExecutionError | Error | EtaResponse | None:
    if response.status_code == 200:
        response_200 = EtaResponse.from_dict(response.json())

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
) -> Response[ApiExecutionError | Error | EtaResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    stop_id: str,
    route: str,
    service_type: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ApiExecutionError | Error | EtaResponse]:
    """Get ETA for a route at a stop

     Returns ETA information for the specified stop, route, and service type. Results may also include
    ETA data for other service types of the same route number when they share the stop. Up to three ETA
    records may be returned for each direction.

    Args:
        stop_id (str):
        route (str):
        service_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiExecutionError | Error | EtaResponse]
    """

    kwargs = _get_kwargs(
        stop_id=stop_id,
        route=route,
        service_type=service_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    stop_id: str,
    route: str,
    service_type: str,
    *,
    client: AuthenticatedClient | Client,
) -> ApiExecutionError | Error | EtaResponse | None:
    """Get ETA for a route at a stop

     Returns ETA information for the specified stop, route, and service type. Results may also include
    ETA data for other service types of the same route number when they share the stop. Up to three ETA
    records may be returned for each direction.

    Args:
        stop_id (str):
        route (str):
        service_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiExecutionError | Error | EtaResponse
    """

    return sync_detailed(
        stop_id=stop_id,
        route=route,
        service_type=service_type,
        client=client,
    ).parsed


async def asyncio_detailed(
    stop_id: str,
    route: str,
    service_type: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ApiExecutionError | Error | EtaResponse]:
    """Get ETA for a route at a stop

     Returns ETA information for the specified stop, route, and service type. Results may also include
    ETA data for other service types of the same route number when they share the stop. Up to three ETA
    records may be returned for each direction.

    Args:
        stop_id (str):
        route (str):
        service_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiExecutionError | Error | EtaResponse]
    """

    kwargs = _get_kwargs(
        stop_id=stop_id,
        route=route,
        service_type=service_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    stop_id: str,
    route: str,
    service_type: str,
    *,
    client: AuthenticatedClient | Client,
) -> ApiExecutionError | Error | EtaResponse | None:
    """Get ETA for a route at a stop

     Returns ETA information for the specified stop, route, and service type. Results may also include
    ETA data for other service types of the same route number when they share the stop. Up to three ETA
    records may be returned for each direction.

    Args:
        stop_id (str):
        route (str):
        service_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiExecutionError | Error | EtaResponse
    """

    return (
        await asyncio_detailed(
            stop_id=stop_id,
            route=route,
            service_type=service_type,
            client=client,
        )
    ).parsed
