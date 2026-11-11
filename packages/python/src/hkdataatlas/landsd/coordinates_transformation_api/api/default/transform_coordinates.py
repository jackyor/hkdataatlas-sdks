from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.transform_coordinates_in_sys import (
    TransformCoordinatesInSys,
)
from ...models.transform_coordinates_in_unit import (
    TransformCoordinatesInUnit,
)
from ...models.transform_coordinates_out_sys import (
    TransformCoordinatesOutSys,
)
from ...models.transform_coordinates_out_unit import (
    TransformCoordinatesOutUnit,
)
from ...models.transformation_result import TransformationResult
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    in_sys: TransformCoordinatesInSys,
    out_sys: TransformCoordinatesOutSys | Unset = "all",
    lat: float | Unset = UNSET,
    long: float | Unset = UNSET,
    n: float | Unset = UNSET,
    e: float | Unset = UNSET,
    h: float | Unset = UNSET,
    zone: str | Unset = UNSET,
    in_unit: TransformCoordinatesInUnit | Unset = "dms",
    out_unit: TransformCoordinatesOutUnit | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_in_sys: str = in_sys
    params["inSys"] = json_in_sys

    json_out_sys: str | Unset = UNSET
    if not isinstance(out_sys, Unset):
        json_out_sys = out_sys

    params["outSys"] = json_out_sys

    params["lat"] = lat

    params["long"] = long

    params["n"] = n

    params["e"] = e

    params["h"] = h

    params["zone"] = zone

    json_in_unit: str | Unset = UNSET
    if not isinstance(in_unit, Unset):
        json_in_unit = in_unit

    params["inUnit"] = json_in_unit

    json_out_unit: str | Unset = UNSET
    if not isinstance(out_unit, Unset):
        json_out_unit = out_unit

    params["outUnit"] = json_out_unit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> TransformationResult | None:
    if response.status_code == 200:
        media_type = (
            response.headers.get("content-type", "").split(";", 1)[0].strip().lower()
        )
        if media_type != "application/json" and not media_type.endswith("+json"):
            return None
        response_200 = TransformationResult.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[TransformationResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    in_sys: TransformCoordinatesInSys,
    out_sys: TransformCoordinatesOutSys | Unset = "all",
    lat: float | Unset = UNSET,
    long: float | Unset = UNSET,
    n: float | Unset = UNSET,
    e: float | Unset = UNSET,
    h: float | Unset = UNSET,
    zone: str | Unset = UNSET,
    in_unit: TransformCoordinatesInUnit | Unset = "dms",
    out_unit: TransformCoordinatesOutUnit | Unset = UNSET,
) -> Response[TransformationResult]:
    """Transform coordinates

     Provide input coordinates in the system selected by `inSys`; output systems are selected by
    `outSys`. The publisher documents a JSON return result and the following error codes: 1 missing
    mandatory variable; 2 unrecognized `inSys` / `outSys`; 3 invalid input value(s); 4 coordinates out
    of range; 5 identical `inSys` and `outSys`; 6 unrecognized UTM Grid or UTM Grid Reference
    northing/easting; 7 unrecognized `inUnit` / `outUnit`. The dictionary does not specify HTTP status
    codes or a response media type. For further guidance, see
    http://www.geodetic.gov.hk/transform/tformAPI_manual.pdf.

    Args:
        in_sys (TransformCoordinatesInSys):
        out_sys (TransformCoordinatesOutSys | Unset):  Default: 'all'.
        lat (float | Unset):
        long (float | Unset):
        n (float | Unset):
        e (float | Unset):
        h (float | Unset):
        zone (str | Unset):
        in_unit (TransformCoordinatesInUnit | Unset):  Default: 'dms'.
        out_unit (TransformCoordinatesOutUnit | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TransformationResult]
    """

    kwargs = _get_kwargs(
        in_sys=in_sys,
        out_sys=out_sys,
        lat=lat,
        long=long,
        n=n,
        e=e,
        h=h,
        zone=zone,
        in_unit=in_unit,
        out_unit=out_unit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    in_sys: TransformCoordinatesInSys,
    out_sys: TransformCoordinatesOutSys | Unset = "all",
    lat: float | Unset = UNSET,
    long: float | Unset = UNSET,
    n: float | Unset = UNSET,
    e: float | Unset = UNSET,
    h: float | Unset = UNSET,
    zone: str | Unset = UNSET,
    in_unit: TransformCoordinatesInUnit | Unset = "dms",
    out_unit: TransformCoordinatesOutUnit | Unset = UNSET,
) -> TransformationResult | None:
    """Transform coordinates

     Provide input coordinates in the system selected by `inSys`; output systems are selected by
    `outSys`. The publisher documents a JSON return result and the following error codes: 1 missing
    mandatory variable; 2 unrecognized `inSys` / `outSys`; 3 invalid input value(s); 4 coordinates out
    of range; 5 identical `inSys` and `outSys`; 6 unrecognized UTM Grid or UTM Grid Reference
    northing/easting; 7 unrecognized `inUnit` / `outUnit`. The dictionary does not specify HTTP status
    codes or a response media type. For further guidance, see
    http://www.geodetic.gov.hk/transform/tformAPI_manual.pdf.

    Args:
        in_sys (TransformCoordinatesInSys):
        out_sys (TransformCoordinatesOutSys | Unset):  Default: 'all'.
        lat (float | Unset):
        long (float | Unset):
        n (float | Unset):
        e (float | Unset):
        h (float | Unset):
        zone (str | Unset):
        in_unit (TransformCoordinatesInUnit | Unset):  Default: 'dms'.
        out_unit (TransformCoordinatesOutUnit | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TransformationResult
    """

    return sync_detailed(
        client=client,
        in_sys=in_sys,
        out_sys=out_sys,
        lat=lat,
        long=long,
        n=n,
        e=e,
        h=h,
        zone=zone,
        in_unit=in_unit,
        out_unit=out_unit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    in_sys: TransformCoordinatesInSys,
    out_sys: TransformCoordinatesOutSys | Unset = "all",
    lat: float | Unset = UNSET,
    long: float | Unset = UNSET,
    n: float | Unset = UNSET,
    e: float | Unset = UNSET,
    h: float | Unset = UNSET,
    zone: str | Unset = UNSET,
    in_unit: TransformCoordinatesInUnit | Unset = "dms",
    out_unit: TransformCoordinatesOutUnit | Unset = UNSET,
) -> Response[TransformationResult]:
    """Transform coordinates

     Provide input coordinates in the system selected by `inSys`; output systems are selected by
    `outSys`. The publisher documents a JSON return result and the following error codes: 1 missing
    mandatory variable; 2 unrecognized `inSys` / `outSys`; 3 invalid input value(s); 4 coordinates out
    of range; 5 identical `inSys` and `outSys`; 6 unrecognized UTM Grid or UTM Grid Reference
    northing/easting; 7 unrecognized `inUnit` / `outUnit`. The dictionary does not specify HTTP status
    codes or a response media type. For further guidance, see
    http://www.geodetic.gov.hk/transform/tformAPI_manual.pdf.

    Args:
        in_sys (TransformCoordinatesInSys):
        out_sys (TransformCoordinatesOutSys | Unset):  Default: 'all'.
        lat (float | Unset):
        long (float | Unset):
        n (float | Unset):
        e (float | Unset):
        h (float | Unset):
        zone (str | Unset):
        in_unit (TransformCoordinatesInUnit | Unset):  Default: 'dms'.
        out_unit (TransformCoordinatesOutUnit | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TransformationResult]
    """

    kwargs = _get_kwargs(
        in_sys=in_sys,
        out_sys=out_sys,
        lat=lat,
        long=long,
        n=n,
        e=e,
        h=h,
        zone=zone,
        in_unit=in_unit,
        out_unit=out_unit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    in_sys: TransformCoordinatesInSys,
    out_sys: TransformCoordinatesOutSys | Unset = "all",
    lat: float | Unset = UNSET,
    long: float | Unset = UNSET,
    n: float | Unset = UNSET,
    e: float | Unset = UNSET,
    h: float | Unset = UNSET,
    zone: str | Unset = UNSET,
    in_unit: TransformCoordinatesInUnit | Unset = "dms",
    out_unit: TransformCoordinatesOutUnit | Unset = UNSET,
) -> TransformationResult | None:
    """Transform coordinates

     Provide input coordinates in the system selected by `inSys`; output systems are selected by
    `outSys`. The publisher documents a JSON return result and the following error codes: 1 missing
    mandatory variable; 2 unrecognized `inSys` / `outSys`; 3 invalid input value(s); 4 coordinates out
    of range; 5 identical `inSys` and `outSys`; 6 unrecognized UTM Grid or UTM Grid Reference
    northing/easting; 7 unrecognized `inUnit` / `outUnit`. The dictionary does not specify HTTP status
    codes or a response media type. For further guidance, see
    http://www.geodetic.gov.hk/transform/tformAPI_manual.pdf.

    Args:
        in_sys (TransformCoordinatesInSys):
        out_sys (TransformCoordinatesOutSys | Unset):  Default: 'all'.
        lat (float | Unset):
        long (float | Unset):
        n (float | Unset):
        e (float | Unset):
        h (float | Unset):
        zone (str | Unset):
        in_unit (TransformCoordinatesInUnit | Unset):  Default: 'dms'.
        out_unit (TransformCoordinatesOutUnit | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TransformationResult
    """

    return (
        await asyncio_detailed(
            client=client,
            in_sys=in_sys,
            out_sys=out_sys,
            lat=lat,
            long=long,
            n=n,
            e=e,
            h=h,
            zone=zone,
            in_unit=in_unit,
            out_unit=out_unit,
        )
    ).parsed
