"""Contains all the data models used in inputs/outputs"""

from .carpark_vacancy import CarparkVacancy
from .carpark_vacancy_private_car import CarparkVacancyPrivateCar
from .ev_vacancy_response import EvVacancyResponse

__all__ = (
    "CarparkVacancy",
    "CarparkVacancyPrivateCar",
    "EvVacancyResponse",
)
