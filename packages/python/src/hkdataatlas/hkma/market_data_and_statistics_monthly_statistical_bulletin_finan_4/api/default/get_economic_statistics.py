from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.sortorder import Sortorder
from ...models.source_response_model import SourceResponseModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    pagesize: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    fields: str | Unset = UNSET,
    column: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
    choose: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    sortby: str | Unset = UNSET,
    sortorder: Sortorder | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["pagesize"] = pagesize

    params["offset"] = offset

    params["fields"] = fields

    params["column"] = column

    params["filter"] = filter_

    params["choose"] = choose

    params["from"] = from_

    params["to"] = to

    params["sortby"] = sortby

    json_sortorder: str | Unset = UNSET
    if not isinstance(sortorder, Unset):
        json_sortorder = sortorder

    params["sortorder"] = json_sortorder

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/economic-statistics",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ErrorResponse | SourceResponseModel | None:
    if response.status_code == 200:
        response_200 = SourceResponseModel.from_dict(response.json())

        return response_200

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ErrorResponse | SourceResponseModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    pagesize: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    fields: str | Unset = UNSET,
    column: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
    choose: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    sortby: str | Unset = UNSET,
    sortorder: Sortorder | Unset = UNSET,
) -> Response[ErrorResponse | SourceResponseModel]:
    """Retrieve data of Economic statistics

    Args:
        pagesize (int | Unset):
        offset (int | Unset):
        fields (str | Unset):
        column (str | Unset):
        filter_ (str | Unset):
        choose (str | Unset):
        from_ (str | Unset):
        to (str | Unset):
        sortby (str | Unset):
        sortorder (Sortorder | Unset):  Example: asc.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | SourceResponseModel]
    """

    kwargs = _get_kwargs(
        pagesize=pagesize,
        offset=offset,
        fields=fields,
        column=column,
        filter_=filter_,
        choose=choose,
        from_=from_,
        to=to,
        sortby=sortby,
        sortorder=sortorder,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    pagesize: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    fields: str | Unset = UNSET,
    column: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
    choose: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    sortby: str | Unset = UNSET,
    sortorder: Sortorder | Unset = UNSET,
) -> ErrorResponse | SourceResponseModel | None:
    """Retrieve data of Economic statistics

    Args:
        pagesize (int | Unset):
        offset (int | Unset):
        fields (str | Unset):
        column (str | Unset):
        filter_ (str | Unset):
        choose (str | Unset):
        from_ (str | Unset):
        to (str | Unset):
        sortby (str | Unset):
        sortorder (Sortorder | Unset):  Example: asc.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | SourceResponseModel
    """

    return sync_detailed(
        client=client,
        pagesize=pagesize,
        offset=offset,
        fields=fields,
        column=column,
        filter_=filter_,
        choose=choose,
        from_=from_,
        to=to,
        sortby=sortby,
        sortorder=sortorder,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    pagesize: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    fields: str | Unset = UNSET,
    column: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
    choose: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    sortby: str | Unset = UNSET,
    sortorder: Sortorder | Unset = UNSET,
) -> Response[ErrorResponse | SourceResponseModel]:
    """Retrieve data of Economic statistics

    Args:
        pagesize (int | Unset):
        offset (int | Unset):
        fields (str | Unset):
        column (str | Unset):
        filter_ (str | Unset):
        choose (str | Unset):
        from_ (str | Unset):
        to (str | Unset):
        sortby (str | Unset):
        sortorder (Sortorder | Unset):  Example: asc.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | SourceResponseModel]
    """

    kwargs = _get_kwargs(
        pagesize=pagesize,
        offset=offset,
        fields=fields,
        column=column,
        filter_=filter_,
        choose=choose,
        from_=from_,
        to=to,
        sortby=sortby,
        sortorder=sortorder,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    pagesize: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    fields: str | Unset = UNSET,
    column: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
    choose: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    sortby: str | Unset = UNSET,
    sortorder: Sortorder | Unset = UNSET,
) -> ErrorResponse | SourceResponseModel | None:
    """Retrieve data of Economic statistics

    Args:
        pagesize (int | Unset):
        offset (int | Unset):
        fields (str | Unset):
        column (str | Unset):
        filter_ (str | Unset):
        choose (str | Unset):
        from_ (str | Unset):
        to (str | Unset):
        sortby (str | Unset):
        sortorder (Sortorder | Unset):  Example: asc.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | SourceResponseModel
    """

    return (
        await asyncio_detailed(
            client=client,
            pagesize=pagesize,
            offset=offset,
            fields=fields,
            column=column,
            filter_=filter_,
            choose=choose,
            from_=from_,
            to=to,
            sortby=sortby,
            sortorder=sortorder,
        )
    ).parsed
