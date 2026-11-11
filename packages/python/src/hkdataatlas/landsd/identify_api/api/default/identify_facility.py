from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.identify_facility_lang import (
    IdentifyFacilityLang,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    version: str,
    *,
    x: float | Unset = UNSET,
    y: float | Unset = UNSET,
    lang: IdentifyFacilityLang | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["x"] = x

    params["y"] = y

    json_lang: str | Unset = UNSET
    if not isinstance(lang, Unset):
        json_lang = lang

    params["lang"] = json_lang

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/{version}/identify".format(
            version=quote(str(version), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | None:
    if response.status_code == 200:
        return None

    if response.status_code == 400:
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
    *,
    client: AuthenticatedClient | Client,
    x: float | Unset = UNSET,
    y: float | Unset = UNSET,
    lang: IdentifyFacilityLang | Unset = UNSET,
) -> Response[Any]:
    """Identify facility information

     Identifies information about a facility at the selected geographic location. The documented current
    API version is v1.0.0; the publisher notes that versions may be updated and old versions may be
    removed without notice. The response is JSON, but the source does not document its object structure.

    Args:
        version (str):
        x (float | Unset):
        y (float | Unset):
        lang (IdentifyFacilityLang | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        version=version,
        x=x,
        y=y,
        lang=lang,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    version: str,
    *,
    client: AuthenticatedClient | Client,
    x: float | Unset = UNSET,
    y: float | Unset = UNSET,
    lang: IdentifyFacilityLang | Unset = UNSET,
) -> Response[Any]:
    """Identify facility information

     Identifies information about a facility at the selected geographic location. The documented current
    API version is v1.0.0; the publisher notes that versions may be updated and old versions may be
    removed without notice. The response is JSON, but the source does not document its object structure.

    Args:
        version (str):
        x (float | Unset):
        y (float | Unset):
        lang (IdentifyFacilityLang | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        version=version,
        x=x,
        y=y,
        lang=lang,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
