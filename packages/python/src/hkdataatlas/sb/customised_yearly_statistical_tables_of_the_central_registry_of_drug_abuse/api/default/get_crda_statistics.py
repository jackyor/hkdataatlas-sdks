from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_crda_statistics_abuser import (
    GetCrdaStatisticsAbuser,
)
from ...models.get_crda_statistics_age import (
    GetCrdaStatisticsAge,
)
from ...models.get_crda_statistics_age_group import (
    GetCrdaStatisticsAgeGroup,
)
from ...models.get_crda_statistics_analysis_var_item import (
    GetCrdaStatisticsAnalysisVarItem,
)
from ...models.get_crda_statistics_period import (
    GetCrdaStatisticsPeriod,
)
from ...models.get_crda_statistics_period_earlier import (
    GetCrdaStatisticsPeriodEarlier,
)
from ...models.get_crda_statistics_sex import (
    GetCrdaStatisticsSex,
)
from ...models.warning import Warning_
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    period: GetCrdaStatisticsPeriod | Unset = UNSET,
    period_earlier: GetCrdaStatisticsPeriodEarlier | Unset = UNSET,
    abuser: GetCrdaStatisticsAbuser,
    sex: GetCrdaStatisticsSex | Unset = UNSET,
    age: GetCrdaStatisticsAge | Unset = UNSET,
    age_group: GetCrdaStatisticsAgeGroup | Unset = UNSET,
    analysis_var: list[GetCrdaStatisticsAnalysisVarItem] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_period: str | Unset = UNSET
    if not isinstance(period, Unset):
        json_period = period

    params["period"] = json_period

    json_period_earlier: str | Unset = UNSET
    if not isinstance(period_earlier, Unset):
        json_period_earlier = period_earlier

    params["period_earlier"] = json_period_earlier

    json_abuser: str = abuser
    params["abuser"] = json_abuser

    json_sex: str | Unset = UNSET
    if not isinstance(sex, Unset):
        json_sex = sex

    params["sex"] = json_sex

    json_age: str | Unset = UNSET
    if not isinstance(age, Unset):
        json_age = age

    params["age"] = json_age

    json_age_group: str | Unset = UNSET
    if not isinstance(age_group, Unset):
        json_age_group = age_group

    params["age_group"] = json_age_group

    json_analysis_var: list[str] | Unset = UNSET
    if not isinstance(analysis_var, Unset):
        json_analysis_var = []
        for analysis_var_item_data in analysis_var:
            analysis_var_item: str = analysis_var_item_data
            json_analysis_var.append(analysis_var_item)

    params["analysis_var"] = json_analysis_var

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/psi_v1.php",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Warning_ | str | None:
    if response.status_code == 200:
        response_200 = response.text
        return response_200

    if response.status_code == 400:
        response_400 = Warning_.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Warning_ | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    period: GetCrdaStatisticsPeriod | Unset = UNSET,
    period_earlier: GetCrdaStatisticsPeriodEarlier | Unset = UNSET,
    abuser: GetCrdaStatisticsAbuser,
    sex: GetCrdaStatisticsSex | Unset = UNSET,
    age: GetCrdaStatisticsAge | Unset = UNSET,
    age_group: GetCrdaStatisticsAgeGroup | Unset = UNSET,
    analysis_var: list[GetCrdaStatisticsAnalysisVarItem] | Unset = UNSET,
) -> Response[Warning_ | str]:
    """Get customized CRDA statistics

     Returns a customized statistical table as a UTF-8 CSV file. `period` and `period_earlier` must not
    be supplied together; `age` and `age_group` must not be supplied together. The specification's
    example request is `https://www.nd.gov.hk/en/psi_v1.php?period=2016-2025&abuser=00001`.

    Args:
        period (GetCrdaStatisticsPeriod | Unset):
        period_earlier (GetCrdaStatisticsPeriodEarlier | Unset):
        abuser (GetCrdaStatisticsAbuser):
        sex (GetCrdaStatisticsSex | Unset):
        age (GetCrdaStatisticsAge | Unset):
        age_group (GetCrdaStatisticsAgeGroup | Unset):
        analysis_var (list[GetCrdaStatisticsAnalysisVarItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Warning_ | str]
    """

    kwargs = _get_kwargs(
        period=period,
        period_earlier=period_earlier,
        abuser=abuser,
        sex=sex,
        age=age,
        age_group=age_group,
        analysis_var=analysis_var,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    period: GetCrdaStatisticsPeriod | Unset = UNSET,
    period_earlier: GetCrdaStatisticsPeriodEarlier | Unset = UNSET,
    abuser: GetCrdaStatisticsAbuser,
    sex: GetCrdaStatisticsSex | Unset = UNSET,
    age: GetCrdaStatisticsAge | Unset = UNSET,
    age_group: GetCrdaStatisticsAgeGroup | Unset = UNSET,
    analysis_var: list[GetCrdaStatisticsAnalysisVarItem] | Unset = UNSET,
) -> Warning_ | str | None:
    """Get customized CRDA statistics

     Returns a customized statistical table as a UTF-8 CSV file. `period` and `period_earlier` must not
    be supplied together; `age` and `age_group` must not be supplied together. The specification's
    example request is `https://www.nd.gov.hk/en/psi_v1.php?period=2016-2025&abuser=00001`.

    Args:
        period (GetCrdaStatisticsPeriod | Unset):
        period_earlier (GetCrdaStatisticsPeriodEarlier | Unset):
        abuser (GetCrdaStatisticsAbuser):
        sex (GetCrdaStatisticsSex | Unset):
        age (GetCrdaStatisticsAge | Unset):
        age_group (GetCrdaStatisticsAgeGroup | Unset):
        analysis_var (list[GetCrdaStatisticsAnalysisVarItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Warning_ | str
    """

    return sync_detailed(
        client=client,
        period=period,
        period_earlier=period_earlier,
        abuser=abuser,
        sex=sex,
        age=age,
        age_group=age_group,
        analysis_var=analysis_var,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    period: GetCrdaStatisticsPeriod | Unset = UNSET,
    period_earlier: GetCrdaStatisticsPeriodEarlier | Unset = UNSET,
    abuser: GetCrdaStatisticsAbuser,
    sex: GetCrdaStatisticsSex | Unset = UNSET,
    age: GetCrdaStatisticsAge | Unset = UNSET,
    age_group: GetCrdaStatisticsAgeGroup | Unset = UNSET,
    analysis_var: list[GetCrdaStatisticsAnalysisVarItem] | Unset = UNSET,
) -> Response[Warning_ | str]:
    """Get customized CRDA statistics

     Returns a customized statistical table as a UTF-8 CSV file. `period` and `period_earlier` must not
    be supplied together; `age` and `age_group` must not be supplied together. The specification's
    example request is `https://www.nd.gov.hk/en/psi_v1.php?period=2016-2025&abuser=00001`.

    Args:
        period (GetCrdaStatisticsPeriod | Unset):
        period_earlier (GetCrdaStatisticsPeriodEarlier | Unset):
        abuser (GetCrdaStatisticsAbuser):
        sex (GetCrdaStatisticsSex | Unset):
        age (GetCrdaStatisticsAge | Unset):
        age_group (GetCrdaStatisticsAgeGroup | Unset):
        analysis_var (list[GetCrdaStatisticsAnalysisVarItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Warning_ | str]
    """

    kwargs = _get_kwargs(
        period=period,
        period_earlier=period_earlier,
        abuser=abuser,
        sex=sex,
        age=age,
        age_group=age_group,
        analysis_var=analysis_var,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    period: GetCrdaStatisticsPeriod | Unset = UNSET,
    period_earlier: GetCrdaStatisticsPeriodEarlier | Unset = UNSET,
    abuser: GetCrdaStatisticsAbuser,
    sex: GetCrdaStatisticsSex | Unset = UNSET,
    age: GetCrdaStatisticsAge | Unset = UNSET,
    age_group: GetCrdaStatisticsAgeGroup | Unset = UNSET,
    analysis_var: list[GetCrdaStatisticsAnalysisVarItem] | Unset = UNSET,
) -> Warning_ | str | None:
    """Get customized CRDA statistics

     Returns a customized statistical table as a UTF-8 CSV file. `period` and `period_earlier` must not
    be supplied together; `age` and `age_group` must not be supplied together. The specification's
    example request is `https://www.nd.gov.hk/en/psi_v1.php?period=2016-2025&abuser=00001`.

    Args:
        period (GetCrdaStatisticsPeriod | Unset):
        period_earlier (GetCrdaStatisticsPeriodEarlier | Unset):
        abuser (GetCrdaStatisticsAbuser):
        sex (GetCrdaStatisticsSex | Unset):
        age (GetCrdaStatisticsAge | Unset):
        age_group (GetCrdaStatisticsAgeGroup | Unset):
        analysis_var (list[GetCrdaStatisticsAnalysisVarItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Warning_ | str
    """

    return (
        await asyncio_detailed(
            client=client,
            period=period,
            period_earlier=period_earlier,
            abuser=abuser,
            sex=sex,
            age=age,
            age_group=age_group,
            analysis_var=analysis_var,
        )
    ).parsed
