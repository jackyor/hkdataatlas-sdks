from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.search_press_releases_response_200 import SearchPressReleasesResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    lang: str,
    start: str | Unset = UNSET,
    end: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["lang"] = lang

    params["start"] = start

    params["end"] = end

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/search",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> SearchPressReleasesResponse200 | None:
    if response.status_code == 200:
        response_200 = SearchPressReleasesResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[SearchPressReleasesResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    lang: str,
    start: str | Unset = UNSET,
    end: str | Unset = UNSET,
) -> Response[SearchPressReleasesResponse200]:
    """Search press releases

     Dates and times are interpreted in HKT (GMT+8). A maximum of 400 records will be returned.

    Args:
        lang (str):
        start (str | Unset):
        end (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchPressReleasesResponse200]
    """

    kwargs = _get_kwargs(
        lang=lang,
        start=start,
        end=end,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    lang: str,
    start: str | Unset = UNSET,
    end: str | Unset = UNSET,
) -> SearchPressReleasesResponse200 | None:
    """Search press releases

     Dates and times are interpreted in HKT (GMT+8). A maximum of 400 records will be returned.

    Args:
        lang (str):
        start (str | Unset):
        end (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchPressReleasesResponse200
    """

    return sync_detailed(
        client=client,
        lang=lang,
        start=start,
        end=end,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    lang: str,
    start: str | Unset = UNSET,
    end: str | Unset = UNSET,
) -> Response[SearchPressReleasesResponse200]:
    """Search press releases

     Dates and times are interpreted in HKT (GMT+8). A maximum of 400 records will be returned.

    Args:
        lang (str):
        start (str | Unset):
        end (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchPressReleasesResponse200]
    """

    kwargs = _get_kwargs(
        lang=lang,
        start=start,
        end=end,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    lang: str,
    start: str | Unset = UNSET,
    end: str | Unset = UNSET,
) -> SearchPressReleasesResponse200 | None:
    """Search press releases

     Dates and times are interpreted in HKT (GMT+8). A maximum of 400 records will be returned.

    Args:
        lang (str):
        start (str | Unset):
        end (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchPressReleasesResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            lang=lang,
            start=start,
            end=end,
        )
    ).parsed
