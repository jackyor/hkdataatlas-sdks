from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.estimated_arrivals_request import EstimatedArrivalsRequest
from ...models.estimated_arrivals_response import EstimatedArrivalsResponse
from ...models.route_stops_request import RouteStopsRequest
from ...models.stop_operations_action import (
    StopOperationsAction,
)
from ...models.stops_response import StopsResponse
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: EstimatedArrivalsRequest | RouteStopsRequest,
    action: StopOperationsAction,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_action: str = action
    params["action"] = json_action

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/stop.php",
        "params": params,
    }

    if isinstance(body, RouteStopsRequest):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> EstimatedArrivalsResponse | StopsResponse | None:
    if response.status_code == 200:

        def _parse_response_200(
            data: object,
        ) -> EstimatedArrivalsResponse | StopsResponse:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = StopsResponse.from_dict(data)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = EstimatedArrivalsResponse.from_dict(data)

            return response_200_type_1

        response_200 = _parse_response_200(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[EstimatedArrivalsResponse | StopsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: EstimatedArrivalsRequest | RouteStopsRequest,
    action: StopOperationsAction,
) -> Response[EstimatedArrivalsResponse | StopsResponse]:
    """Get stops of a route or estimated arrivals

    Args:
        action (StopOperationsAction):
        body (EstimatedArrivalsRequest | RouteStopsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EstimatedArrivalsResponse | StopsResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        action=action,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: EstimatedArrivalsRequest | RouteStopsRequest,
    action: StopOperationsAction,
) -> EstimatedArrivalsResponse | StopsResponse | None:
    """Get stops of a route or estimated arrivals

    Args:
        action (StopOperationsAction):
        body (EstimatedArrivalsRequest | RouteStopsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EstimatedArrivalsResponse | StopsResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        action=action,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: EstimatedArrivalsRequest | RouteStopsRequest,
    action: StopOperationsAction,
) -> Response[EstimatedArrivalsResponse | StopsResponse]:
    """Get stops of a route or estimated arrivals

    Args:
        action (StopOperationsAction):
        body (EstimatedArrivalsRequest | RouteStopsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EstimatedArrivalsResponse | StopsResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        action=action,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: EstimatedArrivalsRequest | RouteStopsRequest,
    action: StopOperationsAction,
) -> EstimatedArrivalsResponse | StopsResponse | None:
    """Get stops of a route or estimated arrivals

    Args:
        action (StopOperationsAction):
        body (EstimatedArrivalsRequest | RouteStopsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EstimatedArrivalsResponse | StopsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            action=action,
        )
    ).parsed
