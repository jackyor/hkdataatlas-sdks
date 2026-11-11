from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.retrieve_oral_questions_of_the_fifth_legislative_council_20122016_chinese_version_questionsdb_odata_vieworalquestionschi_filter import (
    RetrieveOralQuestionsOfTheFifthLegislativeCouncil20122016ChineseVersionQuestionsdbOdataVieworalquestionschiFilter,
)
from ...models.retrieve_oral_questions_of_the_fifth_legislative_council_20122016_chinese_version_questionsdb_odata_vieworalquestionschi_format import (
    RetrieveOralQuestionsOfTheFifthLegislativeCouncil20122016ChineseVersionQuestionsdbOdataVieworalquestionschiFormat,
)
from ...models.retrieve_oral_questions_of_the_fifth_legislative_council_20122016_chinese_version_questionsdb_odata_vieworalquestionschi_inlinecount import (
    RetrieveOralQuestionsOfTheFifthLegislativeCouncil20122016ChineseVersionQuestionsdbOdataVieworalquestionschiInlinecount,
)
from ...types import UNSET, Response


def _get_kwargs(
    *,
    inlinecount: RetrieveOralQuestionsOfTheFifthLegislativeCouncil20122016ChineseVersionQuestionsdbOdataVieworalquestionschiInlinecount,
    filter_: RetrieveOralQuestionsOfTheFifthLegislativeCouncil20122016ChineseVersionQuestionsdbOdataVieworalquestionschiFilter,
    format_: RetrieveOralQuestionsOfTheFifthLegislativeCouncil20122016ChineseVersionQuestionsdbOdataVieworalquestionschiFormat,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_inlinecount: str = inlinecount
    params["$inlinecount"] = json_inlinecount

    json_filter_: str = filter_
    params["$filter"] = json_filter_

    json_format_: str = format_
    params["$format"] = json_format_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/QuestionsDB/odata/ViewOralQuestionsChi",
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
    inlinecount: RetrieveOralQuestionsOfTheFifthLegislativeCouncil20122016ChineseVersionQuestionsdbOdataVieworalquestionschiInlinecount,
    filter_: RetrieveOralQuestionsOfTheFifthLegislativeCouncil20122016ChineseVersionQuestionsdbOdataVieworalquestionschiFilter,
    format_: RetrieveOralQuestionsOfTheFifthLegislativeCouncil20122016ChineseVersionQuestionsdbOdataVieworalquestionschiFormat,
) -> Response[Any]:
    """Retrieve Oral questions of the Fifth Legislative Council (2012 - 2016) (Chinese version)

     Read-only retrieval of the exact publisher-listed XML resource https://app.legco.gov.hk/QuestionsDB/
    odata/ViewOralQuestionsChi?$inlinecount=allpages&$filter=MeetingDate+ge+datetime%272012-10-
    01%27+and+MeetingDate+lt+datetime%272016-10-01%27&$format=xml. This is a published data-file link;
    no additional hosted API or URL template is asserted. Dictionary components describe contextual
    record fields without establishing the complete payload shape. Authentication is unspecified.

    Args:
        inlinecount (RetrieveOralQuestionsOfTheFifthLegislativeCouncil20122016ChineseVersionQuesti
            onsdbOdataVieworalquestionschiInlinecount):
        filter_ (RetrieveOralQuestionsOfTheFifthLegislativeCouncil20122016ChineseVersionQuestionsd
            bOdataVieworalquestionschiFilter):
        format_ (RetrieveOralQuestionsOfTheFifthLegislativeCouncil20122016ChineseVersionQuestionsd
            bOdataVieworalquestionschiFormat):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        inlinecount=inlinecount,
        filter_=filter_,
        format_=format_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    inlinecount: RetrieveOralQuestionsOfTheFifthLegislativeCouncil20122016ChineseVersionQuestionsdbOdataVieworalquestionschiInlinecount,
    filter_: RetrieveOralQuestionsOfTheFifthLegislativeCouncil20122016ChineseVersionQuestionsdbOdataVieworalquestionschiFilter,
    format_: RetrieveOralQuestionsOfTheFifthLegislativeCouncil20122016ChineseVersionQuestionsdbOdataVieworalquestionschiFormat,
) -> Response[Any]:
    """Retrieve Oral questions of the Fifth Legislative Council (2012 - 2016) (Chinese version)

     Read-only retrieval of the exact publisher-listed XML resource https://app.legco.gov.hk/QuestionsDB/
    odata/ViewOralQuestionsChi?$inlinecount=allpages&$filter=MeetingDate+ge+datetime%272012-10-
    01%27+and+MeetingDate+lt+datetime%272016-10-01%27&$format=xml. This is a published data-file link;
    no additional hosted API or URL template is asserted. Dictionary components describe contextual
    record fields without establishing the complete payload shape. Authentication is unspecified.

    Args:
        inlinecount (RetrieveOralQuestionsOfTheFifthLegislativeCouncil20122016ChineseVersionQuesti
            onsdbOdataVieworalquestionschiInlinecount):
        filter_ (RetrieveOralQuestionsOfTheFifthLegislativeCouncil20122016ChineseVersionQuestionsd
            bOdataVieworalquestionschiFilter):
        format_ (RetrieveOralQuestionsOfTheFifthLegislativeCouncil20122016ChineseVersionQuestionsd
            bOdataVieworalquestionschiFormat):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        inlinecount=inlinecount,
        filter_=filter_,
        format_=format_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
