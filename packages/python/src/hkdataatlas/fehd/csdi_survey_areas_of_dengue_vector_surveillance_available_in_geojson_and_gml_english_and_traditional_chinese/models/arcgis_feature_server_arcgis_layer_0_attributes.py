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
        ogr_fid (float | None | Unset): Publisher field type: esriFieldTypeDouble
        ops_area (None | str | Unset): Publisher field type: esriFieldTypeString
        ops_area_c (None | str | Unset): Publisher field type: esriFieldTypeString
        district (None | str | Unset): Publisher field type: esriFieldTypeString
        district_c (None | str | Unset): Publisher field type: esriFieldTypeString
        location (None | str | Unset): Publisher field type: esriFieldTypeString
        location_c (None | str | Unset): Publisher field type: esriFieldTypeString
        period (None | str | Unset): Publisher field type: esriFieldTypeString
        agi (float | None | Unset): Publisher field type: esriFieldTypeSingle
        adi (float | None | Unset): Publisher field type: esriFieldTypeSingle
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
        shape_area (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    ogr_fid: float | None | Unset = UNSET
    ops_area: None | str | Unset = UNSET
    ops_area_c: None | str | Unset = UNSET
    district: None | str | Unset = UNSET
    district_c: None | str | Unset = UNSET
    location: None | str | Unset = UNSET
    location_c: None | str | Unset = UNSET
    period: None | str | Unset = UNSET
    agi: float | None | Unset = UNSET
    adi: float | None | Unset = UNSET
    objectid: int | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ogr_fid: float | None | Unset
        if isinstance(self.ogr_fid, Unset):
            ogr_fid = UNSET
        else:
            ogr_fid = self.ogr_fid

        ops_area: None | str | Unset
        if isinstance(self.ops_area, Unset):
            ops_area = UNSET
        else:
            ops_area = self.ops_area

        ops_area_c: None | str | Unset
        if isinstance(self.ops_area_c, Unset):
            ops_area_c = UNSET
        else:
            ops_area_c = self.ops_area_c

        district: None | str | Unset
        if isinstance(self.district, Unset):
            district = UNSET
        else:
            district = self.district

        district_c: None | str | Unset
        if isinstance(self.district_c, Unset):
            district_c = UNSET
        else:
            district_c = self.district_c

        location: None | str | Unset
        if isinstance(self.location, Unset):
            location = UNSET
        else:
            location = self.location

        location_c: None | str | Unset
        if isinstance(self.location_c, Unset):
            location_c = UNSET
        else:
            location_c = self.location_c

        period: None | str | Unset
        if isinstance(self.period, Unset):
            period = UNSET
        else:
            period = self.period

        agi: float | None | Unset
        if isinstance(self.agi, Unset):
            agi = UNSET
        else:
            agi = self.agi

        adi: float | None | Unset
        if isinstance(self.adi, Unset):
            adi = UNSET
        else:
            adi = self.adi

        objectid = self.objectid

        shape_length: float | None | Unset
        if isinstance(self.shape_length, Unset):
            shape_length = UNSET
        else:
            shape_length = self.shape_length

        shape_area: float | None | Unset
        if isinstance(self.shape_area, Unset):
            shape_area = UNSET
        else:
            shape_area = self.shape_area

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ogr_fid is not UNSET:
            field_dict["OGR_FID"] = ogr_fid
        if ops_area is not UNSET:
            field_dict["OPS_AREA"] = ops_area
        if ops_area_c is not UNSET:
            field_dict["OPS_AREA_C"] = ops_area_c
        if district is not UNSET:
            field_dict["DISTRICT"] = district
        if district_c is not UNSET:
            field_dict["DISTRICT_C"] = district_c
        if location is not UNSET:
            field_dict["LOCATION"] = location
        if location_c is not UNSET:
            field_dict["LOCATION_C"] = location_c
        if period is not UNSET:
            field_dict["PERIOD"] = period
        if agi is not UNSET:
            field_dict["AGI"] = agi
        if adi is not UNSET:
            field_dict["ADI"] = adi
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape_length is not UNSET:
            field_dict["Shape__Length"] = shape_length
        if shape_area is not UNSET:
            field_dict["Shape__Area"] = shape_area

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_ogr_fid(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        ogr_fid = _parse_ogr_fid(d.pop("OGR_FID", UNSET))

        def _parse_ops_area(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ops_area = _parse_ops_area(d.pop("OPS_AREA", UNSET))

        def _parse_ops_area_c(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ops_area_c = _parse_ops_area_c(d.pop("OPS_AREA_C", UNSET))

        def _parse_district(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district = _parse_district(d.pop("DISTRICT", UNSET))

        def _parse_district_c(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_c = _parse_district_c(d.pop("DISTRICT_C", UNSET))

        def _parse_location(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location = _parse_location(d.pop("LOCATION", UNSET))

        def _parse_location_c(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_c = _parse_location_c(d.pop("LOCATION_C", UNSET))

        def _parse_period(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        period = _parse_period(d.pop("PERIOD", UNSET))

        def _parse_agi(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        agi = _parse_agi(d.pop("AGI", UNSET))

        def _parse_adi(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        adi = _parse_adi(d.pop("ADI", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        def _parse_shape_length(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_length = _parse_shape_length(d.pop("Shape__Length", UNSET))

        def _parse_shape_area(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_area = _parse_shape_area(d.pop("Shape__Area", UNSET))

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            ogr_fid=ogr_fid,
            ops_area=ops_area,
            ops_area_c=ops_area_c,
            district=district,
            district_c=district_c,
            location=location,
            location_c=location_c,
            period=period,
            agi=agi,
            adi=adi,
            objectid=objectid,
            shape_length=shape_length,
            shape_area=shape_area,
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
