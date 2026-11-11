from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_past_flight_information_lang import (
    GetPastFlightInformationLang,
)
from ...models.observed_day_group import ObservedDayGroup
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    date: str | Unset = UNSET,
    arrival: bool | Unset = UNSET,
    cargo: bool | Unset = UNSET,
    lang: GetPastFlightInformationLang | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["date"] = date

    params["arrival"] = arrival

    params["cargo"] = cargo

    json_lang: str | Unset = UNSET
    if not isinstance(lang, Unset):
        json_lang = lang

    params["lang"] = json_lang

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/flights/past",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> list[ObservedDayGroup] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_observed_flight_response_item_data in _response_200:
            componentsschemas_observed_flight_response_item = (
                ObservedDayGroup.from_dict(
                    componentsschemas_observed_flight_response_item_data
                )
            )

            response_200.append(componentsschemas_observed_flight_response_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[list[ObservedDayGroup]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    date: str | Unset = UNSET,
    arrival: bool | Unset = UNSET,
    cargo: bool | Unset = UNSET,
    lang: GetPastFlightInformationLang | Unset = UNSET,
) -> Response[list[ObservedDayGroup]]:
    """Get past flight information

     Returns historical flight information. The source states that data is up-to-date to the previous
    calendar day. Arrival and cargo parameters select arrival/departure and cargo/passenger categories.
    The source documents semantic field labels but does not establish their exact JSON property names or
    types. An accompanying bounded observed live-response excerpt is represented as an example and does
    not guarantee a complete response contract.

    Args:
        date (str | Unset):
        arrival (bool | Unset):
        cargo (bool | Unset):
        lang (GetPastFlightInformationLang | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[ObservedDayGroup]]
    """

    kwargs = _get_kwargs(
        date=date,
        arrival=arrival,
        cargo=cargo,
        lang=lang,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    date: str | Unset = UNSET,
    arrival: bool | Unset = UNSET,
    cargo: bool | Unset = UNSET,
    lang: GetPastFlightInformationLang | Unset = UNSET,
) -> list[ObservedDayGroup] | None:
    """Get past flight information

     Returns historical flight information. The source states that data is up-to-date to the previous
    calendar day. Arrival and cargo parameters select arrival/departure and cargo/passenger categories.
    The source documents semantic field labels but does not establish their exact JSON property names or
    types. An accompanying bounded observed live-response excerpt is represented as an example and does
    not guarantee a complete response contract.

    Args:
        date (str | Unset):
        arrival (bool | Unset):
        cargo (bool | Unset):
        lang (GetPastFlightInformationLang | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[ObservedDayGroup]
    """

    return sync_detailed(
        client=client,
        date=date,
        arrival=arrival,
        cargo=cargo,
        lang=lang,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    date: str | Unset = UNSET,
    arrival: bool | Unset = UNSET,
    cargo: bool | Unset = UNSET,
    lang: GetPastFlightInformationLang | Unset = UNSET,
) -> Response[list[ObservedDayGroup]]:
    """Get past flight information

     Returns historical flight information. The source states that data is up-to-date to the previous
    calendar day. Arrival and cargo parameters select arrival/departure and cargo/passenger categories.
    The source documents semantic field labels but does not establish their exact JSON property names or
    types. An accompanying bounded observed live-response excerpt is represented as an example and does
    not guarantee a complete response contract.

    Args:
        date (str | Unset):
        arrival (bool | Unset):
        cargo (bool | Unset):
        lang (GetPastFlightInformationLang | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[ObservedDayGroup]]
    """

    kwargs = _get_kwargs(
        date=date,
        arrival=arrival,
        cargo=cargo,
        lang=lang,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    date: str | Unset = UNSET,
    arrival: bool | Unset = UNSET,
    cargo: bool | Unset = UNSET,
    lang: GetPastFlightInformationLang | Unset = UNSET,
) -> list[ObservedDayGroup] | None:
    """Get past flight information

     Returns historical flight information. The source states that data is up-to-date to the previous
    calendar day. Arrival and cargo parameters select arrival/departure and cargo/passenger categories.
    The source documents semantic field labels but does not establish their exact JSON property names or
    types. An accompanying bounded observed live-response excerpt is represented as an example and does
    not guarantee a complete response contract.

    Args:
        date (str | Unset):
        arrival (bool | Unset):
        cargo (bool | Unset):
        lang (GetPastFlightInformationLang | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[ObservedDayGroup]
    """

    return (
        await asyncio_detailed(
            client=client,
            date=date,
            arrival=arrival,
            cargo=cargo,
            lang=lang,
        )
    ).parsed
