from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer10Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer10Attributes:
    """
    Attributes:
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        street_ename (None | str | Unset): Publisher field type: esriFieldTypeString
        street_cname (None | str | Unset): Publisher field type: esriFieldTypeString
        elevation (int | None | Unset): Publisher field type: esriFieldTypeSmallInteger
        st_code (int | None | Unset): Publisher field type: esriFieldTypeInteger
        exit_num (None | str | Unset): Publisher field type: esriFieldTypeString
        route_num (int | None | Unset): Publisher field type: esriFieldTypeSmallInteger
        remarks (None | str | Unset): Publisher field type: esriFieldTypeString
        route_id (int | Unset): Publisher field type: esriFieldTypeInteger
        travel_direction (int | None | Unset): Publisher field type: esriFieldTypeSmallInteger
        cre_date (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains unknown.
        last_upd_date_v (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains
            unknown.
        alias_ename (None | str | Unset): Publisher field type: esriFieldTypeString
        alias_cname (None | str | Unset): Publisher field type: esriFieldTypeString
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    objectid: int | Unset = UNSET
    street_ename: None | str | Unset = UNSET
    street_cname: None | str | Unset = UNSET
    elevation: int | None | Unset = UNSET
    st_code: int | None | Unset = UNSET
    exit_num: None | str | Unset = UNSET
    route_num: int | None | Unset = UNSET
    remarks: None | str | Unset = UNSET
    route_id: int | Unset = UNSET
    travel_direction: int | None | Unset = UNSET
    cre_date: Any | Unset = UNSET
    last_upd_date_v: Any | Unset = UNSET
    alias_ename: None | str | Unset = UNSET
    alias_cname: None | str | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        street_ename: None | str | Unset
        if isinstance(self.street_ename, Unset):
            street_ename = UNSET
        else:
            street_ename = self.street_ename

        street_cname: None | str | Unset
        if isinstance(self.street_cname, Unset):
            street_cname = UNSET
        else:
            street_cname = self.street_cname

        elevation: int | None | Unset
        if isinstance(self.elevation, Unset):
            elevation = UNSET
        else:
            elevation = self.elevation

        st_code: int | None | Unset
        if isinstance(self.st_code, Unset):
            st_code = UNSET
        else:
            st_code = self.st_code

        exit_num: None | str | Unset
        if isinstance(self.exit_num, Unset):
            exit_num = UNSET
        else:
            exit_num = self.exit_num

        route_num: int | None | Unset
        if isinstance(self.route_num, Unset):
            route_num = UNSET
        else:
            route_num = self.route_num

        remarks: None | str | Unset
        if isinstance(self.remarks, Unset):
            remarks = UNSET
        else:
            remarks = self.remarks

        route_id = self.route_id

        travel_direction: int | None | Unset
        if isinstance(self.travel_direction, Unset):
            travel_direction = UNSET
        else:
            travel_direction = self.travel_direction

        cre_date = self.cre_date

        last_upd_date_v = self.last_upd_date_v

        alias_ename: None | str | Unset
        if isinstance(self.alias_ename, Unset):
            alias_ename = UNSET
        else:
            alias_ename = self.alias_ename

        alias_cname: None | str | Unset
        if isinstance(self.alias_cname, Unset):
            alias_cname = UNSET
        else:
            alias_cname = self.alias_cname

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
        if street_ename is not UNSET:
            field_dict["STREET_ENAME"] = street_ename
        if street_cname is not UNSET:
            field_dict["STREET_CNAME"] = street_cname
        if elevation is not UNSET:
            field_dict["ELEVATION"] = elevation
        if st_code is not UNSET:
            field_dict["ST_CODE"] = st_code
        if exit_num is not UNSET:
            field_dict["EXIT_NUM"] = exit_num
        if route_num is not UNSET:
            field_dict["ROUTE_NUM"] = route_num
        if remarks is not UNSET:
            field_dict["REMARKS"] = remarks
        if route_id is not UNSET:
            field_dict["ROUTE_ID"] = route_id
        if travel_direction is not UNSET:
            field_dict["TRAVEL_DIRECTION"] = travel_direction
        if cre_date is not UNSET:
            field_dict["CRE_DATE"] = cre_date
        if last_upd_date_v is not UNSET:
            field_dict["LAST_UPD_DATE_V"] = last_upd_date_v
        if alias_ename is not UNSET:
            field_dict["ALIAS_ENAME"] = alias_ename
        if alias_cname is not UNSET:
            field_dict["ALIAS_CNAME"] = alias_cname
        if shape_length is not UNSET:
            field_dict["Shape__Length"] = shape_length

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_street_ename(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        street_ename = _parse_street_ename(d.pop("STREET_ENAME", UNSET))

        def _parse_street_cname(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        street_cname = _parse_street_cname(d.pop("STREET_CNAME", UNSET))

        def _parse_elevation(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        elevation = _parse_elevation(d.pop("ELEVATION", UNSET))

        def _parse_st_code(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        st_code = _parse_st_code(d.pop("ST_CODE", UNSET))

        def _parse_exit_num(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        exit_num = _parse_exit_num(d.pop("EXIT_NUM", UNSET))

        def _parse_route_num(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        route_num = _parse_route_num(d.pop("ROUTE_NUM", UNSET))

        def _parse_remarks(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remarks = _parse_remarks(d.pop("REMARKS", UNSET))

        route_id = d.pop("ROUTE_ID", UNSET)

        def _parse_travel_direction(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        travel_direction = _parse_travel_direction(d.pop("TRAVEL_DIRECTION", UNSET))

        cre_date = d.pop("CRE_DATE", UNSET)

        last_upd_date_v = d.pop("LAST_UPD_DATE_V", UNSET)

        def _parse_alias_ename(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        alias_ename = _parse_alias_ename(d.pop("ALIAS_ENAME", UNSET))

        def _parse_alias_cname(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        alias_cname = _parse_alias_cname(d.pop("ALIAS_CNAME", UNSET))

        def _parse_shape_length(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_length = _parse_shape_length(d.pop("Shape__Length", UNSET))

        arcgis_feature_server_arcgis_layer_10_attributes = cls(
            objectid=objectid,
            street_ename=street_ename,
            street_cname=street_cname,
            elevation=elevation,
            st_code=st_code,
            exit_num=exit_num,
            route_num=route_num,
            remarks=remarks,
            route_id=route_id,
            travel_direction=travel_direction,
            cre_date=cre_date,
            last_upd_date_v=last_upd_date_v,
            alias_ename=alias_ename,
            alias_cname=alias_cname,
            shape_length=shape_length,
        )

        arcgis_feature_server_arcgis_layer_10_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_10_attributes

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
