from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.address_lookup_result import AddressLookupResult
from ...models.lookup_address_get_3d import (
    LookupAddressGet3D,
)
from ...models.lookup_address_get_accept import (
    LookupAddressGetAccept,
)
from ...models.lookup_address_get_accept_encoding import (
    LookupAddressGetAcceptEncoding,
)
from ...models.lookup_address_get_accept_language import (
    LookupAddressGetAcceptLanguage,
)
from ...models.lookup_address_get_b import LookupAddressGetB
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    q: str,
    n: int | Unset = 200,
    t: int | Unset = 35,
    b: LookupAddressGetB | Unset = 0,
    field_3d: LookupAddressGet3D | Unset = 0,
    floor: str | Unset = UNSET,
    unit: str | Unset = UNSET,
    accept: LookupAddressGetAccept | Unset = "application/xml",
    accept_encoding: LookupAddressGetAcceptEncoding | Unset = UNSET,
    accept_language: LookupAddressGetAcceptLanguage | Unset = "*",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept, Unset):
        headers["Accept"] = str(accept)

    if not isinstance(accept_encoding, Unset):
        headers["Accept-Encoding"] = str(accept_encoding)

    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = str(accept_language)

    params: dict[str, Any] = {}

    params["q"] = q

    params["n"] = n

    params["t"] = t

    json_b: int | Unset = UNSET
    if not isinstance(b, Unset):
        json_b = b

    params["b"] = json_b

    json_field_3d: int | Unset = UNSET
    if not isinstance(field_3d, Unset):
        json_field_3d = field_3d

    params["3d"] = json_field_3d

    params["floor"] = floor

    params["unit"] = unit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/lookup",
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
    q: str,
    n: int | Unset = 200,
    t: int | Unset = 35,
    b: LookupAddressGetB | Unset = 0,
    field_3d: LookupAddressGet3D | Unset = 0,
    floor: str | Unset = UNSET,
    unit: str | Unset = UNSET,
    accept: LookupAddressGetAccept | Unset = "application/xml",
    accept_encoding: LookupAddressGetAcceptEncoding | Unset = UNSET,
    accept_language: LookupAddressGetAcceptLanguage | Unset = "*",
) -> Response[AddressLookupResult | Any]:
    """Address lookup

     Looks up address records from free-text address elements and may return addresses with similar
    spelling or pronunciation. Request and response are encoded in UTF-8. Results are ordered in
    decreasing similarity. The response structure is supported by the publisher's dictionary and one
    documented JSON observation; that observation does not establish universal requiredness or a
    complete response contract.

    Args:
        q (str):
        n (int | Unset):  Default: 200.
        t (int | Unset):  Default: 35.
        b (LookupAddressGetB | Unset):  Default: 0.
        field_3d (LookupAddressGet3D | Unset):  Default: 0.
        floor (str | Unset):
        unit (str | Unset):
        accept (LookupAddressGetAccept | Unset):  Default: 'application/xml'.
        accept_encoding (LookupAddressGetAcceptEncoding | Unset):
        accept_language (LookupAddressGetAcceptLanguage | Unset):  Default: '*'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddressLookupResult | Any]
    """

    kwargs = _get_kwargs(
        q=q,
        n=n,
        t=t,
        b=b,
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
    q: str,
    n: int | Unset = 200,
    t: int | Unset = 35,
    b: LookupAddressGetB | Unset = 0,
    field_3d: LookupAddressGet3D | Unset = 0,
    floor: str | Unset = UNSET,
    unit: str | Unset = UNSET,
    accept: LookupAddressGetAccept | Unset = "application/xml",
    accept_encoding: LookupAddressGetAcceptEncoding | Unset = UNSET,
    accept_language: LookupAddressGetAcceptLanguage | Unset = "*",
) -> AddressLookupResult | Any | None:
    """Address lookup

     Looks up address records from free-text address elements and may return addresses with similar
    spelling or pronunciation. Request and response are encoded in UTF-8. Results are ordered in
    decreasing similarity. The response structure is supported by the publisher's dictionary and one
    documented JSON observation; that observation does not establish universal requiredness or a
    complete response contract.

    Args:
        q (str):
        n (int | Unset):  Default: 200.
        t (int | Unset):  Default: 35.
        b (LookupAddressGetB | Unset):  Default: 0.
        field_3d (LookupAddressGet3D | Unset):  Default: 0.
        floor (str | Unset):
        unit (str | Unset):
        accept (LookupAddressGetAccept | Unset):  Default: 'application/xml'.
        accept_encoding (LookupAddressGetAcceptEncoding | Unset):
        accept_language (LookupAddressGetAcceptLanguage | Unset):  Default: '*'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddressLookupResult | Any
    """

    return sync_detailed(
        client=client,
        q=q,
        n=n,
        t=t,
        b=b,
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
    q: str,
    n: int | Unset = 200,
    t: int | Unset = 35,
    b: LookupAddressGetB | Unset = 0,
    field_3d: LookupAddressGet3D | Unset = 0,
    floor: str | Unset = UNSET,
    unit: str | Unset = UNSET,
    accept: LookupAddressGetAccept | Unset = "application/xml",
    accept_encoding: LookupAddressGetAcceptEncoding | Unset = UNSET,
    accept_language: LookupAddressGetAcceptLanguage | Unset = "*",
) -> Response[AddressLookupResult | Any]:
    """Address lookup

     Looks up address records from free-text address elements and may return addresses with similar
    spelling or pronunciation. Request and response are encoded in UTF-8. Results are ordered in
    decreasing similarity. The response structure is supported by the publisher's dictionary and one
    documented JSON observation; that observation does not establish universal requiredness or a
    complete response contract.

    Args:
        q (str):
        n (int | Unset):  Default: 200.
        t (int | Unset):  Default: 35.
        b (LookupAddressGetB | Unset):  Default: 0.
        field_3d (LookupAddressGet3D | Unset):  Default: 0.
        floor (str | Unset):
        unit (str | Unset):
        accept (LookupAddressGetAccept | Unset):  Default: 'application/xml'.
        accept_encoding (LookupAddressGetAcceptEncoding | Unset):
        accept_language (LookupAddressGetAcceptLanguage | Unset):  Default: '*'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddressLookupResult | Any]
    """

    kwargs = _get_kwargs(
        q=q,
        n=n,
        t=t,
        b=b,
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
    q: str,
    n: int | Unset = 200,
    t: int | Unset = 35,
    b: LookupAddressGetB | Unset = 0,
    field_3d: LookupAddressGet3D | Unset = 0,
    floor: str | Unset = UNSET,
    unit: str | Unset = UNSET,
    accept: LookupAddressGetAccept | Unset = "application/xml",
    accept_encoding: LookupAddressGetAcceptEncoding | Unset = UNSET,
    accept_language: LookupAddressGetAcceptLanguage | Unset = "*",
) -> AddressLookupResult | Any | None:
    """Address lookup

     Looks up address records from free-text address elements and may return addresses with similar
    spelling or pronunciation. Request and response are encoded in UTF-8. Results are ordered in
    decreasing similarity. The response structure is supported by the publisher's dictionary and one
    documented JSON observation; that observation does not establish universal requiredness or a
    complete response contract.

    Args:
        q (str):
        n (int | Unset):  Default: 200.
        t (int | Unset):  Default: 35.
        b (LookupAddressGetB | Unset):  Default: 0.
        field_3d (LookupAddressGet3D | Unset):  Default: 0.
        floor (str | Unset):
        unit (str | Unset):
        accept (LookupAddressGetAccept | Unset):  Default: 'application/xml'.
        accept_encoding (LookupAddressGetAcceptEncoding | Unset):
        accept_language (LookupAddressGetAcceptLanguage | Unset):  Default: '*'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddressLookupResult | Any
    """

    return (
        await asyncio_detailed(
            client=client,
            q=q,
            n=n,
            t=t,
            b=b,
            field_3d=field_3d,
            floor=floor,
            unit=unit,
            accept=accept,
            accept_encoding=accept_encoding,
            accept_language=accept_language,
        )
    ).parsed
