from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.direct_investment_raised import DirectInvestmentRaised
from ...models.get_previous_fiscal_year_direct_investment_raised_response_200_type_1 import (
    GetPreviousFiscalYearDirectInvestmentRaisedResponse200Type1,
)
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> (
    DirectInvestmentRaised
    | GetPreviousFiscalYearDirectInvestmentRaisedResponse200Type1
    | None
):
    if response.status_code == 200:
        media_type = (
            response.headers.get("content-type", "").split(";", 1)[0].strip().lower()
        )
        if media_type != "application/json" and not media_type.endswith("+json"):
            return None

        def _parse_response_200(
            data: object,
        ) -> (
            DirectInvestmentRaised
            | GetPreviousFiscalYearDirectInvestmentRaisedResponse200Type1
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = DirectInvestmentRaised.from_dict(data)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = (
                GetPreviousFiscalYearDirectInvestmentRaisedResponse200Type1.from_dict(
                    data
                )
            )

            return response_200_type_1

        response_200 = _parse_response_200(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[
    DirectInvestmentRaised | GetPreviousFiscalYearDirectInvestmentRaisedResponse200Type1
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    DirectInvestmentRaised | GetPreviousFiscalYearDirectInvestmentRaisedResponse200Type1
]:
    """Get direct investment raised in the previous fiscal year

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DirectInvestmentRaised | GetPreviousFiscalYearDirectInvestmentRaisedResponse200Type1]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> (
    DirectInvestmentRaised
    | GetPreviousFiscalYearDirectInvestmentRaisedResponse200Type1
    | None
):
    """Get direct investment raised in the previous fiscal year

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DirectInvestmentRaised | GetPreviousFiscalYearDirectInvestmentRaisedResponse200Type1
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    DirectInvestmentRaised | GetPreviousFiscalYearDirectInvestmentRaisedResponse200Type1
]:
    """Get direct investment raised in the previous fiscal year

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DirectInvestmentRaised | GetPreviousFiscalYearDirectInvestmentRaisedResponse200Type1]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> (
    DirectInvestmentRaised
    | GetPreviousFiscalYearDirectInvestmentRaisedResponse200Type1
    | None
):
    """Get direct investment raised in the previous fiscal year

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DirectInvestmentRaised | GetPreviousFiscalYearDirectInvestmentRaisedResponse200Type1
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
