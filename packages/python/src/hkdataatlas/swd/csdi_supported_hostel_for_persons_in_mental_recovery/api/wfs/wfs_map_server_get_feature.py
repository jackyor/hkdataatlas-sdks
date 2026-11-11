from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.wfs_map_server_get_feature_output_format import (
    WfsMapServerGetFeatureOutputFormat,
)
from ...models.wfs_map_server_get_feature_request import (
    WfsMapServerGetFeatureRequest,
)
from ...models.wfs_map_server_get_feature_service import (
    WfsMapServerGetFeatureService,
)
from ...models.wfs_map_server_get_feature_version import (
    WfsMapServerGetFeatureVersion,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    service: WfsMapServerGetFeatureService,
    version: WfsMapServerGetFeatureVersion,
    request: WfsMapServerGetFeatureRequest,
    type_names: str,
    output_format: WfsMapServerGetFeatureOutputFormat | Unset = UNSET,
    count: int | Unset = UNSET,
    srs_name: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_service: str = service
    params["service"] = json_service

    json_version: str = version
    params["version"] = json_version

    json_request: str = request
    params["request"] = json_request

    params["typeNames"] = type_names

    json_output_format: str | Unset = UNSET
    if not isinstance(output_format, Unset):
        json_output_format = output_format

    params["outputFormat"] = json_output_format

    params["count"] = count

    params["srsName"] = srs_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/server/services/common/swd_rcd_1633509894764_67814/MapServer/WFSServer",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> str | None:
    if response.status_code == 200:
        response_200 = response.text
        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    service: WfsMapServerGetFeatureService,
    version: WfsMapServerGetFeatureVersion,
    request: WfsMapServerGetFeatureRequest,
    type_names: str,
    output_format: WfsMapServerGetFeatureOutputFormat | Unset = UNSET,
    count: int | Unset = UNSET,
    srs_name: str | Unset = UNSET,
) -> Response[str]:
    """Retrieve published features

     One read-only GET operation selects published feature types by name. Attribute types derive from
    retained DescribeFeatureType XSD when available; missing XSD, geometry, unread response data and
    unknown fields remain explicit limitations.

    Args:
        service (WfsMapServerGetFeatureService):
        version (WfsMapServerGetFeatureVersion):
        request (WfsMapServerGetFeatureRequest):
        type_names (str):
        output_format (WfsMapServerGetFeatureOutputFormat | Unset):
        count (int | Unset):
        srs_name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[str]
    """

    kwargs = _get_kwargs(
        service=service,
        version=version,
        request=request,
        type_names=type_names,
        output_format=output_format,
        count=count,
        srs_name=srs_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    service: WfsMapServerGetFeatureService,
    version: WfsMapServerGetFeatureVersion,
    request: WfsMapServerGetFeatureRequest,
    type_names: str,
    output_format: WfsMapServerGetFeatureOutputFormat | Unset = UNSET,
    count: int | Unset = UNSET,
    srs_name: str | Unset = UNSET,
) -> str | None:
    """Retrieve published features

     One read-only GET operation selects published feature types by name. Attribute types derive from
    retained DescribeFeatureType XSD when available; missing XSD, geometry, unread response data and
    unknown fields remain explicit limitations.

    Args:
        service (WfsMapServerGetFeatureService):
        version (WfsMapServerGetFeatureVersion):
        request (WfsMapServerGetFeatureRequest):
        type_names (str):
        output_format (WfsMapServerGetFeatureOutputFormat | Unset):
        count (int | Unset):
        srs_name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        str
    """

    return sync_detailed(
        client=client,
        service=service,
        version=version,
        request=request,
        type_names=type_names,
        output_format=output_format,
        count=count,
        srs_name=srs_name,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    service: WfsMapServerGetFeatureService,
    version: WfsMapServerGetFeatureVersion,
    request: WfsMapServerGetFeatureRequest,
    type_names: str,
    output_format: WfsMapServerGetFeatureOutputFormat | Unset = UNSET,
    count: int | Unset = UNSET,
    srs_name: str | Unset = UNSET,
) -> Response[str]:
    """Retrieve published features

     One read-only GET operation selects published feature types by name. Attribute types derive from
    retained DescribeFeatureType XSD when available; missing XSD, geometry, unread response data and
    unknown fields remain explicit limitations.

    Args:
        service (WfsMapServerGetFeatureService):
        version (WfsMapServerGetFeatureVersion):
        request (WfsMapServerGetFeatureRequest):
        type_names (str):
        output_format (WfsMapServerGetFeatureOutputFormat | Unset):
        count (int | Unset):
        srs_name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[str]
    """

    kwargs = _get_kwargs(
        service=service,
        version=version,
        request=request,
        type_names=type_names,
        output_format=output_format,
        count=count,
        srs_name=srs_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    service: WfsMapServerGetFeatureService,
    version: WfsMapServerGetFeatureVersion,
    request: WfsMapServerGetFeatureRequest,
    type_names: str,
    output_format: WfsMapServerGetFeatureOutputFormat | Unset = UNSET,
    count: int | Unset = UNSET,
    srs_name: str | Unset = UNSET,
) -> str | None:
    """Retrieve published features

     One read-only GET operation selects published feature types by name. Attribute types derive from
    retained DescribeFeatureType XSD when available; missing XSD, geometry, unread response data and
    unknown fields remain explicit limitations.

    Args:
        service (WfsMapServerGetFeatureService):
        version (WfsMapServerGetFeatureVersion):
        request (WfsMapServerGetFeatureRequest):
        type_names (str):
        output_format (WfsMapServerGetFeatureOutputFormat | Unset):
        count (int | Unset):
        srs_name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        str
    """

    return (
        await asyncio_detailed(
            client=client,
            service=service,
            version=version,
            request=request,
            type_names=type_names,
            output_format=output_format,
            count=count,
            srs_name=srs_name,
        )
    ).parsed
