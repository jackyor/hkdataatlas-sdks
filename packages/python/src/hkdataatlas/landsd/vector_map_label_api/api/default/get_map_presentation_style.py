from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_map_presentation_style_lang import (
    GetMapPresentationStyleLang,
)
from ...models.get_map_presentation_style_sr import (
    GetMapPresentationStyleSr,
)
from ...types import Response


def _get_kwargs(
    version: str,
    lang: GetMapPresentationStyleLang,
    sr: GetMapPresentationStyleSr,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/gs/api/{version}/vt/label/hk/{lang}/{sr}/resources/styles/root.json".format(
            version=quote(str(version), safe=""),
            lang=quote(str(lang), safe=""),
            sr=quote(str(sr), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | None:
    if response.status_code == 200:
        return None

    if response.status_code == 204:
        return None

    if response.status_code == 500:
        return None

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
    version: str,
    lang: GetMapPresentationStyleLang,
    sr: GetMapPresentationStyleSr,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any]:
    """Retrieve the map presentation style

     Returns the map presentation style file in JSON. The guide documents the URL format and examples but
    does not specify the JSON object's fields or a more detailed response schema.

    Args:
        version (str):
        lang (GetMapPresentationStyleLang):
        sr (GetMapPresentationStyleSr):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        version=version,
        lang=lang,
        sr=sr,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    version: str,
    lang: GetMapPresentationStyleLang,
    sr: GetMapPresentationStyleSr,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any]:
    """Retrieve the map presentation style

     Returns the map presentation style file in JSON. The guide documents the URL format and examples but
    does not specify the JSON object's fields or a more detailed response schema.

    Args:
        version (str):
        lang (GetMapPresentationStyleLang):
        sr (GetMapPresentationStyleSr):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        version=version,
        lang=lang,
        sr=sr,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
