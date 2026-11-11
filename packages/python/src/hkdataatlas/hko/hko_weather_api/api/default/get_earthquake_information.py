from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.felt_earth_tremor_report import FeltEarthTremorReport
from ...models.get_earthquake_information_data_type import (
    GetEarthquakeInformationDataType,
)
from ...models.get_earthquake_information_lang import (
    GetEarthquakeInformationLang,
)
from ...models.quick_earthquake_message import QuickEarthquakeMessage
from ...types import UNSET, Response


def _get_kwargs(
    *,
    data_type: GetEarthquakeInformationDataType,
    lang: GetEarthquakeInformationLang = "en",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_data_type: str = data_type
    params["dataType"] = json_data_type

    json_lang: str = lang
    params["lang"] = json_lang

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/earthquake.php",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> FeltEarthTremorReport | QuickEarthquakeMessage | None:
    if response.status_code == 200:

        def _parse_response_200(
            data: object,
        ) -> FeltEarthTremorReport | QuickEarthquakeMessage:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = QuickEarthquakeMessage.from_dict(data)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = FeltEarthTremorReport.from_dict(data)

            return response_200_type_1

        response_200 = _parse_response_200(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[FeltEarthTremorReport | QuickEarthquakeMessage]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    data_type: GetEarthquakeInformationDataType,
    lang: GetEarthquakeInformationLang = "en",
) -> Response[FeltEarthTremorReport | QuickEarthquakeMessage]:
    """Earthquake information

     Returns quick earthquake messages (qem) or a locally felt earth tremor report (feltearthquake),
    selected by dataType.

    Args:
        data_type (GetEarthquakeInformationDataType):
        lang (GetEarthquakeInformationLang):  Default: 'en'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FeltEarthTremorReport | QuickEarthquakeMessage]
    """

    kwargs = _get_kwargs(
        data_type=data_type,
        lang=lang,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    data_type: GetEarthquakeInformationDataType,
    lang: GetEarthquakeInformationLang = "en",
) -> FeltEarthTremorReport | QuickEarthquakeMessage | None:
    """Earthquake information

     Returns quick earthquake messages (qem) or a locally felt earth tremor report (feltearthquake),
    selected by dataType.

    Args:
        data_type (GetEarthquakeInformationDataType):
        lang (GetEarthquakeInformationLang):  Default: 'en'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FeltEarthTremorReport | QuickEarthquakeMessage
    """

    return sync_detailed(
        client=client,
        data_type=data_type,
        lang=lang,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    data_type: GetEarthquakeInformationDataType,
    lang: GetEarthquakeInformationLang = "en",
) -> Response[FeltEarthTremorReport | QuickEarthquakeMessage]:
    """Earthquake information

     Returns quick earthquake messages (qem) or a locally felt earth tremor report (feltearthquake),
    selected by dataType.

    Args:
        data_type (GetEarthquakeInformationDataType):
        lang (GetEarthquakeInformationLang):  Default: 'en'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FeltEarthTremorReport | QuickEarthquakeMessage]
    """

    kwargs = _get_kwargs(
        data_type=data_type,
        lang=lang,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    data_type: GetEarthquakeInformationDataType,
    lang: GetEarthquakeInformationLang = "en",
) -> FeltEarthTremorReport | QuickEarthquakeMessage | None:
    """Earthquake information

     Returns quick earthquake messages (qem) or a locally felt earth tremor report (feltearthquake),
    selected by dataType.

    Args:
        data_type (GetEarthquakeInformationDataType):
        lang (GetEarthquakeInformationLang):  Default: 'en'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FeltEarthTremorReport | QuickEarthquakeMessage
    """

    return (
        await asyncio_detailed(
            client=client,
            data_type=data_type,
            lang=lang,
        )
    ).parsed
