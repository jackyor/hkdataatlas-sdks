from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer8Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer8Attributes:
    """
    Attributes:
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        vehicle_type (int | None | Unset): Publisher field type: esriFieldTypeInteger
        time_zone (int | None | Unset): Publisher field type: esriFieldTypeInteger
        effective_day (int | None | Unset): Publisher field type: esriFieldTypeInteger
        cre_date (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains unknown.
        nsr_id (int | Unset): Publisher field type: esriFieldTypeInteger
        st_code_1 (int | None | Unset): Publisher field type: esriFieldTypeInteger
        st_code_2 (int | None | Unset): Publisher field type: esriFieldTypeInteger
        st_code_3 (int | None | Unset): Publisher field type: esriFieldTypeInteger
        st_code_4 (int | None | Unset): Publisher field type: esriFieldTypeInteger
        st_code_5 (int | None | Unset): Publisher field type: esriFieldTypeInteger
        st_code_6 (int | None | Unset): Publisher field type: esriFieldTypeInteger
        remarks (None | str | Unset): Publisher field type: esriFieldTypeString
        last_upd_date_v (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains
            unknown.
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    objectid: int | Unset = UNSET
    vehicle_type: int | None | Unset = UNSET
    time_zone: int | None | Unset = UNSET
    effective_day: int | None | Unset = UNSET
    cre_date: Any | Unset = UNSET
    nsr_id: int | Unset = UNSET
    st_code_1: int | None | Unset = UNSET
    st_code_2: int | None | Unset = UNSET
    st_code_3: int | None | Unset = UNSET
    st_code_4: int | None | Unset = UNSET
    st_code_5: int | None | Unset = UNSET
    st_code_6: int | None | Unset = UNSET
    remarks: None | str | Unset = UNSET
    last_upd_date_v: Any | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        vehicle_type: int | None | Unset
        if isinstance(self.vehicle_type, Unset):
            vehicle_type = UNSET
        else:
            vehicle_type = self.vehicle_type

        time_zone: int | None | Unset
        if isinstance(self.time_zone, Unset):
            time_zone = UNSET
        else:
            time_zone = self.time_zone

        effective_day: int | None | Unset
        if isinstance(self.effective_day, Unset):
            effective_day = UNSET
        else:
            effective_day = self.effective_day

        cre_date = self.cre_date

        nsr_id = self.nsr_id

        st_code_1: int | None | Unset
        if isinstance(self.st_code_1, Unset):
            st_code_1 = UNSET
        else:
            st_code_1 = self.st_code_1

        st_code_2: int | None | Unset
        if isinstance(self.st_code_2, Unset):
            st_code_2 = UNSET
        else:
            st_code_2 = self.st_code_2

        st_code_3: int | None | Unset
        if isinstance(self.st_code_3, Unset):
            st_code_3 = UNSET
        else:
            st_code_3 = self.st_code_3

        st_code_4: int | None | Unset
        if isinstance(self.st_code_4, Unset):
            st_code_4 = UNSET
        else:
            st_code_4 = self.st_code_4

        st_code_5: int | None | Unset
        if isinstance(self.st_code_5, Unset):
            st_code_5 = UNSET
        else:
            st_code_5 = self.st_code_5

        st_code_6: int | None | Unset
        if isinstance(self.st_code_6, Unset):
            st_code_6 = UNSET
        else:
            st_code_6 = self.st_code_6

        remarks: None | str | Unset
        if isinstance(self.remarks, Unset):
            remarks = UNSET
        else:
            remarks = self.remarks

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
        if vehicle_type is not UNSET:
            field_dict["VEHICLE_TYPE"] = vehicle_type
        if time_zone is not UNSET:
            field_dict["TIME_ZONE"] = time_zone
        if effective_day is not UNSET:
            field_dict["EFFECTIVE_DAY"] = effective_day
        if cre_date is not UNSET:
            field_dict["CRE_DATE"] = cre_date
        if nsr_id is not UNSET:
            field_dict["NSR_ID"] = nsr_id
        if st_code_1 is not UNSET:
            field_dict["ST_CODE_1"] = st_code_1
        if st_code_2 is not UNSET:
            field_dict["ST_CODE_2"] = st_code_2
        if st_code_3 is not UNSET:
            field_dict["ST_CODE_3"] = st_code_3
        if st_code_4 is not UNSET:
            field_dict["ST_CODE_4"] = st_code_4
        if st_code_5 is not UNSET:
            field_dict["ST_CODE_5"] = st_code_5
        if st_code_6 is not UNSET:
            field_dict["ST_CODE_6"] = st_code_6
        if remarks is not UNSET:
            field_dict["REMARKS"] = remarks
        if last_upd_date_v is not UNSET:
            field_dict["LAST_UPD_DATE_V"] = last_upd_date_v
        if shape_length is not UNSET:
            field_dict["Shape__Length"] = shape_length

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_vehicle_type(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        vehicle_type = _parse_vehicle_type(d.pop("VEHICLE_TYPE", UNSET))

        def _parse_time_zone(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        time_zone = _parse_time_zone(d.pop("TIME_ZONE", UNSET))

        def _parse_effective_day(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        effective_day = _parse_effective_day(d.pop("EFFECTIVE_DAY", UNSET))

        cre_date = d.pop("CRE_DATE", UNSET)

        nsr_id = d.pop("NSR_ID", UNSET)

        def _parse_st_code_1(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        st_code_1 = _parse_st_code_1(d.pop("ST_CODE_1", UNSET))

        def _parse_st_code_2(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        st_code_2 = _parse_st_code_2(d.pop("ST_CODE_2", UNSET))

        def _parse_st_code_3(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        st_code_3 = _parse_st_code_3(d.pop("ST_CODE_3", UNSET))

        def _parse_st_code_4(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        st_code_4 = _parse_st_code_4(d.pop("ST_CODE_4", UNSET))

        def _parse_st_code_5(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        st_code_5 = _parse_st_code_5(d.pop("ST_CODE_5", UNSET))

        def _parse_st_code_6(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        st_code_6 = _parse_st_code_6(d.pop("ST_CODE_6", UNSET))

        def _parse_remarks(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remarks = _parse_remarks(d.pop("REMARKS", UNSET))

        last_upd_date_v = d.pop("LAST_UPD_DATE_V", UNSET)

        def _parse_shape_length(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_length = _parse_shape_length(d.pop("Shape__Length", UNSET))

        arcgis_feature_server_arcgis_layer_8_attributes = cls(
            objectid=objectid,
            vehicle_type=vehicle_type,
            time_zone=time_zone,
            effective_day=effective_day,
            cre_date=cre_date,
            nsr_id=nsr_id,
            st_code_1=st_code_1,
            st_code_2=st_code_2,
            st_code_3=st_code_3,
            st_code_4=st_code_4,
            st_code_5=st_code_5,
            st_code_6=st_code_6,
            remarks=remarks,
            last_upd_date_v=last_upd_date_v,
            shape_length=shape_length,
        )

        arcgis_feature_server_arcgis_layer_8_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_8_attributes

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
