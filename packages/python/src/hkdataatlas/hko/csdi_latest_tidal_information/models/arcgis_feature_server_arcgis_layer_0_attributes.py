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
        data_url (None | str | Unset): Publisher field type: esriFieldTypeString
        tide_station_en (None | str | Unset): Publisher field type: esriFieldTypeString
        tide_station_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        tide_station_uc (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    data_url: None | str | Unset = UNSET
    tide_station_en: None | str | Unset = UNSET
    tide_station_sc: None | str | Unset = UNSET
    tide_station_uc: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data_url: None | str | Unset
        if isinstance(self.data_url, Unset):
            data_url = UNSET
        else:
            data_url = self.data_url

        tide_station_en: None | str | Unset
        if isinstance(self.tide_station_en, Unset):
            tide_station_en = UNSET
        else:
            tide_station_en = self.tide_station_en

        tide_station_sc: None | str | Unset
        if isinstance(self.tide_station_sc, Unset):
            tide_station_sc = UNSET
        else:
            tide_station_sc = self.tide_station_sc

        tide_station_uc: None | str | Unset
        if isinstance(self.tide_station_uc, Unset):
            tide_station_uc = UNSET
        else:
            tide_station_uc = self.tide_station_uc

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data_url is not UNSET:
            field_dict["Data_url"] = data_url
        if tide_station_en is not UNSET:
            field_dict["TideStation_en"] = tide_station_en
        if tide_station_sc is not UNSET:
            field_dict["TideStation_sc"] = tide_station_sc
        if tide_station_uc is not UNSET:
            field_dict["TideStation_uc"] = tide_station_uc
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_data_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        data_url = _parse_data_url(d.pop("Data_url", UNSET))

        def _parse_tide_station_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tide_station_en = _parse_tide_station_en(d.pop("TideStation_en", UNSET))

        def _parse_tide_station_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tide_station_sc = _parse_tide_station_sc(d.pop("TideStation_sc", UNSET))

        def _parse_tide_station_uc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tide_station_uc = _parse_tide_station_uc(d.pop("TideStation_uc", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            data_url=data_url,
            tide_station_en=tide_station_en,
            tide_station_sc=tide_station_sc,
            tide_station_uc=tide_station_uc,
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
