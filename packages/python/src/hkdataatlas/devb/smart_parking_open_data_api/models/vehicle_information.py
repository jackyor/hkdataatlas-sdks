from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.day_night_park import DayNightPark
    from ..models.hourly_charge import HourlyCharge
    from ..models.monthly_charge import MonthlyCharge
    from ..models.privilege import Privilege
    from ..models.unloading_charge import UnloadingCharge


T = TypeVar("T", bound="VehicleInformation")


@_attrs_define
class VehicleInformation:
    """Fields vary by vehicle type and availability. Vacancy-only responses primarily provide vacancy fields; detailed
    information may include spaces and charges.

        Attributes:
            day_night_parks (list[DayNightPark] | Unset):
            hourly_charges (list[HourlyCharge] | Unset):
            monthly_charges (list[MonthlyCharge] | Unset):
            privileges (list[Privilege] | Unset):
            space (float | Unset):
            space_dis (float | Unset):
            space_ev (float | Unset):
            space_unl (float | Unset):
            unloadings (list[UnloadingCharge] | Unset):
            vacancy (float | Unset):
            vacancy_dis (float | Unset):
            vacancy_ev (float | Unset):
            vacancy_unl (float | Unset):
    """

    day_night_parks: list[DayNightPark] | Unset = UNSET
    hourly_charges: list[HourlyCharge] | Unset = UNSET
    monthly_charges: list[MonthlyCharge] | Unset = UNSET
    privileges: list[Privilege] | Unset = UNSET
    space: float | Unset = UNSET
    space_dis: float | Unset = UNSET
    space_ev: float | Unset = UNSET
    space_unl: float | Unset = UNSET
    unloadings: list[UnloadingCharge] | Unset = UNSET
    vacancy: float | Unset = UNSET
    vacancy_dis: float | Unset = UNSET
    vacancy_ev: float | Unset = UNSET
    vacancy_unl: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        day_night_parks: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.day_night_parks, Unset):
            day_night_parks = []
            for day_night_parks_item_data in self.day_night_parks:
                day_night_parks_item = day_night_parks_item_data.to_dict()
                day_night_parks.append(day_night_parks_item)

        hourly_charges: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.hourly_charges, Unset):
            hourly_charges = []
            for hourly_charges_item_data in self.hourly_charges:
                hourly_charges_item = hourly_charges_item_data.to_dict()
                hourly_charges.append(hourly_charges_item)

        monthly_charges: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.monthly_charges, Unset):
            monthly_charges = []
            for monthly_charges_item_data in self.monthly_charges:
                monthly_charges_item = monthly_charges_item_data.to_dict()
                monthly_charges.append(monthly_charges_item)

        privileges: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.privileges, Unset):
            privileges = []
            for privileges_item_data in self.privileges:
                privileges_item = privileges_item_data.to_dict()
                privileges.append(privileges_item)

        space = self.space

        space_dis = self.space_dis

        space_ev = self.space_ev

        space_unl = self.space_unl

        unloadings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.unloadings, Unset):
            unloadings = []
            for unloadings_item_data in self.unloadings:
                unloadings_item = unloadings_item_data.to_dict()
                unloadings.append(unloadings_item)

        vacancy = self.vacancy

        vacancy_dis = self.vacancy_dis

        vacancy_ev = self.vacancy_ev

        vacancy_unl = self.vacancy_unl

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if day_night_parks is not UNSET:
            field_dict["dayNightParks"] = day_night_parks
        if hourly_charges is not UNSET:
            field_dict["hourlyCharges"] = hourly_charges
        if monthly_charges is not UNSET:
            field_dict["monthlyCharges"] = monthly_charges
        if privileges is not UNSET:
            field_dict["privileges"] = privileges
        if space is not UNSET:
            field_dict["space"] = space
        if space_dis is not UNSET:
            field_dict["spaceDIS"] = space_dis
        if space_ev is not UNSET:
            field_dict["spaceEV"] = space_ev
        if space_unl is not UNSET:
            field_dict["spaceUNL"] = space_unl
        if unloadings is not UNSET:
            field_dict["unloadings"] = unloadings
        if vacancy is not UNSET:
            field_dict["vacancy"] = vacancy
        if vacancy_dis is not UNSET:
            field_dict["vacancyDIS"] = vacancy_dis
        if vacancy_ev is not UNSET:
            field_dict["vacancyEV"] = vacancy_ev
        if vacancy_unl is not UNSET:
            field_dict["vacancyUNL"] = vacancy_unl

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.day_night_park import DayNightPark
        from ..models.hourly_charge import HourlyCharge
        from ..models.monthly_charge import MonthlyCharge
        from ..models.privilege import Privilege
        from ..models.unloading_charge import UnloadingCharge

        d = dict(src_dict)
        _day_night_parks = d.pop("dayNightParks", UNSET)
        day_night_parks: list[DayNightPark] | Unset = UNSET
        if _day_night_parks is not UNSET:
            day_night_parks = []
            for day_night_parks_item_data in _day_night_parks:
                day_night_parks_item = DayNightPark.from_dict(day_night_parks_item_data)

                day_night_parks.append(day_night_parks_item)

        _hourly_charges = d.pop("hourlyCharges", UNSET)
        hourly_charges: list[HourlyCharge] | Unset = UNSET
        if _hourly_charges is not UNSET:
            hourly_charges = []
            for hourly_charges_item_data in _hourly_charges:
                hourly_charges_item = HourlyCharge.from_dict(hourly_charges_item_data)

                hourly_charges.append(hourly_charges_item)

        _monthly_charges = d.pop("monthlyCharges", UNSET)
        monthly_charges: list[MonthlyCharge] | Unset = UNSET
        if _monthly_charges is not UNSET:
            monthly_charges = []
            for monthly_charges_item_data in _monthly_charges:
                monthly_charges_item = MonthlyCharge.from_dict(
                    monthly_charges_item_data
                )

                monthly_charges.append(monthly_charges_item)

        _privileges = d.pop("privileges", UNSET)
        privileges: list[Privilege] | Unset = UNSET
        if _privileges is not UNSET:
            privileges = []
            for privileges_item_data in _privileges:
                privileges_item = Privilege.from_dict(privileges_item_data)

                privileges.append(privileges_item)

        space = d.pop("space", UNSET)

        space_dis = d.pop("spaceDIS", UNSET)

        space_ev = d.pop("spaceEV", UNSET)

        space_unl = d.pop("spaceUNL", UNSET)

        _unloadings = d.pop("unloadings", UNSET)
        unloadings: list[UnloadingCharge] | Unset = UNSET
        if _unloadings is not UNSET:
            unloadings = []
            for unloadings_item_data in _unloadings:
                unloadings_item = UnloadingCharge.from_dict(unloadings_item_data)

                unloadings.append(unloadings_item)

        vacancy = d.pop("vacancy", UNSET)

        vacancy_dis = d.pop("vacancyDIS", UNSET)

        vacancy_ev = d.pop("vacancyEV", UNSET)

        vacancy_unl = d.pop("vacancyUNL", UNSET)

        vehicle_information = cls(
            day_night_parks=day_night_parks,
            hourly_charges=hourly_charges,
            monthly_charges=monthly_charges,
            privileges=privileges,
            space=space,
            space_dis=space_dis,
            space_ev=space_ev,
            space_unl=space_unl,
            unloadings=unloadings,
            vacancy=vacancy,
            vacancy_dis=vacancy_dis,
            vacancy_ev=vacancy_ev,
            vacancy_unl=vacancy_unl,
        )

        vehicle_information.additional_properties = d
        return vehicle_information

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
