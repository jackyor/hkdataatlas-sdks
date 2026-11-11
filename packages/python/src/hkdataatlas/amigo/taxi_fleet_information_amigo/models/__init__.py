"""Contains all the data models used in inputs/outputs"""

from .find_nearby_vehicles_unit import FindNearbyVehiclesUnit
from .taxi_fleet_td_slim_record import TaxiFleetTdSlimRecord
from .taxi_fleet_td_slim_record_op_status import TaxiFleetTdSlimRecordOpStatus
from .taxi_fleet_td_slim_record_taxi_type import TaxiFleetTdSlimRecordTaxiType
from .vehicle_list_response import VehicleListResponse

__all__ = (
    "FindNearbyVehiclesUnit",
    "TaxiFleetTdSlimRecord",
    "TaxiFleetTdSlimRecordOpStatus",
    "TaxiFleetTdSlimRecordTaxiType",
    "VehicleListResponse",
)
