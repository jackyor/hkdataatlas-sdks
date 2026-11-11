from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.compartment_data_response import CompartmentDataResponse
from ...models.message_response import MessageResponse
from ...types import UNSET, Response


def _get_kwargs(
    *,
    pi: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["pi"] = pi

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/smacs",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> CompartmentDataResponse | MessageResponse | None:
    if response.status_code == 200:

        def _parse_response_200(
            data: object,
        ) -> CompartmentDataResponse | MessageResponse:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = CompartmentDataResponse.from_dict(data)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = MessageResponse.from_dict(data)

            return response_200_type_1

        response_200 = _parse_response_200(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = MessageResponse.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = MessageResponse.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = MessageResponse.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[CompartmentDataResponse | MessageResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    pi: str,
) -> Response[CompartmentDataResponse | MessageResponse]:
    """Get data by lamppost ID

     Returns the latest validated data (in 10-minute intervals) for the specified lamppost. The response
    is JSON encoded as UTF-8. The API documentation explicitly states that authentication is not
    required.

    Args:
        pi (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CompartmentDataResponse | MessageResponse | MessageResponse]
    """

    kwargs = _get_kwargs(
        pi=pi,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    pi: str,
) -> CompartmentDataResponse | MessageResponse | None:
    """Get data by lamppost ID

     Returns the latest validated data (in 10-minute intervals) for the specified lamppost. The response
    is JSON encoded as UTF-8. The API documentation explicitly states that authentication is not
    required.

    Args:
        pi (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CompartmentDataResponse | MessageResponse | MessageResponse
    """

    return sync_detailed(
        client=client,
        pi=pi,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    pi: str,
) -> Response[CompartmentDataResponse | MessageResponse]:
    """Get data by lamppost ID

     Returns the latest validated data (in 10-minute intervals) for the specified lamppost. The response
    is JSON encoded as UTF-8. The API documentation explicitly states that authentication is not
    required.

    Args:
        pi (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CompartmentDataResponse | MessageResponse | MessageResponse]
    """

    kwargs = _get_kwargs(
        pi=pi,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    pi: str,
) -> CompartmentDataResponse | MessageResponse | None:
    """Get data by lamppost ID

     Returns the latest validated data (in 10-minute intervals) for the specified lamppost. The response
    is JSON encoded as UTF-8. The API documentation explicitly states that authentication is not
    required.

    Args:
        pi (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CompartmentDataResponse | MessageResponse | MessageResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            pi=pi,
        )
    ).parsed
