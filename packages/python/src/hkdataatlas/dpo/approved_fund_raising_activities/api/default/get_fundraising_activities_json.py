from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.fundraising_response import FundraisingResponse
from ...models.get_fundraising_activities_json_activity import (
    GetFundraisingActivitiesJsonActivity,
)
from ...models.get_fundraising_activities_json_charitable import (
    GetFundraisingActivitiesJsonCharitable,
)
from ...models.get_fundraising_activities_json_licence import (
    GetFundraisingActivitiesJsonLicence,
)
from ...models.get_fundraising_activities_json_orderby import (
    GetFundraisingActivitiesJsonOrderby,
)
from ...models.get_fundraising_activities_json_orderstyle import (
    GetFundraisingActivitiesJsonOrderstyle,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    fromdate: str | Unset = UNSET,
    todate: str | Unset = UNSET,
    activity: GetFundraisingActivitiesJsonActivity | Unset = UNSET,
    licence: GetFundraisingActivitiesJsonLicence | Unset = UNSET,
    charitable: GetFundraisingActivitiesJsonCharitable | Unset = UNSET,
    orderby: GetFundraisingActivitiesJsonOrderby | Unset = "date",
    orderstyle: GetFundraisingActivitiesJsonOrderstyle | Unset = "desc",
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
        "url": "/json",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> FundraisingResponse | None:
    if response.status_code == 200:
        media_type = (
            response.headers.get("content-type", "").split(";", 1)[0].strip().lower()
        )
        if media_type != "application/json" and not media_type.endswith("+json"):
            return None
        response_200 = FundraisingResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[FundraisingResponse]:
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
    activity: GetFundraisingActivitiesJsonActivity | Unset = UNSET,
    licence: GetFundraisingActivitiesJsonLicence | Unset = UNSET,
    charitable: GetFundraisingActivitiesJsonCharitable | Unset = UNSET,
    orderby: GetFundraisingActivitiesJsonOrderby | Unset = "date",
    orderstyle: GetFundraisingActivitiesJsonOrderstyle | Unset = "desc",
    itemperpage: int | Unset = 10,
    page: int | Unset = 1,
) -> Response[FundraisingResponse]:
    """Search fund-raising activities (JSON)

     Searches fund-raising activities. If either fromdate or todate is omitted, today's activity is
    returned. If activity, licence, or charitable is omitted, no filter is applied for that criterion.
    Defaults: orderby=date, orderstyle=desc, itemperpage=10, and page=1. A requested itemperpage greater
    than 100 yields at most 100 records per request. An activity schedule with timeFrom and timeTo both
    equal to 00:00 indicates a whole-day event.

    Args:
        fromdate (str | Unset):
        todate (str | Unset):
        activity (GetFundraisingActivitiesJsonActivity | Unset):
        licence (GetFundraisingActivitiesJsonLicence | Unset):
        charitable (GetFundraisingActivitiesJsonCharitable | Unset):
        orderby (GetFundraisingActivitiesJsonOrderby | Unset):  Default: 'date'.
        orderstyle (GetFundraisingActivitiesJsonOrderstyle | Unset):  Default: 'desc'.
        itemperpage (int | Unset):  Default: 10.
        page (int | Unset):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FundraisingResponse]
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


def sync(
    *,
    client: AuthenticatedClient | Client,
    fromdate: str | Unset = UNSET,
    todate: str | Unset = UNSET,
    activity: GetFundraisingActivitiesJsonActivity | Unset = UNSET,
    licence: GetFundraisingActivitiesJsonLicence | Unset = UNSET,
    charitable: GetFundraisingActivitiesJsonCharitable | Unset = UNSET,
    orderby: GetFundraisingActivitiesJsonOrderby | Unset = "date",
    orderstyle: GetFundraisingActivitiesJsonOrderstyle | Unset = "desc",
    itemperpage: int | Unset = 10,
    page: int | Unset = 1,
) -> FundraisingResponse | None:
    """Search fund-raising activities (JSON)

     Searches fund-raising activities. If either fromdate or todate is omitted, today's activity is
    returned. If activity, licence, or charitable is omitted, no filter is applied for that criterion.
    Defaults: orderby=date, orderstyle=desc, itemperpage=10, and page=1. A requested itemperpage greater
    than 100 yields at most 100 records per request. An activity schedule with timeFrom and timeTo both
    equal to 00:00 indicates a whole-day event.

    Args:
        fromdate (str | Unset):
        todate (str | Unset):
        activity (GetFundraisingActivitiesJsonActivity | Unset):
        licence (GetFundraisingActivitiesJsonLicence | Unset):
        charitable (GetFundraisingActivitiesJsonCharitable | Unset):
        orderby (GetFundraisingActivitiesJsonOrderby | Unset):  Default: 'date'.
        orderstyle (GetFundraisingActivitiesJsonOrderstyle | Unset):  Default: 'desc'.
        itemperpage (int | Unset):  Default: 10.
        page (int | Unset):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FundraisingResponse
    """

    return sync_detailed(
        client=client,
        fromdate=fromdate,
        todate=todate,
        activity=activity,
        licence=licence,
        charitable=charitable,
        orderby=orderby,
        orderstyle=orderstyle,
        itemperpage=itemperpage,
        page=page,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    fromdate: str | Unset = UNSET,
    todate: str | Unset = UNSET,
    activity: GetFundraisingActivitiesJsonActivity | Unset = UNSET,
    licence: GetFundraisingActivitiesJsonLicence | Unset = UNSET,
    charitable: GetFundraisingActivitiesJsonCharitable | Unset = UNSET,
    orderby: GetFundraisingActivitiesJsonOrderby | Unset = "date",
    orderstyle: GetFundraisingActivitiesJsonOrderstyle | Unset = "desc",
    itemperpage: int | Unset = 10,
    page: int | Unset = 1,
) -> Response[FundraisingResponse]:
    """Search fund-raising activities (JSON)

     Searches fund-raising activities. If either fromdate or todate is omitted, today's activity is
    returned. If activity, licence, or charitable is omitted, no filter is applied for that criterion.
    Defaults: orderby=date, orderstyle=desc, itemperpage=10, and page=1. A requested itemperpage greater
    than 100 yields at most 100 records per request. An activity schedule with timeFrom and timeTo both
    equal to 00:00 indicates a whole-day event.

    Args:
        fromdate (str | Unset):
        todate (str | Unset):
        activity (GetFundraisingActivitiesJsonActivity | Unset):
        licence (GetFundraisingActivitiesJsonLicence | Unset):
        charitable (GetFundraisingActivitiesJsonCharitable | Unset):
        orderby (GetFundraisingActivitiesJsonOrderby | Unset):  Default: 'date'.
        orderstyle (GetFundraisingActivitiesJsonOrderstyle | Unset):  Default: 'desc'.
        itemperpage (int | Unset):  Default: 10.
        page (int | Unset):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FundraisingResponse]
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


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    fromdate: str | Unset = UNSET,
    todate: str | Unset = UNSET,
    activity: GetFundraisingActivitiesJsonActivity | Unset = UNSET,
    licence: GetFundraisingActivitiesJsonLicence | Unset = UNSET,
    charitable: GetFundraisingActivitiesJsonCharitable | Unset = UNSET,
    orderby: GetFundraisingActivitiesJsonOrderby | Unset = "date",
    orderstyle: GetFundraisingActivitiesJsonOrderstyle | Unset = "desc",
    itemperpage: int | Unset = 10,
    page: int | Unset = 1,
) -> FundraisingResponse | None:
    """Search fund-raising activities (JSON)

     Searches fund-raising activities. If either fromdate or todate is omitted, today's activity is
    returned. If activity, licence, or charitable is omitted, no filter is applied for that criterion.
    Defaults: orderby=date, orderstyle=desc, itemperpage=10, and page=1. A requested itemperpage greater
    than 100 yields at most 100 records per request. An activity schedule with timeFrom and timeTo both
    equal to 00:00 indicates a whole-day event.

    Args:
        fromdate (str | Unset):
        todate (str | Unset):
        activity (GetFundraisingActivitiesJsonActivity | Unset):
        licence (GetFundraisingActivitiesJsonLicence | Unset):
        charitable (GetFundraisingActivitiesJsonCharitable | Unset):
        orderby (GetFundraisingActivitiesJsonOrderby | Unset):  Default: 'date'.
        orderstyle (GetFundraisingActivitiesJsonOrderstyle | Unset):  Default: 'desc'.
        itemperpage (int | Unset):  Default: 10.
        page (int | Unset):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FundraisingResponse
    """

    return (
        await asyncio_detailed(
            client=client,
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
    ).parsed
