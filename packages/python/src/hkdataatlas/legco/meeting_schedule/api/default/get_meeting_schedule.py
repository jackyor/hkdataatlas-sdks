from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.meeting import Meeting
from ...models.meeting_schedule_resource_type_2 import MeetingScheduleResourceType2
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/Tmeeting",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> list[Meeting] | Meeting | MeetingScheduleResourceType2 | None:
    if response.status_code == 200:
        media_type = (
            response.headers.get("content-type", "").split(";", 1)[0].strip().lower()
        )
        if media_type != "application/json" and not media_type.endswith("+json"):
            return None

        def _parse_response_200(
            data: object,
        ) -> list[Meeting] | Meeting | MeetingScheduleResourceType2:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_meeting_schedule_resource_type_0 = Meeting.from_dict(
                    data
                )

                return componentsschemas_meeting_schedule_resource_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                componentsschemas_meeting_schedule_resource_type_1 = []
                _componentsschemas_meeting_schedule_resource_type_1 = data
                for (
                    componentsschemas_meeting_schedule_resource_type_1_item_data
                ) in _componentsschemas_meeting_schedule_resource_type_1:
                    componentsschemas_meeting_schedule_resource_type_1_item = (
                        Meeting.from_dict(
                            componentsschemas_meeting_schedule_resource_type_1_item_data
                        )
                    )

                    componentsschemas_meeting_schedule_resource_type_1.append(
                        componentsschemas_meeting_schedule_resource_type_1_item
                    )

                return componentsschemas_meeting_schedule_resource_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_meeting_schedule_resource_type_2 = (
                MeetingScheduleResourceType2.from_dict(data)
            )

            return componentsschemas_meeting_schedule_resource_type_2

        response_200 = _parse_response_200(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[list[Meeting] | Meeting | MeetingScheduleResourceType2]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[list[Meeting] | Meeting | MeetingScheduleResourceType2]:
    """Retrieve the meeting schedule

     The catalogue lists this exact URL as a JSON resource for the schedule of meetings:
    https://app.legco.gov.hk/ScheduleDB/odata/Tmeeting. This is a literal published resource URL, not
    evidence for additional URL templates or query parameters. The dictionary documents the fields below
    but does not establish response envelope, field requiredness, or authentication.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[Meeting] | Meeting | MeetingScheduleResourceType2]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> list[Meeting] | Meeting | MeetingScheduleResourceType2 | None:
    """Retrieve the meeting schedule

     The catalogue lists this exact URL as a JSON resource for the schedule of meetings:
    https://app.legco.gov.hk/ScheduleDB/odata/Tmeeting. This is a literal published resource URL, not
    evidence for additional URL templates or query parameters. The dictionary documents the fields below
    but does not establish response envelope, field requiredness, or authentication.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[Meeting] | Meeting | MeetingScheduleResourceType2
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[list[Meeting] | Meeting | MeetingScheduleResourceType2]:
    """Retrieve the meeting schedule

     The catalogue lists this exact URL as a JSON resource for the schedule of meetings:
    https://app.legco.gov.hk/ScheduleDB/odata/Tmeeting. This is a literal published resource URL, not
    evidence for additional URL templates or query parameters. The dictionary documents the fields below
    but does not establish response envelope, field requiredness, or authentication.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[Meeting] | Meeting | MeetingScheduleResourceType2]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> list[Meeting] | Meeting | MeetingScheduleResourceType2 | None:
    """Retrieve the meeting schedule

     The catalogue lists this exact URL as a JSON resource for the schedule of meetings:
    https://app.legco.gov.hk/ScheduleDB/odata/Tmeeting. This is a literal published resource URL, not
    evidence for additional URL templates or query parameters. The dictionary documents the fields below
    but does not establish response envelope, field requiredness, or authentication.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[Meeting] | Meeting | MeetingScheduleResourceType2
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
