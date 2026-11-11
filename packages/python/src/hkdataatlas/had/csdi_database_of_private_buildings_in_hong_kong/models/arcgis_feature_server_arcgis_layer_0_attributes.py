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
        addr_of_building_in_chn (None | str | Unset): Publisher field type: esriFieldTypeString
        addr_of_building_in_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        name_of_ocomm_in_chn (None | str | Unset): Publisher field type: esriFieldTypeString
        name_of_ocomm_in_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    addr_of_building_in_chn: None | str | Unset = UNSET
    addr_of_building_in_eng: None | str | Unset = UNSET
    name_of_ocomm_in_chn: None | str | Unset = UNSET
    name_of_ocomm_in_eng: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        addr_of_building_in_chn: None | str | Unset
        if isinstance(self.addr_of_building_in_chn, Unset):
            addr_of_building_in_chn = UNSET
        else:
            addr_of_building_in_chn = self.addr_of_building_in_chn

        addr_of_building_in_eng: None | str | Unset
        if isinstance(self.addr_of_building_in_eng, Unset):
            addr_of_building_in_eng = UNSET
        else:
            addr_of_building_in_eng = self.addr_of_building_in_eng

        name_of_ocomm_in_chn: None | str | Unset
        if isinstance(self.name_of_ocomm_in_chn, Unset):
            name_of_ocomm_in_chn = UNSET
        else:
            name_of_ocomm_in_chn = self.name_of_ocomm_in_chn

        name_of_ocomm_in_eng: None | str | Unset
        if isinstance(self.name_of_ocomm_in_eng, Unset):
            name_of_ocomm_in_eng = UNSET
        else:
            name_of_ocomm_in_eng = self.name_of_ocomm_in_eng

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if addr_of_building_in_chn is not UNSET:
            field_dict["ADDR_OF_BUILDING_IN_CHN"] = addr_of_building_in_chn
        if addr_of_building_in_eng is not UNSET:
            field_dict["ADDR_OF_BUILDING_IN_ENG"] = addr_of_building_in_eng
        if name_of_ocomm_in_chn is not UNSET:
            field_dict["NAME_OF_OCOMM_IN_CHN"] = name_of_ocomm_in_chn
        if name_of_ocomm_in_eng is not UNSET:
            field_dict["NAME_OF_OCOMM_IN_ENG"] = name_of_ocomm_in_eng
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_addr_of_building_in_chn(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        addr_of_building_in_chn = _parse_addr_of_building_in_chn(
            d.pop("ADDR_OF_BUILDING_IN_CHN", UNSET)
        )

        def _parse_addr_of_building_in_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        addr_of_building_in_eng = _parse_addr_of_building_in_eng(
            d.pop("ADDR_OF_BUILDING_IN_ENG", UNSET)
        )

        def _parse_name_of_ocomm_in_chn(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_of_ocomm_in_chn = _parse_name_of_ocomm_in_chn(
            d.pop("NAME_OF_OCOMM_IN_CHN", UNSET)
        )

        def _parse_name_of_ocomm_in_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_of_ocomm_in_eng = _parse_name_of_ocomm_in_eng(
            d.pop("NAME_OF_OCOMM_IN_ENG", UNSET)
        )

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            addr_of_building_in_chn=addr_of_building_in_chn,
            addr_of_building_in_eng=addr_of_building_in_eng,
            name_of_ocomm_in_chn=name_of_ocomm_in_chn,
            name_of_ocomm_in_eng=name_of_ocomm_in_eng,
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
