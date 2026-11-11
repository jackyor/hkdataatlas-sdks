from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_aed_information_lang import (
    GetAedInformationLang,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    lang: GetAedInformationLang | Unset = "EN",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_lang: str | Unset = UNSET
    if not isinstance(lang, Unset):
        json_lang = lang

    params["Lang"] = json_lang

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/aed_api/export_aed.php",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> str | None:
    if response.status_code == 200:
        response_200 = response.text
        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    lang: GetAedInformationLang | Unset = "EN",
) -> Response[str]:
    """Get available AED information

     Returns AED information as CSV. The documentation describes CSV with response encoding recorded as
    “No UTF-8.” The catalogue publishes language-specific retrieval URLs for English, Traditional
    Chinese, and Simplified Chinese; those links are resource examples, not separate endpoints.

    Args:
        lang (GetAedInformationLang | Unset):  Default: 'EN'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[str]
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
    lang: GetAedInformationLang | Unset = "EN",
) -> str | None:
    """Get available AED information

     Returns AED information as CSV. The documentation describes CSV with response encoding recorded as
    “No UTF-8.” The catalogue publishes language-specific retrieval URLs for English, Traditional
    Chinese, and Simplified Chinese; those links are resource examples, not separate endpoints.

    Args:
        lang (GetAedInformationLang | Unset):  Default: 'EN'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        str
    """

    return sync_detailed(
        client=client,
        lang=lang,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    lang: GetAedInformationLang | Unset = "EN",
) -> Response[str]:
    """Get available AED information

     Returns AED information as CSV. The documentation describes CSV with response encoding recorded as
    “No UTF-8.” The catalogue publishes language-specific retrieval URLs for English, Traditional
    Chinese, and Simplified Chinese; those links are resource examples, not separate endpoints.

    Args:
        lang (GetAedInformationLang | Unset):  Default: 'EN'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[str]
    """

    kwargs = _get_kwargs(
        lang=lang,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    lang: GetAedInformationLang | Unset = "EN",
) -> str | None:
    """Get available AED information

     Returns AED information as CSV. The documentation describes CSV with response encoding recorded as
    “No UTF-8.” The catalogue publishes language-specific retrieval URLs for English, Traditional
    Chinese, and Simplified Chinese; those links are resource examples, not separate endpoints.

    Args:
        lang (GetAedInformationLang | Unset):  Default: 'EN'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        str
    """

    return (
        await asyncio_detailed(
            client=client,
            lang=lang,
        )
    ).parsed
