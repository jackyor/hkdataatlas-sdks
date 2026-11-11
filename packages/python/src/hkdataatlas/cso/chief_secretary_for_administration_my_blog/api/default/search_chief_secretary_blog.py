from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.search_chief_secretary_blog_response_200 import (
    SearchChiefSecretaryBlogResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    lang: str = "en",
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
        "url": "/cso/blog/search",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> SearchChiefSecretaryBlogResponse200 | None:
    if response.status_code == 200:
        response_200 = SearchChiefSecretaryBlogResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[SearchChiefSecretaryBlogResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    lang: str = "en",
    start: str | Unset = UNSET,
    end: str | Unset = UNSET,
) -> Response[SearchChiefSecretaryBlogResponse200]:
    """Search My Blog

     Returns My Blog entries. All times are Hong Kong Time (GMT+8). If both date parameters are omitted,
    the last six months of entries are returned. A maximum of 400 records will be returned. The
    documented date range is inclusive.

    Args:
        lang (str):  Default: 'en'.
        start (str | Unset):
        end (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchChiefSecretaryBlogResponse200]
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
    lang: str = "en",
    start: str | Unset = UNSET,
    end: str | Unset = UNSET,
) -> SearchChiefSecretaryBlogResponse200 | None:
    """Search My Blog

     Returns My Blog entries. All times are Hong Kong Time (GMT+8). If both date parameters are omitted,
    the last six months of entries are returned. A maximum of 400 records will be returned. The
    documented date range is inclusive.

    Args:
        lang (str):  Default: 'en'.
        start (str | Unset):
        end (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchChiefSecretaryBlogResponse200
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
    lang: str = "en",
    start: str | Unset = UNSET,
    end: str | Unset = UNSET,
) -> Response[SearchChiefSecretaryBlogResponse200]:
    """Search My Blog

     Returns My Blog entries. All times are Hong Kong Time (GMT+8). If both date parameters are omitted,
    the last six months of entries are returned. A maximum of 400 records will be returned. The
    documented date range is inclusive.

    Args:
        lang (str):  Default: 'en'.
        start (str | Unset):
        end (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchChiefSecretaryBlogResponse200]
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
    lang: str = "en",
    start: str | Unset = UNSET,
    end: str | Unset = UNSET,
) -> SearchChiefSecretaryBlogResponse200 | None:
    """Search My Blog

     Returns My Blog entries. All times are Hong Kong Time (GMT+8). If both date parameters are omitted,
    the last six months of entries are returned. A maximum of 400 records will be returned. The
    documented date range is inclusive.

    Args:
        lang (str):  Default: 'en'.
        start (str | Unset):
        end (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchChiefSecretaryBlogResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            lang=lang,
            start=start,
            end=end,
        )
    ).parsed
