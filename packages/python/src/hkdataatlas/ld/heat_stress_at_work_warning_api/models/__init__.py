"""Contains all the data models used in inputs/outputs"""

from .empty_response import EmptyResponse
from .heat_stress_at_work_warning import HeatStressAtWorkWarning
from .warning_response import WarningResponse

__all__ = (
    "EmptyResponse",
    "HeatStressAtWorkWarning",
    "WarningResponse",
)
