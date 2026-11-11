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
        monetary_base (float | Unset):
        claims_hksar_gov (float | Unset):
        claims_private_sector (float | Unset):
        foreign_assets (float | Unset):
        foreign_liabilities (float | Unset):
    """

    end_of_month: datetime.date | Unset = UNSET
    monetary_base: float | Unset = UNSET
    claims_hksar_gov: float | Unset = UNSET
    claims_private_sector: float | Unset = UNSET
    foreign_assets: float | Unset = UNSET
    foreign_liabilities: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_month: str | Unset = UNSET
        if not isinstance(self.end_of_month, Unset):
            end_of_month = self.end_of_month.isoformat()

        monetary_base = self.monetary_base

        claims_hksar_gov = self.claims_hksar_gov

        claims_private_sector = self.claims_private_sector

        foreign_assets = self.foreign_assets

        foreign_liabilities = self.foreign_liabilities

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_of_month is not UNSET:
            field_dict["end_of_month"] = end_of_month
        if monetary_base is not UNSET:
            field_dict["monetary_base"] = monetary_base
        if claims_hksar_gov is not UNSET:
            field_dict["claims_hksar_gov"] = claims_hksar_gov
        if claims_private_sector is not UNSET:
            field_dict["claims_private_sector"] = claims_private_sector
        if foreign_assets is not UNSET:
            field_dict["foreign_assets"] = foreign_assets
        if foreign_liabilities is not UNSET:
            field_dict["foreign_liabilities"] = foreign_liabilities

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

        monetary_base = d.pop("monetary_base", UNSET)

        claims_hksar_gov = d.pop("claims_hksar_gov", UNSET)

        claims_private_sector = d.pop("claims_private_sector", UNSET)

        foreign_assets = d.pop("foreign_assets", UNSET)

        foreign_liabilities = d.pop("foreign_liabilities", UNSET)

        record = cls(
            end_of_month=end_of_month,
            monetary_base=monetary_base,
            claims_hksar_gov=claims_hksar_gov,
            claims_private_sector=claims_private_sector,
            foreign_assets=foreign_assets,
            foreign_liabilities=foreign_liabilities,
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
