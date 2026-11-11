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
        facility_name_en (None | str | Unset): Publisher field type: esriFieldTypeString
        facility_name_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        remark_en (None | str | Unset): Publisher field type: esriFieldTypeString
        remark_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        service_hour_en (None | str | Unset): Publisher field type: esriFieldTypeString
        service_hour_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    facility_name_en: None | str | Unset = UNSET
    facility_name_tc: None | str | Unset = UNSET
    remark_en: None | str | Unset = UNSET
    remark_tc: None | str | Unset = UNSET
    service_hour_en: None | str | Unset = UNSET
    service_hour_tc: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        facility_name_en: None | str | Unset
        if isinstance(self.facility_name_en, Unset):
            facility_name_en = UNSET
        else:
            facility_name_en = self.facility_name_en

        facility_name_tc: None | str | Unset
        if isinstance(self.facility_name_tc, Unset):
            facility_name_tc = UNSET
        else:
            facility_name_tc = self.facility_name_tc

        remark_en: None | str | Unset
        if isinstance(self.remark_en, Unset):
            remark_en = UNSET
        else:
            remark_en = self.remark_en

        remark_tc: None | str | Unset
        if isinstance(self.remark_tc, Unset):
            remark_tc = UNSET
        else:
            remark_tc = self.remark_tc

        service_hour_en: None | str | Unset
        if isinstance(self.service_hour_en, Unset):
            service_hour_en = UNSET
        else:
            service_hour_en = self.service_hour_en

        service_hour_tc: None | str | Unset
        if isinstance(self.service_hour_tc, Unset):
            service_hour_tc = UNSET
        else:
            service_hour_tc = self.service_hour_tc

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if facility_name_en is not UNSET:
            field_dict["FACILITY_NAME_EN"] = facility_name_en
        if facility_name_tc is not UNSET:
            field_dict["FACILITY_NAME_TC"] = facility_name_tc
        if remark_en is not UNSET:
            field_dict["REMARK_EN"] = remark_en
        if remark_tc is not UNSET:
            field_dict["REMARK_TC"] = remark_tc
        if service_hour_en is not UNSET:
            field_dict["SERVICE_HOUR_EN"] = service_hour_en
        if service_hour_tc is not UNSET:
            field_dict["SERVICE_HOUR_TC"] = service_hour_tc
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_facility_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        facility_name_en = _parse_facility_name_en(d.pop("FACILITY_NAME_EN", UNSET))

        def _parse_facility_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        facility_name_tc = _parse_facility_name_tc(d.pop("FACILITY_NAME_TC", UNSET))

        def _parse_remark_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remark_en = _parse_remark_en(d.pop("REMARK_EN", UNSET))

        def _parse_remark_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remark_tc = _parse_remark_tc(d.pop("REMARK_TC", UNSET))

        def _parse_service_hour_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        service_hour_en = _parse_service_hour_en(d.pop("SERVICE_HOUR_EN", UNSET))

        def _parse_service_hour_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        service_hour_tc = _parse_service_hour_tc(d.pop("SERVICE_HOUR_TC", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            facility_name_en=facility_name_en,
            facility_name_tc=facility_name_tc,
            remark_en=remark_en,
            remark_tc=remark_tc,
            service_hour_en=service_hour_en,
            service_hour_tc=service_hour_tc,
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
