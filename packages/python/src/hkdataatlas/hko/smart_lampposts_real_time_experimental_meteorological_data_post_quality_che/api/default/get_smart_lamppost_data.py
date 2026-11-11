from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.message_response import MessageResponse
from ...models.meteorological_data_response import MeteorologicalDataResponse
from ...models.no_record_found_response import NoRecordFoundResponse
from ...types import UNSET, Response


def _get_kwargs(
    *,
    pi: str,
    di: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["pi"] = pi

    params["di"] = di

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/smart-lamppost.php",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> MessageResponse | MeteorologicalDataResponse | NoRecordFoundResponse | None:
    if response.status_code == 200:

        def _parse_response_200(
            data: object,
        ) -> MeteorologicalDataResponse | NoRecordFoundResponse:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = MeteorologicalDataResponse.from_dict(data)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = NoRecordFoundResponse.from_dict(data)

            return response_200_type_1

        response_200 = _parse_response_200(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = MessageResponse.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = MessageResponse.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = MessageResponse.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[MessageResponse | MeteorologicalDataResponse | NoRecordFoundResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    pi: str,
    di: str,
) -> Response[MessageResponse | MeteorologicalDataResponse | NoRecordFoundResponse]:
    """Get data by lamppost ID and device ID

     Returns the latest processed data (in 10-minute intervals) for the specified lamppost and device.
    For lists of valid lamppost and device IDs, consult the HKO static datasets:
    https://www.hko.gov.hk/common/hko_data/R3/files/smart_lamppost_met_device_location.json,
    https://www.hko.gov.hk/common/hko_data/R3/files/smart_lamppost_met_device_type.json, and
    https://www.hko.gov.hk/common/hko_data/R3/files/smart_lamppost_met_device_element.json. The API
    documentation states that authentication is not required.

    Args:
        pi (str):
        di (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageResponse | MeteorologicalDataResponse | NoRecordFoundResponse]
    """

    kwargs = _get_kwargs(
        pi=pi,
        di=di,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    pi: str,
    di: str,
) -> MessageResponse | MeteorologicalDataResponse | NoRecordFoundResponse | None:
    """Get data by lamppost ID and device ID

     Returns the latest processed data (in 10-minute intervals) for the specified lamppost and device.
    For lists of valid lamppost and device IDs, consult the HKO static datasets:
    https://www.hko.gov.hk/common/hko_data/R3/files/smart_lamppost_met_device_location.json,
    https://www.hko.gov.hk/common/hko_data/R3/files/smart_lamppost_met_device_type.json, and
    https://www.hko.gov.hk/common/hko_data/R3/files/smart_lamppost_met_device_element.json. The API
    documentation states that authentication is not required.

    Args:
        pi (str):
        di (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageResponse | MeteorologicalDataResponse | NoRecordFoundResponse
    """

    return sync_detailed(
        client=client,
        pi=pi,
        di=di,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    pi: str,
    di: str,
) -> Response[MessageResponse | MeteorologicalDataResponse | NoRecordFoundResponse]:
    """Get data by lamppost ID and device ID

     Returns the latest processed data (in 10-minute intervals) for the specified lamppost and device.
    For lists of valid lamppost and device IDs, consult the HKO static datasets:
    https://www.hko.gov.hk/common/hko_data/R3/files/smart_lamppost_met_device_location.json,
    https://www.hko.gov.hk/common/hko_data/R3/files/smart_lamppost_met_device_type.json, and
    https://www.hko.gov.hk/common/hko_data/R3/files/smart_lamppost_met_device_element.json. The API
    documentation states that authentication is not required.

    Args:
        pi (str):
        di (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageResponse | MeteorologicalDataResponse | NoRecordFoundResponse]
    """

    kwargs = _get_kwargs(
        pi=pi,
        di=di,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    pi: str,
    di: str,
) -> MessageResponse | MeteorologicalDataResponse | NoRecordFoundResponse | None:
    """Get data by lamppost ID and device ID

     Returns the latest processed data (in 10-minute intervals) for the specified lamppost and device.
    For lists of valid lamppost and device IDs, consult the HKO static datasets:
    https://www.hko.gov.hk/common/hko_data/R3/files/smart_lamppost_met_device_location.json,
    https://www.hko.gov.hk/common/hko_data/R3/files/smart_lamppost_met_device_type.json, and
    https://www.hko.gov.hk/common/hko_data/R3/files/smart_lamppost_met_device_element.json. The API
    documentation states that authentication is not required.

    Args:
        pi (str):
        di (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageResponse | MeteorologicalDataResponse | NoRecordFoundResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            pi=pi,
            di=di,
        )
    ).parsed
