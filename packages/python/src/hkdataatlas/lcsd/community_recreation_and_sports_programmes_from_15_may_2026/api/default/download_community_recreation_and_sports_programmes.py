from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.programme_resource import ProgrammeResource
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/cms/api/v1/publ/contents/open-data/activity-prog/file",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ProgrammeResource | None:
    if response.status_code == 200:
        media_type = (
            response.headers.get("content-type", "").split(";", 1)[0].strip().lower()
        )
        if media_type != "application/json" and not media_type.endswith("+json"):
            return None
        response_200 = ProgrammeResource.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ProgrammeResource]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[ProgrammeResource]:
    """Retrieve the published programme resource

     The catalogue publishes this literal URL for a JSON resource and identifies it as an API resource.
    Its HTTP method, response envelope, and authentication requirements are not specified by the
    publisher documentation. This operation describes retrieval of the exact published resource URL
    only; no URL template or query parameters are documented.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProgrammeResource]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> ProgrammeResource | None:
    """Retrieve the published programme resource

     The catalogue publishes this literal URL for a JSON resource and identifies it as an API resource.
    Its HTTP method, response envelope, and authentication requirements are not specified by the
    publisher documentation. This operation describes retrieval of the exact published resource URL
    only; no URL template or query parameters are documented.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProgrammeResource
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[ProgrammeResource]:
    """Retrieve the published programme resource

     The catalogue publishes this literal URL for a JSON resource and identifies it as an API resource.
    Its HTTP method, response envelope, and authentication requirements are not specified by the
    publisher documentation. This operation describes retrieval of the exact published resource URL
    only; no URL template or query parameters are documented.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProgrammeResource]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> ProgrammeResource | None:
    """Retrieve the published programme resource

     The catalogue publishes this literal URL for a JSON resource and identifies it as an API resource.
    Its HTTP method, response envelope, and authentication requirements are not specified by the
    publisher documentation. This operation describes retrieval of the exact published resource URL
    only; no URL template or query parameters are documented.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProgrammeResource
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
