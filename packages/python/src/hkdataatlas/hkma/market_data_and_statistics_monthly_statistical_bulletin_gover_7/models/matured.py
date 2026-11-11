from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Matured")


@_attrs_define
class Matured:
    """
    Attributes:
        end_of_month (datetime.date | Unset):
        ind_pricing_02gb1109 (float | Unset):
        ind_pricing_02gb1203 (float | Unset):
        ind_pricing_02gb1209 (float | Unset):
        ind_pricing_02gb1303 (float | Unset):
        ind_pricing_02gb1309 (float | Unset):
        ind_pricing_02gb1403 (float | Unset):
        ind_pricing_05gb1411 (float | Unset):
        ind_pricing_03gb1505 (float | Unset):
        ind_pricing_05gb1512 (float | Unset):
        ind_pricing_03gb1605 (float | Unset):
        ind_pricing_05gb1612 (float | Unset):
        ind_pricing_03gb1704 (float | Unset):
        ind_pricing_03gb1711 (float | Unset):
        ind_pricing_05gb1802 (float | Unset):
        ind_pricing_05gb1902 (float | Unset):
        closing_ref_rate_02gb1109 (float | Unset):
        closing_ref_rate_02gb1203 (float | Unset):
        closing_ref_rate_02gb1209 (float | Unset):
        closing_ref_rate_02gb1303 (float | Unset):
        closing_ref_rate_02gb1309 (float | Unset):
        closing_ref_rate_02gb1403 (float | Unset):
        closing_ref_rate_05gb1411 (float | Unset):
        closing_ref_rate_03gb1505 (float | Unset):
        closing_ref_rate_05gb1512 (float | Unset):
        closing_ref_rate_03gb1605 (float | Unset):
        closing_ref_rate_05gb1612 (float | Unset):
        closing_ref_rate_03gb1704 (float | Unset):
        closing_ref_rate_03gb1711 (float | Unset):
        closing_ref_rate_05gb1802 (float | Unset):
        closing_ref_rate_05gb1902 (float | Unset):
    """

    end_of_month: datetime.date | Unset = UNSET
    ind_pricing_02gb1109: float | Unset = UNSET
    ind_pricing_02gb1203: float | Unset = UNSET
    ind_pricing_02gb1209: float | Unset = UNSET
    ind_pricing_02gb1303: float | Unset = UNSET
    ind_pricing_02gb1309: float | Unset = UNSET
    ind_pricing_02gb1403: float | Unset = UNSET
    ind_pricing_05gb1411: float | Unset = UNSET
    ind_pricing_03gb1505: float | Unset = UNSET
    ind_pricing_05gb1512: float | Unset = UNSET
    ind_pricing_03gb1605: float | Unset = UNSET
    ind_pricing_05gb1612: float | Unset = UNSET
    ind_pricing_03gb1704: float | Unset = UNSET
    ind_pricing_03gb1711: float | Unset = UNSET
    ind_pricing_05gb1802: float | Unset = UNSET
    ind_pricing_05gb1902: float | Unset = UNSET
    closing_ref_rate_02gb1109: float | Unset = UNSET
    closing_ref_rate_02gb1203: float | Unset = UNSET
    closing_ref_rate_02gb1209: float | Unset = UNSET
    closing_ref_rate_02gb1303: float | Unset = UNSET
    closing_ref_rate_02gb1309: float | Unset = UNSET
    closing_ref_rate_02gb1403: float | Unset = UNSET
    closing_ref_rate_05gb1411: float | Unset = UNSET
    closing_ref_rate_03gb1505: float | Unset = UNSET
    closing_ref_rate_05gb1512: float | Unset = UNSET
    closing_ref_rate_03gb1605: float | Unset = UNSET
    closing_ref_rate_05gb1612: float | Unset = UNSET
    closing_ref_rate_03gb1704: float | Unset = UNSET
    closing_ref_rate_03gb1711: float | Unset = UNSET
    closing_ref_rate_05gb1802: float | Unset = UNSET
    closing_ref_rate_05gb1902: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_month: str | Unset = UNSET
        if not isinstance(self.end_of_month, Unset):
            end_of_month = self.end_of_month.isoformat()

        ind_pricing_02gb1109 = self.ind_pricing_02gb1109

        ind_pricing_02gb1203 = self.ind_pricing_02gb1203

        ind_pricing_02gb1209 = self.ind_pricing_02gb1209

        ind_pricing_02gb1303 = self.ind_pricing_02gb1303

        ind_pricing_02gb1309 = self.ind_pricing_02gb1309

        ind_pricing_02gb1403 = self.ind_pricing_02gb1403

        ind_pricing_05gb1411 = self.ind_pricing_05gb1411

        ind_pricing_03gb1505 = self.ind_pricing_03gb1505

        ind_pricing_05gb1512 = self.ind_pricing_05gb1512

        ind_pricing_03gb1605 = self.ind_pricing_03gb1605

        ind_pricing_05gb1612 = self.ind_pricing_05gb1612

        ind_pricing_03gb1704 = self.ind_pricing_03gb1704

        ind_pricing_03gb1711 = self.ind_pricing_03gb1711

        ind_pricing_05gb1802 = self.ind_pricing_05gb1802

        ind_pricing_05gb1902 = self.ind_pricing_05gb1902

        closing_ref_rate_02gb1109 = self.closing_ref_rate_02gb1109

        closing_ref_rate_02gb1203 = self.closing_ref_rate_02gb1203

        closing_ref_rate_02gb1209 = self.closing_ref_rate_02gb1209

        closing_ref_rate_02gb1303 = self.closing_ref_rate_02gb1303

        closing_ref_rate_02gb1309 = self.closing_ref_rate_02gb1309

        closing_ref_rate_02gb1403 = self.closing_ref_rate_02gb1403

        closing_ref_rate_05gb1411 = self.closing_ref_rate_05gb1411

        closing_ref_rate_03gb1505 = self.closing_ref_rate_03gb1505

        closing_ref_rate_05gb1512 = self.closing_ref_rate_05gb1512

        closing_ref_rate_03gb1605 = self.closing_ref_rate_03gb1605

        closing_ref_rate_05gb1612 = self.closing_ref_rate_05gb1612

        closing_ref_rate_03gb1704 = self.closing_ref_rate_03gb1704

        closing_ref_rate_03gb1711 = self.closing_ref_rate_03gb1711

        closing_ref_rate_05gb1802 = self.closing_ref_rate_05gb1802

        closing_ref_rate_05gb1902 = self.closing_ref_rate_05gb1902

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_of_month is not UNSET:
            field_dict["end_of_month"] = end_of_month
        if ind_pricing_02gb1109 is not UNSET:
            field_dict["ind_pricing_02gb1109"] = ind_pricing_02gb1109
        if ind_pricing_02gb1203 is not UNSET:
            field_dict["ind_pricing_02gb1203"] = ind_pricing_02gb1203
        if ind_pricing_02gb1209 is not UNSET:
            field_dict["ind_pricing_02gb1209"] = ind_pricing_02gb1209
        if ind_pricing_02gb1303 is not UNSET:
            field_dict["ind_pricing_02gb1303"] = ind_pricing_02gb1303
        if ind_pricing_02gb1309 is not UNSET:
            field_dict["ind_pricing_02gb1309"] = ind_pricing_02gb1309
        if ind_pricing_02gb1403 is not UNSET:
            field_dict["ind_pricing_02gb1403"] = ind_pricing_02gb1403
        if ind_pricing_05gb1411 is not UNSET:
            field_dict["ind_pricing_05gb1411"] = ind_pricing_05gb1411
        if ind_pricing_03gb1505 is not UNSET:
            field_dict["ind_pricing_03gb1505"] = ind_pricing_03gb1505
        if ind_pricing_05gb1512 is not UNSET:
            field_dict["ind_pricing_05gb1512"] = ind_pricing_05gb1512
        if ind_pricing_03gb1605 is not UNSET:
            field_dict["ind_pricing_03gb1605"] = ind_pricing_03gb1605
        if ind_pricing_05gb1612 is not UNSET:
            field_dict["ind_pricing_05gb1612"] = ind_pricing_05gb1612
        if ind_pricing_03gb1704 is not UNSET:
            field_dict["ind_pricing_03gb1704"] = ind_pricing_03gb1704
        if ind_pricing_03gb1711 is not UNSET:
            field_dict["ind_pricing_03gb1711"] = ind_pricing_03gb1711
        if ind_pricing_05gb1802 is not UNSET:
            field_dict["ind_pricing_05gb1802"] = ind_pricing_05gb1802
        if ind_pricing_05gb1902 is not UNSET:
            field_dict["ind_pricing_05gb1902"] = ind_pricing_05gb1902
        if closing_ref_rate_02gb1109 is not UNSET:
            field_dict["closing_ref_rate_02gb1109"] = closing_ref_rate_02gb1109
        if closing_ref_rate_02gb1203 is not UNSET:
            field_dict["closing_ref_rate_02gb1203"] = closing_ref_rate_02gb1203
        if closing_ref_rate_02gb1209 is not UNSET:
            field_dict["closing_ref_rate_02gb1209"] = closing_ref_rate_02gb1209
        if closing_ref_rate_02gb1303 is not UNSET:
            field_dict["closing_ref_rate_02gb1303"] = closing_ref_rate_02gb1303
        if closing_ref_rate_02gb1309 is not UNSET:
            field_dict["closing_ref_rate_02gb1309"] = closing_ref_rate_02gb1309
        if closing_ref_rate_02gb1403 is not UNSET:
            field_dict["closing_ref_rate_02gb1403"] = closing_ref_rate_02gb1403
        if closing_ref_rate_05gb1411 is not UNSET:
            field_dict["closing_ref_rate_05gb1411"] = closing_ref_rate_05gb1411
        if closing_ref_rate_03gb1505 is not UNSET:
            field_dict["closing_ref_rate_03gb1505"] = closing_ref_rate_03gb1505
        if closing_ref_rate_05gb1512 is not UNSET:
            field_dict["closing_ref_rate_05gb1512"] = closing_ref_rate_05gb1512
        if closing_ref_rate_03gb1605 is not UNSET:
            field_dict["closing_ref_rate_03gb1605"] = closing_ref_rate_03gb1605
        if closing_ref_rate_05gb1612 is not UNSET:
            field_dict["closing_ref_rate_05gb1612"] = closing_ref_rate_05gb1612
        if closing_ref_rate_03gb1704 is not UNSET:
            field_dict["closing_ref_rate_03gb1704"] = closing_ref_rate_03gb1704
        if closing_ref_rate_03gb1711 is not UNSET:
            field_dict["closing_ref_rate_03gb1711"] = closing_ref_rate_03gb1711
        if closing_ref_rate_05gb1802 is not UNSET:
            field_dict["closing_ref_rate_05gb1802"] = closing_ref_rate_05gb1802
        if closing_ref_rate_05gb1902 is not UNSET:
            field_dict["closing_ref_rate_05gb1902"] = closing_ref_rate_05gb1902

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

        ind_pricing_02gb1109 = d.pop("ind_pricing_02gb1109", UNSET)

        ind_pricing_02gb1203 = d.pop("ind_pricing_02gb1203", UNSET)

        ind_pricing_02gb1209 = d.pop("ind_pricing_02gb1209", UNSET)

        ind_pricing_02gb1303 = d.pop("ind_pricing_02gb1303", UNSET)

        ind_pricing_02gb1309 = d.pop("ind_pricing_02gb1309", UNSET)

        ind_pricing_02gb1403 = d.pop("ind_pricing_02gb1403", UNSET)

        ind_pricing_05gb1411 = d.pop("ind_pricing_05gb1411", UNSET)

        ind_pricing_03gb1505 = d.pop("ind_pricing_03gb1505", UNSET)

        ind_pricing_05gb1512 = d.pop("ind_pricing_05gb1512", UNSET)

        ind_pricing_03gb1605 = d.pop("ind_pricing_03gb1605", UNSET)

        ind_pricing_05gb1612 = d.pop("ind_pricing_05gb1612", UNSET)

        ind_pricing_03gb1704 = d.pop("ind_pricing_03gb1704", UNSET)

        ind_pricing_03gb1711 = d.pop("ind_pricing_03gb1711", UNSET)

        ind_pricing_05gb1802 = d.pop("ind_pricing_05gb1802", UNSET)

        ind_pricing_05gb1902 = d.pop("ind_pricing_05gb1902", UNSET)

        closing_ref_rate_02gb1109 = d.pop("closing_ref_rate_02gb1109", UNSET)

        closing_ref_rate_02gb1203 = d.pop("closing_ref_rate_02gb1203", UNSET)

        closing_ref_rate_02gb1209 = d.pop("closing_ref_rate_02gb1209", UNSET)

        closing_ref_rate_02gb1303 = d.pop("closing_ref_rate_02gb1303", UNSET)

        closing_ref_rate_02gb1309 = d.pop("closing_ref_rate_02gb1309", UNSET)

        closing_ref_rate_02gb1403 = d.pop("closing_ref_rate_02gb1403", UNSET)

        closing_ref_rate_05gb1411 = d.pop("closing_ref_rate_05gb1411", UNSET)

        closing_ref_rate_03gb1505 = d.pop("closing_ref_rate_03gb1505", UNSET)

        closing_ref_rate_05gb1512 = d.pop("closing_ref_rate_05gb1512", UNSET)

        closing_ref_rate_03gb1605 = d.pop("closing_ref_rate_03gb1605", UNSET)

        closing_ref_rate_05gb1612 = d.pop("closing_ref_rate_05gb1612", UNSET)

        closing_ref_rate_03gb1704 = d.pop("closing_ref_rate_03gb1704", UNSET)

        closing_ref_rate_03gb1711 = d.pop("closing_ref_rate_03gb1711", UNSET)

        closing_ref_rate_05gb1802 = d.pop("closing_ref_rate_05gb1802", UNSET)

        closing_ref_rate_05gb1902 = d.pop("closing_ref_rate_05gb1902", UNSET)

        matured = cls(
            end_of_month=end_of_month,
            ind_pricing_02gb1109=ind_pricing_02gb1109,
            ind_pricing_02gb1203=ind_pricing_02gb1203,
            ind_pricing_02gb1209=ind_pricing_02gb1209,
            ind_pricing_02gb1303=ind_pricing_02gb1303,
            ind_pricing_02gb1309=ind_pricing_02gb1309,
            ind_pricing_02gb1403=ind_pricing_02gb1403,
            ind_pricing_05gb1411=ind_pricing_05gb1411,
            ind_pricing_03gb1505=ind_pricing_03gb1505,
            ind_pricing_05gb1512=ind_pricing_05gb1512,
            ind_pricing_03gb1605=ind_pricing_03gb1605,
            ind_pricing_05gb1612=ind_pricing_05gb1612,
            ind_pricing_03gb1704=ind_pricing_03gb1704,
            ind_pricing_03gb1711=ind_pricing_03gb1711,
            ind_pricing_05gb1802=ind_pricing_05gb1802,
            ind_pricing_05gb1902=ind_pricing_05gb1902,
            closing_ref_rate_02gb1109=closing_ref_rate_02gb1109,
            closing_ref_rate_02gb1203=closing_ref_rate_02gb1203,
            closing_ref_rate_02gb1209=closing_ref_rate_02gb1209,
            closing_ref_rate_02gb1303=closing_ref_rate_02gb1303,
            closing_ref_rate_02gb1309=closing_ref_rate_02gb1309,
            closing_ref_rate_02gb1403=closing_ref_rate_02gb1403,
            closing_ref_rate_05gb1411=closing_ref_rate_05gb1411,
            closing_ref_rate_03gb1505=closing_ref_rate_03gb1505,
            closing_ref_rate_05gb1512=closing_ref_rate_05gb1512,
            closing_ref_rate_03gb1605=closing_ref_rate_03gb1605,
            closing_ref_rate_05gb1612=closing_ref_rate_05gb1612,
            closing_ref_rate_03gb1704=closing_ref_rate_03gb1704,
            closing_ref_rate_03gb1711=closing_ref_rate_03gb1711,
            closing_ref_rate_05gb1802=closing_ref_rate_05gb1802,
            closing_ref_rate_05gb1902=closing_ref_rate_05gb1902,
        )

        matured.additional_properties = d
        return matured

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
