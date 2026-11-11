from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_vector_map_label_tile_lang import (
    GetVectorMapLabelTileLang,
)
from ...models.get_vector_map_label_tile_sr import (
    GetVectorMapLabelTileSr,
)
from ...types import Response


def _get_kwargs(
    version: str,
    lang: GetVectorMapLabelTileLang,
    sr: GetVectorMapLabelTileSr,
    z: int,
    y: int,
    x: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/gs/api/{version}/vt/label/hk/{lang}/{sr}/tile/{z}/{y}/{x}.pbf".format(
            version=quote(str(version), safe=""),
            lang=quote(str(lang), safe=""),
            sr=quote(str(sr), safe=""),
            z=quote(str(z), safe=""),
            y=quote(str(y), safe=""),
            x=quote(str(x), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | None:
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
    lang: GetVectorMapLabelTileLang,
    sr: GetVectorMapLabelTileSr,
    z: int,
    y: int,
    x: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any]:
    """Retrieve a vector map label tile

     Returns vector map labels as an ESRI Vector Tile (protocol buffers file) in PBF format. Tile
    coordinates use the XYZ Tile Scheme. Documented URL example:
    `/gs/api/v1.0.0/vt/label/hk/en/HK80/tile/15/6161/4600.pbf`; the guide also shows `tc` in a query URL
    example.

    Args:
        version (str):
        lang (GetVectorMapLabelTileLang):
        sr (GetVectorMapLabelTileSr):
        z (int):
        y (int):
        x (int):

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
        z=z,
        y=y,
        x=x,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    version: str,
    lang: GetVectorMapLabelTileLang,
    sr: GetVectorMapLabelTileSr,
    z: int,
    y: int,
    x: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any]:
    """Retrieve a vector map label tile

     Returns vector map labels as an ESRI Vector Tile (protocol buffers file) in PBF format. Tile
    coordinates use the XYZ Tile Scheme. Documented URL example:
    `/gs/api/v1.0.0/vt/label/hk/en/HK80/tile/15/6161/4600.pbf`; the guide also shows `tc` in a query URL
    example.

    Args:
        version (str):
        lang (GetVectorMapLabelTileLang):
        sr (GetVectorMapLabelTileSr):
        z (int):
        y (int):
        x (int):

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
        z=z,
        y=y,
        x=x,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
