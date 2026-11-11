from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_housing_archive_or_commercial_leasing_data_id import (
    GetHousingArchiveOrCommercialLeasingDataId,
)
from ...models.get_housing_archive_or_commercial_leasing_data_type import (
    GetHousingArchiveOrCommercialLeasingDataType,
)
from ...models.housing_estate_record import HousingEstateRecord
from ...models.shop_record import ShopRecord
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    type_: GetHousingArchiveOrCommercialLeasingDataType,
    id: GetHousingArchiveOrCommercialLeasingDataId | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_type_: str = type_
    params["type"] = json_type_

    json_id: str | Unset = UNSET
    if not isinstance(id, Unset):
        json_id = id

    params["id"] = json_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/json",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> list[HousingEstateRecord | ShopRecord] | None:
    if response.status_code == 200:
        media_type = (
            response.headers.get("content-type", "").split(";", 1)[0].strip().lower()
        )
        if media_type != "application/json" and not media_type.endswith("+json"):
            return None
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:

            def _parse_response_200_item(
                data: object,
            ) -> HousingEstateRecord | ShopRecord:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_200_item_type_0 = HousingEstateRecord.from_dict(data)

                    return response_200_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_item_type_1 = ShopRecord.from_dict(data)

                return response_200_item_type_1

            response_200_item = _parse_response_200_item(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[list[HousingEstateRecord | ShopRecord]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    type_: GetHousingArchiveOrCommercialLeasingDataType,
    id: GetHousingArchiveOrCommercialLeasingDataId | Unset = UNSET,
) -> Response[list[HousingEstateRecord | ShopRecord]]:
    """Retrieve a documented housing archive or shop data resource

     This operation represents the exact publisher resource URLs documented in the data dictionary.
    Select the resource using the query parameters; the documented housing resource identifiers are
    individual published values, not evidence of a general identifier template. The dictionary does not
    specify a response envelope. The field schema describes documented record fields and does not
    establish that all fields are present in every response.

    Args:
        type_ (GetHousingArchiveOrCommercialLeasingDataType):
        id (GetHousingArchiveOrCommercialLeasingDataId | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[HousingEstateRecord | ShopRecord]]
    """

    kwargs = _get_kwargs(
        type_=type_,
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    type_: GetHousingArchiveOrCommercialLeasingDataType,
    id: GetHousingArchiveOrCommercialLeasingDataId | Unset = UNSET,
) -> list[HousingEstateRecord | ShopRecord] | None:
    """Retrieve a documented housing archive or shop data resource

     This operation represents the exact publisher resource URLs documented in the data dictionary.
    Select the resource using the query parameters; the documented housing resource identifiers are
    individual published values, not evidence of a general identifier template. The dictionary does not
    specify a response envelope. The field schema describes documented record fields and does not
    establish that all fields are present in every response.

    Args:
        type_ (GetHousingArchiveOrCommercialLeasingDataType):
        id (GetHousingArchiveOrCommercialLeasingDataId | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[HousingEstateRecord | ShopRecord]
    """

    return sync_detailed(
        client=client,
        type_=type_,
        id=id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    type_: GetHousingArchiveOrCommercialLeasingDataType,
    id: GetHousingArchiveOrCommercialLeasingDataId | Unset = UNSET,
) -> Response[list[HousingEstateRecord | ShopRecord]]:
    """Retrieve a documented housing archive or shop data resource

     This operation represents the exact publisher resource URLs documented in the data dictionary.
    Select the resource using the query parameters; the documented housing resource identifiers are
    individual published values, not evidence of a general identifier template. The dictionary does not
    specify a response envelope. The field schema describes documented record fields and does not
    establish that all fields are present in every response.

    Args:
        type_ (GetHousingArchiveOrCommercialLeasingDataType):
        id (GetHousingArchiveOrCommercialLeasingDataId | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[HousingEstateRecord | ShopRecord]]
    """

    kwargs = _get_kwargs(
        type_=type_,
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    type_: GetHousingArchiveOrCommercialLeasingDataType,
    id: GetHousingArchiveOrCommercialLeasingDataId | Unset = UNSET,
) -> list[HousingEstateRecord | ShopRecord] | None:
    """Retrieve a documented housing archive or shop data resource

     This operation represents the exact publisher resource URLs documented in the data dictionary.
    Select the resource using the query parameters; the documented housing resource identifiers are
    individual published values, not evidence of a general identifier template. The dictionary does not
    specify a response envelope. The field schema describes documented record fields and does not
    establish that all fields are present in every response.

    Args:
        type_ (GetHousingArchiveOrCommercialLeasingDataType):
        id (GetHousingArchiveOrCommercialLeasingDataId | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[HousingEstateRecord | ShopRecord]
    """

    return (
        await asyncio_detailed(
            client=client,
            type_=type_,
            id=id,
        )
    ).parsed
