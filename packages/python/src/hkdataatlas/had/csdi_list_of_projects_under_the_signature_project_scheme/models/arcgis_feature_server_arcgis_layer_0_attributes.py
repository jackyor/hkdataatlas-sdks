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
        project_chin (None | str | Unset): Publisher field type: esriFieldTypeString
        district_chin (None | str | Unset): Publisher field type: esriFieldTypeString
        project_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        district_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    project_chin: None | str | Unset = UNSET
    district_chin: None | str | Unset = UNSET
    project_eng: None | str | Unset = UNSET
    district_eng: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_chin: None | str | Unset
        if isinstance(self.project_chin, Unset):
            project_chin = UNSET
        else:
            project_chin = self.project_chin

        district_chin: None | str | Unset
        if isinstance(self.district_chin, Unset):
            district_chin = UNSET
        else:
            district_chin = self.district_chin

        project_eng: None | str | Unset
        if isinstance(self.project_eng, Unset):
            project_eng = UNSET
        else:
            project_eng = self.project_eng

        district_eng: None | str | Unset
        if isinstance(self.district_eng, Unset):
            district_eng = UNSET
        else:
            district_eng = self.district_eng

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if project_chin is not UNSET:
            field_dict["Project__Chin_"] = project_chin
        if district_chin is not UNSET:
            field_dict["District__Chin_"] = district_chin
        if project_eng is not UNSET:
            field_dict["Project__Eng_"] = project_eng
        if district_eng is not UNSET:
            field_dict["District__Eng_"] = district_eng
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_project_chin(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_chin = _parse_project_chin(d.pop("Project__Chin_", UNSET))

        def _parse_district_chin(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_chin = _parse_district_chin(d.pop("District__Chin_", UNSET))

        def _parse_project_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_eng = _parse_project_eng(d.pop("Project__Eng_", UNSET))

        def _parse_district_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_eng = _parse_district_eng(d.pop("District__Eng_", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            project_chin=project_chin,
            district_chin=district_chin,
            project_eng=project_eng,
            district_eng=district_eng,
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
