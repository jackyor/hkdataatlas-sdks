from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.estimated_arrivals_response import EstimatedArrivalsResponse
from ...models.get_route_stops_or_estimated_arrivals_action import (
    GetRouteStopsOrEstimatedArrivalsAction,
)
from ...models.get_route_stops_or_estimated_arrivals_language import (
    GetRouteStopsOrEstimatedArrivalsLanguage,
)
from ...models.get_route_stops_or_estimated_arrivals_response_200_type_0 import (
    GetRouteStopsOrEstimatedArrivalsResponse200Type0,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    action: GetRouteStopsOrEstimatedArrivalsAction,
    route_id: int,
    stop_id: int | Unset = UNSET,
    language: GetRouteStopsOrEstimatedArrivalsLanguage | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_action: str = action
    params["action"] = json_action

    params["routeId"] = route_id

    params["stopId"] = stop_id

    json_language: str | Unset = UNSET
    if not isinstance(language, Unset):
        json_language = language

    params["language"] = json_language

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/stop.php",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> (
    EstimatedArrivalsResponse | GetRouteStopsOrEstimatedArrivalsResponse200Type0 | None
):
    if response.status_code == 200:

        def _parse_response_200(
            data: object,
        ) -> (
            EstimatedArrivalsResponse | GetRouteStopsOrEstimatedArrivalsResponse200Type0
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = (
                    GetRouteStopsOrEstimatedArrivalsResponse200Type0.from_dict(data)
                )

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
) -> Response[
    EstimatedArrivalsResponse | GetRouteStopsOrEstimatedArrivalsResponse200Type0
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    action: GetRouteStopsOrEstimatedArrivalsAction,
    route_id: int,
    stop_id: int | Unset = UNSET,
    language: GetRouteStopsOrEstimatedArrivalsLanguage | Unset = UNSET,
) -> Response[
    EstimatedArrivalsResponse | GetRouteStopsOrEstimatedArrivalsResponse200Type0
]:
    """Get stops of a route or estimated arrivals for a stop

     The `list` action returns stops ordered by stop sequence of the route. The `estimatedArrivals`
    action returns arrival information. Scheduled arrival time is calculated from the timetable; actual
    departure time may change subject to operational adjustment. Estimated arrival time is calculated
    from historical data, not real-time traffic data. The `estimatedArrivals` property does not exist if
    the bus estimated arrival time for that route is currently unavailable.

    Args:
        action (GetRouteStopsOrEstimatedArrivalsAction):
        route_id (int):
        stop_id (int | Unset):
        language (GetRouteStopsOrEstimatedArrivalsLanguage | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EstimatedArrivalsResponse | GetRouteStopsOrEstimatedArrivalsResponse200Type0]
    """

    kwargs = _get_kwargs(
        action=action,
        route_id=route_id,
        stop_id=stop_id,
        language=language,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    action: GetRouteStopsOrEstimatedArrivalsAction,
    route_id: int,
    stop_id: int | Unset = UNSET,
    language: GetRouteStopsOrEstimatedArrivalsLanguage | Unset = UNSET,
) -> (
    EstimatedArrivalsResponse | GetRouteStopsOrEstimatedArrivalsResponse200Type0 | None
):
    """Get stops of a route or estimated arrivals for a stop

     The `list` action returns stops ordered by stop sequence of the route. The `estimatedArrivals`
    action returns arrival information. Scheduled arrival time is calculated from the timetable; actual
    departure time may change subject to operational adjustment. Estimated arrival time is calculated
    from historical data, not real-time traffic data. The `estimatedArrivals` property does not exist if
    the bus estimated arrival time for that route is currently unavailable.

    Args:
        action (GetRouteStopsOrEstimatedArrivalsAction):
        route_id (int):
        stop_id (int | Unset):
        language (GetRouteStopsOrEstimatedArrivalsLanguage | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EstimatedArrivalsResponse | GetRouteStopsOrEstimatedArrivalsResponse200Type0
    """

    return sync_detailed(
        client=client,
        action=action,
        route_id=route_id,
        stop_id=stop_id,
        language=language,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    action: GetRouteStopsOrEstimatedArrivalsAction,
    route_id: int,
    stop_id: int | Unset = UNSET,
    language: GetRouteStopsOrEstimatedArrivalsLanguage | Unset = UNSET,
) -> Response[
    EstimatedArrivalsResponse | GetRouteStopsOrEstimatedArrivalsResponse200Type0
]:
    """Get stops of a route or estimated arrivals for a stop

     The `list` action returns stops ordered by stop sequence of the route. The `estimatedArrivals`
    action returns arrival information. Scheduled arrival time is calculated from the timetable; actual
    departure time may change subject to operational adjustment. Estimated arrival time is calculated
    from historical data, not real-time traffic data. The `estimatedArrivals` property does not exist if
    the bus estimated arrival time for that route is currently unavailable.

    Args:
        action (GetRouteStopsOrEstimatedArrivalsAction):
        route_id (int):
        stop_id (int | Unset):
        language (GetRouteStopsOrEstimatedArrivalsLanguage | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EstimatedArrivalsResponse | GetRouteStopsOrEstimatedArrivalsResponse200Type0]
    """

    kwargs = _get_kwargs(
        action=action,
        route_id=route_id,
        stop_id=stop_id,
        language=language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    action: GetRouteStopsOrEstimatedArrivalsAction,
    route_id: int,
    stop_id: int | Unset = UNSET,
    language: GetRouteStopsOrEstimatedArrivalsLanguage | Unset = UNSET,
) -> (
    EstimatedArrivalsResponse | GetRouteStopsOrEstimatedArrivalsResponse200Type0 | None
):
    """Get stops of a route or estimated arrivals for a stop

     The `list` action returns stops ordered by stop sequence of the route. The `estimatedArrivals`
    action returns arrival information. Scheduled arrival time is calculated from the timetable; actual
    departure time may change subject to operational adjustment. Estimated arrival time is calculated
    from historical data, not real-time traffic data. The `estimatedArrivals` property does not exist if
    the bus estimated arrival time for that route is currently unavailable.

    Args:
        action (GetRouteStopsOrEstimatedArrivalsAction):
        route_id (int):
        stop_id (int | Unset):
        language (GetRouteStopsOrEstimatedArrivalsLanguage | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EstimatedArrivalsResponse | GetRouteStopsOrEstimatedArrivalsResponse200Type0
    """

    return (
        await asyncio_detailed(
            client=client,
            action=action,
            route_id=route_id,
            stop_id=stop_id,
            language=language,
        )
    ).parsed
