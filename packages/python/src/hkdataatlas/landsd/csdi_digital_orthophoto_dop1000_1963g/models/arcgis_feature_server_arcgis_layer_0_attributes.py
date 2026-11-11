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
        sheetno (str | Unset): Publisher field type: esriFieldTypeString
        date_of_photograph (str | Unset): Publisher field type: esriFieldTypeString
        download_link_grid_version (str | Unset): Publisher field type: esriFieldTypeString
        download_link_plain_image_version (str | Unset): Publisher field type: esriFieldTypeString
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
        shape_area (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    objectid: int | Unset = UNSET
    sheetno: str | Unset = UNSET
    date_of_photograph: str | Unset = UNSET
    download_link_grid_version: str | Unset = UNSET
    download_link_plain_image_version: str | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        sheetno = self.sheetno

        date_of_photograph = self.date_of_photograph

        download_link_grid_version = self.download_link_grid_version

        download_link_plain_image_version = self.download_link_plain_image_version

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
        if sheetno is not UNSET:
            field_dict["SHEETNO"] = sheetno
        if date_of_photograph is not UNSET:
            field_dict["DATE_OF_PHOTOGRAPH"] = date_of_photograph
        if download_link_grid_version is not UNSET:
            field_dict["DOWNLOAD_LINK_GRID_VERSION"] = download_link_grid_version
        if download_link_plain_image_version is not UNSET:
            field_dict["DOWNLOAD_LINK_PLAIN_IMAGE_VERSION"] = (
                download_link_plain_image_version
            )
        if shape_length is not UNSET:
            field_dict["Shape__Length"] = shape_length
        if shape_area is not UNSET:
            field_dict["Shape__Area"] = shape_area

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        sheetno = d.pop("SHEETNO", UNSET)

        date_of_photograph = d.pop("DATE_OF_PHOTOGRAPH", UNSET)

        download_link_grid_version = d.pop("DOWNLOAD_LINK_GRID_VERSION", UNSET)

        download_link_plain_image_version = d.pop(
            "DOWNLOAD_LINK_PLAIN_IMAGE_VERSION", UNSET
        )

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
            sheetno=sheetno,
            date_of_photograph=date_of_photograph,
            download_link_grid_version=download_link_grid_version,
            download_link_plain_image_version=download_link_plain_image_version,
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
