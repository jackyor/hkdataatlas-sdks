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
        ncds_outstanding_hkd (float | Unset):
        ncds_outstanding_fc (float | Unset):
        ncds_outstanding_total (float | Unset):
        of_which_by_ais_hkd (float | Unset):
        of_which_by_ais_fc (float | Unset):
        of_which_by_ais_total (float | Unset):
        of_which_by_pub_hkd (float | Unset):
        of_which_by_pub_fc (float | Unset):
        of_which_by_pub_total (float | Unset):
        proport_outstand_ncds_by_pub_hkd (float | Unset):
        proport_outstand_ncds_by_pub_fc (float | Unset):
        proport_outstand_ncds_by_pub_total (float | Unset):
    """

    end_of_month: datetime.date | Unset = UNSET
    ncds_outstanding_hkd: float | Unset = UNSET
    ncds_outstanding_fc: float | Unset = UNSET
    ncds_outstanding_total: float | Unset = UNSET
    of_which_by_ais_hkd: float | Unset = UNSET
    of_which_by_ais_fc: float | Unset = UNSET
    of_which_by_ais_total: float | Unset = UNSET
    of_which_by_pub_hkd: float | Unset = UNSET
    of_which_by_pub_fc: float | Unset = UNSET
    of_which_by_pub_total: float | Unset = UNSET
    proport_outstand_ncds_by_pub_hkd: float | Unset = UNSET
    proport_outstand_ncds_by_pub_fc: float | Unset = UNSET
    proport_outstand_ncds_by_pub_total: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_month: str | Unset = UNSET
        if not isinstance(self.end_of_month, Unset):
            end_of_month = self.end_of_month.isoformat()

        ncds_outstanding_hkd = self.ncds_outstanding_hkd

        ncds_outstanding_fc = self.ncds_outstanding_fc

        ncds_outstanding_total = self.ncds_outstanding_total

        of_which_by_ais_hkd = self.of_which_by_ais_hkd

        of_which_by_ais_fc = self.of_which_by_ais_fc

        of_which_by_ais_total = self.of_which_by_ais_total

        of_which_by_pub_hkd = self.of_which_by_pub_hkd

        of_which_by_pub_fc = self.of_which_by_pub_fc

        of_which_by_pub_total = self.of_which_by_pub_total

        proport_outstand_ncds_by_pub_hkd = self.proport_outstand_ncds_by_pub_hkd

        proport_outstand_ncds_by_pub_fc = self.proport_outstand_ncds_by_pub_fc

        proport_outstand_ncds_by_pub_total = self.proport_outstand_ncds_by_pub_total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_of_month is not UNSET:
            field_dict["end_of_month"] = end_of_month
        if ncds_outstanding_hkd is not UNSET:
            field_dict["ncds_outstanding_hkd"] = ncds_outstanding_hkd
        if ncds_outstanding_fc is not UNSET:
            field_dict["ncds_outstanding_fc"] = ncds_outstanding_fc
        if ncds_outstanding_total is not UNSET:
            field_dict["ncds_outstanding_total"] = ncds_outstanding_total
        if of_which_by_ais_hkd is not UNSET:
            field_dict["of_which_by_ais_hkd"] = of_which_by_ais_hkd
        if of_which_by_ais_fc is not UNSET:
            field_dict["of_which_by_ais_fc"] = of_which_by_ais_fc
        if of_which_by_ais_total is not UNSET:
            field_dict["of_which_by_ais_total"] = of_which_by_ais_total
        if of_which_by_pub_hkd is not UNSET:
            field_dict["of_which_by_pub_hkd"] = of_which_by_pub_hkd
        if of_which_by_pub_fc is not UNSET:
            field_dict["of_which_by_pub_fc"] = of_which_by_pub_fc
        if of_which_by_pub_total is not UNSET:
            field_dict["of_which_by_pub_total"] = of_which_by_pub_total
        if proport_outstand_ncds_by_pub_hkd is not UNSET:
            field_dict["proport_outstand_ncds_by_pub_hkd"] = (
                proport_outstand_ncds_by_pub_hkd
            )
        if proport_outstand_ncds_by_pub_fc is not UNSET:
            field_dict["proport_outstand_ncds_by_pub_fc"] = (
                proport_outstand_ncds_by_pub_fc
            )
        if proport_outstand_ncds_by_pub_total is not UNSET:
            field_dict["proport_outstand_ncds_by_pub_total"] = (
                proport_outstand_ncds_by_pub_total
            )

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

        ncds_outstanding_hkd = d.pop("ncds_outstanding_hkd", UNSET)

        ncds_outstanding_fc = d.pop("ncds_outstanding_fc", UNSET)

        ncds_outstanding_total = d.pop("ncds_outstanding_total", UNSET)

        of_which_by_ais_hkd = d.pop("of_which_by_ais_hkd", UNSET)

        of_which_by_ais_fc = d.pop("of_which_by_ais_fc", UNSET)

        of_which_by_ais_total = d.pop("of_which_by_ais_total", UNSET)

        of_which_by_pub_hkd = d.pop("of_which_by_pub_hkd", UNSET)

        of_which_by_pub_fc = d.pop("of_which_by_pub_fc", UNSET)

        of_which_by_pub_total = d.pop("of_which_by_pub_total", UNSET)

        proport_outstand_ncds_by_pub_hkd = d.pop(
            "proport_outstand_ncds_by_pub_hkd", UNSET
        )

        proport_outstand_ncds_by_pub_fc = d.pop(
            "proport_outstand_ncds_by_pub_fc", UNSET
        )

        proport_outstand_ncds_by_pub_total = d.pop(
            "proport_outstand_ncds_by_pub_total", UNSET
        )

        record = cls(
            end_of_month=end_of_month,
            ncds_outstanding_hkd=ncds_outstanding_hkd,
            ncds_outstanding_fc=ncds_outstanding_fc,
            ncds_outstanding_total=ncds_outstanding_total,
            of_which_by_ais_hkd=of_which_by_ais_hkd,
            of_which_by_ais_fc=of_which_by_ais_fc,
            of_which_by_ais_total=of_which_by_ais_total,
            of_which_by_pub_hkd=of_which_by_pub_hkd,
            of_which_by_pub_fc=of_which_by_pub_fc,
            of_which_by_pub_total=of_which_by_pub_total,
            proport_outstand_ncds_by_pub_hkd=proport_outstand_ncds_by_pub_hkd,
            proport_outstand_ncds_by_pub_fc=proport_outstand_ncds_by_pub_fc,
            proport_outstand_ncds_by_pub_total=proport_outstand_ncds_by_pub_total,
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
