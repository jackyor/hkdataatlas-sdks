from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.retrieve_the_voting_results_of_the_finance_committee_of_the_fifth_legislative_council_20122016_vrdb_odata_vvotingresult_filter import (
    RetrieveTheVotingResultsOfTheFinanceCommitteeOfTheFifthLegislativeCouncil20122016VrdbOdataVvotingresultFilter,
)
from ...models.retrieve_the_voting_results_of_the_finance_committee_of_the_fifth_legislative_council_20122016_vrdb_odata_vvotingresult_format import (
    RetrieveTheVotingResultsOfTheFinanceCommitteeOfTheFifthLegislativeCouncil20122016VrdbOdataVvotingresultFormat,
)
from ...models.retrieve_the_voting_results_of_the_finance_committee_of_the_fifth_legislative_council_20122016_vrdb_odata_vvotingresult_inlinecount import (
    RetrieveTheVotingResultsOfTheFinanceCommitteeOfTheFifthLegislativeCouncil20122016VrdbOdataVvotingresultInlinecount,
)
from ...types import UNSET, Response


def _get_kwargs(
    *,
    format_: RetrieveTheVotingResultsOfTheFinanceCommitteeOfTheFifthLegislativeCouncil20122016VrdbOdataVvotingresultFormat,
    filter_: RetrieveTheVotingResultsOfTheFinanceCommitteeOfTheFifthLegislativeCouncil20122016VrdbOdataVvotingresultFilter,
    inlinecount: RetrieveTheVotingResultsOfTheFinanceCommitteeOfTheFifthLegislativeCouncil20122016VrdbOdataVvotingresultInlinecount,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_format_: str = format_
    params["$format"] = json_format_

    json_filter_: str = filter_
    params["$filter"] = json_filter_

    json_inlinecount: str = inlinecount
    params["$inlinecount"] = json_inlinecount

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/vrdb/odata/vVotingResult",
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
    format_: RetrieveTheVotingResultsOfTheFinanceCommitteeOfTheFifthLegislativeCouncil20122016VrdbOdataVvotingresultFormat,
    filter_: RetrieveTheVotingResultsOfTheFinanceCommitteeOfTheFifthLegislativeCouncil20122016VrdbOdataVvotingresultFilter,
    inlinecount: RetrieveTheVotingResultsOfTheFinanceCommitteeOfTheFifthLegislativeCouncil20122016VrdbOdataVvotingresultInlinecount,
) -> Response[Any]:
    """Retrieve The voting results of the Finance Committee of the Fifth Legislative Council (2012 - 2016)

     Read-only retrieval of the exact publisher-listed XML resource https://app.legco.gov.hk/vrdb/odata/v
    VotingResult?$format=xml&$filter=type+eq+%27Finance+Committee%27+and+start_date+ge+datetime%272012-
    10-01%27+and+start_date+lt+datetime%272016-10-01%27&$inlinecount=allpages. This is a published data-
    file link; no additional hosted API or URL template is asserted. Dictionary components describe
    contextual record fields without establishing the complete payload shape. Authentication is
    unspecified.

    Args:
        format_ (RetrieveTheVotingResultsOfTheFinanceCommitteeOfTheFifthLegislativeCouncil20122016
            VrdbOdataVvotingresultFormat):
        filter_ (RetrieveTheVotingResultsOfTheFinanceCommitteeOfTheFifthLegislativeCouncil20122016
            VrdbOdataVvotingresultFilter):
        inlinecount (RetrieveTheVotingResultsOfTheFinanceCommitteeOfTheFifthLegislativeCouncil2012
            2016VrdbOdataVvotingresultInlinecount):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        format_=format_,
        filter_=filter_,
        inlinecount=inlinecount,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    format_: RetrieveTheVotingResultsOfTheFinanceCommitteeOfTheFifthLegislativeCouncil20122016VrdbOdataVvotingresultFormat,
    filter_: RetrieveTheVotingResultsOfTheFinanceCommitteeOfTheFifthLegislativeCouncil20122016VrdbOdataVvotingresultFilter,
    inlinecount: RetrieveTheVotingResultsOfTheFinanceCommitteeOfTheFifthLegislativeCouncil20122016VrdbOdataVvotingresultInlinecount,
) -> Response[Any]:
    """Retrieve The voting results of the Finance Committee of the Fifth Legislative Council (2012 - 2016)

     Read-only retrieval of the exact publisher-listed XML resource https://app.legco.gov.hk/vrdb/odata/v
    VotingResult?$format=xml&$filter=type+eq+%27Finance+Committee%27+and+start_date+ge+datetime%272012-
    10-01%27+and+start_date+lt+datetime%272016-10-01%27&$inlinecount=allpages. This is a published data-
    file link; no additional hosted API or URL template is asserted. Dictionary components describe
    contextual record fields without establishing the complete payload shape. Authentication is
    unspecified.

    Args:
        format_ (RetrieveTheVotingResultsOfTheFinanceCommitteeOfTheFifthLegislativeCouncil20122016
            VrdbOdataVvotingresultFormat):
        filter_ (RetrieveTheVotingResultsOfTheFinanceCommitteeOfTheFifthLegislativeCouncil20122016
            VrdbOdataVvotingresultFilter):
        inlinecount (RetrieveTheVotingResultsOfTheFinanceCommitteeOfTheFifthLegislativeCouncil2012
            2016VrdbOdataVvotingresultInlinecount):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        format_=format_,
        filter_=filter_,
        inlinecount=inlinecount,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
