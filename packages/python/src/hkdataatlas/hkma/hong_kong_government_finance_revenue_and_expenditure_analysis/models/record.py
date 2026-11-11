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
        gov_yr (datetime.date | Unset):
        gov_rev_a (float | Unset):
        gov_expen_a (float | Unset):
        gov_exp_genad_a (float | Unset):
        gov_exp_govund_a (float | Unset):
        gov_exp_pubhea_a (float | Unset):
        gov_exp_pubins_a (float | Unset):
        gov_exp_pubor_a (float | Unset):
        gov_exp_wk_a (float | Unset):
        gov_exp_defen_a (float | Unset):
    """

    gov_yr: datetime.date | Unset = UNSET
    gov_rev_a: float | Unset = UNSET
    gov_expen_a: float | Unset = UNSET
    gov_exp_genad_a: float | Unset = UNSET
    gov_exp_govund_a: float | Unset = UNSET
    gov_exp_pubhea_a: float | Unset = UNSET
    gov_exp_pubins_a: float | Unset = UNSET
    gov_exp_pubor_a: float | Unset = UNSET
    gov_exp_wk_a: float | Unset = UNSET
    gov_exp_defen_a: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        gov_yr: str | Unset = UNSET
        if not isinstance(self.gov_yr, Unset):
            gov_yr = self.gov_yr.isoformat()

        gov_rev_a = self.gov_rev_a

        gov_expen_a = self.gov_expen_a

        gov_exp_genad_a = self.gov_exp_genad_a

        gov_exp_govund_a = self.gov_exp_govund_a

        gov_exp_pubhea_a = self.gov_exp_pubhea_a

        gov_exp_pubins_a = self.gov_exp_pubins_a

        gov_exp_pubor_a = self.gov_exp_pubor_a

        gov_exp_wk_a = self.gov_exp_wk_a

        gov_exp_defen_a = self.gov_exp_defen_a

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if gov_yr is not UNSET:
            field_dict["Gov_yr"] = gov_yr
        if gov_rev_a is not UNSET:
            field_dict["Gov_rev_a"] = gov_rev_a
        if gov_expen_a is not UNSET:
            field_dict["Gov_expen_a"] = gov_expen_a
        if gov_exp_genad_a is not UNSET:
            field_dict["Gov_exp_genad_a"] = gov_exp_genad_a
        if gov_exp_govund_a is not UNSET:
            field_dict["Gov_exp_govund_a"] = gov_exp_govund_a
        if gov_exp_pubhea_a is not UNSET:
            field_dict["Gov_exp_pubhea_a"] = gov_exp_pubhea_a
        if gov_exp_pubins_a is not UNSET:
            field_dict["Gov_exp_pubins_a"] = gov_exp_pubins_a
        if gov_exp_pubor_a is not UNSET:
            field_dict["Gov_exp_pubor_a"] = gov_exp_pubor_a
        if gov_exp_wk_a is not UNSET:
            field_dict["Gov_exp_wk_a"] = gov_exp_wk_a
        if gov_exp_defen_a is not UNSET:
            field_dict["Gov_exp_defen_a"] = gov_exp_defen_a

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _gov_yr = d.pop("Gov_yr", UNSET)
        gov_yr: datetime.date | Unset
        if isinstance(_gov_yr, Unset):
            gov_yr = UNSET
        else:
            gov_yr = datetime.date.fromisoformat(_gov_yr)

        gov_rev_a = d.pop("Gov_rev_a", UNSET)

        gov_expen_a = d.pop("Gov_expen_a", UNSET)

        gov_exp_genad_a = d.pop("Gov_exp_genad_a", UNSET)

        gov_exp_govund_a = d.pop("Gov_exp_govund_a", UNSET)

        gov_exp_pubhea_a = d.pop("Gov_exp_pubhea_a", UNSET)

        gov_exp_pubins_a = d.pop("Gov_exp_pubins_a", UNSET)

        gov_exp_pubor_a = d.pop("Gov_exp_pubor_a", UNSET)

        gov_exp_wk_a = d.pop("Gov_exp_wk_a", UNSET)

        gov_exp_defen_a = d.pop("Gov_exp_defen_a", UNSET)

        record = cls(
            gov_yr=gov_yr,
            gov_rev_a=gov_rev_a,
            gov_expen_a=gov_expen_a,
            gov_exp_genad_a=gov_exp_genad_a,
            gov_exp_govund_a=gov_exp_govund_a,
            gov_exp_pubhea_a=gov_exp_pubhea_a,
            gov_exp_pubins_a=gov_exp_pubins_a,
            gov_exp_pubor_a=gov_exp_pubor_a,
            gov_exp_wk_a=gov_exp_wk_a,
            gov_exp_defen_a=gov_exp_defen_a,
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
