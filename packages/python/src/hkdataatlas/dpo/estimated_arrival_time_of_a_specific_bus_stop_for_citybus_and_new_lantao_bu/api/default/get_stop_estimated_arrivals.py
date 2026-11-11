from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.get_stop_estimated_arrivals_company_id import (
    GetStopEstimatedArrivalsCompanyId,
)
from ...models.get_stop_estimated_arrivals_lang import (
    GetStopEstimatedArrivalsLang,
)
from ...models.stop_eta_response import StopEtaResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    company_id: GetStopEstimatedArrivalsCompanyId,
    stop_id: str,
    *,
    lang: GetStopEstimatedArrivalsLang | Unset = "en",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_lang: str | Unset = UNSET
    if not isinstance(lang, Unset):
        json_lang = lang

    params["lang"] = json_lang

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/transport/batch/stop-eta/{company_id}/{stop_id}".format(
            company_id=quote(str(company_id), safe=""),
            stop_id=quote(str(stop_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | Error | StopEtaResponse | None:
    if response.status_code == 200:
        response_200 = StopEtaResponse.from_dict(response.json())

        return response_200

    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = cast(Any, None)
        return response_429

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if response.status_code == 502:
        response_502 = cast(Any, None)
        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | Error | StopEtaResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    company_id: GetStopEstimatedArrivalsCompanyId,
    stop_id: str,
    *,
    client: AuthenticatedClient | Client,
    lang: GetStopEstimatedArrivalsLang | Unset = "en",
) -> Response[Any | Error | StopEtaResponse]:
    """Get estimated arrivals for a bus stop

     Returns ETA data for the specified stop and company. CTB stop IDs are documented in Citybus stop and
    route-stop datasets; NLB stop IDs are documented in its Stops of a route dataset. For the associated
    field definitions, see the data dictionary.

    Args:
        company_id (GetStopEstimatedArrivalsCompanyId):
        stop_id (str):
        lang (GetStopEstimatedArrivalsLang | Unset):  Default: 'en'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error | StopEtaResponse]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        stop_id=stop_id,
        lang=lang,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    company_id: GetStopEstimatedArrivalsCompanyId,
    stop_id: str,
    *,
    client: AuthenticatedClient | Client,
    lang: GetStopEstimatedArrivalsLang | Unset = "en",
) -> Any | Error | StopEtaResponse | None:
    """Get estimated arrivals for a bus stop

     Returns ETA data for the specified stop and company. CTB stop IDs are documented in Citybus stop and
    route-stop datasets; NLB stop IDs are documented in its Stops of a route dataset. For the associated
    field definitions, see the data dictionary.

    Args:
        company_id (GetStopEstimatedArrivalsCompanyId):
        stop_id (str):
        lang (GetStopEstimatedArrivalsLang | Unset):  Default: 'en'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error | StopEtaResponse
    """

    return sync_detailed(
        company_id=company_id,
        stop_id=stop_id,
        client=client,
        lang=lang,
    ).parsed


async def asyncio_detailed(
    company_id: GetStopEstimatedArrivalsCompanyId,
    stop_id: str,
    *,
    client: AuthenticatedClient | Client,
    lang: GetStopEstimatedArrivalsLang | Unset = "en",
) -> Response[Any | Error | StopEtaResponse]:
    """Get estimated arrivals for a bus stop

     Returns ETA data for the specified stop and company. CTB stop IDs are documented in Citybus stop and
    route-stop datasets; NLB stop IDs are documented in its Stops of a route dataset. For the associated
    field definitions, see the data dictionary.

    Args:
        company_id (GetStopEstimatedArrivalsCompanyId):
        stop_id (str):
        lang (GetStopEstimatedArrivalsLang | Unset):  Default: 'en'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error | StopEtaResponse]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        stop_id=stop_id,
        lang=lang,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: GetStopEstimatedArrivalsCompanyId,
    stop_id: str,
    *,
    client: AuthenticatedClient | Client,
    lang: GetStopEstimatedArrivalsLang | Unset = "en",
) -> Any | Error | StopEtaResponse | None:
    """Get estimated arrivals for a bus stop

     Returns ETA data for the specified stop and company. CTB stop IDs are documented in Citybus stop and
    route-stop datasets; NLB stop IDs are documented in its Stops of a route dataset. For the associated
    field definitions, see the data dictionary.

    Args:
        company_id (GetStopEstimatedArrivalsCompanyId):
        stop_id (str):
        lang (GetStopEstimatedArrivalsLang | Unset):  Default: 'en'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error | StopEtaResponse
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            stop_id=stop_id,
            client=client,
            lang=lang,
        )
    ).parsed
