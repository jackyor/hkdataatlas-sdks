from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.search_chief_executive_speeches_and_articles_lang import (
    SearchChiefExecutiveSpeechesAndArticlesLang,
)
from ...models.search_chief_executive_speeches_and_articles_response_200 import (
    SearchChiefExecutiveSpeechesAndArticlesResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    lang: SearchChiefExecutiveSpeechesAndArticlesLang,
    official: str,
    type_: str,
    start: str | Unset = UNSET,
    end: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_lang: str = lang
    params["lang"] = json_lang

    params["official"] = official

    params["type"] = type_

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
) -> SearchChiefExecutiveSpeechesAndArticlesResponse200 | None:
    if response.status_code == 200:
        response_200 = SearchChiefExecutiveSpeechesAndArticlesResponse200.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[SearchChiefExecutiveSpeechesAndArticlesResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    lang: SearchChiefExecutiveSpeechesAndArticlesLang,
    official: str,
    type_: str,
    start: str | Unset = UNSET,
    end: str | Unset = UNSET,
) -> Response[SearchChiefExecutiveSpeechesAndArticlesResponse200]:
    """Search speeches and articles

     Returns speeches and articles of the Chief Executive. All time is in HKT (GMT+8). If start and end
    are omitted, records for the last six months will be returned. A maximum of 400 records will be
    returned.

    Args:
        lang (SearchChiefExecutiveSpeechesAndArticlesLang):
        official (str):
        type_ (str):
        start (str | Unset):
        end (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchChiefExecutiveSpeechesAndArticlesResponse200]
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
    lang: SearchChiefExecutiveSpeechesAndArticlesLang,
    official: str,
    type_: str,
    start: str | Unset = UNSET,
    end: str | Unset = UNSET,
) -> SearchChiefExecutiveSpeechesAndArticlesResponse200 | None:
    """Search speeches and articles

     Returns speeches and articles of the Chief Executive. All time is in HKT (GMT+8). If start and end
    are omitted, records for the last six months will be returned. A maximum of 400 records will be
    returned.

    Args:
        lang (SearchChiefExecutiveSpeechesAndArticlesLang):
        official (str):
        type_ (str):
        start (str | Unset):
        end (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchChiefExecutiveSpeechesAndArticlesResponse200
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
    lang: SearchChiefExecutiveSpeechesAndArticlesLang,
    official: str,
    type_: str,
    start: str | Unset = UNSET,
    end: str | Unset = UNSET,
) -> Response[SearchChiefExecutiveSpeechesAndArticlesResponse200]:
    """Search speeches and articles

     Returns speeches and articles of the Chief Executive. All time is in HKT (GMT+8). If start and end
    are omitted, records for the last six months will be returned. A maximum of 400 records will be
    returned.

    Args:
        lang (SearchChiefExecutiveSpeechesAndArticlesLang):
        official (str):
        type_ (str):
        start (str | Unset):
        end (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchChiefExecutiveSpeechesAndArticlesResponse200]
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
    lang: SearchChiefExecutiveSpeechesAndArticlesLang,
    official: str,
    type_: str,
    start: str | Unset = UNSET,
    end: str | Unset = UNSET,
) -> SearchChiefExecutiveSpeechesAndArticlesResponse200 | None:
    """Search speeches and articles

     Returns speeches and articles of the Chief Executive. All time is in HKT (GMT+8). If start and end
    are omitted, records for the last six months will be returned. A maximum of 400 records will be
    returned.

    Args:
        lang (SearchChiefExecutiveSpeechesAndArticlesLang):
        official (str):
        type_ (str):
        start (str | Unset):
        end (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchChiefExecutiveSpeechesAndArticlesResponse200
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
