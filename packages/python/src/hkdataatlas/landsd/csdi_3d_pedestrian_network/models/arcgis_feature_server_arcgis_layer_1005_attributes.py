from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer1005Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer1005Attributes:
    """
    Attributes:
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        access_time_id (int | Unset): Publisher field type: esriFieldTypeInteger
        access_time_type (str | Unset): Publisher field type: esriFieldTypeString
        description_tc (str | Unset): Publisher field type: esriFieldTypeString
        description_en (str | Unset): Publisher field type: esriFieldTypeString
        creation_date (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains unknown.
        modified_by (str | Unset): Publisher field type: esriFieldTypeString
        last_amendment_date (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains
            unknown.
    """

    objectid: int | Unset = UNSET
    access_time_id: int | Unset = UNSET
    access_time_type: str | Unset = UNSET
    description_tc: str | Unset = UNSET
    description_en: str | Unset = UNSET
    creation_date: Any | Unset = UNSET
    modified_by: str | Unset = UNSET
    last_amendment_date: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        access_time_id = self.access_time_id

        access_time_type = self.access_time_type

        description_tc = self.description_tc

        description_en = self.description_en

        creation_date = self.creation_date

        modified_by = self.modified_by

        last_amendment_date = self.last_amendment_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if access_time_id is not UNSET:
            field_dict["AccessTimeID"] = access_time_id
        if access_time_type is not UNSET:
            field_dict["AccessTimeType"] = access_time_type
        if description_tc is not UNSET:
            field_dict["DescriptionTC"] = description_tc
        if description_en is not UNSET:
            field_dict["DescriptionEN"] = description_en
        if creation_date is not UNSET:
            field_dict["CreationDate"] = creation_date
        if modified_by is not UNSET:
            field_dict["ModifiedBy"] = modified_by
        if last_amendment_date is not UNSET:
            field_dict["LastAmendmentDate"] = last_amendment_date

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        access_time_id = d.pop("AccessTimeID", UNSET)

        access_time_type = d.pop("AccessTimeType", UNSET)

        description_tc = d.pop("DescriptionTC", UNSET)

        description_en = d.pop("DescriptionEN", UNSET)

        creation_date = d.pop("CreationDate", UNSET)

        modified_by = d.pop("ModifiedBy", UNSET)

        last_amendment_date = d.pop("LastAmendmentDate", UNSET)

        arcgis_feature_server_arcgis_layer_1005_attributes = cls(
            objectid=objectid,
            access_time_id=access_time_id,
            access_time_type=access_time_type,
            description_tc=description_tc,
            description_en=description_en,
            creation_date=creation_date,
            modified_by=modified_by,
            last_amendment_date=last_amendment_date,
        )

        arcgis_feature_server_arcgis_layer_1005_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_1005_attributes

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
