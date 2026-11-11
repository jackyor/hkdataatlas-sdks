from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.meteorological_data_response_body import (
        MeteorologicalDataResponseBODY,
    )


T = TypeVar("T", bound="MeteorologicalDataResponse")


@_attrs_define
class MeteorologicalDataResponse:
    """Documented response fields for a successful data result. Fields and nesting are based on the data dictionary and the
    documented example; the source does not explicitly establish a complete or closed response contract.

        Example:
            {'BD': '00', 'BODY': {'HKO': {'DH': '12', 'RH': '71.7', 'T0': '33.5', 'TP': '20230913174049', 'TS':
                '20230913174049', 'VN': '1.0', 'WD': '143', 'WS': '4'}}, 'DI': '01', 'GI': '00', 'PI': 'GF3637', 'TS': '0'}

        Attributes:
            bd (str | Unset): Reserved for HKSARG Department Code under the Interoperability Framework (IF) for
                E-Government; currently not in use. Default value: "00". Default: '00'. Example: 00.
            body (MeteorologicalDataResponseBODY | Unset):
            di (str | Unset): Device ID. 2 characters. Example: 01.
            gi (str | Unset): Reserved for Branch/Division/Section code; currently not in use. Default value: "00". Default:
                '00'. Example: 00.
            pi (str | Unset): Lamppost ID. Maximum 8 characters. Example: GF3637.
            ts (str | Unset): Packet creation date and time, up to millisecond precision. Unix time stamp. Currently not in
                use; default value: "0". Default: '0'. Example: 0.
    """

    bd: str | Unset = "00"
    body: MeteorologicalDataResponseBODY | Unset = UNSET
    di: str | Unset = UNSET
    gi: str | Unset = "00"
    pi: str | Unset = UNSET
    ts: str | Unset = "0"
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
        from ..models.meteorological_data_response_body import (
            MeteorologicalDataResponseBODY,
        )

        d = dict(src_dict)
        bd = d.pop("BD", UNSET)

        _body = d.pop("BODY", UNSET)
        body: MeteorologicalDataResponseBODY | Unset
        if isinstance(_body, Unset):
            body = UNSET
        else:
            body = MeteorologicalDataResponseBODY.from_dict(_body)

        di = d.pop("DI", UNSET)

        gi = d.pop("GI", UNSET)

        pi = d.pop("PI", UNSET)

        ts = d.pop("TS", UNSET)

        meteorological_data_response = cls(
            bd=bd,
            body=body,
            di=di,
            gi=gi,
            pi=pi,
            ts=ts,
        )

        meteorological_data_response.additional_properties = d
        return meteorological_data_response

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
