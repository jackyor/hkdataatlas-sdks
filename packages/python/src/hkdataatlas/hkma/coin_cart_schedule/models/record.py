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
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):
        cart_no (float | Unset):
        district (str | Unset):
        address (str | Unset):
        latitude (float | Unset):
        longitude (float | Unset):
        remarks (float | Unset):
    """

    start_date: datetime.date | Unset = UNSET
    end_date: datetime.date | Unset = UNSET
    cart_no: float | Unset = UNSET
    district: str | Unset = UNSET
    address: str | Unset = UNSET
    latitude: float | Unset = UNSET
    longitude: float | Unset = UNSET
    remarks: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start_date: str | Unset = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        end_date: str | Unset = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        cart_no = self.cart_no

        district = self.district

        address = self.address

        latitude = self.latitude

        longitude = self.longitude

        remarks = self.remarks

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if cart_no is not UNSET:
            field_dict["cart_no"] = cart_no
        if district is not UNSET:
            field_dict["district"] = district
        if address is not UNSET:
            field_dict["address"] = address
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if remarks is not UNSET:
            field_dict["remarks"] = remarks

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _start_date = d.pop("start_date", UNSET)
        start_date: datetime.date | Unset
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = datetime.date.fromisoformat(_start_date)

        _end_date = d.pop("end_date", UNSET)
        end_date: datetime.date | Unset
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = datetime.date.fromisoformat(_end_date)

        cart_no = d.pop("cart_no", UNSET)

        district = d.pop("district", UNSET)

        address = d.pop("address", UNSET)

        latitude = d.pop("latitude", UNSET)

        longitude = d.pop("longitude", UNSET)

        remarks = d.pop("remarks", UNSET)

        record = cls(
            start_date=start_date,
            end_date=end_date,
            cart_no=cart_no,
            district=district,
            address=address,
            latitude=latitude,
            longitude=longitude,
            remarks=remarks,
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
