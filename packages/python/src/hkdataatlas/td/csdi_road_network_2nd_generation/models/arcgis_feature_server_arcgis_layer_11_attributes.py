from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer11Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer11Attributes:
    """
    Attributes:
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        edge1end (None | str | Unset): Publisher field type: esriFieldTypeString
        edge1fcid (int | None | Unset): Publisher field type: esriFieldTypeInteger
        edge1fid (int | None | Unset): Publisher field type: esriFieldTypeInteger
        edge1pos (float | None | Unset): Publisher field type: esriFieldTypeDouble
        edge2fcid (int | None | Unset): Publisher field type: esriFieldTypeInteger
        edge2fid (int | None | Unset): Publisher field type: esriFieldTypeInteger
        edge2pos (float | None | Unset): Publisher field type: esriFieldTypeDouble
        edge3fcid (int | None | Unset): Publisher field type: esriFieldTypeInteger
        edge3fid (int | None | Unset): Publisher field type: esriFieldTypeInteger
        edge3pos (float | None | Unset): Publisher field type: esriFieldTypeDouble
        edge4fcid (int | None | Unset): Publisher field type: esriFieldTypeInteger
        edge4fid (int | None | Unset): Publisher field type: esriFieldTypeInteger
        edge4pos (float | None | Unset): Publisher field type: esriFieldTypeDouble
        edge5fcid (int | None | Unset): Publisher field type: esriFieldTypeInteger
        edge5fid (int | None | Unset): Publisher field type: esriFieldTypeInteger
        edge5pos (float | None | Unset): Publisher field type: esriFieldTypeDouble
        edge6fcid (int | None | Unset): Publisher field type: esriFieldTypeInteger
        edge6fid (int | None | Unset): Publisher field type: esriFieldTypeInteger
        edge6pos (float | None | Unset): Publisher field type: esriFieldTypeDouble
        edge7fcid (int | None | Unset): Publisher field type: esriFieldTypeInteger
        edge7fid (int | None | Unset): Publisher field type: esriFieldTypeInteger
        edge7pos (float | None | Unset): Publisher field type: esriFieldTypeDouble
        edge8fcid (int | None | Unset): Publisher field type: esriFieldTypeInteger
        edge8fid (int | None | Unset): Publisher field type: esriFieldTypeInteger
        edge8pos (float | None | Unset): Publisher field type: esriFieldTypeDouble
        no_turn (int | None | Unset): Publisher field type: esriFieldTypeSmallInteger
        cre_date (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains unknown.
        remarks (None | str | Unset): Publisher field type: esriFieldTypeString
        last_upd_date_v (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains
            unknown.
        turn_id (int | None | Unset): Publisher field type: esriFieldTypeInteger
        exc_veh_type (None | str | Unset): Publisher field type: esriFieldTypeString
        inc_veh_type (None | str | Unset): Publisher field type: esriFieldTypeString
        part_time_rest (None | str | Unset): Publisher field type: esriFieldTypeString
        eff_all_days (None | str | Unset): Publisher field type: esriFieldTypeString
        other_rest_type (None | str | Unset): Publisher field type: esriFieldTypeString
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    objectid: int | Unset = UNSET
    edge1end: None | str | Unset = UNSET
    edge1fcid: int | None | Unset = UNSET
    edge1fid: int | None | Unset = UNSET
    edge1pos: float | None | Unset = UNSET
    edge2fcid: int | None | Unset = UNSET
    edge2fid: int | None | Unset = UNSET
    edge2pos: float | None | Unset = UNSET
    edge3fcid: int | None | Unset = UNSET
    edge3fid: int | None | Unset = UNSET
    edge3pos: float | None | Unset = UNSET
    edge4fcid: int | None | Unset = UNSET
    edge4fid: int | None | Unset = UNSET
    edge4pos: float | None | Unset = UNSET
    edge5fcid: int | None | Unset = UNSET
    edge5fid: int | None | Unset = UNSET
    edge5pos: float | None | Unset = UNSET
    edge6fcid: int | None | Unset = UNSET
    edge6fid: int | None | Unset = UNSET
    edge6pos: float | None | Unset = UNSET
    edge7fcid: int | None | Unset = UNSET
    edge7fid: int | None | Unset = UNSET
    edge7pos: float | None | Unset = UNSET
    edge8fcid: int | None | Unset = UNSET
    edge8fid: int | None | Unset = UNSET
    edge8pos: float | None | Unset = UNSET
    no_turn: int | None | Unset = UNSET
    cre_date: Any | Unset = UNSET
    remarks: None | str | Unset = UNSET
    last_upd_date_v: Any | Unset = UNSET
    turn_id: int | None | Unset = UNSET
    exc_veh_type: None | str | Unset = UNSET
    inc_veh_type: None | str | Unset = UNSET
    part_time_rest: None | str | Unset = UNSET
    eff_all_days: None | str | Unset = UNSET
    other_rest_type: None | str | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        edge1end: None | str | Unset
        if isinstance(self.edge1end, Unset):
            edge1end = UNSET
        else:
            edge1end = self.edge1end

        edge1fcid: int | None | Unset
        if isinstance(self.edge1fcid, Unset):
            edge1fcid = UNSET
        else:
            edge1fcid = self.edge1fcid

        edge1fid: int | None | Unset
        if isinstance(self.edge1fid, Unset):
            edge1fid = UNSET
        else:
            edge1fid = self.edge1fid

        edge1pos: float | None | Unset
        if isinstance(self.edge1pos, Unset):
            edge1pos = UNSET
        else:
            edge1pos = self.edge1pos

        edge2fcid: int | None | Unset
        if isinstance(self.edge2fcid, Unset):
            edge2fcid = UNSET
        else:
            edge2fcid = self.edge2fcid

        edge2fid: int | None | Unset
        if isinstance(self.edge2fid, Unset):
            edge2fid = UNSET
        else:
            edge2fid = self.edge2fid

        edge2pos: float | None | Unset
        if isinstance(self.edge2pos, Unset):
            edge2pos = UNSET
        else:
            edge2pos = self.edge2pos

        edge3fcid: int | None | Unset
        if isinstance(self.edge3fcid, Unset):
            edge3fcid = UNSET
        else:
            edge3fcid = self.edge3fcid

        edge3fid: int | None | Unset
        if isinstance(self.edge3fid, Unset):
            edge3fid = UNSET
        else:
            edge3fid = self.edge3fid

        edge3pos: float | None | Unset
        if isinstance(self.edge3pos, Unset):
            edge3pos = UNSET
        else:
            edge3pos = self.edge3pos

        edge4fcid: int | None | Unset
        if isinstance(self.edge4fcid, Unset):
            edge4fcid = UNSET
        else:
            edge4fcid = self.edge4fcid

        edge4fid: int | None | Unset
        if isinstance(self.edge4fid, Unset):
            edge4fid = UNSET
        else:
            edge4fid = self.edge4fid

        edge4pos: float | None | Unset
        if isinstance(self.edge4pos, Unset):
            edge4pos = UNSET
        else:
            edge4pos = self.edge4pos

        edge5fcid: int | None | Unset
        if isinstance(self.edge5fcid, Unset):
            edge5fcid = UNSET
        else:
            edge5fcid = self.edge5fcid

        edge5fid: int | None | Unset
        if isinstance(self.edge5fid, Unset):
            edge5fid = UNSET
        else:
            edge5fid = self.edge5fid

        edge5pos: float | None | Unset
        if isinstance(self.edge5pos, Unset):
            edge5pos = UNSET
        else:
            edge5pos = self.edge5pos

        edge6fcid: int | None | Unset
        if isinstance(self.edge6fcid, Unset):
            edge6fcid = UNSET
        else:
            edge6fcid = self.edge6fcid

        edge6fid: int | None | Unset
        if isinstance(self.edge6fid, Unset):
            edge6fid = UNSET
        else:
            edge6fid = self.edge6fid

        edge6pos: float | None | Unset
        if isinstance(self.edge6pos, Unset):
            edge6pos = UNSET
        else:
            edge6pos = self.edge6pos

        edge7fcid: int | None | Unset
        if isinstance(self.edge7fcid, Unset):
            edge7fcid = UNSET
        else:
            edge7fcid = self.edge7fcid

        edge7fid: int | None | Unset
        if isinstance(self.edge7fid, Unset):
            edge7fid = UNSET
        else:
            edge7fid = self.edge7fid

        edge7pos: float | None | Unset
        if isinstance(self.edge7pos, Unset):
            edge7pos = UNSET
        else:
            edge7pos = self.edge7pos

        edge8fcid: int | None | Unset
        if isinstance(self.edge8fcid, Unset):
            edge8fcid = UNSET
        else:
            edge8fcid = self.edge8fcid

        edge8fid: int | None | Unset
        if isinstance(self.edge8fid, Unset):
            edge8fid = UNSET
        else:
            edge8fid = self.edge8fid

        edge8pos: float | None | Unset
        if isinstance(self.edge8pos, Unset):
            edge8pos = UNSET
        else:
            edge8pos = self.edge8pos

        no_turn: int | None | Unset
        if isinstance(self.no_turn, Unset):
            no_turn = UNSET
        else:
            no_turn = self.no_turn

        cre_date = self.cre_date

        remarks: None | str | Unset
        if isinstance(self.remarks, Unset):
            remarks = UNSET
        else:
            remarks = self.remarks

        last_upd_date_v = self.last_upd_date_v

        turn_id: int | None | Unset
        if isinstance(self.turn_id, Unset):
            turn_id = UNSET
        else:
            turn_id = self.turn_id

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

        part_time_rest: None | str | Unset
        if isinstance(self.part_time_rest, Unset):
            part_time_rest = UNSET
        else:
            part_time_rest = self.part_time_rest

        eff_all_days: None | str | Unset
        if isinstance(self.eff_all_days, Unset):
            eff_all_days = UNSET
        else:
            eff_all_days = self.eff_all_days

        other_rest_type: None | str | Unset
        if isinstance(self.other_rest_type, Unset):
            other_rest_type = UNSET
        else:
            other_rest_type = self.other_rest_type

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
        if edge1end is not UNSET:
            field_dict["EDGE1END"] = edge1end
        if edge1fcid is not UNSET:
            field_dict["EDGE1FCID"] = edge1fcid
        if edge1fid is not UNSET:
            field_dict["EDGE1FID"] = edge1fid
        if edge1pos is not UNSET:
            field_dict["EDGE1POS"] = edge1pos
        if edge2fcid is not UNSET:
            field_dict["EDGE2FCID"] = edge2fcid
        if edge2fid is not UNSET:
            field_dict["EDGE2FID"] = edge2fid
        if edge2pos is not UNSET:
            field_dict["EDGE2POS"] = edge2pos
        if edge3fcid is not UNSET:
            field_dict["EDGE3FCID"] = edge3fcid
        if edge3fid is not UNSET:
            field_dict["EDGE3FID"] = edge3fid
        if edge3pos is not UNSET:
            field_dict["EDGE3POS"] = edge3pos
        if edge4fcid is not UNSET:
            field_dict["EDGE4FCID"] = edge4fcid
        if edge4fid is not UNSET:
            field_dict["EDGE4FID"] = edge4fid
        if edge4pos is not UNSET:
            field_dict["EDGE4POS"] = edge4pos
        if edge5fcid is not UNSET:
            field_dict["EDGE5FCID"] = edge5fcid
        if edge5fid is not UNSET:
            field_dict["EDGE5FID"] = edge5fid
        if edge5pos is not UNSET:
            field_dict["EDGE5POS"] = edge5pos
        if edge6fcid is not UNSET:
            field_dict["EDGE6FCID"] = edge6fcid
        if edge6fid is not UNSET:
            field_dict["EDGE6FID"] = edge6fid
        if edge6pos is not UNSET:
            field_dict["EDGE6POS"] = edge6pos
        if edge7fcid is not UNSET:
            field_dict["EDGE7FCID"] = edge7fcid
        if edge7fid is not UNSET:
            field_dict["EDGE7FID"] = edge7fid
        if edge7pos is not UNSET:
            field_dict["EDGE7POS"] = edge7pos
        if edge8fcid is not UNSET:
            field_dict["EDGE8FCID"] = edge8fcid
        if edge8fid is not UNSET:
            field_dict["EDGE8FID"] = edge8fid
        if edge8pos is not UNSET:
            field_dict["EDGE8POS"] = edge8pos
        if no_turn is not UNSET:
            field_dict["NO_TURN"] = no_turn
        if cre_date is not UNSET:
            field_dict["CRE_DATE"] = cre_date
        if remarks is not UNSET:
            field_dict["REMARKS"] = remarks
        if last_upd_date_v is not UNSET:
            field_dict["LAST_UPD_DATE_V"] = last_upd_date_v
        if turn_id is not UNSET:
            field_dict["TURN_ID"] = turn_id
        if exc_veh_type is not UNSET:
            field_dict["EXC_VEH_TYPE"] = exc_veh_type
        if inc_veh_type is not UNSET:
            field_dict["INC_VEH_TYPE"] = inc_veh_type
        if part_time_rest is not UNSET:
            field_dict["PART_TIME_REST"] = part_time_rest
        if eff_all_days is not UNSET:
            field_dict["EFF_ALL_DAYS"] = eff_all_days
        if other_rest_type is not UNSET:
            field_dict["OTHER_REST_TYPE"] = other_rest_type
        if shape_length is not UNSET:
            field_dict["Shape__Length"] = shape_length

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_edge1end(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        edge1end = _parse_edge1end(d.pop("EDGE1END", UNSET))

        def _parse_edge1fcid(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        edge1fcid = _parse_edge1fcid(d.pop("EDGE1FCID", UNSET))

        def _parse_edge1fid(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        edge1fid = _parse_edge1fid(d.pop("EDGE1FID", UNSET))

        def _parse_edge1pos(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        edge1pos = _parse_edge1pos(d.pop("EDGE1POS", UNSET))

        def _parse_edge2fcid(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        edge2fcid = _parse_edge2fcid(d.pop("EDGE2FCID", UNSET))

        def _parse_edge2fid(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        edge2fid = _parse_edge2fid(d.pop("EDGE2FID", UNSET))

        def _parse_edge2pos(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        edge2pos = _parse_edge2pos(d.pop("EDGE2POS", UNSET))

        def _parse_edge3fcid(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        edge3fcid = _parse_edge3fcid(d.pop("EDGE3FCID", UNSET))

        def _parse_edge3fid(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        edge3fid = _parse_edge3fid(d.pop("EDGE3FID", UNSET))

        def _parse_edge3pos(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        edge3pos = _parse_edge3pos(d.pop("EDGE3POS", UNSET))

        def _parse_edge4fcid(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        edge4fcid = _parse_edge4fcid(d.pop("EDGE4FCID", UNSET))

        def _parse_edge4fid(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        edge4fid = _parse_edge4fid(d.pop("EDGE4FID", UNSET))

        def _parse_edge4pos(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        edge4pos = _parse_edge4pos(d.pop("EDGE4POS", UNSET))

        def _parse_edge5fcid(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        edge5fcid = _parse_edge5fcid(d.pop("EDGE5FCID", UNSET))

        def _parse_edge5fid(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        edge5fid = _parse_edge5fid(d.pop("EDGE5FID", UNSET))

        def _parse_edge5pos(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        edge5pos = _parse_edge5pos(d.pop("EDGE5POS", UNSET))

        def _parse_edge6fcid(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        edge6fcid = _parse_edge6fcid(d.pop("EDGE6FCID", UNSET))

        def _parse_edge6fid(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        edge6fid = _parse_edge6fid(d.pop("EDGE6FID", UNSET))

        def _parse_edge6pos(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        edge6pos = _parse_edge6pos(d.pop("EDGE6POS", UNSET))

        def _parse_edge7fcid(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        edge7fcid = _parse_edge7fcid(d.pop("EDGE7FCID", UNSET))

        def _parse_edge7fid(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        edge7fid = _parse_edge7fid(d.pop("EDGE7FID", UNSET))

        def _parse_edge7pos(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        edge7pos = _parse_edge7pos(d.pop("EDGE7POS", UNSET))

        def _parse_edge8fcid(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        edge8fcid = _parse_edge8fcid(d.pop("EDGE8FCID", UNSET))

        def _parse_edge8fid(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        edge8fid = _parse_edge8fid(d.pop("EDGE8FID", UNSET))

        def _parse_edge8pos(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        edge8pos = _parse_edge8pos(d.pop("EDGE8POS", UNSET))

        def _parse_no_turn(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        no_turn = _parse_no_turn(d.pop("NO_TURN", UNSET))

        cre_date = d.pop("CRE_DATE", UNSET)

        def _parse_remarks(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remarks = _parse_remarks(d.pop("REMARKS", UNSET))

        last_upd_date_v = d.pop("LAST_UPD_DATE_V", UNSET)

        def _parse_turn_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        turn_id = _parse_turn_id(d.pop("TURN_ID", UNSET))

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

        def _parse_part_time_rest(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        part_time_rest = _parse_part_time_rest(d.pop("PART_TIME_REST", UNSET))

        def _parse_eff_all_days(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        eff_all_days = _parse_eff_all_days(d.pop("EFF_ALL_DAYS", UNSET))

        def _parse_other_rest_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        other_rest_type = _parse_other_rest_type(d.pop("OTHER_REST_TYPE", UNSET))

        def _parse_shape_length(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_length = _parse_shape_length(d.pop("Shape__Length", UNSET))

        arcgis_feature_server_arcgis_layer_11_attributes = cls(
            objectid=objectid,
            edge1end=edge1end,
            edge1fcid=edge1fcid,
            edge1fid=edge1fid,
            edge1pos=edge1pos,
            edge2fcid=edge2fcid,
            edge2fid=edge2fid,
            edge2pos=edge2pos,
            edge3fcid=edge3fcid,
            edge3fid=edge3fid,
            edge3pos=edge3pos,
            edge4fcid=edge4fcid,
            edge4fid=edge4fid,
            edge4pos=edge4pos,
            edge5fcid=edge5fcid,
            edge5fid=edge5fid,
            edge5pos=edge5pos,
            edge6fcid=edge6fcid,
            edge6fid=edge6fid,
            edge6pos=edge6pos,
            edge7fcid=edge7fcid,
            edge7fid=edge7fid,
            edge7pos=edge7pos,
            edge8fcid=edge8fcid,
            edge8fid=edge8fid,
            edge8pos=edge8pos,
            no_turn=no_turn,
            cre_date=cre_date,
            remarks=remarks,
            last_upd_date_v=last_upd_date_v,
            turn_id=turn_id,
            exc_veh_type=exc_veh_type,
            inc_veh_type=inc_veh_type,
            part_time_rest=part_time_rest,
            eff_all_days=eff_all_days,
            other_rest_type=other_rest_type,
            shape_length=shape_length,
        )

        arcgis_feature_server_arcgis_layer_11_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_11_attributes

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
