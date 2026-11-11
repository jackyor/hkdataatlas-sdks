from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_technology_companies_count_response_200_type_1 import (
    GetTechnologyCompaniesCountResponse200Type1,
)
from ...models.technology_companies_response import TechnologyCompaniesResponse
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/corporate/figures/technologycompanies/v1/",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> GetTechnologyCompaniesCountResponse200Type1 | TechnologyCompaniesResponse | None:
    if response.status_code == 200:
        media_type = (
            response.headers.get("content-type", "").split(";", 1)[0].strip().lower()
        )
        if media_type != "application/json" and not media_type.endswith("+json"):
            return None

        def _parse_response_200(
            data: object,
        ) -> GetTechnologyCompaniesCountResponse200Type1 | TechnologyCompaniesResponse:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = TechnologyCompaniesResponse.from_dict(data)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = GetTechnologyCompaniesCountResponse200Type1.from_dict(
                data
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
    GetTechnologyCompaniesCountResponse200Type1 | TechnologyCompaniesResponse
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
    GetTechnologyCompaniesCountResponse200Type1 | TechnologyCompaniesResponse
]:
    """Get number of technology companies

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetTechnologyCompaniesCountResponse200Type1 | TechnologyCompaniesResponse]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> GetTechnologyCompaniesCountResponse200Type1 | TechnologyCompaniesResponse | None:
    """Get number of technology companies

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetTechnologyCompaniesCountResponse200Type1 | TechnologyCompaniesResponse
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    GetTechnologyCompaniesCountResponse200Type1 | TechnologyCompaniesResponse
]:
    """Get number of technology companies

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetTechnologyCompaniesCountResponse200Type1 | TechnologyCompaniesResponse]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> GetTechnologyCompaniesCountResponse200Type1 | TechnologyCompaniesResponse | None:
    """Get number of technology companies

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetTechnologyCompaniesCountResponse200Type1 | TechnologyCompaniesResponse
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
