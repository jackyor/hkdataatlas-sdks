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
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
        shape_area (float | None | Unset): Publisher field type: esriFieldTypeDouble
        licence_id (int | Unset): Publisher field type: esriFieldTypeInteger
        licence_number (str | Unset): Publisher field type: esriFieldTypeString
        district (str | Unset): Publisher field type: esriFieldTypeString
        district_licence_number (str | Unset): Publisher field type: esriFieldTypeString
        lbs_info (str | Unset): Publisher field type: esriFieldTypeString
    """

    objectid: int | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    licence_id: int | Unset = UNSET
    licence_number: str | Unset = UNSET
    district: str | Unset = UNSET
    district_licence_number: str | Unset = UNSET
    lbs_info: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        licence_id = self.licence_id

        licence_number = self.licence_number

        district = self.district

        district_licence_number = self.district_licence_number

        lbs_info = self.lbs_info

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape_length is not UNSET:
            field_dict["Shape__Length"] = shape_length
        if shape_area is not UNSET:
            field_dict["Shape__Area"] = shape_area
        if licence_id is not UNSET:
            field_dict["LicenceID"] = licence_id
        if licence_number is not UNSET:
            field_dict["LicenceNumber"] = licence_number
        if district is not UNSET:
            field_dict["District"] = district
        if district_licence_number is not UNSET:
            field_dict["DistrictLicenceNumber"] = district_licence_number
        if lbs_info is not UNSET:
            field_dict["LBSInfo"] = lbs_info

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
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

        licence_id = d.pop("LicenceID", UNSET)

        licence_number = d.pop("LicenceNumber", UNSET)

        district = d.pop("District", UNSET)

        district_licence_number = d.pop("DistrictLicenceNumber", UNSET)

        lbs_info = d.pop("LBSInfo", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            objectid=objectid,
            shape_length=shape_length,
            shape_area=shape_area,
            licence_id=licence_id,
            licence_number=licence_number,
            district=district,
            district_licence_number=district_licence_number,
            lbs_info=lbs_info,
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
