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
        stop_id (int | None | Unset): Publisher field type: esriFieldTypeInteger
        last_update_date (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains
            unknown.
    """

    objectid: int | Unset = UNSET
    stop_id: int | None | Unset = UNSET
    last_update_date: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        stop_id: int | None | Unset
        if isinstance(self.stop_id, Unset):
            stop_id = UNSET
        else:
            stop_id = self.stop_id

        last_update_date = self.last_update_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if stop_id is not UNSET:
            field_dict["STOP_ID"] = stop_id
        if last_update_date is not UNSET:
            field_dict["LAST_UPDATE_DATE"] = last_update_date

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_stop_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        stop_id = _parse_stop_id(d.pop("STOP_ID", UNSET))

        last_update_date = d.pop("LAST_UPDATE_DATE", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            objectid=objectid,
            stop_id=stop_id,
            last_update_date=last_update_date,
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
