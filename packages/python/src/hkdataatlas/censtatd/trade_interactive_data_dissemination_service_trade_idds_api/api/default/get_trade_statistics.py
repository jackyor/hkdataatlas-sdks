from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.data_response import DataResponse
from ...models.get_trade_statistics_ccclass import (
    GetTradeStatisticsCcclass,
)
from ...models.get_trade_statistics_coclass import (
    GetTradeStatisticsCoclass,
)
from ...models.get_trade_statistics_codeclass import (
    GetTradeStatisticsCodeclass,
)
from ...models.get_trade_statistics_freq import (
    GetTradeStatisticsFreq,
)
from ...models.get_trade_statistics_lang import (
    GetTradeStatisticsLang,
)
from ...models.get_trade_statistics_sv_item import (
    GetTradeStatisticsSvItem,
)
from ...models.get_trade_statistics_tm import (
    GetTradeStatisticsTm,
)
from ...models.get_trade_statistics_ttype import (
    GetTradeStatisticsTtype,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    lang: GetTradeStatisticsLang,
    sv: list[GetTradeStatisticsSvItem],
    freq: GetTradeStatisticsFreq,
    period: str,
    ttype: GetTradeStatisticsTtype,
    tm: GetTradeStatisticsTm | Unset = UNSET,
    coclass: GetTradeStatisticsCoclass | Unset = UNSET,
    co: list[str] | Unset = UNSET,
    ccclass: GetTradeStatisticsCcclass | Unset = UNSET,
    cc: list[str] | Unset = UNSET,
    codeclass: GetTradeStatisticsCodeclass | Unset = UNSET,
    code: list[str] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_lang: str = lang
    params["lang"] = json_lang

    json_sv = []
    for sv_item_data in sv:
        sv_item: str = sv_item_data
        json_sv.append(sv_item)

    params["sv"] = json_sv

    json_freq: str = freq
    params["freq"] = json_freq

    params["period"] = period

    json_ttype: str = ttype
    params["ttype"] = json_ttype

    json_tm: str | Unset = UNSET
    if not isinstance(tm, Unset):
        json_tm = tm

    params["tm"] = json_tm

    json_coclass: str | Unset = UNSET
    if not isinstance(coclass, Unset):
        json_coclass = coclass

    params["coclass"] = json_coclass

    json_co: list[str] | Unset = UNSET
    if not isinstance(co, Unset):
        json_co = co

    params["co"] = json_co

    json_ccclass: str | Unset = UNSET
    if not isinstance(ccclass, Unset):
        json_ccclass = ccclass

    params["ccclass"] = json_ccclass

    json_cc: list[str] | Unset = UNSET
    if not isinstance(cc, Unset):
        json_cc = cc

    params["cc"] = json_cc

    json_codeclass: str | Unset = UNSET
    if not isinstance(codeclass, Unset):
        json_codeclass = codeclass

    params["codeclass"] = json_codeclass

    json_code: list[str] | Unset = UNSET
    if not isinstance(code, Unset):
        json_code = code

    params["code"] = json_code

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/get",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> DataResponse | None:
    if response.status_code == 200:
        response_200 = DataResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[DataResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    lang: GetTradeStatisticsLang,
    sv: list[GetTradeStatisticsSvItem],
    freq: GetTradeStatisticsFreq,
    period: str,
    ttype: GetTradeStatisticsTtype,
    tm: GetTradeStatisticsTm | Unset = UNSET,
    coclass: GetTradeStatisticsCoclass | Unset = UNSET,
    co: list[str] | Unset = UNSET,
    ccclass: GetTradeStatisticsCcclass | Unset = UNSET,
    cc: list[str] | Unset = UNSET,
    codeclass: GetTradeStatisticsCodeclass | Unset = UNSET,
    code: list[str] | Unset = UNSET,
) -> Response[DataResponse]:
    """Get trade statistics

     The publisher documents a GET data request and a JSON response. Parameters and values are case-
    insensitive. The `period` range is inclusive; annual values use YYYY and monthly values use YYYYMM.
    The response includes textual descriptions in the selected language. Nil/default or unspecified
    values are documented for several optional selectors. Usage limits may be adjusted without prior
    notice. See the official documentation for Annex 1 origin and consignment codes and Annex 2
    commodity classification references.

    Args:
        lang (GetTradeStatisticsLang):
        sv (list[GetTradeStatisticsSvItem]):
        freq (GetTradeStatisticsFreq):
        period (str):
        ttype (GetTradeStatisticsTtype):
        tm (GetTradeStatisticsTm | Unset):
        coclass (GetTradeStatisticsCoclass | Unset):
        co (list[str] | Unset):
        ccclass (GetTradeStatisticsCcclass | Unset):
        cc (list[str] | Unset):
        codeclass (GetTradeStatisticsCodeclass | Unset):
        code (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DataResponse]
    """

    kwargs = _get_kwargs(
        lang=lang,
        sv=sv,
        freq=freq,
        period=period,
        ttype=ttype,
        tm=tm,
        coclass=coclass,
        co=co,
        ccclass=ccclass,
        cc=cc,
        codeclass=codeclass,
        code=code,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    lang: GetTradeStatisticsLang,
    sv: list[GetTradeStatisticsSvItem],
    freq: GetTradeStatisticsFreq,
    period: str,
    ttype: GetTradeStatisticsTtype,
    tm: GetTradeStatisticsTm | Unset = UNSET,
    coclass: GetTradeStatisticsCoclass | Unset = UNSET,
    co: list[str] | Unset = UNSET,
    ccclass: GetTradeStatisticsCcclass | Unset = UNSET,
    cc: list[str] | Unset = UNSET,
    codeclass: GetTradeStatisticsCodeclass | Unset = UNSET,
    code: list[str] | Unset = UNSET,
) -> DataResponse | None:
    """Get trade statistics

     The publisher documents a GET data request and a JSON response. Parameters and values are case-
    insensitive. The `period` range is inclusive; annual values use YYYY and monthly values use YYYYMM.
    The response includes textual descriptions in the selected language. Nil/default or unspecified
    values are documented for several optional selectors. Usage limits may be adjusted without prior
    notice. See the official documentation for Annex 1 origin and consignment codes and Annex 2
    commodity classification references.

    Args:
        lang (GetTradeStatisticsLang):
        sv (list[GetTradeStatisticsSvItem]):
        freq (GetTradeStatisticsFreq):
        period (str):
        ttype (GetTradeStatisticsTtype):
        tm (GetTradeStatisticsTm | Unset):
        coclass (GetTradeStatisticsCoclass | Unset):
        co (list[str] | Unset):
        ccclass (GetTradeStatisticsCcclass | Unset):
        cc (list[str] | Unset):
        codeclass (GetTradeStatisticsCodeclass | Unset):
        code (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DataResponse
    """

    return sync_detailed(
        client=client,
        lang=lang,
        sv=sv,
        freq=freq,
        period=period,
        ttype=ttype,
        tm=tm,
        coclass=coclass,
        co=co,
        ccclass=ccclass,
        cc=cc,
        codeclass=codeclass,
        code=code,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    lang: GetTradeStatisticsLang,
    sv: list[GetTradeStatisticsSvItem],
    freq: GetTradeStatisticsFreq,
    period: str,
    ttype: GetTradeStatisticsTtype,
    tm: GetTradeStatisticsTm | Unset = UNSET,
    coclass: GetTradeStatisticsCoclass | Unset = UNSET,
    co: list[str] | Unset = UNSET,
    ccclass: GetTradeStatisticsCcclass | Unset = UNSET,
    cc: list[str] | Unset = UNSET,
    codeclass: GetTradeStatisticsCodeclass | Unset = UNSET,
    code: list[str] | Unset = UNSET,
) -> Response[DataResponse]:
    """Get trade statistics

     The publisher documents a GET data request and a JSON response. Parameters and values are case-
    insensitive. The `period` range is inclusive; annual values use YYYY and monthly values use YYYYMM.
    The response includes textual descriptions in the selected language. Nil/default or unspecified
    values are documented for several optional selectors. Usage limits may be adjusted without prior
    notice. See the official documentation for Annex 1 origin and consignment codes and Annex 2
    commodity classification references.

    Args:
        lang (GetTradeStatisticsLang):
        sv (list[GetTradeStatisticsSvItem]):
        freq (GetTradeStatisticsFreq):
        period (str):
        ttype (GetTradeStatisticsTtype):
        tm (GetTradeStatisticsTm | Unset):
        coclass (GetTradeStatisticsCoclass | Unset):
        co (list[str] | Unset):
        ccclass (GetTradeStatisticsCcclass | Unset):
        cc (list[str] | Unset):
        codeclass (GetTradeStatisticsCodeclass | Unset):
        code (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DataResponse]
    """

    kwargs = _get_kwargs(
        lang=lang,
        sv=sv,
        freq=freq,
        period=period,
        ttype=ttype,
        tm=tm,
        coclass=coclass,
        co=co,
        ccclass=ccclass,
        cc=cc,
        codeclass=codeclass,
        code=code,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    lang: GetTradeStatisticsLang,
    sv: list[GetTradeStatisticsSvItem],
    freq: GetTradeStatisticsFreq,
    period: str,
    ttype: GetTradeStatisticsTtype,
    tm: GetTradeStatisticsTm | Unset = UNSET,
    coclass: GetTradeStatisticsCoclass | Unset = UNSET,
    co: list[str] | Unset = UNSET,
    ccclass: GetTradeStatisticsCcclass | Unset = UNSET,
    cc: list[str] | Unset = UNSET,
    codeclass: GetTradeStatisticsCodeclass | Unset = UNSET,
    code: list[str] | Unset = UNSET,
) -> DataResponse | None:
    """Get trade statistics

     The publisher documents a GET data request and a JSON response. Parameters and values are case-
    insensitive. The `period` range is inclusive; annual values use YYYY and monthly values use YYYYMM.
    The response includes textual descriptions in the selected language. Nil/default or unspecified
    values are documented for several optional selectors. Usage limits may be adjusted without prior
    notice. See the official documentation for Annex 1 origin and consignment codes and Annex 2
    commodity classification references.

    Args:
        lang (GetTradeStatisticsLang):
        sv (list[GetTradeStatisticsSvItem]):
        freq (GetTradeStatisticsFreq):
        period (str):
        ttype (GetTradeStatisticsTtype):
        tm (GetTradeStatisticsTm | Unset):
        coclass (GetTradeStatisticsCoclass | Unset):
        co (list[str] | Unset):
        ccclass (GetTradeStatisticsCcclass | Unset):
        cc (list[str] | Unset):
        codeclass (GetTradeStatisticsCodeclass | Unset):
        code (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DataResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            lang=lang,
            sv=sv,
            freq=freq,
            period=period,
            ttype=ttype,
            tm=tm,
            coclass=coclass,
            co=co,
            ccclass=ccclass,
            cc=cc,
            codeclass=codeclass,
            code=code,
        )
    ).parsed
