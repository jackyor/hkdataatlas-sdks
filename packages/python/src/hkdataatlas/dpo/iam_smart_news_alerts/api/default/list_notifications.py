from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_notifications_lang import (
    ListNotificationsLang,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    lang: ListNotificationsLang | Unset = "en",
    max_: int | Unset = UNSET,
    page: int | Unset = 1,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_lang: str | Unset = UNSET
    if not isinstance(lang, Unset):
        json_lang = lang

    params["lang"] = json_lang

    params["max"] = max_

    params["page"] = page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/ogcmn/service/list/catwc/OGCMN*",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | None:
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    lang: ListNotificationsLang | Unset = "en",
    max_: int | Unset = UNSET,
    page: int | Unset = 1,
) -> Response[Any]:
    """List notifications

     Lists alert notifications issued via “iAM Smart” News & Alerts. Only messages from the past seven
    days are available; requests for messages older than seven days result in an empty message list. The
    documented list response describes notification fields but does not specify a response envelope.

    Args:
        lang (ListNotificationsLang | Unset):  Default: 'en'.
        max_ (int | Unset):
        page (int | Unset):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        lang=lang,
        max_=max_,
        page=page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    lang: ListNotificationsLang | Unset = "en",
    max_: int | Unset = UNSET,
    page: int | Unset = 1,
) -> Response[Any]:
    """List notifications

     Lists alert notifications issued via “iAM Smart” News & Alerts. Only messages from the past seven
    days are available; requests for messages older than seven days result in an empty message list. The
    documented list response describes notification fields but does not specify a response envelope.

    Args:
        lang (ListNotificationsLang | Unset):  Default: 'en'.
        max_ (int | Unset):
        page (int | Unset):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        lang=lang,
        max_=max_,
        page=page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
