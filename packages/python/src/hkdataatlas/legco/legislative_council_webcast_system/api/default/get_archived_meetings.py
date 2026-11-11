from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_archived_meetings_response_200 import GetArchivedMeetingsResponse200
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/VArchiveMeeting",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> GetArchivedMeetingsResponse200 | None:
    if response.status_code == 200:
        media_type = (
            response.headers.get("content-type", "").split(";", 1)[0].strip().lower()
        )
        if media_type != "application/json" and not media_type.endswith("+json"):
            return None
        response_200 = GetArchivedMeetingsResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[GetArchivedMeetingsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetArchivedMeetingsResponse200]:
    """Retrieve archived meeting information

     The exact published JSON resource URL is https://app.legco.gov.hk/wcod/odata/VArchiveMeeting. An XML
    resource is also published at https://app.legco.gov.hk/wcod/odata/VArchiveMeeting?$format=xml.
    Catalogue URLs include date-filtered downloads for specified council terms, but the data dictionary
    does not document a general filter parameter contract. Response envelope and status-code details are
    not documented.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetArchivedMeetingsResponse200]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> GetArchivedMeetingsResponse200 | None:
    """Retrieve archived meeting information

     The exact published JSON resource URL is https://app.legco.gov.hk/wcod/odata/VArchiveMeeting. An XML
    resource is also published at https://app.legco.gov.hk/wcod/odata/VArchiveMeeting?$format=xml.
    Catalogue URLs include date-filtered downloads for specified council terms, but the data dictionary
    does not document a general filter parameter contract. Response envelope and status-code details are
    not documented.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetArchivedMeetingsResponse200
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetArchivedMeetingsResponse200]:
    """Retrieve archived meeting information

     The exact published JSON resource URL is https://app.legco.gov.hk/wcod/odata/VArchiveMeeting. An XML
    resource is also published at https://app.legco.gov.hk/wcod/odata/VArchiveMeeting?$format=xml.
    Catalogue URLs include date-filtered downloads for specified council terms, but the data dictionary
    does not document a general filter parameter contract. Response envelope and status-code details are
    not documented.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetArchivedMeetingsResponse200]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> GetArchivedMeetingsResponse200 | None:
    """Retrieve archived meeting information

     The exact published JSON resource URL is https://app.legco.gov.hk/wcod/odata/VArchiveMeeting. An XML
    resource is also published at https://app.legco.gov.hk/wcod/odata/VArchiveMeeting?$format=xml.
    Catalogue URLs include date-filtered downloads for specified council terms, but the data dictionary
    does not document a general filter parameter contract. Response envelope and status-code details are
    not documented.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetArchivedMeetingsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
