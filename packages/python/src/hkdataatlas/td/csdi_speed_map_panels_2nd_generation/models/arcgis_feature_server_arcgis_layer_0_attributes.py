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
        image_file_url (None | str | Unset): Publisher field type: esriFieldTypeString
        description (None | str | Unset): Publisher field type: esriFieldTypeString
        smp_location_easting_coordinate (float | None | Unset): Publisher field type: esriFieldTypeDouble
        smp_location_northing_coordinate (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    objectid: int | Unset = UNSET
    image_file_url: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    smp_location_easting_coordinate: float | None | Unset = UNSET
    smp_location_northing_coordinate: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        image_file_url: None | str | Unset
        if isinstance(self.image_file_url, Unset):
            image_file_url = UNSET
        else:
            image_file_url = self.image_file_url

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        smp_location_easting_coordinate: float | None | Unset
        if isinstance(self.smp_location_easting_coordinate, Unset):
            smp_location_easting_coordinate = UNSET
        else:
            smp_location_easting_coordinate = self.smp_location_easting_coordinate

        smp_location_northing_coordinate: float | None | Unset
        if isinstance(self.smp_location_northing_coordinate, Unset):
            smp_location_northing_coordinate = UNSET
        else:
            smp_location_northing_coordinate = self.smp_location_northing_coordinate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if image_file_url is not UNSET:
            field_dict["Image_File_URL"] = image_file_url
        if description is not UNSET:
            field_dict["Description"] = description
        if smp_location_easting_coordinate is not UNSET:
            field_dict["SMP_Location_Easting_Coordinate"] = (
                smp_location_easting_coordinate
            )
        if smp_location_northing_coordinate is not UNSET:
            field_dict["SMP_Location_Northing_Coordinate"] = (
                smp_location_northing_coordinate
            )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_image_file_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        image_file_url = _parse_image_file_url(d.pop("Image_File_URL", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("Description", UNSET))

        def _parse_smp_location_easting_coordinate(
            data: object,
        ) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        smp_location_easting_coordinate = _parse_smp_location_easting_coordinate(
            d.pop("SMP_Location_Easting_Coordinate", UNSET)
        )

        def _parse_smp_location_northing_coordinate(
            data: object,
        ) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        smp_location_northing_coordinate = _parse_smp_location_northing_coordinate(
            d.pop("SMP_Location_Northing_Coordinate", UNSET)
        )

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            objectid=objectid,
            image_file_url=image_file_url,
            description=description,
            smp_location_easting_coordinate=smp_location_easting_coordinate,
            smp_location_northing_coordinate=smp_location_northing_coordinate,
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
