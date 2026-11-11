from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.address_lookup_result import AddressLookupResult
from ...models.lookup_geo_address_get_3d import (
    LookupGeoAddressGet3D,
)
from ...models.lookup_geo_address_get_accept import (
    LookupGeoAddressGetAccept,
)
from ...models.lookup_geo_address_get_accept_encoding import (
    LookupGeoAddressGetAcceptEncoding,
)
from ...models.lookup_geo_address_get_accept_language import (
    LookupGeoAddressGetAcceptLanguage,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ga: str,
    n: int | Unset = 200,
    field_3d: LookupGeoAddressGet3D | Unset = 0,
    floor: str | Unset = UNSET,
    unit: str | Unset = UNSET,
    accept: LookupGeoAddressGetAccept | Unset = "application/xml",
    accept_encoding: LookupGeoAddressGetAcceptEncoding | Unset = UNSET,
    accept_language: LookupGeoAddressGetAcceptLanguage | Unset = "*",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept, Unset):
        headers["Accept"] = str(accept)

    if not isinstance(accept_encoding, Unset):
        headers["Accept-Encoding"] = str(accept_encoding)

    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = str(accept_language)

    params: dict[str, Any] = {}

    params["ga"] = ga

    params["n"] = n

    json_field_3d: int | Unset = UNSET
    if not isinstance(field_3d, Unset):
        json_field_3d = field_3d

    params["3d"] = json_field_3d

    params["floor"] = floor

    params["unit"] = unit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/galookup",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> AddressLookupResult | Any | None:
    if response.status_code == 200:
        response_200 = AddressLookupResult.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 406:
        response_406 = cast(Any, None)
        return response_406

    if response.status_code == 413:
        response_413 = cast(Any, None)
        return response_413

    if response.status_code == 429:
        response_429 = cast(Any, None)
        return response_429

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[AddressLookupResult | Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    ga: str,
    n: int | Unset = 200,
    field_3d: LookupGeoAddressGet3D | Unset = 0,
    floor: str | Unset = UNSET,
    unit: str | Unset = UNSET,
    accept: LookupGeoAddressGetAccept | Unset = "application/xml",
    accept_encoding: LookupGeoAddressGetAcceptEncoding | Unset = UNSET,
    accept_language: LookupGeoAddressGetAcceptLanguage | Unset = "*",
) -> Response[AddressLookupResult | Any]:
    """GeoAddress lookup

     Looks up address records using a GeoAddress, a 19-character standardized identifier for a
    corresponding building or address. The documented identifier consists of ten leading digits derived
    from HK1980 grid coordinates with leading 8 digits removed, a `P` (podium) or `T` (tower) character,
    and an address record creation date in YYYYMMDD form. Request and response are encoded in UTF-8.

    Args:
        ga (str):
        n (int | Unset):  Default: 200.
        field_3d (LookupGeoAddressGet3D | Unset):  Default: 0.
        floor (str | Unset):
        unit (str | Unset):
        accept (LookupGeoAddressGetAccept | Unset):  Default: 'application/xml'.
        accept_encoding (LookupGeoAddressGetAcceptEncoding | Unset):
        accept_language (LookupGeoAddressGetAcceptLanguage | Unset):  Default: '*'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddressLookupResult | Any]
    """

    kwargs = _get_kwargs(
        ga=ga,
        n=n,
        field_3d=field_3d,
        floor=floor,
        unit=unit,
        accept=accept,
        accept_encoding=accept_encoding,
        accept_language=accept_language,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    ga: str,
    n: int | Unset = 200,
    field_3d: LookupGeoAddressGet3D | Unset = 0,
    floor: str | Unset = UNSET,
    unit: str | Unset = UNSET,
    accept: LookupGeoAddressGetAccept | Unset = "application/xml",
    accept_encoding: LookupGeoAddressGetAcceptEncoding | Unset = UNSET,
    accept_language: LookupGeoAddressGetAcceptLanguage | Unset = "*",
) -> AddressLookupResult | Any | None:
    """GeoAddress lookup

     Looks up address records using a GeoAddress, a 19-character standardized identifier for a
    corresponding building or address. The documented identifier consists of ten leading digits derived
    from HK1980 grid coordinates with leading 8 digits removed, a `P` (podium) or `T` (tower) character,
    and an address record creation date in YYYYMMDD form. Request and response are encoded in UTF-8.

    Args:
        ga (str):
        n (int | Unset):  Default: 200.
        field_3d (LookupGeoAddressGet3D | Unset):  Default: 0.
        floor (str | Unset):
        unit (str | Unset):
        accept (LookupGeoAddressGetAccept | Unset):  Default: 'application/xml'.
        accept_encoding (LookupGeoAddressGetAcceptEncoding | Unset):
        accept_language (LookupGeoAddressGetAcceptLanguage | Unset):  Default: '*'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddressLookupResult | Any
    """

    return sync_detailed(
        client=client,
        ga=ga,
        n=n,
        field_3d=field_3d,
        floor=floor,
        unit=unit,
        accept=accept,
        accept_encoding=accept_encoding,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    ga: str,
    n: int | Unset = 200,
    field_3d: LookupGeoAddressGet3D | Unset = 0,
    floor: str | Unset = UNSET,
    unit: str | Unset = UNSET,
    accept: LookupGeoAddressGetAccept | Unset = "application/xml",
    accept_encoding: LookupGeoAddressGetAcceptEncoding | Unset = UNSET,
    accept_language: LookupGeoAddressGetAcceptLanguage | Unset = "*",
) -> Response[AddressLookupResult | Any]:
    """GeoAddress lookup

     Looks up address records using a GeoAddress, a 19-character standardized identifier for a
    corresponding building or address. The documented identifier consists of ten leading digits derived
    from HK1980 grid coordinates with leading 8 digits removed, a `P` (podium) or `T` (tower) character,
    and an address record creation date in YYYYMMDD form. Request and response are encoded in UTF-8.

    Args:
        ga (str):
        n (int | Unset):  Default: 200.
        field_3d (LookupGeoAddressGet3D | Unset):  Default: 0.
        floor (str | Unset):
        unit (str | Unset):
        accept (LookupGeoAddressGetAccept | Unset):  Default: 'application/xml'.
        accept_encoding (LookupGeoAddressGetAcceptEncoding | Unset):
        accept_language (LookupGeoAddressGetAcceptLanguage | Unset):  Default: '*'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddressLookupResult | Any]
    """

    kwargs = _get_kwargs(
        ga=ga,
        n=n,
        field_3d=field_3d,
        floor=floor,
        unit=unit,
        accept=accept,
        accept_encoding=accept_encoding,
        accept_language=accept_language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    ga: str,
    n: int | Unset = 200,
    field_3d: LookupGeoAddressGet3D | Unset = 0,
    floor: str | Unset = UNSET,
    unit: str | Unset = UNSET,
    accept: LookupGeoAddressGetAccept | Unset = "application/xml",
    accept_encoding: LookupGeoAddressGetAcceptEncoding | Unset = UNSET,
    accept_language: LookupGeoAddressGetAcceptLanguage | Unset = "*",
) -> AddressLookupResult | Any | None:
    """GeoAddress lookup

     Looks up address records using a GeoAddress, a 19-character standardized identifier for a
    corresponding building or address. The documented identifier consists of ten leading digits derived
    from HK1980 grid coordinates with leading 8 digits removed, a `P` (podium) or `T` (tower) character,
    and an address record creation date in YYYYMMDD form. Request and response are encoded in UTF-8.

    Args:
        ga (str):
        n (int | Unset):  Default: 200.
        field_3d (LookupGeoAddressGet3D | Unset):  Default: 0.
        floor (str | Unset):
        unit (str | Unset):
        accept (LookupGeoAddressGetAccept | Unset):  Default: 'application/xml'.
        accept_encoding (LookupGeoAddressGetAcceptEncoding | Unset):
        accept_language (LookupGeoAddressGetAcceptLanguage | Unset):  Default: '*'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddressLookupResult | Any
    """

    return (
        await asyncio_detailed(
            client=client,
            ga=ga,
            n=n,
            field_3d=field_3d,
            floor=floor,
            unit=unit,
            accept=accept,
            accept_encoding=accept_encoding,
            accept_language=accept_language,
        )
    ).parsed
