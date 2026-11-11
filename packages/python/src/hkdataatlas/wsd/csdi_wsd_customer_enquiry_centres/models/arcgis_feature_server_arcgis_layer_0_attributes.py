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
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        name_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        name_chi (None | str | Unset): Publisher field type: esriFieldTypeString
        address_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        address_chi (None | str | Unset): Publisher field type: esriFieldTypeString
        off_hrs_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        off_hrs_chi (None | str | Unset): Publisher field type: esriFieldTypeString
    """

    objectid: int | Unset = UNSET
    name_eng: None | str | Unset = UNSET
    name_chi: None | str | Unset = UNSET
    address_eng: None | str | Unset = UNSET
    address_chi: None | str | Unset = UNSET
    off_hrs_eng: None | str | Unset = UNSET
    off_hrs_chi: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        name_eng: None | str | Unset
        if isinstance(self.name_eng, Unset):
            name_eng = UNSET
        else:
            name_eng = self.name_eng

        name_chi: None | str | Unset
        if isinstance(self.name_chi, Unset):
            name_chi = UNSET
        else:
            name_chi = self.name_chi

        address_eng: None | str | Unset
        if isinstance(self.address_eng, Unset):
            address_eng = UNSET
        else:
            address_eng = self.address_eng

        address_chi: None | str | Unset
        if isinstance(self.address_chi, Unset):
            address_chi = UNSET
        else:
            address_chi = self.address_chi

        off_hrs_eng: None | str | Unset
        if isinstance(self.off_hrs_eng, Unset):
            off_hrs_eng = UNSET
        else:
            off_hrs_eng = self.off_hrs_eng

        off_hrs_chi: None | str | Unset
        if isinstance(self.off_hrs_chi, Unset):
            off_hrs_chi = UNSET
        else:
            off_hrs_chi = self.off_hrs_chi

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if name_eng is not UNSET:
            field_dict["NAME_ENG"] = name_eng
        if name_chi is not UNSET:
            field_dict["NAME_CHI"] = name_chi
        if address_eng is not UNSET:
            field_dict["ADDRESS_ENG"] = address_eng
        if address_chi is not UNSET:
            field_dict["ADDRESS_CHI"] = address_chi
        if off_hrs_eng is not UNSET:
            field_dict["OFF_HRS_ENG"] = off_hrs_eng
        if off_hrs_chi is not UNSET:
            field_dict["OFF_HRS_CHI"] = off_hrs_chi

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_name_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_eng = _parse_name_eng(d.pop("NAME_ENG", UNSET))

        def _parse_name_chi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_chi = _parse_name_chi(d.pop("NAME_CHI", UNSET))

        def _parse_address_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_eng = _parse_address_eng(d.pop("ADDRESS_ENG", UNSET))

        def _parse_address_chi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_chi = _parse_address_chi(d.pop("ADDRESS_CHI", UNSET))

        def _parse_off_hrs_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        off_hrs_eng = _parse_off_hrs_eng(d.pop("OFF_HRS_ENG", UNSET))

        def _parse_off_hrs_chi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        off_hrs_chi = _parse_off_hrs_chi(d.pop("OFF_HRS_CHI", UNSET))

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            objectid=objectid,
            name_eng=name_eng,
            name_chi=name_chi,
            address_eng=address_eng,
            address_chi=address_chi,
            off_hrs_eng=off_hrs_eng,
            off_hrs_chi=off_hrs_chi,
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
