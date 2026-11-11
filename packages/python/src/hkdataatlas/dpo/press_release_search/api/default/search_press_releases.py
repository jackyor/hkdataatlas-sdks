from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.search_press_releases_lang import (
    SearchPressReleasesLang,
)
from ...models.search_press_releases_official import (
    SearchPressReleasesOfficial,
)
from ...models.search_press_releases_type import (
    SearchPressReleasesType,
)
from ...models.search_response import SearchResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    start: str | Unset = UNSET,
    end: str | Unset = UNSET,
    lang: SearchPressReleasesLang | Unset = UNSET,
    official: SearchPressReleasesOfficial,
    type_: SearchPressReleasesType | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["start"] = start

    params["end"] = end

    json_lang: str | Unset = UNSET
    if not isinstance(lang, Unset):
        json_lang = lang

    params["lang"] = json_lang

    json_official: str = official
    params["official"] = json_official

    json_type_: str | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_

    params["type"] = json_type_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/pressrelease/search",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | SearchResponse | None:
    if response.status_code == 200:
        response_200 = SearchResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | SearchResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    start: str | Unset = UNSET,
    end: str | Unset = UNSET,
    lang: SearchPressReleasesLang | Unset = UNSET,
    official: SearchPressReleasesOfficial,
    type_: SearchPressReleasesType | Unset = UNSET,
) -> Response[Any | SearchResponse]:
    """Search press releases

     Retrieves press releases within the inclusive date period, with the specified official as subject.
    If lang is specified, results are limited to that language; otherwise all languages are included.
    The earliest accepted start date depends on the official: CE 2017-07-01; CS and FS 2017-01-16; SJ
    2017-07-01; other officials 2019-01-01. The latest accepted end date is today.

    Args:
        start (str | Unset):
        end (str | Unset):
        lang (SearchPressReleasesLang | Unset):
        official (SearchPressReleasesOfficial):
        type_ (SearchPressReleasesType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | SearchResponse]
    """

    kwargs = _get_kwargs(
        start=start,
        end=end,
        lang=lang,
        official=official,
        type_=type_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    start: str | Unset = UNSET,
    end: str | Unset = UNSET,
    lang: SearchPressReleasesLang | Unset = UNSET,
    official: SearchPressReleasesOfficial,
    type_: SearchPressReleasesType | Unset = UNSET,
) -> Any | SearchResponse | None:
    """Search press releases

     Retrieves press releases within the inclusive date period, with the specified official as subject.
    If lang is specified, results are limited to that language; otherwise all languages are included.
    The earliest accepted start date depends on the official: CE 2017-07-01; CS and FS 2017-01-16; SJ
    2017-07-01; other officials 2019-01-01. The latest accepted end date is today.

    Args:
        start (str | Unset):
        end (str | Unset):
        lang (SearchPressReleasesLang | Unset):
        official (SearchPressReleasesOfficial):
        type_ (SearchPressReleasesType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | SearchResponse
    """

    return sync_detailed(
        client=client,
        start=start,
        end=end,
        lang=lang,
        official=official,
        type_=type_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    start: str | Unset = UNSET,
    end: str | Unset = UNSET,
    lang: SearchPressReleasesLang | Unset = UNSET,
    official: SearchPressReleasesOfficial,
    type_: SearchPressReleasesType | Unset = UNSET,
) -> Response[Any | SearchResponse]:
    """Search press releases

     Retrieves press releases within the inclusive date period, with the specified official as subject.
    If lang is specified, results are limited to that language; otherwise all languages are included.
    The earliest accepted start date depends on the official: CE 2017-07-01; CS and FS 2017-01-16; SJ
    2017-07-01; other officials 2019-01-01. The latest accepted end date is today.

    Args:
        start (str | Unset):
        end (str | Unset):
        lang (SearchPressReleasesLang | Unset):
        official (SearchPressReleasesOfficial):
        type_ (SearchPressReleasesType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | SearchResponse]
    """

    kwargs = _get_kwargs(
        start=start,
        end=end,
        lang=lang,
        official=official,
        type_=type_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    start: str | Unset = UNSET,
    end: str | Unset = UNSET,
    lang: SearchPressReleasesLang | Unset = UNSET,
    official: SearchPressReleasesOfficial,
    type_: SearchPressReleasesType | Unset = UNSET,
) -> Any | SearchResponse | None:
    """Search press releases

     Retrieves press releases within the inclusive date period, with the specified official as subject.
    If lang is specified, results are limited to that language; otherwise all languages are included.
    The earliest accepted start date depends on the official: CE 2017-07-01; CS and FS 2017-01-16; SJ
    2017-07-01; other officials 2019-01-01. The latest accepted end date is today.

    Args:
        start (str | Unset):
        end (str | Unset):
        lang (SearchPressReleasesLang | Unset):
        official (SearchPressReleasesOfficial):
        type_ (SearchPressReleasesType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | SearchResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            start=start,
            end=end,
            lang=lang,
            official=official,
            type_=type_,
        )
    ).parsed
