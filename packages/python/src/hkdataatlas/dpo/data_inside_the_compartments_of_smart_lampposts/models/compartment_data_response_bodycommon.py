from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.compartment_measurements import CompartmentMeasurements


T = TypeVar("T", bound="CompartmentDataResponseBODYCOMMON")


@_attrs_define
class CompartmentDataResponseBODYCOMMON:
    """Internal Data Sensor measurements.

    Attributes:
        c1 (CompartmentMeasurements | Unset): Temperature and relative-humidity values for a compartment. The source
            documents string values; “////” indicates failure of quality control, and for compartments 3 and 4 “N.A.”
            indicates that the compartment does not exist.
        c2 (CompartmentMeasurements | Unset): Temperature and relative-humidity values for a compartment. The source
            documents string values; “////” indicates failure of quality control, and for compartments 3 and 4 “N.A.”
            indicates that the compartment does not exist.
        c3 (CompartmentMeasurements | Unset): Temperature and relative-humidity values for a compartment. The source
            documents string values; “////” indicates failure of quality control, and for compartments 3 and 4 “N.A.”
            indicates that the compartment does not exist.
        c4 (CompartmentMeasurements | Unset): Temperature and relative-humidity values for a compartment. The source
            documents string values; “////” indicates failure of quality control, and for compartments 3 and 4 “N.A.”
            indicates that the compartment does not exist.
        ts (str | Unset): Latest of the data measurement times of all compartments of a smart lamppost. Format
            YYYYMMDDHHMMSS (ISO 8601 notation, Hong Kong Time). Example: 20190506161726.
    """

    c1: CompartmentMeasurements | Unset = UNSET
    c2: CompartmentMeasurements | Unset = UNSET
    c3: CompartmentMeasurements | Unset = UNSET
    c4: CompartmentMeasurements | Unset = UNSET
    ts: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        c1: dict[str, Any] | Unset = UNSET
        if not isinstance(self.c1, Unset):
            c1 = self.c1.to_dict()

        c2: dict[str, Any] | Unset = UNSET
        if not isinstance(self.c2, Unset):
            c2 = self.c2.to_dict()

        c3: dict[str, Any] | Unset = UNSET
        if not isinstance(self.c3, Unset):
            c3 = self.c3.to_dict()

        c4: dict[str, Any] | Unset = UNSET
        if not isinstance(self.c4, Unset):
            c4 = self.c4.to_dict()

        ts = self.ts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if c1 is not UNSET:
            field_dict["C1"] = c1
        if c2 is not UNSET:
            field_dict["C2"] = c2
        if c3 is not UNSET:
            field_dict["C3"] = c3
        if c4 is not UNSET:
            field_dict["C4"] = c4
        if ts is not UNSET:
            field_dict["TS"] = ts

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.compartment_measurements import CompartmentMeasurements

        d = dict(src_dict)
        _c1 = d.pop("C1", UNSET)
        c1: CompartmentMeasurements | Unset
        if isinstance(_c1, Unset):
            c1 = UNSET
        else:
            c1 = CompartmentMeasurements.from_dict(_c1)

        _c2 = d.pop("C2", UNSET)
        c2: CompartmentMeasurements | Unset
        if isinstance(_c2, Unset):
            c2 = UNSET
        else:
            c2 = CompartmentMeasurements.from_dict(_c2)

        _c3 = d.pop("C3", UNSET)
        c3: CompartmentMeasurements | Unset
        if isinstance(_c3, Unset):
            c3 = UNSET
        else:
            c3 = CompartmentMeasurements.from_dict(_c3)

        _c4 = d.pop("C4", UNSET)
        c4: CompartmentMeasurements | Unset
        if isinstance(_c4, Unset):
            c4 = UNSET
        else:
            c4 = CompartmentMeasurements.from_dict(_c4)

        ts = d.pop("TS", UNSET)

        compartment_data_response_bodycommon = cls(
            c1=c1,
            c2=c2,
            c3=c3,
            c4=c4,
            ts=ts,
        )

        compartment_data_response_bodycommon.additional_properties = d
        return compartment_data_response_bodycommon

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
