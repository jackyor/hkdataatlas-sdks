from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_location_and_profile_data_dataresource import (
    GetLocationAndProfileDataDataresource,
)
from ...models.get_location_and_profile_data_format import (
    GetLocationAndProfileDataFormat,
)
from ...models.get_location_and_profile_data_lang import (
    GetLocationAndProfileDataLang,
)
from ...models.location_profile_response import LocationProfileResponse
from ...types import Response


def _get_kwargs(
    dataresource: GetLocationAndProfileDataDataresource,
    lang: GetLocationAndProfileDataLang,
    format_: GetLocationAndProfileDataFormat,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/criteriafilter/{dataresource}/{lang}/{format_}".format(
            dataresource=quote(str(dataresource), safe=""),
            lang=quote(str(lang), safe=""),
            format_=quote(str(format_), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | LocationProfileResponse | None:
    if response.status_code == 200:
        response_200 = LocationProfileResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | LocationProfileResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dataresource: GetLocationAndProfileDataDataresource,
    lang: GetLocationAndProfileDataLang,
    format_: GetLocationAndProfileDataFormat,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | LocationProfileResponse]:
    """Get location and profile data

     Retrieves the selected dataset in the requested language and format. The documentation's example
    response is for Public Housing Estates. The data dictionary describes the fields for four resource
    types; it does not establish that every field appears in every returned record. The example response
    spells some keys with underscores where the dictionary presents labels with spaces; these spellings
    are preserved separately rather than assumed to be interchangeable. Authentication is explicitly not
    required.

    Args:
        dataresource (GetLocationAndProfileDataDataresource):
        lang (GetLocationAndProfileDataLang):
        format_ (GetLocationAndProfileDataFormat):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | LocationProfileResponse]
    """

    kwargs = _get_kwargs(
        dataresource=dataresource,
        lang=lang,
        format_=format_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dataresource: GetLocationAndProfileDataDataresource,
    lang: GetLocationAndProfileDataLang,
    format_: GetLocationAndProfileDataFormat,
    *,
    client: AuthenticatedClient | Client,
) -> Any | LocationProfileResponse | None:
    """Get location and profile data

     Retrieves the selected dataset in the requested language and format. The documentation's example
    response is for Public Housing Estates. The data dictionary describes the fields for four resource
    types; it does not establish that every field appears in every returned record. The example response
    spells some keys with underscores where the dictionary presents labels with spaces; these spellings
    are preserved separately rather than assumed to be interchangeable. Authentication is explicitly not
    required.

    Args:
        dataresource (GetLocationAndProfileDataDataresource):
        lang (GetLocationAndProfileDataLang):
        format_ (GetLocationAndProfileDataFormat):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | LocationProfileResponse
    """

    return sync_detailed(
        dataresource=dataresource,
        lang=lang,
        format_=format_,
        client=client,
    ).parsed


async def asyncio_detailed(
    dataresource: GetLocationAndProfileDataDataresource,
    lang: GetLocationAndProfileDataLang,
    format_: GetLocationAndProfileDataFormat,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | LocationProfileResponse]:
    """Get location and profile data

     Retrieves the selected dataset in the requested language and format. The documentation's example
    response is for Public Housing Estates. The data dictionary describes the fields for four resource
    types; it does not establish that every field appears in every returned record. The example response
    spells some keys with underscores where the dictionary presents labels with spaces; these spellings
    are preserved separately rather than assumed to be interchangeable. Authentication is explicitly not
    required.

    Args:
        dataresource (GetLocationAndProfileDataDataresource):
        lang (GetLocationAndProfileDataLang):
        format_ (GetLocationAndProfileDataFormat):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | LocationProfileResponse]
    """

    kwargs = _get_kwargs(
        dataresource=dataresource,
        lang=lang,
        format_=format_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dataresource: GetLocationAndProfileDataDataresource,
    lang: GetLocationAndProfileDataLang,
    format_: GetLocationAndProfileDataFormat,
    *,
    client: AuthenticatedClient | Client,
) -> Any | LocationProfileResponse | None:
    """Get location and profile data

     Retrieves the selected dataset in the requested language and format. The documentation's example
    response is for Public Housing Estates. The data dictionary describes the fields for four resource
    types; it does not establish that every field appears in every returned record. The example response
    spells some keys with underscores where the dictionary presents labels with spaces; these spellings
    are preserved separately rather than assumed to be interchangeable. Authentication is explicitly not
    required.

    Args:
        dataresource (GetLocationAndProfileDataDataresource):
        lang (GetLocationAndProfileDataLang):
        format_ (GetLocationAndProfileDataFormat):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | LocationProfileResponse
    """

    return (
        await asyncio_detailed(
            dataresource=dataresource,
            lang=lang,
            format_=format_,
            client=client,
        )
    ).parsed
