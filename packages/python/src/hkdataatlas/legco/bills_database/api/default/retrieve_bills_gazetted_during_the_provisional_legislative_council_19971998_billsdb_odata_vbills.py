from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.observed_bills_response import ObservedBillsResponse
from ...models.retrieve_bills_gazetted_during_the_provisional_legislative_council_19971998_billsdb_odata_vbills_filter import (
    RetrieveBillsGazettedDuringTheProvisionalLegislativeCouncil19971998BillsdbOdataVbillsFilter,
)
from ...models.retrieve_bills_gazetted_during_the_provisional_legislative_council_19971998_billsdb_odata_vbills_format import (
    RetrieveBillsGazettedDuringTheProvisionalLegislativeCouncil19971998BillsdbOdataVbillsFormat,
)
from ...models.retrieve_bills_gazetted_during_the_provisional_legislative_council_19971998_billsdb_odata_vbills_inlinecount import (
    RetrieveBillsGazettedDuringTheProvisionalLegislativeCouncil19971998BillsdbOdataVbillsInlinecount,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    format_: RetrieveBillsGazettedDuringTheProvisionalLegislativeCouncil19971998BillsdbOdataVbillsFormat
    | Unset = UNSET,
    inlinecount: RetrieveBillsGazettedDuringTheProvisionalLegislativeCouncil19971998BillsdbOdataVbillsInlinecount
    | Unset = UNSET,
    filter_: RetrieveBillsGazettedDuringTheProvisionalLegislativeCouncil19971998BillsdbOdataVbillsFilter
    | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_format_: str | Unset = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_

    params["$format"] = json_format_

    json_inlinecount: str | Unset = UNSET
    if not isinstance(inlinecount, Unset):
        json_inlinecount = inlinecount

    params["$inlinecount"] = json_inlinecount

    json_filter_: str | Unset = UNSET
    if not isinstance(filter_, Unset):
        json_filter_ = filter_

    params["$filter"] = json_filter_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/BillsDB/odata/Vbills",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ObservedBillsResponse | None:
    if response.status_code == 200:
        media_type = (
            response.headers.get("content-type", "").split(";", 1)[0].strip().lower()
        )
        if media_type != "application/json" and not media_type.endswith("+json"):
            return None
        response_200 = ObservedBillsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ObservedBillsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    format_: RetrieveBillsGazettedDuringTheProvisionalLegislativeCouncil19971998BillsdbOdataVbillsFormat
    | Unset = UNSET,
    inlinecount: RetrieveBillsGazettedDuringTheProvisionalLegislativeCouncil19971998BillsdbOdataVbillsInlinecount
    | Unset = UNSET,
    filter_: RetrieveBillsGazettedDuringTheProvisionalLegislativeCouncil19971998BillsdbOdataVbillsFilter
    | Unset = UNSET,
) -> Response[ObservedBillsResponse]:
    """Retrieve Bills Database

     Read-only retrieval of exact publisher-listed resources, beginning with https://app.legco.gov.hk/Bil
    lsDB/odata/Vbills?$format=json&$inlinecount=allpages&$filter=bill_gazette_date+ge+datetime%271997-
    07-01%27+and+bill_gazette_date+lt+datetime%271998-07-01%27. The complete evidenced URLs and native
    formats are retained in x-published-resource-requests; only their recorded selector combinations are
    evidenced. These are published retrieval links; no additional hosted API or URL template is
    asserted. Dictionary components describe contextual record fields without establishing the complete
    payload shape. Authentication is unspecified. The JSON response envelope and eight nullable date
    alternatives are observations from one complete retained response, separate from the PDF-defined
    record fields. Other selector results and XML payload structure remain unassessed.

    Args:
        format_ (RetrieveBillsGazettedDuringTheProvisionalLegislativeCouncil19971998BillsdbOdataVb
            illsFormat | Unset):
        inlinecount (RetrieveBillsGazettedDuringTheProvisionalLegislativeCouncil19971998BillsdbOda
            taVbillsInlinecount | Unset):
        filter_ (RetrieveBillsGazettedDuringTheProvisionalLegislativeCouncil19971998BillsdbOdataVb
            illsFilter | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ObservedBillsResponse]
    """

    kwargs = _get_kwargs(
        format_=format_,
        inlinecount=inlinecount,
        filter_=filter_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    format_: RetrieveBillsGazettedDuringTheProvisionalLegislativeCouncil19971998BillsdbOdataVbillsFormat
    | Unset = UNSET,
    inlinecount: RetrieveBillsGazettedDuringTheProvisionalLegislativeCouncil19971998BillsdbOdataVbillsInlinecount
    | Unset = UNSET,
    filter_: RetrieveBillsGazettedDuringTheProvisionalLegislativeCouncil19971998BillsdbOdataVbillsFilter
    | Unset = UNSET,
) -> ObservedBillsResponse | None:
    """Retrieve Bills Database

     Read-only retrieval of exact publisher-listed resources, beginning with https://app.legco.gov.hk/Bil
    lsDB/odata/Vbills?$format=json&$inlinecount=allpages&$filter=bill_gazette_date+ge+datetime%271997-
    07-01%27+and+bill_gazette_date+lt+datetime%271998-07-01%27. The complete evidenced URLs and native
    formats are retained in x-published-resource-requests; only their recorded selector combinations are
    evidenced. These are published retrieval links; no additional hosted API or URL template is
    asserted. Dictionary components describe contextual record fields without establishing the complete
    payload shape. Authentication is unspecified. The JSON response envelope and eight nullable date
    alternatives are observations from one complete retained response, separate from the PDF-defined
    record fields. Other selector results and XML payload structure remain unassessed.

    Args:
        format_ (RetrieveBillsGazettedDuringTheProvisionalLegislativeCouncil19971998BillsdbOdataVb
            illsFormat | Unset):
        inlinecount (RetrieveBillsGazettedDuringTheProvisionalLegislativeCouncil19971998BillsdbOda
            taVbillsInlinecount | Unset):
        filter_ (RetrieveBillsGazettedDuringTheProvisionalLegislativeCouncil19971998BillsdbOdataVb
            illsFilter | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ObservedBillsResponse
    """

    return sync_detailed(
        client=client,
        format_=format_,
        inlinecount=inlinecount,
        filter_=filter_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    format_: RetrieveBillsGazettedDuringTheProvisionalLegislativeCouncil19971998BillsdbOdataVbillsFormat
    | Unset = UNSET,
    inlinecount: RetrieveBillsGazettedDuringTheProvisionalLegislativeCouncil19971998BillsdbOdataVbillsInlinecount
    | Unset = UNSET,
    filter_: RetrieveBillsGazettedDuringTheProvisionalLegislativeCouncil19971998BillsdbOdataVbillsFilter
    | Unset = UNSET,
) -> Response[ObservedBillsResponse]:
    """Retrieve Bills Database

     Read-only retrieval of exact publisher-listed resources, beginning with https://app.legco.gov.hk/Bil
    lsDB/odata/Vbills?$format=json&$inlinecount=allpages&$filter=bill_gazette_date+ge+datetime%271997-
    07-01%27+and+bill_gazette_date+lt+datetime%271998-07-01%27. The complete evidenced URLs and native
    formats are retained in x-published-resource-requests; only their recorded selector combinations are
    evidenced. These are published retrieval links; no additional hosted API or URL template is
    asserted. Dictionary components describe contextual record fields without establishing the complete
    payload shape. Authentication is unspecified. The JSON response envelope and eight nullable date
    alternatives are observations from one complete retained response, separate from the PDF-defined
    record fields. Other selector results and XML payload structure remain unassessed.

    Args:
        format_ (RetrieveBillsGazettedDuringTheProvisionalLegislativeCouncil19971998BillsdbOdataVb
            illsFormat | Unset):
        inlinecount (RetrieveBillsGazettedDuringTheProvisionalLegislativeCouncil19971998BillsdbOda
            taVbillsInlinecount | Unset):
        filter_ (RetrieveBillsGazettedDuringTheProvisionalLegislativeCouncil19971998BillsdbOdataVb
            illsFilter | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ObservedBillsResponse]
    """

    kwargs = _get_kwargs(
        format_=format_,
        inlinecount=inlinecount,
        filter_=filter_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    format_: RetrieveBillsGazettedDuringTheProvisionalLegislativeCouncil19971998BillsdbOdataVbillsFormat
    | Unset = UNSET,
    inlinecount: RetrieveBillsGazettedDuringTheProvisionalLegislativeCouncil19971998BillsdbOdataVbillsInlinecount
    | Unset = UNSET,
    filter_: RetrieveBillsGazettedDuringTheProvisionalLegislativeCouncil19971998BillsdbOdataVbillsFilter
    | Unset = UNSET,
) -> ObservedBillsResponse | None:
    """Retrieve Bills Database

     Read-only retrieval of exact publisher-listed resources, beginning with https://app.legco.gov.hk/Bil
    lsDB/odata/Vbills?$format=json&$inlinecount=allpages&$filter=bill_gazette_date+ge+datetime%271997-
    07-01%27+and+bill_gazette_date+lt+datetime%271998-07-01%27. The complete evidenced URLs and native
    formats are retained in x-published-resource-requests; only their recorded selector combinations are
    evidenced. These are published retrieval links; no additional hosted API or URL template is
    asserted. Dictionary components describe contextual record fields without establishing the complete
    payload shape. Authentication is unspecified. The JSON response envelope and eight nullable date
    alternatives are observations from one complete retained response, separate from the PDF-defined
    record fields. Other selector results and XML payload structure remain unassessed.

    Args:
        format_ (RetrieveBillsGazettedDuringTheProvisionalLegislativeCouncil19971998BillsdbOdataVb
            illsFormat | Unset):
        inlinecount (RetrieveBillsGazettedDuringTheProvisionalLegislativeCouncil19971998BillsdbOda
            taVbillsInlinecount | Unset):
        filter_ (RetrieveBillsGazettedDuringTheProvisionalLegislativeCouncil19971998BillsdbOdataVb
            illsFilter | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ObservedBillsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            format_=format_,
            inlinecount=inlinecount,
            filter_=filter_,
        )
    ).parsed
