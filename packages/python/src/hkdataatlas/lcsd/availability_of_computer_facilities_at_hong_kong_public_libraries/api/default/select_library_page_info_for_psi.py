from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.library_availability import LibraryAvailability
from ...models.select_library_page_info_for_psi_language import (
    SelectLibraryPageInfoForPsiLanguage,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    req_page: int | Unset = UNSET,
    size_per_page: int | Unset = UNSET,
    language: SelectLibraryPageInfoForPsiLanguage | Unset = "zh-HK",
    library_code: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["reqPage"] = req_page

    params["sizePerPage"] = size_per_page

    json_language: str | Unset = UNSET
    if not isinstance(language, Unset):
        json_language = language

    params["language"] = json_language

    params["libraryCode"] = library_code

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/library/selectLibraryPageInfoForPSI",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | list[LibraryAvailability] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = LibraryAvailability.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | list[LibraryAvailability]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    req_page: int | Unset = UNSET,
    size_per_page: int | Unset = UNSET,
    language: SelectLibraryPageInfoForPsiLanguage | Unset = "zh-HK",
    library_code: str | Unset = UNSET,
) -> Response[Any | list[LibraryAvailability]]:
    """Retrieve library computer-facility availability

     Returns information about available workstations at public libraries. All query parameters are case-
    sensitive. The sample request uses language=en-US, reqPage=1, sizePerPage=9999, and
    libraryCode=LCKPL.

    Args:
        req_page (int | Unset):
        size_per_page (int | Unset):
        language (SelectLibraryPageInfoForPsiLanguage | Unset):  Default: 'zh-HK'.
        library_code (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[LibraryAvailability]]
    """

    kwargs = _get_kwargs(
        req_page=req_page,
        size_per_page=size_per_page,
        language=language,
        library_code=library_code,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    req_page: int | Unset = UNSET,
    size_per_page: int | Unset = UNSET,
    language: SelectLibraryPageInfoForPsiLanguage | Unset = "zh-HK",
    library_code: str | Unset = UNSET,
) -> Any | list[LibraryAvailability] | None:
    """Retrieve library computer-facility availability

     Returns information about available workstations at public libraries. All query parameters are case-
    sensitive. The sample request uses language=en-US, reqPage=1, sizePerPage=9999, and
    libraryCode=LCKPL.

    Args:
        req_page (int | Unset):
        size_per_page (int | Unset):
        language (SelectLibraryPageInfoForPsiLanguage | Unset):  Default: 'zh-HK'.
        library_code (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[LibraryAvailability]
    """

    return sync_detailed(
        client=client,
        req_page=req_page,
        size_per_page=size_per_page,
        language=language,
        library_code=library_code,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    req_page: int | Unset = UNSET,
    size_per_page: int | Unset = UNSET,
    language: SelectLibraryPageInfoForPsiLanguage | Unset = "zh-HK",
    library_code: str | Unset = UNSET,
) -> Response[Any | list[LibraryAvailability]]:
    """Retrieve library computer-facility availability

     Returns information about available workstations at public libraries. All query parameters are case-
    sensitive. The sample request uses language=en-US, reqPage=1, sizePerPage=9999, and
    libraryCode=LCKPL.

    Args:
        req_page (int | Unset):
        size_per_page (int | Unset):
        language (SelectLibraryPageInfoForPsiLanguage | Unset):  Default: 'zh-HK'.
        library_code (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[LibraryAvailability]]
    """

    kwargs = _get_kwargs(
        req_page=req_page,
        size_per_page=size_per_page,
        language=language,
        library_code=library_code,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    req_page: int | Unset = UNSET,
    size_per_page: int | Unset = UNSET,
    language: SelectLibraryPageInfoForPsiLanguage | Unset = "zh-HK",
    library_code: str | Unset = UNSET,
) -> Any | list[LibraryAvailability] | None:
    """Retrieve library computer-facility availability

     Returns information about available workstations at public libraries. All query parameters are case-
    sensitive. The sample request uses language=en-US, reqPage=1, sizePerPage=9999, and
    libraryCode=LCKPL.

    Args:
        req_page (int | Unset):
        size_per_page (int | Unset):
        language (SelectLibraryPageInfoForPsiLanguage | Unset):  Default: 'zh-HK'.
        library_code (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[LibraryAvailability]
    """

    return (
        await asyncio_detailed(
            client=client,
            req_page=req_page,
            size_per_page=size_per_page,
            language=language,
            library_code=library_code,
        )
    ).parsed
