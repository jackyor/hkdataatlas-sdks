from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.search_blog_lang import SearchBlogLang
from ...models.search_blog_response_200 import SearchBlogResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    lang: SearchBlogLang,
    start: str | Unset = UNSET,
    end: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_lang: str = lang
    params["lang"] = json_lang

    params["start"] = start

    params["end"] = end

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/blog/search",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> SearchBlogResponse200 | None:
    if response.status_code == 200:
        response_200 = SearchBlogResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[SearchBlogResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    lang: SearchBlogLang,
    start: str | Unset = UNSET,
    end: str | Unset = UNSET,
) -> Response[SearchBlogResponse200]:
    """Search My Blog entries

     Searches My Blog entries. All times are in HKT (GMT+8). If both date parameters are omitted, entries
    from the last six months are returned. A maximum of 400 records is returned.

    Args:
        lang (SearchBlogLang):
        start (str | Unset):
        end (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchBlogResponse200]
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
    lang: SearchBlogLang,
    start: str | Unset = UNSET,
    end: str | Unset = UNSET,
) -> SearchBlogResponse200 | None:
    """Search My Blog entries

     Searches My Blog entries. All times are in HKT (GMT+8). If both date parameters are omitted, entries
    from the last six months are returned. A maximum of 400 records is returned.

    Args:
        lang (SearchBlogLang):
        start (str | Unset):
        end (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchBlogResponse200
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
    lang: SearchBlogLang,
    start: str | Unset = UNSET,
    end: str | Unset = UNSET,
) -> Response[SearchBlogResponse200]:
    """Search My Blog entries

     Searches My Blog entries. All times are in HKT (GMT+8). If both date parameters are omitted, entries
    from the last six months are returned. A maximum of 400 records is returned.

    Args:
        lang (SearchBlogLang):
        start (str | Unset):
        end (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchBlogResponse200]
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
    lang: SearchBlogLang,
    start: str | Unset = UNSET,
    end: str | Unset = UNSET,
) -> SearchBlogResponse200 | None:
    """Search My Blog entries

     Searches My Blog entries. All times are in HKT (GMT+8). If both date parameters are omitted, entries
    from the last six months are returned. A maximum of 400 records is returned.

    Args:
        lang (SearchBlogLang):
        start (str | Unset):
        end (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchBlogResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            lang=lang,
            start=start,
            end=end,
        )
    ).parsed
