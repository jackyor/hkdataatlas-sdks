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
        venue_id (None | str | Unset): Publisher field type: esriFieldTypeString
        venue_eng_name (None | str | Unset): Publisher field type: esriFieldTypeString
        venue_chi_name (None | str | Unset): Publisher field type: esriFieldTypeString
        building_eng_name (None | str | Unset): Publisher field type: esriFieldTypeString
        building_chi_name (None | str | Unset): Publisher field type: esriFieldTypeString
        a_eng_name (None | str | Unset): Publisher field type: esriFieldTypeString
        a_chi_name (None | str | Unset): Publisher field type: esriFieldTypeString
        type_ (None | str | Unset): Publisher field type: esriFieldTypeString
        shapefile (None | str | Unset): Publisher field type: esriFieldTypeString
        geo_json (None | str | Unset): Publisher field type: esriFieldTypeString
        revisiondate (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains unknown.
        remarks (None | str | Unset): Publisher field type: esriFieldTypeString
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
        shape_area (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    objectid: int | Unset = UNSET
    venue_id: None | str | Unset = UNSET
    venue_eng_name: None | str | Unset = UNSET
    venue_chi_name: None | str | Unset = UNSET
    building_eng_name: None | str | Unset = UNSET
    building_chi_name: None | str | Unset = UNSET
    a_eng_name: None | str | Unset = UNSET
    a_chi_name: None | str | Unset = UNSET
    type_: None | str | Unset = UNSET
    shapefile: None | str | Unset = UNSET
    geo_json: None | str | Unset = UNSET
    revisiondate: Any | Unset = UNSET
    remarks: None | str | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        venue_id: None | str | Unset
        if isinstance(self.venue_id, Unset):
            venue_id = UNSET
        else:
            venue_id = self.venue_id

        venue_eng_name: None | str | Unset
        if isinstance(self.venue_eng_name, Unset):
            venue_eng_name = UNSET
        else:
            venue_eng_name = self.venue_eng_name

        venue_chi_name: None | str | Unset
        if isinstance(self.venue_chi_name, Unset):
            venue_chi_name = UNSET
        else:
            venue_chi_name = self.venue_chi_name

        building_eng_name: None | str | Unset
        if isinstance(self.building_eng_name, Unset):
            building_eng_name = UNSET
        else:
            building_eng_name = self.building_eng_name

        building_chi_name: None | str | Unset
        if isinstance(self.building_chi_name, Unset):
            building_chi_name = UNSET
        else:
            building_chi_name = self.building_chi_name

        a_eng_name: None | str | Unset
        if isinstance(self.a_eng_name, Unset):
            a_eng_name = UNSET
        else:
            a_eng_name = self.a_eng_name

        a_chi_name: None | str | Unset
        if isinstance(self.a_chi_name, Unset):
            a_chi_name = UNSET
        else:
            a_chi_name = self.a_chi_name

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        shapefile: None | str | Unset
        if isinstance(self.shapefile, Unset):
            shapefile = UNSET
        else:
            shapefile = self.shapefile

        geo_json: None | str | Unset
        if isinstance(self.geo_json, Unset):
            geo_json = UNSET
        else:
            geo_json = self.geo_json

        revisiondate = self.revisiondate

        remarks: None | str | Unset
        if isinstance(self.remarks, Unset):
            remarks = UNSET
        else:
            remarks = self.remarks

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
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if venue_id is not UNSET:
            field_dict["Venue_ID"] = venue_id
        if venue_eng_name is not UNSET:
            field_dict["Venue_Eng_name"] = venue_eng_name
        if venue_chi_name is not UNSET:
            field_dict["Venue_Chi_name"] = venue_chi_name
        if building_eng_name is not UNSET:
            field_dict["Building_Eng_name"] = building_eng_name
        if building_chi_name is not UNSET:
            field_dict["Building_Chi_name"] = building_chi_name
        if a_eng_name is not UNSET:
            field_dict["A_Eng_name"] = a_eng_name
        if a_chi_name is not UNSET:
            field_dict["A_Chi_name"] = a_chi_name
        if type_ is not UNSET:
            field_dict["Type"] = type_
        if shapefile is not UNSET:
            field_dict["Shapefile"] = shapefile
        if geo_json is not UNSET:
            field_dict["GeoJSON"] = geo_json
        if revisiondate is not UNSET:
            field_dict["REVISIONDATE"] = revisiondate
        if remarks is not UNSET:
            field_dict["REMARKS"] = remarks
        if shape_length is not UNSET:
            field_dict["Shape__Length"] = shape_length
        if shape_area is not UNSET:
            field_dict["Shape__Area"] = shape_area

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_venue_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        venue_id = _parse_venue_id(d.pop("Venue_ID", UNSET))

        def _parse_venue_eng_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        venue_eng_name = _parse_venue_eng_name(d.pop("Venue_Eng_name", UNSET))

        def _parse_venue_chi_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        venue_chi_name = _parse_venue_chi_name(d.pop("Venue_Chi_name", UNSET))

        def _parse_building_eng_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        building_eng_name = _parse_building_eng_name(d.pop("Building_Eng_name", UNSET))

        def _parse_building_chi_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        building_chi_name = _parse_building_chi_name(d.pop("Building_Chi_name", UNSET))

        def _parse_a_eng_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        a_eng_name = _parse_a_eng_name(d.pop("A_Eng_name", UNSET))

        def _parse_a_chi_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        a_chi_name = _parse_a_chi_name(d.pop("A_Chi_name", UNSET))

        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("Type", UNSET))

        def _parse_shapefile(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        shapefile = _parse_shapefile(d.pop("Shapefile", UNSET))

        def _parse_geo_json(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        geo_json = _parse_geo_json(d.pop("GeoJSON", UNSET))

        revisiondate = d.pop("REVISIONDATE", UNSET)

        def _parse_remarks(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remarks = _parse_remarks(d.pop("REMARKS", UNSET))

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
            objectid=objectid,
            venue_id=venue_id,
            venue_eng_name=venue_eng_name,
            venue_chi_name=venue_chi_name,
            building_eng_name=building_eng_name,
            building_chi_name=building_chi_name,
            a_eng_name=a_eng_name,
            a_chi_name=a_chi_name,
            type_=type_,
            shapefile=shapefile,
            geo_json=geo_json,
            revisiondate=revisiondate,
            remarks=remarks,
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
