from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vacancy_record import VacancyRecord


T = TypeVar("T", bound="CarparkVacancy")


@_attrs_define
class CarparkVacancy:
    """Parking vacancy data. Vehicle properties contain arrays of vacancy records.

    Attributes:
        park_id (str): The system ID of the car park.
        cv (list[VacancyRecord] | Unset):
        hgv (list[VacancyRecord] | Unset):
        lgv (list[VacancyRecord] | Unset):
        coach (list[VacancyRecord] | Unset):
        motor_cycle (list[VacancyRecord] | Unset):
        private_car (list[VacancyRecord] | Unset):
    """

    park_id: str
    cv: list[VacancyRecord] | Unset = UNSET
    hgv: list[VacancyRecord] | Unset = UNSET
    lgv: list[VacancyRecord] | Unset = UNSET
    coach: list[VacancyRecord] | Unset = UNSET
    motor_cycle: list[VacancyRecord] | Unset = UNSET
    private_car: list[VacancyRecord] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        park_id = self.park_id

        cv: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.cv, Unset):
            cv = []
            for cv_item_data in self.cv:
                cv_item = cv_item_data.to_dict()
                cv.append(cv_item)

        hgv: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.hgv, Unset):
            hgv = []
            for hgv_item_data in self.hgv:
                hgv_item = hgv_item_data.to_dict()
                hgv.append(hgv_item)

        lgv: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.lgv, Unset):
            lgv = []
            for lgv_item_data in self.lgv:
                lgv_item = lgv_item_data.to_dict()
                lgv.append(lgv_item)

        coach: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.coach, Unset):
            coach = []
            for coach_item_data in self.coach:
                coach_item = coach_item_data.to_dict()
                coach.append(coach_item)

        motor_cycle: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.motor_cycle, Unset):
            motor_cycle = []
            for motor_cycle_item_data in self.motor_cycle:
                motor_cycle_item = motor_cycle_item_data.to_dict()
                motor_cycle.append(motor_cycle_item)

        private_car: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.private_car, Unset):
            private_car = []
            for private_car_item_data in self.private_car:
                private_car_item = private_car_item_data.to_dict()
                private_car.append(private_car_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "park_Id": park_id,
            }
        )
        if cv is not UNSET:
            field_dict["CV"] = cv
        if hgv is not UNSET:
            field_dict["HGV"] = hgv
        if lgv is not UNSET:
            field_dict["LGV"] = lgv
        if coach is not UNSET:
            field_dict["coach"] = coach
        if motor_cycle is not UNSET:
            field_dict["motorCycle"] = motor_cycle
        if private_car is not UNSET:
            field_dict["privateCar"] = private_car

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.vacancy_record import VacancyRecord

        d = dict(src_dict)
        park_id = d.pop("park_Id")

        _cv = d.pop("CV", UNSET)
        cv: list[VacancyRecord] | Unset = UNSET
        if _cv is not UNSET:
            cv = []
            for cv_item_data in _cv:
                cv_item = VacancyRecord.from_dict(cv_item_data)

                cv.append(cv_item)

        _hgv = d.pop("HGV", UNSET)
        hgv: list[VacancyRecord] | Unset = UNSET
        if _hgv is not UNSET:
            hgv = []
            for hgv_item_data in _hgv:
                hgv_item = VacancyRecord.from_dict(hgv_item_data)

                hgv.append(hgv_item)

        _lgv = d.pop("LGV", UNSET)
        lgv: list[VacancyRecord] | Unset = UNSET
        if _lgv is not UNSET:
            lgv = []
            for lgv_item_data in _lgv:
                lgv_item = VacancyRecord.from_dict(lgv_item_data)

                lgv.append(lgv_item)

        _coach = d.pop("coach", UNSET)
        coach: list[VacancyRecord] | Unset = UNSET
        if _coach is not UNSET:
            coach = []
            for coach_item_data in _coach:
                coach_item = VacancyRecord.from_dict(coach_item_data)

                coach.append(coach_item)

        _motor_cycle = d.pop("motorCycle", UNSET)
        motor_cycle: list[VacancyRecord] | Unset = UNSET
        if _motor_cycle is not UNSET:
            motor_cycle = []
            for motor_cycle_item_data in _motor_cycle:
                motor_cycle_item = VacancyRecord.from_dict(motor_cycle_item_data)

                motor_cycle.append(motor_cycle_item)

        _private_car = d.pop("privateCar", UNSET)
        private_car: list[VacancyRecord] | Unset = UNSET
        if _private_car is not UNSET:
            private_car = []
            for private_car_item_data in _private_car:
                private_car_item = VacancyRecord.from_dict(private_car_item_data)

                private_car.append(private_car_item)

        carpark_vacancy = cls(
            park_id=park_id,
            cv=cv,
            hgv=hgv,
            lgv=lgv,
            coach=coach,
            motor_cycle=motor_cycle,
            private_car=private_car,
        )

        carpark_vacancy.additional_properties = d
        return carpark_vacancy

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
