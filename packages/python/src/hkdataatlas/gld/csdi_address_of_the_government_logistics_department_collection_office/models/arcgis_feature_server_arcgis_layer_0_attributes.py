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
        en_name (None | str | Unset): Publisher field type: esriFieldTypeString
        en_opening_hr (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_address (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_name (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_opening_hr (None | str | Unset): Publisher field type: esriFieldTypeString
        tc_address (None | str | Unset): Publisher field type: esriFieldTypeString
        tc_name (None | str | Unset): Publisher field type: esriFieldTypeString
        tc_opening_hr (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    en_address: None | str | Unset = UNSET
    en_name: None | str | Unset = UNSET
    en_opening_hr: None | str | Unset = UNSET
    sc_address: None | str | Unset = UNSET
    sc_name: None | str | Unset = UNSET
    sc_opening_hr: None | str | Unset = UNSET
    tc_address: None | str | Unset = UNSET
    tc_name: None | str | Unset = UNSET
    tc_opening_hr: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        en_address: None | str | Unset
        if isinstance(self.en_address, Unset):
            en_address = UNSET
        else:
            en_address = self.en_address

        en_name: None | str | Unset
        if isinstance(self.en_name, Unset):
            en_name = UNSET
        else:
            en_name = self.en_name

        en_opening_hr: None | str | Unset
        if isinstance(self.en_opening_hr, Unset):
            en_opening_hr = UNSET
        else:
            en_opening_hr = self.en_opening_hr

        sc_address: None | str | Unset
        if isinstance(self.sc_address, Unset):
            sc_address = UNSET
        else:
            sc_address = self.sc_address

        sc_name: None | str | Unset
        if isinstance(self.sc_name, Unset):
            sc_name = UNSET
        else:
            sc_name = self.sc_name

        sc_opening_hr: None | str | Unset
        if isinstance(self.sc_opening_hr, Unset):
            sc_opening_hr = UNSET
        else:
            sc_opening_hr = self.sc_opening_hr

        tc_address: None | str | Unset
        if isinstance(self.tc_address, Unset):
            tc_address = UNSET
        else:
            tc_address = self.tc_address

        tc_name: None | str | Unset
        if isinstance(self.tc_name, Unset):
            tc_name = UNSET
        else:
            tc_name = self.tc_name

        tc_opening_hr: None | str | Unset
        if isinstance(self.tc_opening_hr, Unset):
            tc_opening_hr = UNSET
        else:
            tc_opening_hr = self.tc_opening_hr

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if en_address is not UNSET:
            field_dict["EN_ADDRESS"] = en_address
        if en_name is not UNSET:
            field_dict["EN_NAME"] = en_name
        if en_opening_hr is not UNSET:
            field_dict["EN_OPENING_HR"] = en_opening_hr
        if sc_address is not UNSET:
            field_dict["SC_ADDRESS"] = sc_address
        if sc_name is not UNSET:
            field_dict["SC_NAME"] = sc_name
        if sc_opening_hr is not UNSET:
            field_dict["SC_OPENING_HR"] = sc_opening_hr
        if tc_address is not UNSET:
            field_dict["TC_ADDRESS"] = tc_address
        if tc_name is not UNSET:
            field_dict["TC_NAME"] = tc_name
        if tc_opening_hr is not UNSET:
            field_dict["TC_OPENING_HR"] = tc_opening_hr
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

        en_address = _parse_en_address(d.pop("EN_ADDRESS", UNSET))

        def _parse_en_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        en_name = _parse_en_name(d.pop("EN_NAME", UNSET))

        def _parse_en_opening_hr(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        en_opening_hr = _parse_en_opening_hr(d.pop("EN_OPENING_HR", UNSET))

        def _parse_sc_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_address = _parse_sc_address(d.pop("SC_ADDRESS", UNSET))

        def _parse_sc_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_name = _parse_sc_name(d.pop("SC_NAME", UNSET))

        def _parse_sc_opening_hr(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_opening_hr = _parse_sc_opening_hr(d.pop("SC_OPENING_HR", UNSET))

        def _parse_tc_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tc_address = _parse_tc_address(d.pop("TC_ADDRESS", UNSET))

        def _parse_tc_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tc_name = _parse_tc_name(d.pop("TC_NAME", UNSET))

        def _parse_tc_opening_hr(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tc_opening_hr = _parse_tc_opening_hr(d.pop("TC_OPENING_HR", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            en_address=en_address,
            en_name=en_name,
            en_opening_hr=en_opening_hr,
            sc_address=sc_address,
            sc_name=sc_name,
            sc_opening_hr=sc_opening_hr,
            tc_address=tc_address,
            tc_name=tc_name,
            tc_opening_hr=tc_opening_hr,
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
