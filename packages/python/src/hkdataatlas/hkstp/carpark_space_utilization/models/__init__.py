"""Contains all the data models used in inputs/outputs"""

from .carpark_utilization import CarparkUtilization
from .private_car_utilization import PrivateCarUtilization
from .utilization_response import UtilizationResponse

__all__ = (
    "CarparkUtilization",
    "PrivateCarUtilization",
    "UtilizationResponse",
)
