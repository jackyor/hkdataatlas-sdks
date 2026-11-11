"""Contains all the data models used in inputs/outputs"""

from .carpark_vacancy import CarparkVacancy
from .private_car_vacancy import PrivateCarVacancy
from .vacancy_response import VacancyResponse

__all__ = (
    "CarparkVacancy",
    "PrivateCarVacancy",
    "VacancyResponse",
)
