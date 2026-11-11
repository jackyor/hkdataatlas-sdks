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
        address (None | str | Unset): Publisher field type: esriFieldTypeString
        bldg_engnm (None | str | Unset): Publisher field type: esriFieldTypeString
        bldg_chtnm (None | str | Unset): Publisher field type: esriFieldTypeString
        os_type (str | Unset): Publisher field type: esriFieldTypeString
        os_status (str | Unset): Publisher field type: esriFieldTypeString
        beach (str | Unset): Publisher field type: esriFieldTypeString
        amenity_area (str | Unset): Publisher field type: esriFieldTypeString
        indoor_facilities (str | Unset): Publisher field type: esriFieldTypeString
        completion_year (int | None | Unset): Publisher field type: esriFieldTypeInteger
        last_update (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains unknown.
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
        shape_area (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    objectid: int | Unset = UNSET
    address: None | str | Unset = UNSET
    bldg_engnm: None | str | Unset = UNSET
    bldg_chtnm: None | str | Unset = UNSET
    os_type: str | Unset = UNSET
    os_status: str | Unset = UNSET
    beach: str | Unset = UNSET
    amenity_area: str | Unset = UNSET
    indoor_facilities: str | Unset = UNSET
    completion_year: int | None | Unset = UNSET
    last_update: Any | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        address: None | str | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        bldg_engnm: None | str | Unset
        if isinstance(self.bldg_engnm, Unset):
            bldg_engnm = UNSET
        else:
            bldg_engnm = self.bldg_engnm

        bldg_chtnm: None | str | Unset
        if isinstance(self.bldg_chtnm, Unset):
            bldg_chtnm = UNSET
        else:
            bldg_chtnm = self.bldg_chtnm

        os_type = self.os_type

        os_status = self.os_status

        beach = self.beach

        amenity_area = self.amenity_area

        indoor_facilities = self.indoor_facilities

        completion_year: int | None | Unset
        if isinstance(self.completion_year, Unset):
            completion_year = UNSET
        else:
            completion_year = self.completion_year

        last_update = self.last_update

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
        if address is not UNSET:
            field_dict["ADDRESS"] = address
        if bldg_engnm is not UNSET:
            field_dict["BLDG_ENGNM"] = bldg_engnm
        if bldg_chtnm is not UNSET:
            field_dict["BLDG_CHTNM"] = bldg_chtnm
        if os_type is not UNSET:
            field_dict["OS_TYPE"] = os_type
        if os_status is not UNSET:
            field_dict["OS_STATUS"] = os_status
        if beach is not UNSET:
            field_dict["BEACH"] = beach
        if amenity_area is not UNSET:
            field_dict["AMENITY_AREA"] = amenity_area
        if indoor_facilities is not UNSET:
            field_dict["INDOOR_FACILITIES"] = indoor_facilities
        if completion_year is not UNSET:
            field_dict["COMPLETION_YEAR"] = completion_year
        if last_update is not UNSET:
            field_dict["LAST_UPDATE"] = last_update
        if shape_length is not UNSET:
            field_dict["Shape__Length"] = shape_length
        if shape_area is not UNSET:
            field_dict["Shape__Area"] = shape_area

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address = _parse_address(d.pop("ADDRESS", UNSET))

        def _parse_bldg_engnm(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bldg_engnm = _parse_bldg_engnm(d.pop("BLDG_ENGNM", UNSET))

        def _parse_bldg_chtnm(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bldg_chtnm = _parse_bldg_chtnm(d.pop("BLDG_CHTNM", UNSET))

        os_type = d.pop("OS_TYPE", UNSET)

        os_status = d.pop("OS_STATUS", UNSET)

        beach = d.pop("BEACH", UNSET)

        amenity_area = d.pop("AMENITY_AREA", UNSET)

        indoor_facilities = d.pop("INDOOR_FACILITIES", UNSET)

        def _parse_completion_year(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        completion_year = _parse_completion_year(d.pop("COMPLETION_YEAR", UNSET))

        last_update = d.pop("LAST_UPDATE", UNSET)

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
            address=address,
            bldg_engnm=bldg_engnm,
            bldg_chtnm=bldg_chtnm,
            os_type=os_type,
            os_status=os_status,
            beach=beach,
            amenity_area=amenity_area,
            indoor_facilities=indoor_facilities,
            completion_year=completion_year,
            last_update=last_update,
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
