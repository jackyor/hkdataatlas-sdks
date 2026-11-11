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
        end_of_month (datetime.date | Unset):
        fc_resv_assets_ef (float | Unset):
        fc_resv_assets_lf (float | Unset):
        fc_resv_assets_total (float | Unset):
        unsettle_fx_contracts_ef (float | Unset):
        unsettle_fx_contracts_lf (float | Unset):
        unsettle_fx_contracts_total (float | Unset):
        fc_assets_fx_contracts_ef (float | Unset):
        fc_assets_fx_contracts_lf (float | Unset):
        fc_assets_fx_contracts_total (float | Unset):
    """

    end_of_month: datetime.date | Unset = UNSET
    fc_resv_assets_ef: float | Unset = UNSET
    fc_resv_assets_lf: float | Unset = UNSET
    fc_resv_assets_total: float | Unset = UNSET
    unsettle_fx_contracts_ef: float | Unset = UNSET
    unsettle_fx_contracts_lf: float | Unset = UNSET
    unsettle_fx_contracts_total: float | Unset = UNSET
    fc_assets_fx_contracts_ef: float | Unset = UNSET
    fc_assets_fx_contracts_lf: float | Unset = UNSET
    fc_assets_fx_contracts_total: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_month: str | Unset = UNSET
        if not isinstance(self.end_of_month, Unset):
            end_of_month = self.end_of_month.isoformat()

        fc_resv_assets_ef = self.fc_resv_assets_ef

        fc_resv_assets_lf = self.fc_resv_assets_lf

        fc_resv_assets_total = self.fc_resv_assets_total

        unsettle_fx_contracts_ef = self.unsettle_fx_contracts_ef

        unsettle_fx_contracts_lf = self.unsettle_fx_contracts_lf

        unsettle_fx_contracts_total = self.unsettle_fx_contracts_total

        fc_assets_fx_contracts_ef = self.fc_assets_fx_contracts_ef

        fc_assets_fx_contracts_lf = self.fc_assets_fx_contracts_lf

        fc_assets_fx_contracts_total = self.fc_assets_fx_contracts_total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_of_month is not UNSET:
            field_dict["end_of_month"] = end_of_month
        if fc_resv_assets_ef is not UNSET:
            field_dict["fc_resv_assets_ef"] = fc_resv_assets_ef
        if fc_resv_assets_lf is not UNSET:
            field_dict["fc_resv_assets_lf"] = fc_resv_assets_lf
        if fc_resv_assets_total is not UNSET:
            field_dict["fc_resv_assets_total"] = fc_resv_assets_total
        if unsettle_fx_contracts_ef is not UNSET:
            field_dict["unsettle_fx_contracts_ef"] = unsettle_fx_contracts_ef
        if unsettle_fx_contracts_lf is not UNSET:
            field_dict["unsettle_fx_contracts_lf"] = unsettle_fx_contracts_lf
        if unsettle_fx_contracts_total is not UNSET:
            field_dict["unsettle_fx_contracts_total"] = unsettle_fx_contracts_total
        if fc_assets_fx_contracts_ef is not UNSET:
            field_dict["fc_assets_fx_contracts_ef"] = fc_assets_fx_contracts_ef
        if fc_assets_fx_contracts_lf is not UNSET:
            field_dict["fc_assets_fx_contracts_lf"] = fc_assets_fx_contracts_lf
        if fc_assets_fx_contracts_total is not UNSET:
            field_dict["fc_assets_fx_contracts_total"] = fc_assets_fx_contracts_total

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _end_of_month = d.pop("end_of_month", UNSET)
        end_of_month: datetime.date | Unset
        if isinstance(_end_of_month, Unset):
            end_of_month = UNSET
        else:
            end_of_month = datetime.date.fromisoformat(_end_of_month)

        fc_resv_assets_ef = d.pop("fc_resv_assets_ef", UNSET)

        fc_resv_assets_lf = d.pop("fc_resv_assets_lf", UNSET)

        fc_resv_assets_total = d.pop("fc_resv_assets_total", UNSET)

        unsettle_fx_contracts_ef = d.pop("unsettle_fx_contracts_ef", UNSET)

        unsettle_fx_contracts_lf = d.pop("unsettle_fx_contracts_lf", UNSET)

        unsettle_fx_contracts_total = d.pop("unsettle_fx_contracts_total", UNSET)

        fc_assets_fx_contracts_ef = d.pop("fc_assets_fx_contracts_ef", UNSET)

        fc_assets_fx_contracts_lf = d.pop("fc_assets_fx_contracts_lf", UNSET)

        fc_assets_fx_contracts_total = d.pop("fc_assets_fx_contracts_total", UNSET)

        record = cls(
            end_of_month=end_of_month,
            fc_resv_assets_ef=fc_resv_assets_ef,
            fc_resv_assets_lf=fc_resv_assets_lf,
            fc_resv_assets_total=fc_resv_assets_total,
            unsettle_fx_contracts_ef=unsettle_fx_contracts_ef,
            unsettle_fx_contracts_lf=unsettle_fx_contracts_lf,
            unsettle_fx_contracts_total=unsettle_fx_contracts_total,
            fc_assets_fx_contracts_ef=fc_assets_fx_contracts_ef,
            fc_assets_fx_contracts_lf=fc_assets_fx_contracts_lf,
            fc_assets_fx_contracts_total=fc_assets_fx_contracts_total,
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
