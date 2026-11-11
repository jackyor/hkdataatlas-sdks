from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.retrieve_the_committees_of_the_sixth_legislative_council_20162021_scheduledb_odata_tcommittee_filter import (
    RetrieveTheCommitteesOfTheSixthLegislativeCouncil20162021ScheduledbOdataTcommitteeFilter,
)
from ...models.retrieve_the_committees_of_the_sixth_legislative_council_20162021_scheduledb_odata_tcommittee_format import (
    RetrieveTheCommitteesOfTheSixthLegislativeCouncil20162021ScheduledbOdataTcommitteeFormat,
)
from ...models.retrieve_the_committees_of_the_sixth_legislative_council_20162021_scheduledb_odata_tcommittee_inlinecount import (
    RetrieveTheCommitteesOfTheSixthLegislativeCouncil20162021ScheduledbOdataTcommitteeInlinecount,
)
from ...types import UNSET, Response


def _get_kwargs(
    *,
    filter_: RetrieveTheCommitteesOfTheSixthLegislativeCouncil20162021ScheduledbOdataTcommitteeFilter,
    format_: RetrieveTheCommitteesOfTheSixthLegislativeCouncil20162021ScheduledbOdataTcommitteeFormat,
    inlinecount: RetrieveTheCommitteesOfTheSixthLegislativeCouncil20162021ScheduledbOdataTcommitteeInlinecount,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_filter_: str = filter_
    params["$filter"] = json_filter_

    json_format_: str = format_
    params["$format"] = json_format_

    json_inlinecount: str = inlinecount
    params["$inlinecount"] = json_inlinecount

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/ScheduleDB/odata/Tcommittee",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | None:
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
    *,
    client: AuthenticatedClient | Client,
    filter_: RetrieveTheCommitteesOfTheSixthLegislativeCouncil20162021ScheduledbOdataTcommitteeFilter,
    format_: RetrieveTheCommitteesOfTheSixthLegislativeCouncil20162021ScheduledbOdataTcommitteeFormat,
    inlinecount: RetrieveTheCommitteesOfTheSixthLegislativeCouncil20162021ScheduledbOdataTcommitteeInlinecount,
) -> Response[Any]:
    """Retrieve The committees of the Sixth Legislative Council (2016 - 2021)

     Read-only retrieval of the exact publisher-listed XML resource https://app.legco.gov.hk/ScheduleDB/o
    data/Tcommittee?$filter=term_id+eq+5&$format=xml&$inlinecount=allpages. This is a published data-
    file link; no additional hosted API or URL template is asserted. Dictionary components describe
    contextual record fields without establishing the complete payload shape. Authentication is
    unspecified.

    Args:
        filter_ (RetrieveTheCommitteesOfTheSixthLegislativeCouncil20162021ScheduledbOdataTcommitte
            eFilter):
        format_ (RetrieveTheCommitteesOfTheSixthLegislativeCouncil20162021ScheduledbOdataTcommitte
            eFormat):
        inlinecount (RetrieveTheCommitteesOfTheSixthLegislativeCouncil20162021ScheduledbOdataTcomm
            itteeInlinecount):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        filter_=filter_,
        format_=format_,
        inlinecount=inlinecount,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    filter_: RetrieveTheCommitteesOfTheSixthLegislativeCouncil20162021ScheduledbOdataTcommitteeFilter,
    format_: RetrieveTheCommitteesOfTheSixthLegislativeCouncil20162021ScheduledbOdataTcommitteeFormat,
    inlinecount: RetrieveTheCommitteesOfTheSixthLegislativeCouncil20162021ScheduledbOdataTcommitteeInlinecount,
) -> Response[Any]:
    """Retrieve The committees of the Sixth Legislative Council (2016 - 2021)

     Read-only retrieval of the exact publisher-listed XML resource https://app.legco.gov.hk/ScheduleDB/o
    data/Tcommittee?$filter=term_id+eq+5&$format=xml&$inlinecount=allpages. This is a published data-
    file link; no additional hosted API or URL template is asserted. Dictionary components describe
    contextual record fields without establishing the complete payload shape. Authentication is
    unspecified.

    Args:
        filter_ (RetrieveTheCommitteesOfTheSixthLegislativeCouncil20162021ScheduledbOdataTcommitte
            eFilter):
        format_ (RetrieveTheCommitteesOfTheSixthLegislativeCouncil20162021ScheduledbOdataTcommitte
            eFormat):
        inlinecount (RetrieveTheCommitteesOfTheSixthLegislativeCouncil20162021ScheduledbOdataTcomm
            itteeInlinecount):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        filter_=filter_,
        format_=format_,
        inlinecount=inlinecount,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
