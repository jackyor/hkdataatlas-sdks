from typing import Literal

GetCarparkInfoVacancyData = Literal["info", "vacancy"]

GET_CARPARK_INFO_VACANCY_DATA_VALUES: set[GetCarparkInfoVacancyData] = {
    "info",
    "vacancy",
}


def check_get_carpark_info_vacancy_data(value: str) -> GetCarparkInfoVacancyData:
    if value in GET_CARPARK_INFO_VACANCY_DATA_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_CARPARK_INFO_VACANCY_DATA_VALUES!r}"
    )
