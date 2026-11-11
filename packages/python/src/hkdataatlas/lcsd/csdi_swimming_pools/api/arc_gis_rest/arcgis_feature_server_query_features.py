from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.arcgis_feature_server_arcgis_feature_set import (
    ArcgisFeatureServerArcgisFeatureSet,
)
from ...models.arcgis_feature_server_query_features_f import (
    ArcgisFeatureServerQueryFeaturesF,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    layer_id: str,
    *,
    f: ArcgisFeatureServerQueryFeaturesF | Unset = UNSET,
    where: str | Unset = UNSET,
    out_fields: str | Unset = UNSET,
    return_geometry: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_f: str | Unset = UNSET
    if not isinstance(f, Unset):
        json_f = f

    params["f"] = json_f

    params["where"] = where

    params["outFields"] = out_fields

    params["returnGeometry"] = return_geometry

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/server/rest/services/common/lcsd_rcd_1634540558875_77434/FeatureServer/{layer_id}/query".format(
            layer_id=quote(str(layer_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ArcgisFeatureServerArcgisFeatureSet | None:
    if response.status_code == 200:
        media_type = (
            response.headers.get("content-type", "").split(";", 1)[0].strip().lower()
        )
        if media_type != "application/json" and not media_type.endswith("+json"):
            return None
        response_200 = ArcgisFeatureServerArcgisFeatureSet.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ArcgisFeatureServerArcgisFeatureSet]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    layer_id: str,
    *,
    client: AuthenticatedClient | Client,
    f: ArcgisFeatureServerQueryFeaturesF | Unset = UNSET,
    where: str | Unset = UNSET,
    out_fields: str | Unset = UNSET,
    return_geometry: bool | Unset = UNSET,
) -> Response[ArcgisFeatureServerArcgisFeatureSet]:
    """Query published features

     Read-only GET query follows the source-advertised Query capability. One parameterized operation
    covers all queryable layers. Metadata field types are declared without inventing universally
    required attributes. Omitted f may produce the native REST default representation, which is not
    asserted as a JSON payload.

    Args:
        layer_id (str):
        f (ArcgisFeatureServerQueryFeaturesF | Unset):
        where (str | Unset):
        out_fields (str | Unset):
        return_geometry (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ArcgisFeatureServerArcgisFeatureSet]
    """

    kwargs = _get_kwargs(
        layer_id=layer_id,
        f=f,
        where=where,
        out_fields=out_fields,
        return_geometry=return_geometry,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    layer_id: str,
    *,
    client: AuthenticatedClient | Client,
    f: ArcgisFeatureServerQueryFeaturesF | Unset = UNSET,
    where: str | Unset = UNSET,
    out_fields: str | Unset = UNSET,
    return_geometry: bool | Unset = UNSET,
) -> ArcgisFeatureServerArcgisFeatureSet | None:
    """Query published features

     Read-only GET query follows the source-advertised Query capability. One parameterized operation
    covers all queryable layers. Metadata field types are declared without inventing universally
    required attributes. Omitted f may produce the native REST default representation, which is not
    asserted as a JSON payload.

    Args:
        layer_id (str):
        f (ArcgisFeatureServerQueryFeaturesF | Unset):
        where (str | Unset):
        out_fields (str | Unset):
        return_geometry (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ArcgisFeatureServerArcgisFeatureSet
    """

    return sync_detailed(
        layer_id=layer_id,
        client=client,
        f=f,
        where=where,
        out_fields=out_fields,
        return_geometry=return_geometry,
    ).parsed


async def asyncio_detailed(
    layer_id: str,
    *,
    client: AuthenticatedClient | Client,
    f: ArcgisFeatureServerQueryFeaturesF | Unset = UNSET,
    where: str | Unset = UNSET,
    out_fields: str | Unset = UNSET,
    return_geometry: bool | Unset = UNSET,
) -> Response[ArcgisFeatureServerArcgisFeatureSet]:
    """Query published features

     Read-only GET query follows the source-advertised Query capability. One parameterized operation
    covers all queryable layers. Metadata field types are declared without inventing universally
    required attributes. Omitted f may produce the native REST default representation, which is not
    asserted as a JSON payload.

    Args:
        layer_id (str):
        f (ArcgisFeatureServerQueryFeaturesF | Unset):
        where (str | Unset):
        out_fields (str | Unset):
        return_geometry (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ArcgisFeatureServerArcgisFeatureSet]
    """

    kwargs = _get_kwargs(
        layer_id=layer_id,
        f=f,
        where=where,
        out_fields=out_fields,
        return_geometry=return_geometry,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    layer_id: str,
    *,
    client: AuthenticatedClient | Client,
    f: ArcgisFeatureServerQueryFeaturesF | Unset = UNSET,
    where: str | Unset = UNSET,
    out_fields: str | Unset = UNSET,
    return_geometry: bool | Unset = UNSET,
) -> ArcgisFeatureServerArcgisFeatureSet | None:
    """Query published features

     Read-only GET query follows the source-advertised Query capability. One parameterized operation
    covers all queryable layers. Metadata field types are declared without inventing universally
    required attributes. Omitted f may produce the native REST default representation, which is not
    asserted as a JSON payload.

    Args:
        layer_id (str):
        f (ArcgisFeatureServerQueryFeaturesF | Unset):
        where (str | Unset):
        out_fields (str | Unset):
        return_geometry (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ArcgisFeatureServerArcgisFeatureSet
    """

    return (
        await asyncio_detailed(
            layer_id=layer_id,
            client=client,
            f=f,
            where=where,
            out_fields=out_fields,
            return_geometry=return_geometry,
        )
    ).parsed
