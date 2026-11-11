from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.retrieve_the_terms_of_the_legislative_council_since_the_fifth_term_20122016_scheduledb_odata_tterm_inlinecount import (
    RetrieveTheTermsOfTheLegislativeCouncilSinceTheFifthTerm20122016ScheduledbOdataTtermInlinecount,
)
from ...types import UNSET, Response


def _get_kwargs(
    *,
    inlinecount: RetrieveTheTermsOfTheLegislativeCouncilSinceTheFifthTerm20122016ScheduledbOdataTtermInlinecount,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_inlinecount: str = inlinecount
    params["$inlinecount"] = json_inlinecount

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/ScheduleDB/odata/Tterm",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | None:
    if response.status_code == 200:
        media_type = (
            response.headers.get("content-type", "").split(";", 1)[0].strip().lower()
        )
        if media_type != "application/json" and not media_type.endswith("+json"):
            return None
        return None

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
    inlinecount: RetrieveTheTermsOfTheLegislativeCouncilSinceTheFifthTerm20122016ScheduledbOdataTtermInlinecount,
) -> Response[Any]:
    """Retrieve The terms of the Legislative Council since the Fifth Term (2012 - 2016)

     Read-only retrieval of the exact publisher-listed JSON resource
    https://app.legco.gov.hk/ScheduleDB/odata/Tterm?$inlinecount=allpages. This is a published data-file
    link; no additional hosted API or URL template is asserted. Dictionary components describe
    contextual record fields without establishing the complete payload shape. Authentication is
    unspecified.

    Args:
        inlinecount (RetrieveTheTermsOfTheLegislativeCouncilSinceTheFifthTerm20122016ScheduledbOda
            taTtermInlinecount):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        inlinecount=inlinecount,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    inlinecount: RetrieveTheTermsOfTheLegislativeCouncilSinceTheFifthTerm20122016ScheduledbOdataTtermInlinecount,
) -> Response[Any]:
    """Retrieve The terms of the Legislative Council since the Fifth Term (2012 - 2016)

     Read-only retrieval of the exact publisher-listed JSON resource
    https://app.legco.gov.hk/ScheduleDB/odata/Tterm?$inlinecount=allpages. This is a published data-file
    link; no additional hosted API or URL template is asserted. Dictionary components describe
    contextual record fields without establishing the complete payload shape. Authentication is
    unspecified.

    Args:
        inlinecount (RetrieveTheTermsOfTheLegislativeCouncilSinceTheFifthTerm20122016ScheduledbOda
            taTtermInlinecount):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        inlinecount=inlinecount,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
