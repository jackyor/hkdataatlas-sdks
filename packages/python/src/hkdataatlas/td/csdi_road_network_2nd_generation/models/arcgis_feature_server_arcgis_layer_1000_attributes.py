from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer1000Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer1000Attributes:
    """
    Attributes:
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        tunnel_bridge_name (None | str | Unset): Publisher field type: esriFieldTypeString
        tunnel_bridge_chinese_name (None | str | Unset): Publisher field type: esriFieldTypeString
        feature_id_1 (int | None | Unset): Publisher field type: esriFieldTypeInteger
        feature_id_2 (int | None | Unset): Publisher field type: esriFieldTypeInteger
        effective_date (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains unknown.
        gazetted_toll (float | Unset): Publisher field type: esriFieldTypeDouble
        concession_toll (float | None | Unset): Publisher field type: esriFieldTypeDouble
        vehicle_class_description (str | Unset): Publisher field type: esriFieldTypeString
        remarks (None | str | Unset): Publisher field type: esriFieldTypeString
        last_updated_date (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains
            unknown.
    """

    objectid: int | Unset = UNSET
    tunnel_bridge_name: None | str | Unset = UNSET
    tunnel_bridge_chinese_name: None | str | Unset = UNSET
    feature_id_1: int | None | Unset = UNSET
    feature_id_2: int | None | Unset = UNSET
    effective_date: Any | Unset = UNSET
    gazetted_toll: float | Unset = UNSET
    concession_toll: float | None | Unset = UNSET
    vehicle_class_description: str | Unset = UNSET
    remarks: None | str | Unset = UNSET
    last_updated_date: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        tunnel_bridge_name: None | str | Unset
        if isinstance(self.tunnel_bridge_name, Unset):
            tunnel_bridge_name = UNSET
        else:
            tunnel_bridge_name = self.tunnel_bridge_name

        tunnel_bridge_chinese_name: None | str | Unset
        if isinstance(self.tunnel_bridge_chinese_name, Unset):
            tunnel_bridge_chinese_name = UNSET
        else:
            tunnel_bridge_chinese_name = self.tunnel_bridge_chinese_name

        feature_id_1: int | None | Unset
        if isinstance(self.feature_id_1, Unset):
            feature_id_1 = UNSET
        else:
            feature_id_1 = self.feature_id_1

        feature_id_2: int | None | Unset
        if isinstance(self.feature_id_2, Unset):
            feature_id_2 = UNSET
        else:
            feature_id_2 = self.feature_id_2

        effective_date = self.effective_date

        gazetted_toll = self.gazetted_toll

        concession_toll: float | None | Unset
        if isinstance(self.concession_toll, Unset):
            concession_toll = UNSET
        else:
            concession_toll = self.concession_toll

        vehicle_class_description = self.vehicle_class_description

        remarks: None | str | Unset
        if isinstance(self.remarks, Unset):
            remarks = UNSET
        else:
            remarks = self.remarks

        last_updated_date = self.last_updated_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if tunnel_bridge_name is not UNSET:
            field_dict["TUNNEL_BRIDGE_NAME"] = tunnel_bridge_name
        if tunnel_bridge_chinese_name is not UNSET:
            field_dict["TUNNEL_BRIDGE_CHINESE_NAME"] = tunnel_bridge_chinese_name
        if feature_id_1 is not UNSET:
            field_dict["FEATURE_ID_1"] = feature_id_1
        if feature_id_2 is not UNSET:
            field_dict["FEATURE_ID_2"] = feature_id_2
        if effective_date is not UNSET:
            field_dict["EFFECTIVE_DATE"] = effective_date
        if gazetted_toll is not UNSET:
            field_dict["GAZETTED_TOLL"] = gazetted_toll
        if concession_toll is not UNSET:
            field_dict["CONCESSION_TOLL"] = concession_toll
        if vehicle_class_description is not UNSET:
            field_dict["VEHICLE_CLASS_DESCRIPTION"] = vehicle_class_description
        if remarks is not UNSET:
            field_dict["REMARKS"] = remarks
        if last_updated_date is not UNSET:
            field_dict["LAST_UPDATED_DATE"] = last_updated_date

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_tunnel_bridge_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tunnel_bridge_name = _parse_tunnel_bridge_name(
            d.pop("TUNNEL_BRIDGE_NAME", UNSET)
        )

        def _parse_tunnel_bridge_chinese_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tunnel_bridge_chinese_name = _parse_tunnel_bridge_chinese_name(
            d.pop("TUNNEL_BRIDGE_CHINESE_NAME", UNSET)
        )

        def _parse_feature_id_1(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        feature_id_1 = _parse_feature_id_1(d.pop("FEATURE_ID_1", UNSET))

        def _parse_feature_id_2(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        feature_id_2 = _parse_feature_id_2(d.pop("FEATURE_ID_2", UNSET))

        effective_date = d.pop("EFFECTIVE_DATE", UNSET)

        gazetted_toll = d.pop("GAZETTED_TOLL", UNSET)

        def _parse_concession_toll(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        concession_toll = _parse_concession_toll(d.pop("CONCESSION_TOLL", UNSET))

        vehicle_class_description = d.pop("VEHICLE_CLASS_DESCRIPTION", UNSET)

        def _parse_remarks(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remarks = _parse_remarks(d.pop("REMARKS", UNSET))

        last_updated_date = d.pop("LAST_UPDATED_DATE", UNSET)

        arcgis_feature_server_arcgis_layer_1000_attributes = cls(
            objectid=objectid,
            tunnel_bridge_name=tunnel_bridge_name,
            tunnel_bridge_chinese_name=tunnel_bridge_chinese_name,
            feature_id_1=feature_id_1,
            feature_id_2=feature_id_2,
            effective_date=effective_date,
            gazetted_toll=gazetted_toll,
            concession_toll=concession_toll,
            vehicle_class_description=vehicle_class_description,
            remarks=remarks,
            last_updated_date=last_updated_date,
        )

        arcgis_feature_server_arcgis_layer_1000_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_1000_attributes

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
