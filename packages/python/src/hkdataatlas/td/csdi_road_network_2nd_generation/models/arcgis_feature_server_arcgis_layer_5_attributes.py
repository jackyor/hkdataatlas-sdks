from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer5Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer5Attributes:
    """
    Attributes:
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        prohibition_id (int | Unset): Publisher field type: esriFieldTypeInteger
        exc_veh_type (None | str | Unset): Publisher field type: esriFieldTypeString
        inc_veh_type (None | str | Unset): Publisher field type: esriFieldTypeString
        part_time_prohibition (None | str | Unset): Publisher field type: esriFieldTypeString
        eff_all_days (None | str | Unset): Publisher field type: esriFieldTypeString
        other_rest_type_gv (None | str | Unset): Publisher field type: esriFieldTypeString
        remarks (None | str | Unset): Publisher field type: esriFieldTypeString
        road_route_id (int | Unset): Publisher field type: esriFieldTypeInteger
        cre_date (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains unknown.
        last_upd_date_v (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains
            unknown.
        bound (int | None | Unset): Publisher field type: esriFieldTypeInteger
    """

    objectid: int | Unset = UNSET
    prohibition_id: int | Unset = UNSET
    exc_veh_type: None | str | Unset = UNSET
    inc_veh_type: None | str | Unset = UNSET
    part_time_prohibition: None | str | Unset = UNSET
    eff_all_days: None | str | Unset = UNSET
    other_rest_type_gv: None | str | Unset = UNSET
    remarks: None | str | Unset = UNSET
    road_route_id: int | Unset = UNSET
    cre_date: Any | Unset = UNSET
    last_upd_date_v: Any | Unset = UNSET
    bound: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        prohibition_id = self.prohibition_id

        exc_veh_type: None | str | Unset
        if isinstance(self.exc_veh_type, Unset):
            exc_veh_type = UNSET
        else:
            exc_veh_type = self.exc_veh_type

        inc_veh_type: None | str | Unset
        if isinstance(self.inc_veh_type, Unset):
            inc_veh_type = UNSET
        else:
            inc_veh_type = self.inc_veh_type

        part_time_prohibition: None | str | Unset
        if isinstance(self.part_time_prohibition, Unset):
            part_time_prohibition = UNSET
        else:
            part_time_prohibition = self.part_time_prohibition

        eff_all_days: None | str | Unset
        if isinstance(self.eff_all_days, Unset):
            eff_all_days = UNSET
        else:
            eff_all_days = self.eff_all_days

        other_rest_type_gv: None | str | Unset
        if isinstance(self.other_rest_type_gv, Unset):
            other_rest_type_gv = UNSET
        else:
            other_rest_type_gv = self.other_rest_type_gv

        remarks: None | str | Unset
        if isinstance(self.remarks, Unset):
            remarks = UNSET
        else:
            remarks = self.remarks

        road_route_id = self.road_route_id

        cre_date = self.cre_date

        last_upd_date_v = self.last_upd_date_v

        bound: int | None | Unset
        if isinstance(self.bound, Unset):
            bound = UNSET
        else:
            bound = self.bound

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if prohibition_id is not UNSET:
            field_dict["PROHIBITION_ID"] = prohibition_id
        if exc_veh_type is not UNSET:
            field_dict["EXC_VEH_TYPE"] = exc_veh_type
        if inc_veh_type is not UNSET:
            field_dict["INC_VEH_TYPE"] = inc_veh_type
        if part_time_prohibition is not UNSET:
            field_dict["PART_TIME_PROHIBITION"] = part_time_prohibition
        if eff_all_days is not UNSET:
            field_dict["EFF_ALL_DAYS"] = eff_all_days
        if other_rest_type_gv is not UNSET:
            field_dict["OTHER_REST_TYPE_GV"] = other_rest_type_gv
        if remarks is not UNSET:
            field_dict["REMARKS"] = remarks
        if road_route_id is not UNSET:
            field_dict["ROAD_ROUTE_ID"] = road_route_id
        if cre_date is not UNSET:
            field_dict["CRE_DATE"] = cre_date
        if last_upd_date_v is not UNSET:
            field_dict["LAST_UPD_DATE_V"] = last_upd_date_v
        if bound is not UNSET:
            field_dict["BOUND"] = bound

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        prohibition_id = d.pop("PROHIBITION_ID", UNSET)

        def _parse_exc_veh_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        exc_veh_type = _parse_exc_veh_type(d.pop("EXC_VEH_TYPE", UNSET))

        def _parse_inc_veh_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        inc_veh_type = _parse_inc_veh_type(d.pop("INC_VEH_TYPE", UNSET))

        def _parse_part_time_prohibition(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        part_time_prohibition = _parse_part_time_prohibition(
            d.pop("PART_TIME_PROHIBITION", UNSET)
        )

        def _parse_eff_all_days(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        eff_all_days = _parse_eff_all_days(d.pop("EFF_ALL_DAYS", UNSET))

        def _parse_other_rest_type_gv(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        other_rest_type_gv = _parse_other_rest_type_gv(
            d.pop("OTHER_REST_TYPE_GV", UNSET)
        )

        def _parse_remarks(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remarks = _parse_remarks(d.pop("REMARKS", UNSET))

        road_route_id = d.pop("ROAD_ROUTE_ID", UNSET)

        cre_date = d.pop("CRE_DATE", UNSET)

        last_upd_date_v = d.pop("LAST_UPD_DATE_V", UNSET)

        def _parse_bound(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        bound = _parse_bound(d.pop("BOUND", UNSET))

        arcgis_feature_server_arcgis_layer_5_attributes = cls(
            objectid=objectid,
            prohibition_id=prohibition_id,
            exc_veh_type=exc_veh_type,
            inc_veh_type=inc_veh_type,
            part_time_prohibition=part_time_prohibition,
            eff_all_days=eff_all_days,
            other_rest_type_gv=other_rest_type_gv,
            remarks=remarks,
            road_route_id=road_route_id,
            cre_date=cre_date,
            last_upd_date_v=last_upd_date_v,
            bound=bound,
        )

        arcgis_feature_server_arcgis_layer_5_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_5_attributes

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
