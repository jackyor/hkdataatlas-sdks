from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.empty_response import EmptyResponse
from ...models.warning_response import WarningResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    lang: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["lang"] = lang

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/hsww.php",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> EmptyResponse | WarningResponse | None:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> EmptyResponse | WarningResponse:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = WarningResponse.from_dict(data)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = EmptyResponse.from_dict(data)

            return response_200_type_1

        response_200 = _parse_response_200(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[EmptyResponse | WarningResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    lang: str | Unset = UNSET,
) -> Response[EmptyResponse | WarningResponse]:
    """Get Heat Stress at Work Warning

     The response includes the HSWW parameter when a warning is issued or for up to 60 minutes after
    cancellation (T+60 minutes of the issue time). Otherwise, an empty object is returned. The
    documented examples are samples only and are not real data. Authentication requirements are not
    specified in the source.

    Args:
        lang (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EmptyResponse | WarningResponse]
    """

    kwargs = _get_kwargs(
        lang=lang,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    lang: str | Unset = UNSET,
) -> EmptyResponse | WarningResponse | None:
    """Get Heat Stress at Work Warning

     The response includes the HSWW parameter when a warning is issued or for up to 60 minutes after
    cancellation (T+60 minutes of the issue time). Otherwise, an empty object is returned. The
    documented examples are samples only and are not real data. Authentication requirements are not
    specified in the source.

    Args:
        lang (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EmptyResponse | WarningResponse
    """

    return sync_detailed(
        client=client,
        lang=lang,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    lang: str | Unset = UNSET,
) -> Response[EmptyResponse | WarningResponse]:
    """Get Heat Stress at Work Warning

     The response includes the HSWW parameter when a warning is issued or for up to 60 minutes after
    cancellation (T+60 minutes of the issue time). Otherwise, an empty object is returned. The
    documented examples are samples only and are not real data. Authentication requirements are not
    specified in the source.

    Args:
        lang (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EmptyResponse | WarningResponse]
    """

    kwargs = _get_kwargs(
        lang=lang,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    lang: str | Unset = UNSET,
) -> EmptyResponse | WarningResponse | None:
    """Get Heat Stress at Work Warning

     The response includes the HSWW parameter when a warning is issued or for up to 60 minutes after
    cancellation (T+60 minutes of the issue time). Otherwise, an empty object is returned. The
    documented examples are samples only and are not real data. Authentication requirements are not
    specified in the source.

    Args:
        lang (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EmptyResponse | WarningResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            lang=lang,
        )
    ).parsed
