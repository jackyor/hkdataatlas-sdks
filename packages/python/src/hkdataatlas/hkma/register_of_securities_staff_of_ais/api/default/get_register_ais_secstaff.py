from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.is_curr_rel_indiv import IsCurrRelIndiv
from ...models.lang import Lang
from ...models.searchtype import Searchtype
from ...models.source_response_model import SourceResponseModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    lang: Lang,
    searchtype: Searchtype,
    surname: str | Unset = UNSET,
    forename: str | Unset = UNSET,
    chinesename: str | Unset = UNSET,
    is_curr_rel_indiv: IsCurrRelIndiv,
    reg_code: str | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    fields: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_lang: str = lang
    params["lang"] = json_lang

    json_searchtype: str = searchtype
    params["searchtype"] = json_searchtype

    params["surname"] = surname

    params["forename"] = forename

    params["chinesename"] = chinesename

    json_is_curr_rel_indiv: str = is_curr_rel_indiv
    params["is_curr_rel_indiv"] = json_is_curr_rel_indiv

    params["reg_code"] = reg_code

    params["pagesize"] = pagesize

    params["offset"] = offset

    params["fields"] = fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/register-ais-secstaff",
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
    lang: Lang,
    searchtype: Searchtype,
    surname: str | Unset = UNSET,
    forename: str | Unset = UNSET,
    chinesename: str | Unset = UNSET,
    is_curr_rel_indiv: IsCurrRelIndiv,
    reg_code: str | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    fields: str | Unset = UNSET,
) -> Response[ErrorResponse | SourceResponseModel]:
    """Retrieve data of Register of Securities Staff of AIs (eRegister)

     Select engName, chiName or regNo. engName requires surname and/or forename; chiName requires
    chinesename; regNo requires reg_code. Every search type requires is_curr_rel_indiv.

    OpenAPI3.0 cannot express dependencies between separate query parameters; conditional rules are
    documented in x-conditional-parameter-rules.

    Args:
        lang (Lang):  Example: en.
        searchtype (Searchtype):  Example: engName.
        surname (str | Unset):
        forename (str | Unset):
        chinesename (str | Unset):
        is_curr_rel_indiv (IsCurrRelIndiv):  Example: 0.
        reg_code (str | Unset):
        pagesize (int | Unset):
        offset (int | Unset):
        fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | SourceResponseModel]
    """

    kwargs = _get_kwargs(
        lang=lang,
        searchtype=searchtype,
        surname=surname,
        forename=forename,
        chinesename=chinesename,
        is_curr_rel_indiv=is_curr_rel_indiv,
        reg_code=reg_code,
        pagesize=pagesize,
        offset=offset,
        fields=fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    lang: Lang,
    searchtype: Searchtype,
    surname: str | Unset = UNSET,
    forename: str | Unset = UNSET,
    chinesename: str | Unset = UNSET,
    is_curr_rel_indiv: IsCurrRelIndiv,
    reg_code: str | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    fields: str | Unset = UNSET,
) -> ErrorResponse | SourceResponseModel | None:
    """Retrieve data of Register of Securities Staff of AIs (eRegister)

     Select engName, chiName or regNo. engName requires surname and/or forename; chiName requires
    chinesename; regNo requires reg_code. Every search type requires is_curr_rel_indiv.

    OpenAPI3.0 cannot express dependencies between separate query parameters; conditional rules are
    documented in x-conditional-parameter-rules.

    Args:
        lang (Lang):  Example: en.
        searchtype (Searchtype):  Example: engName.
        surname (str | Unset):
        forename (str | Unset):
        chinesename (str | Unset):
        is_curr_rel_indiv (IsCurrRelIndiv):  Example: 0.
        reg_code (str | Unset):
        pagesize (int | Unset):
        offset (int | Unset):
        fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | SourceResponseModel
    """

    return sync_detailed(
        client=client,
        lang=lang,
        searchtype=searchtype,
        surname=surname,
        forename=forename,
        chinesename=chinesename,
        is_curr_rel_indiv=is_curr_rel_indiv,
        reg_code=reg_code,
        pagesize=pagesize,
        offset=offset,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    lang: Lang,
    searchtype: Searchtype,
    surname: str | Unset = UNSET,
    forename: str | Unset = UNSET,
    chinesename: str | Unset = UNSET,
    is_curr_rel_indiv: IsCurrRelIndiv,
    reg_code: str | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    fields: str | Unset = UNSET,
) -> Response[ErrorResponse | SourceResponseModel]:
    """Retrieve data of Register of Securities Staff of AIs (eRegister)

     Select engName, chiName or regNo. engName requires surname and/or forename; chiName requires
    chinesename; regNo requires reg_code. Every search type requires is_curr_rel_indiv.

    OpenAPI3.0 cannot express dependencies between separate query parameters; conditional rules are
    documented in x-conditional-parameter-rules.

    Args:
        lang (Lang):  Example: en.
        searchtype (Searchtype):  Example: engName.
        surname (str | Unset):
        forename (str | Unset):
        chinesename (str | Unset):
        is_curr_rel_indiv (IsCurrRelIndiv):  Example: 0.
        reg_code (str | Unset):
        pagesize (int | Unset):
        offset (int | Unset):
        fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | SourceResponseModel]
    """

    kwargs = _get_kwargs(
        lang=lang,
        searchtype=searchtype,
        surname=surname,
        forename=forename,
        chinesename=chinesename,
        is_curr_rel_indiv=is_curr_rel_indiv,
        reg_code=reg_code,
        pagesize=pagesize,
        offset=offset,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    lang: Lang,
    searchtype: Searchtype,
    surname: str | Unset = UNSET,
    forename: str | Unset = UNSET,
    chinesename: str | Unset = UNSET,
    is_curr_rel_indiv: IsCurrRelIndiv,
    reg_code: str | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    fields: str | Unset = UNSET,
) -> ErrorResponse | SourceResponseModel | None:
    """Retrieve data of Register of Securities Staff of AIs (eRegister)

     Select engName, chiName or regNo. engName requires surname and/or forename; chiName requires
    chinesename; regNo requires reg_code. Every search type requires is_curr_rel_indiv.

    OpenAPI3.0 cannot express dependencies between separate query parameters; conditional rules are
    documented in x-conditional-parameter-rules.

    Args:
        lang (Lang):  Example: en.
        searchtype (Searchtype):  Example: engName.
        surname (str | Unset):
        forename (str | Unset):
        chinesename (str | Unset):
        is_curr_rel_indiv (IsCurrRelIndiv):  Example: 0.
        reg_code (str | Unset):
        pagesize (int | Unset):
        offset (int | Unset):
        fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | SourceResponseModel
    """

    return (
        await asyncio_detailed(
            client=client,
            lang=lang,
            searchtype=searchtype,
            surname=surname,
            forename=forename,
            chinesename=chinesename,
            is_curr_rel_indiv=is_curr_rel_indiv,
            reg_code=reg_code,
            pagesize=pagesize,
            offset=offset,
            fields=fields,
        )
    ).parsed
