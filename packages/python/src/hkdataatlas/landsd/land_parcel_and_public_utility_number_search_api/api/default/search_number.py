from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    version: str,
    data_type: str,
    *,
    text: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["text"] = text

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/gs/api/{version}/lus/{data_type}/SearchNumber".format(
            version=quote(str(version), safe=""),
            data_type=quote(str(data_type), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | None:
    if response.status_code == 200:
        return None

    if response.status_code == 400:
        return None

    if response.status_code == 500:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    version: str,
    data_type: str,
    *,
    client: AuthenticatedClient | Client,
    text: str | Unset = UNSET,
) -> Response[Any]:
    """Search by land parcel or public utility number

     Returns search data in JSON format. The publisher advises against invoking the API with a large
    number of requests within a short period. The documented URL example uses version v1.0.0 and
    DataType value gla; the query-builder's exact values are lowercase, while the prose lists uppercase
    labels. The API version may change, and old versions may be removed without notice.

    Args:
        version (str):
        data_type (str):
        text (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        version=version,
        data_type=data_type,
        text=text,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    version: str,
    data_type: str,
    *,
    client: AuthenticatedClient | Client,
    text: str | Unset = UNSET,
) -> Response[Any]:
    """Search by land parcel or public utility number

     Returns search data in JSON format. The publisher advises against invoking the API with a large
    number of requests within a short period. The documented URL example uses version v1.0.0 and
    DataType value gla; the query-builder's exact values are lowercase, while the prose lists uppercase
    labels. The API version may change, and old versions may be removed without notice.

    Args:
        version (str):
        data_type (str):
        text (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        version=version,
        data_type=data_type,
        text=text,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
