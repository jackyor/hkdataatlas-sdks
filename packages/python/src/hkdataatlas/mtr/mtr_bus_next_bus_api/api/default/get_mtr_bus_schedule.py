from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.schedule_request import ScheduleRequest
from ...models.schedule_response import ScheduleResponse
from ...types import Response


def _get_kwargs(
    *,
    body: ScheduleRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/transport/mtr/bus/getSchedule",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | ScheduleResponse | None:
    if response.status_code == 200:
        response_200 = ScheduleResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 429:
        response_429 = cast(Any, None)
        return response_429

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | ScheduleResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ScheduleRequest,
) -> Response[Any | ScheduleResponse]:
    """Get bus schedule and estimated arrival times

     Returns estimated time of arrival data for a selected MTR Bus route. The publisher documents HTTP
    200, 400, 429 and 500 response codes but provides a response example only for success; response
    bodies for the error codes are not specified.

    Args:
        body (ScheduleRequest): The publisher says a valid result is returned only when both
            language and routeName are correct.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ScheduleResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: ScheduleRequest,
) -> Any | ScheduleResponse | None:
    """Get bus schedule and estimated arrival times

     Returns estimated time of arrival data for a selected MTR Bus route. The publisher documents HTTP
    200, 400, 429 and 500 response codes but provides a response example only for success; response
    bodies for the error codes are not specified.

    Args:
        body (ScheduleRequest): The publisher says a valid result is returned only when both
            language and routeName are correct.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ScheduleResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ScheduleRequest,
) -> Response[Any | ScheduleResponse]:
    """Get bus schedule and estimated arrival times

     Returns estimated time of arrival data for a selected MTR Bus route. The publisher documents HTTP
    200, 400, 429 and 500 response codes but provides a response example only for success; response
    bodies for the error codes are not specified.

    Args:
        body (ScheduleRequest): The publisher says a valid result is returned only when both
            language and routeName are correct.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ScheduleResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ScheduleRequest,
) -> Any | ScheduleResponse | None:
    """Get bus schedule and estimated arrival times

     Returns estimated time of arrival data for a selected MTR Bus route. The publisher documents HTTP
    200, 400, 429 and 500 response codes but provides a response example only for success; response
    bodies for the error codes are not specified.

    Args:
        body (ScheduleRequest): The publisher says a valid result is returned only when both
            language and routeName are correct.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ScheduleResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
