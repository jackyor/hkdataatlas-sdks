from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.search_speeches_and_articles_response_200_type_1 import (
    SearchSpeechesAndArticlesResponse200Type1,
)
from ...models.speech_article import SpeechArticle
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    official: str,
    type_: str,
    lang: str,
    start: str | Unset = UNSET,
    end: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["official"] = official

    params["type"] = type_

    params["lang"] = lang

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
) -> list[SpeechArticle] | SearchSpeechesAndArticlesResponse200Type1 | None:
    if response.status_code == 200:

        def _parse_response_200(
            data: object,
        ) -> list[SpeechArticle] | SearchSpeechesAndArticlesResponse200Type1:
            try:
                if not isinstance(data, list):
                    raise TypeError()
                response_200_type_0 = []
                _response_200_type_0 = data
                for response_200_type_0_item_data in _response_200_type_0:
                    response_200_type_0_item = SpeechArticle.from_dict(
                        response_200_type_0_item_data
                    )

                    response_200_type_0.append(response_200_type_0_item)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = SearchSpeechesAndArticlesResponse200Type1.from_dict(
                data
            )

            return response_200_type_1

        response_200 = _parse_response_200(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[list[SpeechArticle] | SearchSpeechesAndArticlesResponse200Type1]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    official: str,
    type_: str,
    lang: str,
    start: str | Unset = UNSET,
    end: str | Unset = UNSET,
) -> Response[list[SpeechArticle] | SearchSpeechesAndArticlesResponse200Type1]:
    """Search speeches and articles

     Returns Department of Justice speeches and articles. The documented English endpoint uses
    official=SJ, type=speech, and lang=en. The documented major-speech default applies when both date
    parameters are omitted; the API documentation states that start and end must be used together.

    Args:
        official (str):  Example: SJ.
        type_ (str):  Example: speech.
        lang (str):  Example: en.
        start (str | Unset):  Example: 20190102.
        end (str | Unset):  Example: 20190109.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[SpeechArticle] | SearchSpeechesAndArticlesResponse200Type1]
    """

    kwargs = _get_kwargs(
        official=official,
        type_=type_,
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
    official: str,
    type_: str,
    lang: str,
    start: str | Unset = UNSET,
    end: str | Unset = UNSET,
) -> list[SpeechArticle] | SearchSpeechesAndArticlesResponse200Type1 | None:
    """Search speeches and articles

     Returns Department of Justice speeches and articles. The documented English endpoint uses
    official=SJ, type=speech, and lang=en. The documented major-speech default applies when both date
    parameters are omitted; the API documentation states that start and end must be used together.

    Args:
        official (str):  Example: SJ.
        type_ (str):  Example: speech.
        lang (str):  Example: en.
        start (str | Unset):  Example: 20190102.
        end (str | Unset):  Example: 20190109.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[SpeechArticle] | SearchSpeechesAndArticlesResponse200Type1
    """

    return sync_detailed(
        client=client,
        official=official,
        type_=type_,
        lang=lang,
        start=start,
        end=end,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    official: str,
    type_: str,
    lang: str,
    start: str | Unset = UNSET,
    end: str | Unset = UNSET,
) -> Response[list[SpeechArticle] | SearchSpeechesAndArticlesResponse200Type1]:
    """Search speeches and articles

     Returns Department of Justice speeches and articles. The documented English endpoint uses
    official=SJ, type=speech, and lang=en. The documented major-speech default applies when both date
    parameters are omitted; the API documentation states that start and end must be used together.

    Args:
        official (str):  Example: SJ.
        type_ (str):  Example: speech.
        lang (str):  Example: en.
        start (str | Unset):  Example: 20190102.
        end (str | Unset):  Example: 20190109.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[SpeechArticle] | SearchSpeechesAndArticlesResponse200Type1]
    """

    kwargs = _get_kwargs(
        official=official,
        type_=type_,
        lang=lang,
        start=start,
        end=end,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    official: str,
    type_: str,
    lang: str,
    start: str | Unset = UNSET,
    end: str | Unset = UNSET,
) -> list[SpeechArticle] | SearchSpeechesAndArticlesResponse200Type1 | None:
    """Search speeches and articles

     Returns Department of Justice speeches and articles. The documented English endpoint uses
    official=SJ, type=speech, and lang=en. The documented major-speech default applies when both date
    parameters are omitted; the API documentation states that start and end must be used together.

    Args:
        official (str):  Example: SJ.
        type_ (str):  Example: speech.
        lang (str):  Example: en.
        start (str | Unset):  Example: 20190102.
        end (str | Unset):  Example: 20190109.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[SpeechArticle] | SearchSpeechesAndArticlesResponse200Type1
    """

    return (
        await asyncio_detailed(
            client=client,
            official=official,
            type_=type_,
            lang=lang,
            start=start,
            end=end,
        )
    ).parsed
