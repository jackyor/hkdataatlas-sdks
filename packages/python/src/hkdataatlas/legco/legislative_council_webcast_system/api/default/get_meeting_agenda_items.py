from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_meeting_agenda_items_response_200 import (
    GetMeetingAgendaItemsResponse200,
)
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/VMeetingInfo",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> GetMeetingAgendaItemsResponse200 | None:
    if response.status_code == 200:
        media_type = (
            response.headers.get("content-type", "").split(";", 1)[0].strip().lower()
        )
        if media_type != "application/json" and not media_type.endswith("+json"):
            return None
        response_200 = GetMeetingAgendaItemsResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[GetMeetingAgendaItemsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetMeetingAgendaItemsResponse200]:
    """Retrieve agenda items and time markers

     The exact published JSON resource URL is https://app.legco.gov.hk/wcod/odata/VMeetingInfo. The
    catalogue also publishes an XML resource URL at
    https://app.legco.gov.hk/wcod/odata/VMeetingInfo?$format=xml. Council-term-specific filtered
    download links are listed in the catalogue; those literal links do not establish a general query-
    parameter contract. Response envelope and status-code details are not documented.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetMeetingAgendaItemsResponse200]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> GetMeetingAgendaItemsResponse200 | None:
    """Retrieve agenda items and time markers

     The exact published JSON resource URL is https://app.legco.gov.hk/wcod/odata/VMeetingInfo. The
    catalogue also publishes an XML resource URL at
    https://app.legco.gov.hk/wcod/odata/VMeetingInfo?$format=xml. Council-term-specific filtered
    download links are listed in the catalogue; those literal links do not establish a general query-
    parameter contract. Response envelope and status-code details are not documented.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetMeetingAgendaItemsResponse200
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetMeetingAgendaItemsResponse200]:
    """Retrieve agenda items and time markers

     The exact published JSON resource URL is https://app.legco.gov.hk/wcod/odata/VMeetingInfo. The
    catalogue also publishes an XML resource URL at
    https://app.legco.gov.hk/wcod/odata/VMeetingInfo?$format=xml. Council-term-specific filtered
    download links are listed in the catalogue; those literal links do not establish a general query-
    parameter contract. Response envelope and status-code details are not documented.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetMeetingAgendaItemsResponse200]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> GetMeetingAgendaItemsResponse200 | None:
    """Retrieve agenda items and time markers

     The exact published JSON resource URL is https://app.legco.gov.hk/wcod/odata/VMeetingInfo. The
    catalogue also publishes an XML resource URL at
    https://app.legco.gov.hk/wcod/odata/VMeetingInfo?$format=xml. Council-term-specific filtered
    download links are listed in the catalogue; those literal links do not establish a general query-
    parameter contract. Response envelope and status-code details are not documented.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetMeetingAgendaItemsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
