from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_execution_error import ApiExecutionError
from ...models.error import Error
from ...models.stop_response import StopResponse
from ...types import Response


def _get_kwargs(
    stop_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/transport/kmb/stop/{stop_id}".format(
            stop_id=quote(str(stop_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ApiExecutionError | Error | StopResponse | None:
    if response.status_code == 200:
        response_200 = StopResponse.from_dict(response.json())

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
) -> Response[ApiExecutionError | Error | StopResponse]:
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
) -> Response[ApiExecutionError | Error | StopResponse]:
    """Get stop information

     Returns information for a bus stop identified by its 16-character ID. The Route-Stop API can be used
    to find a corresponding stop ID. Updated daily at 05:00.

    Args:
        stop_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiExecutionError | Error | StopResponse]
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
) -> ApiExecutionError | Error | StopResponse | None:
    """Get stop information

     Returns information for a bus stop identified by its 16-character ID. The Route-Stop API can be used
    to find a corresponding stop ID. Updated daily at 05:00.

    Args:
        stop_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiExecutionError | Error | StopResponse
    """

    return sync_detailed(
        stop_id=stop_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    stop_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ApiExecutionError | Error | StopResponse]:
    """Get stop information

     Returns information for a bus stop identified by its 16-character ID. The Route-Stop API can be used
    to find a corresponding stop ID. Updated daily at 05:00.

    Args:
        stop_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiExecutionError | Error | StopResponse]
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
) -> ApiExecutionError | Error | StopResponse | None:
    """Get stop information

     Returns information for a bus stop identified by its 16-character ID. The Route-Stop API can be used
    to find a corresponding stop ID. Updated daily at 05:00.

    Args:
        stop_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiExecutionError | Error | StopResponse
    """

    return (
        await asyncio_detailed(
            stop_id=stop_id,
            client=client,
        )
    ).parsed
