from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Record")


@_attrs_define
class Record:
    """
    Attributes:
        end_of_year (datetime.date | Unset):
        ef_type (str | Unset):
        changeable_figures (str | Unset):
        staff_salaries (float | Unset):
        staff_retirement (float | Unset):
        premises_equipment_depreciation (float | Unset):
        premises_equipment_rental (float | Unset):
        premises_equipment_other (float | Unset):
        general_operate_equipment_maintenance (float | Unset):
        general_operate_fin_infra_operate (float | Unset):
        general_operate_professional (float | Unset):
        general_operate_fin_info_comm_services (float | Unset):
        general_operate_publicity (float | Unset):
        general_operate_external_relations (float | Unset):
        general_operate_training (float | Unset):
        general_operate_invest_operating_expenses (float | Unset):
        general_operate_invest_lease_payment (float | Unset):
        general_operate_others (float | Unset):
        sme_fin_guarantee_scheme_operating_expenses (float | Unset):
        invest_fee_management_fees (float | Unset):
        invest_fee_transaction_cost (float | Unset):
        invest_fee_tax (float | Unset):
        invest_fee_professional_fees (float | Unset):
        total_operating_expenses (float | Unset):
    """

    end_of_year: datetime.date | Unset = UNSET
    ef_type: str | Unset = UNSET
    changeable_figures: str | Unset = UNSET
    staff_salaries: float | Unset = UNSET
    staff_retirement: float | Unset = UNSET
    premises_equipment_depreciation: float | Unset = UNSET
    premises_equipment_rental: float | Unset = UNSET
    premises_equipment_other: float | Unset = UNSET
    general_operate_equipment_maintenance: float | Unset = UNSET
    general_operate_fin_infra_operate: float | Unset = UNSET
    general_operate_professional: float | Unset = UNSET
    general_operate_fin_info_comm_services: float | Unset = UNSET
    general_operate_publicity: float | Unset = UNSET
    general_operate_external_relations: float | Unset = UNSET
    general_operate_training: float | Unset = UNSET
    general_operate_invest_operating_expenses: float | Unset = UNSET
    general_operate_invest_lease_payment: float | Unset = UNSET
    general_operate_others: float | Unset = UNSET
    sme_fin_guarantee_scheme_operating_expenses: float | Unset = UNSET
    invest_fee_management_fees: float | Unset = UNSET
    invest_fee_transaction_cost: float | Unset = UNSET
    invest_fee_tax: float | Unset = UNSET
    invest_fee_professional_fees: float | Unset = UNSET
    total_operating_expenses: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_year: str | Unset = UNSET
        if not isinstance(self.end_of_year, Unset):
            end_of_year = self.end_of_year.isoformat()

        ef_type = self.ef_type

        changeable_figures = self.changeable_figures

        staff_salaries = self.staff_salaries

        staff_retirement = self.staff_retirement

        premises_equipment_depreciation = self.premises_equipment_depreciation

        premises_equipment_rental = self.premises_equipment_rental

        premises_equipment_other = self.premises_equipment_other

        general_operate_equipment_maintenance = (
            self.general_operate_equipment_maintenance
        )

        general_operate_fin_infra_operate = self.general_operate_fin_infra_operate

        general_operate_professional = self.general_operate_professional

        general_operate_fin_info_comm_services = (
            self.general_operate_fin_info_comm_services
        )

        general_operate_publicity = self.general_operate_publicity

        general_operate_external_relations = self.general_operate_external_relations

        general_operate_training = self.general_operate_training

        general_operate_invest_operating_expenses = (
            self.general_operate_invest_operating_expenses
        )

        general_operate_invest_lease_payment = self.general_operate_invest_lease_payment

        general_operate_others = self.general_operate_others

        sme_fin_guarantee_scheme_operating_expenses = (
            self.sme_fin_guarantee_scheme_operating_expenses
        )

        invest_fee_management_fees = self.invest_fee_management_fees

        invest_fee_transaction_cost = self.invest_fee_transaction_cost

        invest_fee_tax = self.invest_fee_tax

        invest_fee_professional_fees = self.invest_fee_professional_fees

        total_operating_expenses = self.total_operating_expenses

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_of_year is not UNSET:
            field_dict["end_of_year"] = end_of_year
        if ef_type is not UNSET:
            field_dict["ef_type"] = ef_type
        if changeable_figures is not UNSET:
            field_dict["changeable_figures"] = changeable_figures
        if staff_salaries is not UNSET:
            field_dict["staff_salaries"] = staff_salaries
        if staff_retirement is not UNSET:
            field_dict["staff_retirement"] = staff_retirement
        if premises_equipment_depreciation is not UNSET:
            field_dict["premises_equipment_depreciation"] = (
                premises_equipment_depreciation
            )
        if premises_equipment_rental is not UNSET:
            field_dict["premises_equipment_rental"] = premises_equipment_rental
        if premises_equipment_other is not UNSET:
            field_dict["premises_equipment_other"] = premises_equipment_other
        if general_operate_equipment_maintenance is not UNSET:
            field_dict["general_operate_equipment_maintenance"] = (
                general_operate_equipment_maintenance
            )
        if general_operate_fin_infra_operate is not UNSET:
            field_dict["general_operate_fin_infra_operate"] = (
                general_operate_fin_infra_operate
            )
        if general_operate_professional is not UNSET:
            field_dict["general_operate_professional"] = general_operate_professional
        if general_operate_fin_info_comm_services is not UNSET:
            field_dict["general_operate_fin_info_comm_services"] = (
                general_operate_fin_info_comm_services
            )
        if general_operate_publicity is not UNSET:
            field_dict["general_operate_publicity"] = general_operate_publicity
        if general_operate_external_relations is not UNSET:
            field_dict["general_operate_external_relations"] = (
                general_operate_external_relations
            )
        if general_operate_training is not UNSET:
            field_dict["general_operate_training"] = general_operate_training
        if general_operate_invest_operating_expenses is not UNSET:
            field_dict["general_operate_invest_operating_expenses"] = (
                general_operate_invest_operating_expenses
            )
        if general_operate_invest_lease_payment is not UNSET:
            field_dict["general_operate_invest_lease_payment"] = (
                general_operate_invest_lease_payment
            )
        if general_operate_others is not UNSET:
            field_dict["general_operate_others"] = general_operate_others
        if sme_fin_guarantee_scheme_operating_expenses is not UNSET:
            field_dict["sme_fin_guarantee_scheme_operating_expenses"] = (
                sme_fin_guarantee_scheme_operating_expenses
            )
        if invest_fee_management_fees is not UNSET:
            field_dict["invest_fee_management_fees"] = invest_fee_management_fees
        if invest_fee_transaction_cost is not UNSET:
            field_dict["invest_fee_transaction_cost"] = invest_fee_transaction_cost
        if invest_fee_tax is not UNSET:
            field_dict["invest_fee_tax"] = invest_fee_tax
        if invest_fee_professional_fees is not UNSET:
            field_dict["invest_fee_professional_fees"] = invest_fee_professional_fees
        if total_operating_expenses is not UNSET:
            field_dict["total_operating_expenses"] = total_operating_expenses

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _end_of_year = d.pop("end_of_year", UNSET)
        end_of_year: datetime.date | Unset
        if isinstance(_end_of_year, Unset):
            end_of_year = UNSET
        else:
            end_of_year = datetime.date.fromisoformat(_end_of_year)

        ef_type = d.pop("ef_type", UNSET)

        changeable_figures = d.pop("changeable_figures", UNSET)

        staff_salaries = d.pop("staff_salaries", UNSET)

        staff_retirement = d.pop("staff_retirement", UNSET)

        premises_equipment_depreciation = d.pop(
            "premises_equipment_depreciation", UNSET
        )

        premises_equipment_rental = d.pop("premises_equipment_rental", UNSET)

        premises_equipment_other = d.pop("premises_equipment_other", UNSET)

        general_operate_equipment_maintenance = d.pop(
            "general_operate_equipment_maintenance", UNSET
        )

        general_operate_fin_infra_operate = d.pop(
            "general_operate_fin_infra_operate", UNSET
        )

        general_operate_professional = d.pop("general_operate_professional", UNSET)

        general_operate_fin_info_comm_services = d.pop(
            "general_operate_fin_info_comm_services", UNSET
        )

        general_operate_publicity = d.pop("general_operate_publicity", UNSET)

        general_operate_external_relations = d.pop(
            "general_operate_external_relations", UNSET
        )

        general_operate_training = d.pop("general_operate_training", UNSET)

        general_operate_invest_operating_expenses = d.pop(
            "general_operate_invest_operating_expenses", UNSET
        )

        general_operate_invest_lease_payment = d.pop(
            "general_operate_invest_lease_payment", UNSET
        )

        general_operate_others = d.pop("general_operate_others", UNSET)

        sme_fin_guarantee_scheme_operating_expenses = d.pop(
            "sme_fin_guarantee_scheme_operating_expenses", UNSET
        )

        invest_fee_management_fees = d.pop("invest_fee_management_fees", UNSET)

        invest_fee_transaction_cost = d.pop("invest_fee_transaction_cost", UNSET)

        invest_fee_tax = d.pop("invest_fee_tax", UNSET)

        invest_fee_professional_fees = d.pop("invest_fee_professional_fees", UNSET)

        total_operating_expenses = d.pop("total_operating_expenses", UNSET)

        record = cls(
            end_of_year=end_of_year,
            ef_type=ef_type,
            changeable_figures=changeable_figures,
            staff_salaries=staff_salaries,
            staff_retirement=staff_retirement,
            premises_equipment_depreciation=premises_equipment_depreciation,
            premises_equipment_rental=premises_equipment_rental,
            premises_equipment_other=premises_equipment_other,
            general_operate_equipment_maintenance=general_operate_equipment_maintenance,
            general_operate_fin_infra_operate=general_operate_fin_infra_operate,
            general_operate_professional=general_operate_professional,
            general_operate_fin_info_comm_services=general_operate_fin_info_comm_services,
            general_operate_publicity=general_operate_publicity,
            general_operate_external_relations=general_operate_external_relations,
            general_operate_training=general_operate_training,
            general_operate_invest_operating_expenses=general_operate_invest_operating_expenses,
            general_operate_invest_lease_payment=general_operate_invest_lease_payment,
            general_operate_others=general_operate_others,
            sme_fin_guarantee_scheme_operating_expenses=sme_fin_guarantee_scheme_operating_expenses,
            invest_fee_management_fees=invest_fee_management_fees,
            invest_fee_transaction_cost=invest_fee_transaction_cost,
            invest_fee_tax=invest_fee_tax,
            invest_fee_professional_fees=invest_fee_professional_fees,
            total_operating_expenses=total_operating_expenses,
        )

        record.additional_properties = d
        return record

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
