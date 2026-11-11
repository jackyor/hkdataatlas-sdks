from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.search_press_releases_lang import (
    SearchPressReleasesLang,
)
from ...models.search_press_releases_official import (
    SearchPressReleasesOfficial,
)
from ...models.search_press_releases_response_200 import SearchPressReleasesResponse200
from ...models.search_press_releases_type import (
    SearchPressReleasesType,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    lang: SearchPressReleasesLang,
    official: SearchPressReleasesOfficial,
    type_: SearchPressReleasesType,
    start: str | Unset = UNSET,
    end: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_lang: str = lang
    params["lang"] = json_lang

    json_official: str = official
    params["official"] = json_official

    json_type_: str = type_
    params["type"] = json_type_

    params["start"] = start

    params["end"] = end

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/pressrelease/search",
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
    lang: SearchPressReleasesLang,
    official: SearchPressReleasesOfficial,
    type_: SearchPressReleasesType,
    start: str | Unset = UNSET,
    end: str | Unset = UNSET,
) -> Response[SearchPressReleasesResponse200]:
    """Search press releases

     Returns press releases issued by the Chief Executive's Office. The documented request selects
    English-language press releases of type press from official CE. The API documentation does not
    define the complete response envelope.

    Args:
        lang (SearchPressReleasesLang):
        official (SearchPressReleasesOfficial):
        type_ (SearchPressReleasesType):
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
        official=official,
        type_=type_,
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
    lang: SearchPressReleasesLang,
    official: SearchPressReleasesOfficial,
    type_: SearchPressReleasesType,
    start: str | Unset = UNSET,
    end: str | Unset = UNSET,
) -> SearchPressReleasesResponse200 | None:
    """Search press releases

     Returns press releases issued by the Chief Executive's Office. The documented request selects
    English-language press releases of type press from official CE. The API documentation does not
    define the complete response envelope.

    Args:
        lang (SearchPressReleasesLang):
        official (SearchPressReleasesOfficial):
        type_ (SearchPressReleasesType):
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
        official=official,
        type_=type_,
        start=start,
        end=end,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    lang: SearchPressReleasesLang,
    official: SearchPressReleasesOfficial,
    type_: SearchPressReleasesType,
    start: str | Unset = UNSET,
    end: str | Unset = UNSET,
) -> Response[SearchPressReleasesResponse200]:
    """Search press releases

     Returns press releases issued by the Chief Executive's Office. The documented request selects
    English-language press releases of type press from official CE. The API documentation does not
    define the complete response envelope.

    Args:
        lang (SearchPressReleasesLang):
        official (SearchPressReleasesOfficial):
        type_ (SearchPressReleasesType):
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
        official=official,
        type_=type_,
        start=start,
        end=end,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    lang: SearchPressReleasesLang,
    official: SearchPressReleasesOfficial,
    type_: SearchPressReleasesType,
    start: str | Unset = UNSET,
    end: str | Unset = UNSET,
) -> SearchPressReleasesResponse200 | None:
    """Search press releases

     Returns press releases issued by the Chief Executive's Office. The documented request selects
    English-language press releases of type press from official CE. The API documentation does not
    define the complete response envelope.

    Args:
        lang (SearchPressReleasesLang):
        official (SearchPressReleasesOfficial):
        type_ (SearchPressReleasesType):
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
            official=official,
            type_=type_,
            start=start,
            end=end,
        )
    ).parsed
