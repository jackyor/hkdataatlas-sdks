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
        coordinate_easting (None | str | Unset): Publisher field type: esriFieldTypeString
        coordinate_northing (None | str | Unset): Publisher field type: esriFieldTypeString
        site_en (None | str | Unset): Publisher field type: esriFieldTypeString
        site_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        site_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        stage_en (None | str | Unset): Publisher field type: esriFieldTypeString
        stage_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        stage_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        status_en (None | str | Unset): Publisher field type: esriFieldTypeString
        status_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        status_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        estimated_flat_number_about (None | str | Unset): Publisher field type: esriFieldTypeString
        land_area_in_ha (None | str | Unset): Publisher field type: esriFieldTypeString
        estimated_land_availability_year_en (None | str | Unset): Publisher field type: esriFieldTypeString
        estimated_land_availability_year_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        estimated_land_availability_year_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    coordinate_easting: None | str | Unset = UNSET
    coordinate_northing: None | str | Unset = UNSET
    site_en: None | str | Unset = UNSET
    site_sc: None | str | Unset = UNSET
    site_tc: None | str | Unset = UNSET
    stage_en: None | str | Unset = UNSET
    stage_sc: None | str | Unset = UNSET
    stage_tc: None | str | Unset = UNSET
    status_en: None | str | Unset = UNSET
    status_sc: None | str | Unset = UNSET
    status_tc: None | str | Unset = UNSET
    estimated_flat_number_about: None | str | Unset = UNSET
    land_area_in_ha: None | str | Unset = UNSET
    estimated_land_availability_year_en: None | str | Unset = UNSET
    estimated_land_availability_year_sc: None | str | Unset = UNSET
    estimated_land_availability_year_tc: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        coordinate_easting: None | str | Unset
        if isinstance(self.coordinate_easting, Unset):
            coordinate_easting = UNSET
        else:
            coordinate_easting = self.coordinate_easting

        coordinate_northing: None | str | Unset
        if isinstance(self.coordinate_northing, Unset):
            coordinate_northing = UNSET
        else:
            coordinate_northing = self.coordinate_northing

        site_en: None | str | Unset
        if isinstance(self.site_en, Unset):
            site_en = UNSET
        else:
            site_en = self.site_en

        site_sc: None | str | Unset
        if isinstance(self.site_sc, Unset):
            site_sc = UNSET
        else:
            site_sc = self.site_sc

        site_tc: None | str | Unset
        if isinstance(self.site_tc, Unset):
            site_tc = UNSET
        else:
            site_tc = self.site_tc

        stage_en: None | str | Unset
        if isinstance(self.stage_en, Unset):
            stage_en = UNSET
        else:
            stage_en = self.stage_en

        stage_sc: None | str | Unset
        if isinstance(self.stage_sc, Unset):
            stage_sc = UNSET
        else:
            stage_sc = self.stage_sc

        stage_tc: None | str | Unset
        if isinstance(self.stage_tc, Unset):
            stage_tc = UNSET
        else:
            stage_tc = self.stage_tc

        status_en: None | str | Unset
        if isinstance(self.status_en, Unset):
            status_en = UNSET
        else:
            status_en = self.status_en

        status_sc: None | str | Unset
        if isinstance(self.status_sc, Unset):
            status_sc = UNSET
        else:
            status_sc = self.status_sc

        status_tc: None | str | Unset
        if isinstance(self.status_tc, Unset):
            status_tc = UNSET
        else:
            status_tc = self.status_tc

        estimated_flat_number_about: None | str | Unset
        if isinstance(self.estimated_flat_number_about, Unset):
            estimated_flat_number_about = UNSET
        else:
            estimated_flat_number_about = self.estimated_flat_number_about

        land_area_in_ha: None | str | Unset
        if isinstance(self.land_area_in_ha, Unset):
            land_area_in_ha = UNSET
        else:
            land_area_in_ha = self.land_area_in_ha

        estimated_land_availability_year_en: None | str | Unset
        if isinstance(self.estimated_land_availability_year_en, Unset):
            estimated_land_availability_year_en = UNSET
        else:
            estimated_land_availability_year_en = (
                self.estimated_land_availability_year_en
            )

        estimated_land_availability_year_sc: None | str | Unset
        if isinstance(self.estimated_land_availability_year_sc, Unset):
            estimated_land_availability_year_sc = UNSET
        else:
            estimated_land_availability_year_sc = (
                self.estimated_land_availability_year_sc
            )

        estimated_land_availability_year_tc: None | str | Unset
        if isinstance(self.estimated_land_availability_year_tc, Unset):
            estimated_land_availability_year_tc = UNSET
        else:
            estimated_land_availability_year_tc = (
                self.estimated_land_availability_year_tc
            )

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if coordinate_easting is not UNSET:
            field_dict["Coordinate_Easting"] = coordinate_easting
        if coordinate_northing is not UNSET:
            field_dict["Coordinate_Northing"] = coordinate_northing
        if site_en is not UNSET:
            field_dict["Site_en"] = site_en
        if site_sc is not UNSET:
            field_dict["Site_sc"] = site_sc
        if site_tc is not UNSET:
            field_dict["Site_tc"] = site_tc
        if stage_en is not UNSET:
            field_dict["Stage_en"] = stage_en
        if stage_sc is not UNSET:
            field_dict["Stage_sc"] = stage_sc
        if stage_tc is not UNSET:
            field_dict["Stage_tc"] = stage_tc
        if status_en is not UNSET:
            field_dict["Status_en"] = status_en
        if status_sc is not UNSET:
            field_dict["Status_sc"] = status_sc
        if status_tc is not UNSET:
            field_dict["Status_tc"] = status_tc
        if estimated_flat_number_about is not UNSET:
            field_dict["Estimated_Flat_Number_About"] = estimated_flat_number_about
        if land_area_in_ha is not UNSET:
            field_dict["Land_Area_in_ha"] = land_area_in_ha
        if estimated_land_availability_year_en is not UNSET:
            field_dict["Estimated_Land_Availability_Year_en"] = (
                estimated_land_availability_year_en
            )
        if estimated_land_availability_year_sc is not UNSET:
            field_dict["Estimated_Land_Availability_Year_sc"] = (
                estimated_land_availability_year_sc
            )
        if estimated_land_availability_year_tc is not UNSET:
            field_dict["Estimated_Land_Availability_Year_tc"] = (
                estimated_land_availability_year_tc
            )
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_coordinate_easting(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        coordinate_easting = _parse_coordinate_easting(
            d.pop("Coordinate_Easting", UNSET)
        )

        def _parse_coordinate_northing(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        coordinate_northing = _parse_coordinate_northing(
            d.pop("Coordinate_Northing", UNSET)
        )

        def _parse_site_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        site_en = _parse_site_en(d.pop("Site_en", UNSET))

        def _parse_site_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        site_sc = _parse_site_sc(d.pop("Site_sc", UNSET))

        def _parse_site_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        site_tc = _parse_site_tc(d.pop("Site_tc", UNSET))

        def _parse_stage_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stage_en = _parse_stage_en(d.pop("Stage_en", UNSET))

        def _parse_stage_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stage_sc = _parse_stage_sc(d.pop("Stage_sc", UNSET))

        def _parse_stage_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stage_tc = _parse_stage_tc(d.pop("Stage_tc", UNSET))

        def _parse_status_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status_en = _parse_status_en(d.pop("Status_en", UNSET))

        def _parse_status_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status_sc = _parse_status_sc(d.pop("Status_sc", UNSET))

        def _parse_status_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status_tc = _parse_status_tc(d.pop("Status_tc", UNSET))

        def _parse_estimated_flat_number_about(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        estimated_flat_number_about = _parse_estimated_flat_number_about(
            d.pop("Estimated_Flat_Number_About", UNSET)
        )

        def _parse_land_area_in_ha(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        land_area_in_ha = _parse_land_area_in_ha(d.pop("Land_Area_in_ha", UNSET))

        def _parse_estimated_land_availability_year_en(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        estimated_land_availability_year_en = (
            _parse_estimated_land_availability_year_en(
                d.pop("Estimated_Land_Availability_Year_en", UNSET)
            )
        )

        def _parse_estimated_land_availability_year_sc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        estimated_land_availability_year_sc = (
            _parse_estimated_land_availability_year_sc(
                d.pop("Estimated_Land_Availability_Year_sc", UNSET)
            )
        )

        def _parse_estimated_land_availability_year_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        estimated_land_availability_year_tc = (
            _parse_estimated_land_availability_year_tc(
                d.pop("Estimated_Land_Availability_Year_tc", UNSET)
            )
        )

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            coordinate_easting=coordinate_easting,
            coordinate_northing=coordinate_northing,
            site_en=site_en,
            site_sc=site_sc,
            site_tc=site_tc,
            stage_en=stage_en,
            stage_sc=stage_sc,
            stage_tc=stage_tc,
            status_en=status_en,
            status_sc=status_sc,
            status_tc=status_tc,
            estimated_flat_number_about=estimated_flat_number_about,
            land_area_in_ha=land_area_in_ha,
            estimated_land_availability_year_en=estimated_land_availability_year_en,
            estimated_land_availability_year_sc=estimated_land_availability_year_sc,
            estimated_land_availability_year_tc=estimated_land_availability_year_tc,
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
