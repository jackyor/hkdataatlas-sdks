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
        fac_id (None | str | Unset): Publisher field type: esriFieldTypeString
        barrier_free_fac (None | str | Unset): Publisher field type: esriFieldTypeString
        type_en (None | str | Unset): Publisher field type: esriFieldTypeString
        type_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        country_park_en (None | str | Unset): Publisher field type: esriFieldTypeString
        country_park_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        facility_name_en (None | str | Unset): Publisher field type: esriFieldTypeString
        facility_name_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    fac_id: None | str | Unset = UNSET
    barrier_free_fac: None | str | Unset = UNSET
    type_en: None | str | Unset = UNSET
    type_tc: None | str | Unset = UNSET
    country_park_en: None | str | Unset = UNSET
    country_park_tc: None | str | Unset = UNSET
    facility_name_en: None | str | Unset = UNSET
    facility_name_tc: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fac_id: None | str | Unset
        if isinstance(self.fac_id, Unset):
            fac_id = UNSET
        else:
            fac_id = self.fac_id

        barrier_free_fac: None | str | Unset
        if isinstance(self.barrier_free_fac, Unset):
            barrier_free_fac = UNSET
        else:
            barrier_free_fac = self.barrier_free_fac

        type_en: None | str | Unset
        if isinstance(self.type_en, Unset):
            type_en = UNSET
        else:
            type_en = self.type_en

        type_tc: None | str | Unset
        if isinstance(self.type_tc, Unset):
            type_tc = UNSET
        else:
            type_tc = self.type_tc

        country_park_en: None | str | Unset
        if isinstance(self.country_park_en, Unset):
            country_park_en = UNSET
        else:
            country_park_en = self.country_park_en

        country_park_tc: None | str | Unset
        if isinstance(self.country_park_tc, Unset):
            country_park_tc = UNSET
        else:
            country_park_tc = self.country_park_tc

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

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fac_id is not UNSET:
            field_dict["FAC_ID"] = fac_id
        if barrier_free_fac is not UNSET:
            field_dict["BARRIER_FREE_FAC"] = barrier_free_fac
        if type_en is not UNSET:
            field_dict["TYPE_EN"] = type_en
        if type_tc is not UNSET:
            field_dict["TYPE_TC"] = type_tc
        if country_park_en is not UNSET:
            field_dict["COUNTRY_PARK_EN"] = country_park_en
        if country_park_tc is not UNSET:
            field_dict["COUNTRY_PARK_TC"] = country_park_tc
        if facility_name_en is not UNSET:
            field_dict["FACILITY_NAME_EN"] = facility_name_en
        if facility_name_tc is not UNSET:
            field_dict["FACILITY_NAME_TC"] = facility_name_tc
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_fac_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fac_id = _parse_fac_id(d.pop("FAC_ID", UNSET))

        def _parse_barrier_free_fac(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        barrier_free_fac = _parse_barrier_free_fac(d.pop("BARRIER_FREE_FAC", UNSET))

        def _parse_type_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_en = _parse_type_en(d.pop("TYPE_EN", UNSET))

        def _parse_type_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_tc = _parse_type_tc(d.pop("TYPE_TC", UNSET))

        def _parse_country_park_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country_park_en = _parse_country_park_en(d.pop("COUNTRY_PARK_EN", UNSET))

        def _parse_country_park_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country_park_tc = _parse_country_park_tc(d.pop("COUNTRY_PARK_TC", UNSET))

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

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            fac_id=fac_id,
            barrier_free_fac=barrier_free_fac,
            type_en=type_en,
            type_tc=type_tc,
            country_park_en=country_park_en,
            country_park_tc=country_park_tc,
            facility_name_en=facility_name_en,
            facility_name_tc=facility_name_tc,
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
