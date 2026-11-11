from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer0Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer0Attributes:
    """
    Attributes:
        en_address (None | str | Unset): Publisher field type: esriFieldTypeString
        en_remarks (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_address (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_remarks (None | str | Unset): Publisher field type: esriFieldTypeString
        tc_address (None | str | Unset): Publisher field type: esriFieldTypeString
        tc_remarks (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    en_address: None | str | Unset = UNSET
    en_remarks: None | str | Unset = UNSET
    sc_address: None | str | Unset = UNSET
    sc_remarks: None | str | Unset = UNSET
    tc_address: None | str | Unset = UNSET
    tc_remarks: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        en_address: None | str | Unset
        if isinstance(self.en_address, Unset):
            en_address = UNSET
        else:
            en_address = self.en_address

        en_remarks: None | str | Unset
        if isinstance(self.en_remarks, Unset):
            en_remarks = UNSET
        else:
            en_remarks = self.en_remarks

        sc_address: None | str | Unset
        if isinstance(self.sc_address, Unset):
            sc_address = UNSET
        else:
            sc_address = self.sc_address

        sc_remarks: None | str | Unset
        if isinstance(self.sc_remarks, Unset):
            sc_remarks = UNSET
        else:
            sc_remarks = self.sc_remarks

        tc_address: None | str | Unset
        if isinstance(self.tc_address, Unset):
            tc_address = UNSET
        else:
            tc_address = self.tc_address

        tc_remarks: None | str | Unset
        if isinstance(self.tc_remarks, Unset):
            tc_remarks = UNSET
        else:
            tc_remarks = self.tc_remarks

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if en_address is not UNSET:
            field_dict["en_address"] = en_address
        if en_remarks is not UNSET:
            field_dict["en_remarks"] = en_remarks
        if sc_address is not UNSET:
            field_dict["sc_address"] = sc_address
        if sc_remarks is not UNSET:
            field_dict["sc_remarks"] = sc_remarks
        if tc_address is not UNSET:
            field_dict["tc_address"] = tc_address
        if tc_remarks is not UNSET:
            field_dict["tc_remarks"] = tc_remarks
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_en_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        en_address = _parse_en_address(d.pop("en_address", UNSET))

        def _parse_en_remarks(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        en_remarks = _parse_en_remarks(d.pop("en_remarks", UNSET))

        def _parse_sc_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_address = _parse_sc_address(d.pop("sc_address", UNSET))

        def _parse_sc_remarks(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_remarks = _parse_sc_remarks(d.pop("sc_remarks", UNSET))

        def _parse_tc_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tc_address = _parse_tc_address(d.pop("tc_address", UNSET))

        def _parse_tc_remarks(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tc_remarks = _parse_tc_remarks(d.pop("tc_remarks", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            en_address=en_address,
            en_remarks=en_remarks,
            sc_address=sc_address,
            sc_remarks=sc_remarks,
            tc_address=tc_address,
            tc_remarks=tc_remarks,
            objectid=objectid,
        )

        arcgis_feature_server_arcgis_layer_0_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_0_attributes

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
