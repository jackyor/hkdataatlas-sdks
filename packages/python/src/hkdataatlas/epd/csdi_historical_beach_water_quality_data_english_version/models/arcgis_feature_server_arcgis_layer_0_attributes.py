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
        beach_name (None | str | Unset): Publisher field type: esriFieldTypeString
        beach_name_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        beach_name_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        district (None | str | Unset): Publisher field type: esriFieldTypeString
        sampling_date_dd_mm_yyyy (None | str | Unset): Publisher field type: esriFieldTypeString
        e_coli_count_per_100_m_l_on_the_sampling_date (None | str | Unset): Publisher field type: esriFieldTypeString
        easting (None | str | Unset): Publisher field type: esriFieldTypeString
        northing (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    beach_name: None | str | Unset = UNSET
    beach_name_tc: None | str | Unset = UNSET
    beach_name_sc: None | str | Unset = UNSET
    district: None | str | Unset = UNSET
    sampling_date_dd_mm_yyyy: None | str | Unset = UNSET
    e_coli_count_per_100_m_l_on_the_sampling_date: None | str | Unset = UNSET
    easting: None | str | Unset = UNSET
    northing: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        beach_name: None | str | Unset
        if isinstance(self.beach_name, Unset):
            beach_name = UNSET
        else:
            beach_name = self.beach_name

        beach_name_tc: None | str | Unset
        if isinstance(self.beach_name_tc, Unset):
            beach_name_tc = UNSET
        else:
            beach_name_tc = self.beach_name_tc

        beach_name_sc: None | str | Unset
        if isinstance(self.beach_name_sc, Unset):
            beach_name_sc = UNSET
        else:
            beach_name_sc = self.beach_name_sc

        district: None | str | Unset
        if isinstance(self.district, Unset):
            district = UNSET
        else:
            district = self.district

        sampling_date_dd_mm_yyyy: None | str | Unset
        if isinstance(self.sampling_date_dd_mm_yyyy, Unset):
            sampling_date_dd_mm_yyyy = UNSET
        else:
            sampling_date_dd_mm_yyyy = self.sampling_date_dd_mm_yyyy

        e_coli_count_per_100_m_l_on_the_sampling_date: None | str | Unset
        if isinstance(self.e_coli_count_per_100_m_l_on_the_sampling_date, Unset):
            e_coli_count_per_100_m_l_on_the_sampling_date = UNSET
        else:
            e_coli_count_per_100_m_l_on_the_sampling_date = (
                self.e_coli_count_per_100_m_l_on_the_sampling_date
            )

        easting: None | str | Unset
        if isinstance(self.easting, Unset):
            easting = UNSET
        else:
            easting = self.easting

        northing: None | str | Unset
        if isinstance(self.northing, Unset):
            northing = UNSET
        else:
            northing = self.northing

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if beach_name is not UNSET:
            field_dict["Beach_Name"] = beach_name
        if beach_name_tc is not UNSET:
            field_dict["Beach_Name__TC_"] = beach_name_tc
        if beach_name_sc is not UNSET:
            field_dict["Beach_Name__SC_"] = beach_name_sc
        if district is not UNSET:
            field_dict["District"] = district
        if sampling_date_dd_mm_yyyy is not UNSET:
            field_dict["Sampling_Date__DD_MM_YYYY_"] = sampling_date_dd_mm_yyyy
        if e_coli_count_per_100_m_l_on_the_sampling_date is not UNSET:
            field_dict["E__coli_count_per_100mL_on_the_sampling_date"] = (
                e_coli_count_per_100_m_l_on_the_sampling_date
            )
        if easting is not UNSET:
            field_dict["Easting"] = easting
        if northing is not UNSET:
            field_dict["Northing"] = northing
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_beach_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        beach_name = _parse_beach_name(d.pop("Beach_Name", UNSET))

        def _parse_beach_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        beach_name_tc = _parse_beach_name_tc(d.pop("Beach_Name__TC_", UNSET))

        def _parse_beach_name_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        beach_name_sc = _parse_beach_name_sc(d.pop("Beach_Name__SC_", UNSET))

        def _parse_district(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district = _parse_district(d.pop("District", UNSET))

        def _parse_sampling_date_dd_mm_yyyy(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sampling_date_dd_mm_yyyy = _parse_sampling_date_dd_mm_yyyy(
            d.pop("Sampling_Date__DD_MM_YYYY_", UNSET)
        )

        def _parse_e_coli_count_per_100_m_l_on_the_sampling_date(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        e_coli_count_per_100_m_l_on_the_sampling_date = (
            _parse_e_coli_count_per_100_m_l_on_the_sampling_date(
                d.pop("E__coli_count_per_100mL_on_the_sampling_date", UNSET)
            )
        )

        def _parse_easting(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        easting = _parse_easting(d.pop("Easting", UNSET))

        def _parse_northing(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        northing = _parse_northing(d.pop("Northing", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            beach_name=beach_name,
            beach_name_tc=beach_name_tc,
            beach_name_sc=beach_name_sc,
            district=district,
            sampling_date_dd_mm_yyyy=sampling_date_dd_mm_yyyy,
            e_coli_count_per_100_m_l_on_the_sampling_date=e_coli_count_per_100_m_l_on_the_sampling_date,
            easting=easting,
            northing=northing,
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
