from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer7Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer7Attributes:
    """
    Attributes:
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        road_route_id (int | Unset): Publisher field type: esriFieldTypeInteger
        time_zone (None | str | Unset): Publisher field type: esriFieldTypeString
        effective_day (None | str | Unset): Publisher field type: esriFieldTypeString
        remarks (None | str | Unset): Publisher field type: esriFieldTypeString
        ped_zone_id (int | Unset): Publisher field type: esriFieldTypeInteger
        cre_date (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains unknown.
        last_upd_date_v (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains
            unknown.
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    objectid: int | Unset = UNSET
    road_route_id: int | Unset = UNSET
    time_zone: None | str | Unset = UNSET
    effective_day: None | str | Unset = UNSET
    remarks: None | str | Unset = UNSET
    ped_zone_id: int | Unset = UNSET
    cre_date: Any | Unset = UNSET
    last_upd_date_v: Any | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        road_route_id = self.road_route_id

        time_zone: None | str | Unset
        if isinstance(self.time_zone, Unset):
            time_zone = UNSET
        else:
            time_zone = self.time_zone

        effective_day: None | str | Unset
        if isinstance(self.effective_day, Unset):
            effective_day = UNSET
        else:
            effective_day = self.effective_day

        remarks: None | str | Unset
        if isinstance(self.remarks, Unset):
            remarks = UNSET
        else:
            remarks = self.remarks

        ped_zone_id = self.ped_zone_id

        cre_date = self.cre_date

        last_upd_date_v = self.last_upd_date_v

        shape_length: float | None | Unset
        if isinstance(self.shape_length, Unset):
            shape_length = UNSET
        else:
            shape_length = self.shape_length

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if road_route_id is not UNSET:
            field_dict["ROAD_ROUTE_ID"] = road_route_id
        if time_zone is not UNSET:
            field_dict["TIME_ZONE"] = time_zone
        if effective_day is not UNSET:
            field_dict["EFFECTIVE_DAY"] = effective_day
        if remarks is not UNSET:
            field_dict["REMARKS"] = remarks
        if ped_zone_id is not UNSET:
            field_dict["PED_ZONE_ID"] = ped_zone_id
        if cre_date is not UNSET:
            field_dict["CRE_DATE"] = cre_date
        if last_upd_date_v is not UNSET:
            field_dict["LAST_UPD_DATE_V"] = last_upd_date_v
        if shape_length is not UNSET:
            field_dict["Shape__Length"] = shape_length

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        road_route_id = d.pop("ROAD_ROUTE_ID", UNSET)

        def _parse_time_zone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        time_zone = _parse_time_zone(d.pop("TIME_ZONE", UNSET))

        def _parse_effective_day(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        effective_day = _parse_effective_day(d.pop("EFFECTIVE_DAY", UNSET))

        def _parse_remarks(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remarks = _parse_remarks(d.pop("REMARKS", UNSET))

        ped_zone_id = d.pop("PED_ZONE_ID", UNSET)

        cre_date = d.pop("CRE_DATE", UNSET)

        last_upd_date_v = d.pop("LAST_UPD_DATE_V", UNSET)

        def _parse_shape_length(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_length = _parse_shape_length(d.pop("Shape__Length", UNSET))

        arcgis_feature_server_arcgis_layer_7_attributes = cls(
            objectid=objectid,
            road_route_id=road_route_id,
            time_zone=time_zone,
            effective_day=effective_day,
            remarks=remarks,
            ped_zone_id=ped_zone_id,
            cre_date=cre_date,
            last_upd_date_v=last_upd_date_v,
            shape_length=shape_length,
        )

        arcgis_feature_server_arcgis_layer_7_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_7_attributes

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
