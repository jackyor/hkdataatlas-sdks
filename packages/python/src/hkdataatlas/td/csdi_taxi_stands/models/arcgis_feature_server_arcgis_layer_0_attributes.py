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
        region_en (None | str | Unset): Publisher field type: esriFieldTypeString
        region_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        region_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        district_en (None | str | Unset): Publisher field type: esriFieldTypeString
        district_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        district_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        location_en (None | str | Unset): Publisher field type: esriFieldTypeString
        location_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        location_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        status_en (None | str | Unset): Publisher field type: esriFieldTypeString
        status_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        status_sc (None | str | Unset): Publisher field type: esriFieldTypeString
    """

    objectid: int | Unset = UNSET
    region_en: None | str | Unset = UNSET
    region_tc: None | str | Unset = UNSET
    region_sc: None | str | Unset = UNSET
    district_en: None | str | Unset = UNSET
    district_tc: None | str | Unset = UNSET
    district_sc: None | str | Unset = UNSET
    location_en: None | str | Unset = UNSET
    location_tc: None | str | Unset = UNSET
    location_sc: None | str | Unset = UNSET
    status_en: None | str | Unset = UNSET
    status_tc: None | str | Unset = UNSET
    status_sc: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        region_en: None | str | Unset
        if isinstance(self.region_en, Unset):
            region_en = UNSET
        else:
            region_en = self.region_en

        region_tc: None | str | Unset
        if isinstance(self.region_tc, Unset):
            region_tc = UNSET
        else:
            region_tc = self.region_tc

        region_sc: None | str | Unset
        if isinstance(self.region_sc, Unset):
            region_sc = UNSET
        else:
            region_sc = self.region_sc

        district_en: None | str | Unset
        if isinstance(self.district_en, Unset):
            district_en = UNSET
        else:
            district_en = self.district_en

        district_tc: None | str | Unset
        if isinstance(self.district_tc, Unset):
            district_tc = UNSET
        else:
            district_tc = self.district_tc

        district_sc: None | str | Unset
        if isinstance(self.district_sc, Unset):
            district_sc = UNSET
        else:
            district_sc = self.district_sc

        location_en: None | str | Unset
        if isinstance(self.location_en, Unset):
            location_en = UNSET
        else:
            location_en = self.location_en

        location_tc: None | str | Unset
        if isinstance(self.location_tc, Unset):
            location_tc = UNSET
        else:
            location_tc = self.location_tc

        location_sc: None | str | Unset
        if isinstance(self.location_sc, Unset):
            location_sc = UNSET
        else:
            location_sc = self.location_sc

        status_en: None | str | Unset
        if isinstance(self.status_en, Unset):
            status_en = UNSET
        else:
            status_en = self.status_en

        status_tc: None | str | Unset
        if isinstance(self.status_tc, Unset):
            status_tc = UNSET
        else:
            status_tc = self.status_tc

        status_sc: None | str | Unset
        if isinstance(self.status_sc, Unset):
            status_sc = UNSET
        else:
            status_sc = self.status_sc

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if region_en is not UNSET:
            field_dict["Region_EN"] = region_en
        if region_tc is not UNSET:
            field_dict["Region_TC"] = region_tc
        if region_sc is not UNSET:
            field_dict["Region_SC"] = region_sc
        if district_en is not UNSET:
            field_dict["District_EN"] = district_en
        if district_tc is not UNSET:
            field_dict["District_TC"] = district_tc
        if district_sc is not UNSET:
            field_dict["District_SC"] = district_sc
        if location_en is not UNSET:
            field_dict["Location_EN"] = location_en
        if location_tc is not UNSET:
            field_dict["Location_TC"] = location_tc
        if location_sc is not UNSET:
            field_dict["Location_SC"] = location_sc
        if status_en is not UNSET:
            field_dict["Status_EN"] = status_en
        if status_tc is not UNSET:
            field_dict["Status_TC"] = status_tc
        if status_sc is not UNSET:
            field_dict["Status_SC"] = status_sc

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_region_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_en = _parse_region_en(d.pop("Region_EN", UNSET))

        def _parse_region_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_tc = _parse_region_tc(d.pop("Region_TC", UNSET))

        def _parse_region_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_sc = _parse_region_sc(d.pop("Region_SC", UNSET))

        def _parse_district_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_en = _parse_district_en(d.pop("District_EN", UNSET))

        def _parse_district_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_tc = _parse_district_tc(d.pop("District_TC", UNSET))

        def _parse_district_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_sc = _parse_district_sc(d.pop("District_SC", UNSET))

        def _parse_location_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_en = _parse_location_en(d.pop("Location_EN", UNSET))

        def _parse_location_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_tc = _parse_location_tc(d.pop("Location_TC", UNSET))

        def _parse_location_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_sc = _parse_location_sc(d.pop("Location_SC", UNSET))

        def _parse_status_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status_en = _parse_status_en(d.pop("Status_EN", UNSET))

        def _parse_status_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status_tc = _parse_status_tc(d.pop("Status_TC", UNSET))

        def _parse_status_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status_sc = _parse_status_sc(d.pop("Status_SC", UNSET))

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            objectid=objectid,
            region_en=region_en,
            region_tc=region_tc,
            region_sc=region_sc,
            district_en=district_en,
            district_tc=district_tc,
            district_sc=district_sc,
            location_en=location_en,
            location_tc=location_tc,
            location_sc=location_sc,
            status_en=status_en,
            status_tc=status_tc,
            status_sc=status_sc,
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
