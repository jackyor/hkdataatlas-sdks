from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.compartment_data_response_body import CompartmentDataResponseBODY


T = TypeVar("T", bound="CompartmentDataResponse")


@_attrs_define
class CompartmentDataResponse:
    """Example response structure. The source defines the fields in the data dictionary, but does not state that every
    field is required in every response.

        Example:
            {'BD': 'COMMON', 'BODY': {'COMMON': {'C1': {'RH': '73.5', 'T0': '34.5'}, 'C2': {'RH': '74.3', 'T0': '34.8'},
                'C3': {'RH': '73.8', 'T0': '34.8'}, 'C4': {'RH': '75.0', 'T0': '34.6'}, 'TS': '20220919163357'}}, 'DI': '10',
                'GI': '00', 'PI': 'DF3647', 'TS': '1562748177518'}

        Attributes:
            bd (str | Unset): HKSAR Government Bureau/Department Code. The data dictionary identifies the value as a string
                and says it is always “COMMON” for the Internal Data Sensor. Example: COMMON.
            body (CompartmentDataResponseBODY | Unset):
            di (str | Unset): Device ID. The data dictionary identifies the value as a string, with format 2 characters and
                value “10” for the Internal Data Sensor. Example: 10.
            gi (str | Unset): Branch/Division/Section code, reserved and currently not in use. The data dictionary
                identifies the value as a string with default value “00”. Example: 00.
            pi (str | Unset): Lamppost ID. The data dictionary identifies this as a string with a maximum of 8 characters.
                Example: DF3647.
            ts (str | Unset): Date and time when the JSON packet is created, up to millisecond. The data dictionary
                specifies a Unix time stamp and default value “0”. Example: 1562748177518.
    """

    bd: str | Unset = UNSET
    body: CompartmentDataResponseBODY | Unset = UNSET
    di: str | Unset = UNSET
    gi: str | Unset = UNSET
    pi: str | Unset = UNSET
    ts: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bd = self.bd

        body: dict[str, Any] | Unset = UNSET
        if not isinstance(self.body, Unset):
            body = self.body.to_dict()

        di = self.di

        gi = self.gi

        pi = self.pi

        ts = self.ts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bd is not UNSET:
            field_dict["BD"] = bd
        if body is not UNSET:
            field_dict["BODY"] = body
        if di is not UNSET:
            field_dict["DI"] = di
        if gi is not UNSET:
            field_dict["GI"] = gi
        if pi is not UNSET:
            field_dict["PI"] = pi
        if ts is not UNSET:
            field_dict["TS"] = ts

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.compartment_data_response_body import CompartmentDataResponseBODY

        d = dict(src_dict)
        bd = d.pop("BD", UNSET)

        _body = d.pop("BODY", UNSET)
        body: CompartmentDataResponseBODY | Unset
        if isinstance(_body, Unset):
            body = UNSET
        else:
            body = CompartmentDataResponseBODY.from_dict(_body)

        di = d.pop("DI", UNSET)

        gi = d.pop("GI", UNSET)

        pi = d.pop("PI", UNSET)

        ts = d.pop("TS", UNSET)

        compartment_data_response = cls(
            bd=bd,
            body=body,
            di=di,
            gi=gi,
            pi=pi,
            ts=ts,
        )

        compartment_data_response.additional_properties = d
        return compartment_data_response

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
