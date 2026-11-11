from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_lot_index_bbox_item_type_4 import (
    GetLotIndexBboxItemType4,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    version: str,
    lit: str,
    *,
    bbox: list[float | GetLotIndexBboxItemType4] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_bbox: list[float | str] | Unset = UNSET
    if not isinstance(bbox, Unset):
        json_bbox = []
        for bbox_item_data in bbox:
            bbox_item: float | str
            if isinstance(bbox_item_data, str):
                bbox_item = bbox_item_data
            else:
                bbox_item = bbox_item_data
            json_bbox.append(bbox_item)

    params["bbox"] = json_bbox

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/gs/api/{version}/iC1000/{lit}".format(
            version=quote(str(version), safe=""),
            lit=quote(str(lit), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | None:
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
    lit: str,
    *,
    client: AuthenticatedClient | Client,
    bbox: list[float | GetLotIndexBboxItemType4] | Unset = UNSET,
) -> Response[Any]:
    """Retrieve lot index features

     Returns features in GML. The returned data uses the HK80 spatial reference system. The map extent
    must be at most 750 m × 600 m on the ground, equivalent to a standard 1:1000 (HP1C) topographic map
    tile.

    Args:
        version (str):
        lit (str):
        bbox (list[float | GetLotIndexBboxItemType4] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        version=version,
        lit=lit,
        bbox=bbox,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    version: str,
    lit: str,
    *,
    client: AuthenticatedClient | Client,
    bbox: list[float | GetLotIndexBboxItemType4] | Unset = UNSET,
) -> Response[Any]:
    """Retrieve lot index features

     Returns features in GML. The returned data uses the HK80 spatial reference system. The map extent
    must be at most 750 m × 600 m on the ground, equivalent to a standard 1:1000 (HP1C) topographic map
    tile.

    Args:
        version (str):
        lit (str):
        bbox (list[float | GetLotIndexBboxItemType4] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        version=version,
        lit=lit,
        bbox=bbox,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
