from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.wms_map_server_get_map_format import (
    WmsMapServerGetMapFormat,
)
from ...models.wms_map_server_get_map_request import (
    WmsMapServerGetMapRequest,
)
from ...models.wms_map_server_get_map_service import (
    WmsMapServerGetMapService,
)
from ...models.wms_map_server_get_map_version import (
    WmsMapServerGetMapVersion,
)
from ...types import UNSET, Response


def _get_kwargs(
    *,
    service: WmsMapServerGetMapService,
    version: WmsMapServerGetMapVersion,
    request: WmsMapServerGetMapRequest,
    layers: str,
    styles: str,
    format_: WmsMapServerGetMapFormat,
    width: int,
    height: int,
    crs: str,
    bbox: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_service: str = service
    params["service"] = json_service

    json_version: str = version
    params["version"] = json_version

    json_request: str = request
    params["request"] = json_request

    params["layers"] = layers

    params["styles"] = styles

    json_format_: str = format_
    params["format"] = json_format_

    params["width"] = width

    params["height"] = height

    params["crs"] = crs

    params["bbox"] = bbox

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/server/services/common/mardep_rcd_1671158138988_60545/MapServer/WMSServer",
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
    service: WmsMapServerGetMapService,
    version: WmsMapServerGetMapVersion,
    request: WmsMapServerGetMapRequest,
    layers: str,
    styles: str,
    format_: WmsMapServerGetMapFormat,
    width: int,
    height: int,
    crs: str,
    bbox: str,
) -> Response[Any]:
    """Render a map image

     Map rendering returns its advertised native image/document representation. It does not return a
    feature JSON collection. Layer CRS, style and bounding-box choices are retained; no data observation
    is implied by metadata availability.

    Args:
        service (WmsMapServerGetMapService):
        version (WmsMapServerGetMapVersion):
        request (WmsMapServerGetMapRequest):
        layers (str):
        styles (str):
        format_ (WmsMapServerGetMapFormat):
        width (int):
        height (int):
        crs (str):
        bbox (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        service=service,
        version=version,
        request=request,
        layers=layers,
        styles=styles,
        format_=format_,
        width=width,
        height=height,
        crs=crs,
        bbox=bbox,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    service: WmsMapServerGetMapService,
    version: WmsMapServerGetMapVersion,
    request: WmsMapServerGetMapRequest,
    layers: str,
    styles: str,
    format_: WmsMapServerGetMapFormat,
    width: int,
    height: int,
    crs: str,
    bbox: str,
) -> Response[Any]:
    """Render a map image

     Map rendering returns its advertised native image/document representation. It does not return a
    feature JSON collection. Layer CRS, style and bounding-box choices are retained; no data observation
    is implied by metadata availability.

    Args:
        service (WmsMapServerGetMapService):
        version (WmsMapServerGetMapVersion):
        request (WmsMapServerGetMapRequest):
        layers (str):
        styles (str):
        format_ (WmsMapServerGetMapFormat):
        width (int):
        height (int):
        crs (str):
        bbox (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        service=service,
        version=version,
        request=request,
        layers=layers,
        styles=styles,
        format_=format_,
        width=width,
        height=height,
        crs=crs,
        bbox=bbox,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
