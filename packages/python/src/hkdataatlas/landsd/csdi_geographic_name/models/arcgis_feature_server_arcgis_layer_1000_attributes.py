from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer1000Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer1000Attributes:
    """
    Attributes:
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        place_name_id (int | Unset): Publisher field type: esriFieldTypeInteger
        geo_name_id (str | Unset): Publisher field type: esriFieldTypeString
        name_en (None | str | Unset): Publisher field type: esriFieldTypeString
        name_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        name_status (str | Unset): Publisher field type: esriFieldTypeString
    """

    objectid: int | Unset = UNSET
    place_name_id: int | Unset = UNSET
    geo_name_id: str | Unset = UNSET
    name_en: None | str | Unset = UNSET
    name_tc: None | str | Unset = UNSET
    name_status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        place_name_id = self.place_name_id

        geo_name_id = self.geo_name_id

        name_en: None | str | Unset
        if isinstance(self.name_en, Unset):
            name_en = UNSET
        else:
            name_en = self.name_en

        name_tc: None | str | Unset
        if isinstance(self.name_tc, Unset):
            name_tc = UNSET
        else:
            name_tc = self.name_tc

        name_status = self.name_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if place_name_id is not UNSET:
            field_dict["PLACE_NAME_ID"] = place_name_id
        if geo_name_id is not UNSET:
            field_dict["GEO_NAME_ID"] = geo_name_id
        if name_en is not UNSET:
            field_dict["NAME_EN"] = name_en
        if name_tc is not UNSET:
            field_dict["NAME_TC"] = name_tc
        if name_status is not UNSET:
            field_dict["NAME_STATUS"] = name_status

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        place_name_id = d.pop("PLACE_NAME_ID", UNSET)

        geo_name_id = d.pop("GEO_NAME_ID", UNSET)

        def _parse_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_en = _parse_name_en(d.pop("NAME_EN", UNSET))

        def _parse_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_tc = _parse_name_tc(d.pop("NAME_TC", UNSET))

        name_status = d.pop("NAME_STATUS", UNSET)

        arcgis_feature_server_arcgis_layer_1000_attributes = cls(
            objectid=objectid,
            place_name_id=place_name_id,
            geo_name_id=geo_name_id,
            name_en=name_en,
            name_tc=name_tc,
            name_status=name_status,
        )

        arcgis_feature_server_arcgis_layer_1000_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_1000_attributes

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
