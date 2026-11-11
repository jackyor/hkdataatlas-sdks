from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer1006Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer1006Attributes:
    """
    Attributes:
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        access_time_id (int | Unset): Publisher field type: esriFieldTypeInteger
        day_code (str | Unset): Publisher field type: esriFieldTypeString
        from_time (int | Unset): Publisher field type: esriFieldTypeInteger
        to_time (int | Unset): Publisher field type: esriFieldTypeInteger
    """

    objectid: int | Unset = UNSET
    access_time_id: int | Unset = UNSET
    day_code: str | Unset = UNSET
    from_time: int | Unset = UNSET
    to_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        access_time_id = self.access_time_id

        day_code = self.day_code

        from_time = self.from_time

        to_time = self.to_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if access_time_id is not UNSET:
            field_dict["AccessTimeID"] = access_time_id
        if day_code is not UNSET:
            field_dict["DayCode"] = day_code
        if from_time is not UNSET:
            field_dict["FromTime"] = from_time
        if to_time is not UNSET:
            field_dict["ToTime"] = to_time

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        access_time_id = d.pop("AccessTimeID", UNSET)

        day_code = d.pop("DayCode", UNSET)

        from_time = d.pop("FromTime", UNSET)

        to_time = d.pop("ToTime", UNSET)

        arcgis_feature_server_arcgis_layer_1006_attributes = cls(
            objectid=objectid,
            access_time_id=access_time_id,
            day_code=day_code,
            from_time=from_time,
            to_time=to_time,
        )

        arcgis_feature_server_arcgis_layer_1006_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_1006_attributes

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
