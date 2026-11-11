from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_3d_photo_realistic_model_tiles_file_type import (
    Get3DPhotoRealisticModelTilesFileType,
)
from ...models.tiles_response import TilesResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    e: int,
    n: int,
    file_type: Get3DPhotoRealisticModelTilesFileType | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["e"] = e

    params["n"] = n

    json_file_type: str | Unset = UNSET
    if not isinstance(file_type, Unset):
        json_file_type = file_type

    params["fileType"] = json_file_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/plandapi/Tiles",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | TilesResponse | None:
    if response.status_code == 200:
        response_200 = TilesResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if response.status_code == 503:
        response_503 = cast(Any, None)
        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | TilesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    e: int,
    n: int,
    file_type: Get3DPhotoRealisticModelTilesFileType | Unset = UNSET,
) -> Response[Any | TilesResponse]:
    """Get 3D photo-realistic model tile download URLs

     Returns model tile information for a supplied HK1980 Grid coordinate. The current resource
    description documents this endpoint. The legacy 2019 specification instead documents
    https://ppgis.pland.gov.hk/opd/api/3D-model-tile; no redirect or migration statement is documented.
    The legacy response dictionary is used for field context and may not fully describe the current
    response.

    Args:
        e (int):
        n (int):
        file_type (Get3DPhotoRealisticModelTilesFileType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | TilesResponse]
    """

    kwargs = _get_kwargs(
        e=e,
        n=n,
        file_type=file_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    e: int,
    n: int,
    file_type: Get3DPhotoRealisticModelTilesFileType | Unset = UNSET,
) -> Any | TilesResponse | None:
    """Get 3D photo-realistic model tile download URLs

     Returns model tile information for a supplied HK1980 Grid coordinate. The current resource
    description documents this endpoint. The legacy 2019 specification instead documents
    https://ppgis.pland.gov.hk/opd/api/3D-model-tile; no redirect or migration statement is documented.
    The legacy response dictionary is used for field context and may not fully describe the current
    response.

    Args:
        e (int):
        n (int):
        file_type (Get3DPhotoRealisticModelTilesFileType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | TilesResponse
    """

    return sync_detailed(
        client=client,
        e=e,
        n=n,
        file_type=file_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    e: int,
    n: int,
    file_type: Get3DPhotoRealisticModelTilesFileType | Unset = UNSET,
) -> Response[Any | TilesResponse]:
    """Get 3D photo-realistic model tile download URLs

     Returns model tile information for a supplied HK1980 Grid coordinate. The current resource
    description documents this endpoint. The legacy 2019 specification instead documents
    https://ppgis.pland.gov.hk/opd/api/3D-model-tile; no redirect or migration statement is documented.
    The legacy response dictionary is used for field context and may not fully describe the current
    response.

    Args:
        e (int):
        n (int):
        file_type (Get3DPhotoRealisticModelTilesFileType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | TilesResponse]
    """

    kwargs = _get_kwargs(
        e=e,
        n=n,
        file_type=file_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    e: int,
    n: int,
    file_type: Get3DPhotoRealisticModelTilesFileType | Unset = UNSET,
) -> Any | TilesResponse | None:
    """Get 3D photo-realistic model tile download URLs

     Returns model tile information for a supplied HK1980 Grid coordinate. The current resource
    description documents this endpoint. The legacy 2019 specification instead documents
    https://ppgis.pland.gov.hk/opd/api/3D-model-tile; no redirect or migration statement is documented.
    The legacy response dictionary is used for field context and may not fully describe the current
    response.

    Args:
        e (int):
        n (int):
        file_type (Get3DPhotoRealisticModelTilesFileType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | TilesResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            e=e,
            n=n,
            file_type=file_type,
        )
    ).parsed
