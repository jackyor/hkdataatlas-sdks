from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_fundraising_activities_xml_activity import (
    GetFundraisingActivitiesXmlActivity,
)
from ...models.get_fundraising_activities_xml_charitable import (
    GetFundraisingActivitiesXmlCharitable,
)
from ...models.get_fundraising_activities_xml_licence import (
    GetFundraisingActivitiesXmlLicence,
)
from ...models.get_fundraising_activities_xml_orderby import (
    GetFundraisingActivitiesXmlOrderby,
)
from ...models.get_fundraising_activities_xml_orderstyle import (
    GetFundraisingActivitiesXmlOrderstyle,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    fromdate: str | Unset = UNSET,
    todate: str | Unset = UNSET,
    activity: GetFundraisingActivitiesXmlActivity | Unset = UNSET,
    licence: GetFundraisingActivitiesXmlLicence | Unset = UNSET,
    charitable: GetFundraisingActivitiesXmlCharitable | Unset = UNSET,
    orderby: GetFundraisingActivitiesXmlOrderby | Unset = "date",
    orderstyle: GetFundraisingActivitiesXmlOrderstyle | Unset = "desc",
    itemperpage: int | Unset = 10,
    page: int | Unset = 1,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["fromdate"] = fromdate

    params["todate"] = todate

    json_activity: str | Unset = UNSET
    if not isinstance(activity, Unset):
        json_activity = activity

    params["activity"] = json_activity

    json_licence: str | Unset = UNSET
    if not isinstance(licence, Unset):
        json_licence = licence

    params["licence"] = json_licence

    json_charitable: int | Unset = UNSET
    if not isinstance(charitable, Unset):
        json_charitable = charitable

    params["charitable"] = json_charitable

    json_orderby: str | Unset = UNSET
    if not isinstance(orderby, Unset):
        json_orderby = orderby

    params["orderby"] = json_orderby

    json_orderstyle: str | Unset = UNSET
    if not isinstance(orderstyle, Unset):
        json_orderstyle = orderstyle

    params["orderstyle"] = json_orderstyle

    params["itemperpage"] = itemperpage

    params["page"] = page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/xml",
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
    fromdate: str | Unset = UNSET,
    todate: str | Unset = UNSET,
    activity: GetFundraisingActivitiesXmlActivity | Unset = UNSET,
    licence: GetFundraisingActivitiesXmlLicence | Unset = UNSET,
    charitable: GetFundraisingActivitiesXmlCharitable | Unset = UNSET,
    orderby: GetFundraisingActivitiesXmlOrderby | Unset = "date",
    orderstyle: GetFundraisingActivitiesXmlOrderstyle | Unset = "desc",
    itemperpage: int | Unset = 10,
    page: int | Unset = 1,
) -> Response[Any]:
    """Search fund-raising activities (XML)

     Searches fund-raising activities using the same documented query parameters and behavior as the JSON
    resource. An activity schedule with timeFrom and timeTo both equal to 00:00 indicates a whole-day
    event.

    Args:
        fromdate (str | Unset):
        todate (str | Unset):
        activity (GetFundraisingActivitiesXmlActivity | Unset):
        licence (GetFundraisingActivitiesXmlLicence | Unset):
        charitable (GetFundraisingActivitiesXmlCharitable | Unset):
        orderby (GetFundraisingActivitiesXmlOrderby | Unset):  Default: 'date'.
        orderstyle (GetFundraisingActivitiesXmlOrderstyle | Unset):  Default: 'desc'.
        itemperpage (int | Unset):  Default: 10.
        page (int | Unset):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        fromdate=fromdate,
        todate=todate,
        activity=activity,
        licence=licence,
        charitable=charitable,
        orderby=orderby,
        orderstyle=orderstyle,
        itemperpage=itemperpage,
        page=page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    fromdate: str | Unset = UNSET,
    todate: str | Unset = UNSET,
    activity: GetFundraisingActivitiesXmlActivity | Unset = UNSET,
    licence: GetFundraisingActivitiesXmlLicence | Unset = UNSET,
    charitable: GetFundraisingActivitiesXmlCharitable | Unset = UNSET,
    orderby: GetFundraisingActivitiesXmlOrderby | Unset = "date",
    orderstyle: GetFundraisingActivitiesXmlOrderstyle | Unset = "desc",
    itemperpage: int | Unset = 10,
    page: int | Unset = 1,
) -> Response[Any]:
    """Search fund-raising activities (XML)

     Searches fund-raising activities using the same documented query parameters and behavior as the JSON
    resource. An activity schedule with timeFrom and timeTo both equal to 00:00 indicates a whole-day
    event.

    Args:
        fromdate (str | Unset):
        todate (str | Unset):
        activity (GetFundraisingActivitiesXmlActivity | Unset):
        licence (GetFundraisingActivitiesXmlLicence | Unset):
        charitable (GetFundraisingActivitiesXmlCharitable | Unset):
        orderby (GetFundraisingActivitiesXmlOrderby | Unset):  Default: 'date'.
        orderstyle (GetFundraisingActivitiesXmlOrderstyle | Unset):  Default: 'desc'.
        itemperpage (int | Unset):  Default: 10.
        page (int | Unset):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        fromdate=fromdate,
        todate=todate,
        activity=activity,
        licence=licence,
        charitable=charitable,
        orderby=orderby,
        orderstyle=orderstyle,
        itemperpage=itemperpage,
        page=page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
