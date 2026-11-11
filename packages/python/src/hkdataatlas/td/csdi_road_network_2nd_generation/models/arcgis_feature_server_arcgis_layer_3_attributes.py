from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer3Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer3Attributes:
    """
    Attributes:
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        run_in_out_id (int | Unset): Publisher field type: esriFieldTypeInteger
        run_in_out_type (int | None | Unset): Publisher field type: esriFieldTypeSmallInteger
        parking_id (None | str | Unset): Publisher field type: esriFieldTypeString
        building_ename (None | str | Unset): Publisher field type: esriFieldTypeString
        building_cname (None | str | Unset): Publisher field type: esriFieldTypeString
        cre_date (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains unknown.
        rd_id_1 (int | None | Unset): Publisher field type: esriFieldTypeInteger
        rd_id_2 (int | None | Unset): Publisher field type: esriFieldTypeInteger
        rd_id_3 (int | None | Unset): Publisher field type: esriFieldTypeInteger
        rd_id_4 (int | None | Unset): Publisher field type: esriFieldTypeInteger
        remarks (None | str | Unset): Publisher field type: esriFieldTypeString
        last_upd_date_v (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains
            unknown.
        building_address (None | str | Unset): Publisher field type: esriFieldTypeString
    """

    objectid: int | Unset = UNSET
    run_in_out_id: int | Unset = UNSET
    run_in_out_type: int | None | Unset = UNSET
    parking_id: None | str | Unset = UNSET
    building_ename: None | str | Unset = UNSET
    building_cname: None | str | Unset = UNSET
    cre_date: Any | Unset = UNSET
    rd_id_1: int | None | Unset = UNSET
    rd_id_2: int | None | Unset = UNSET
    rd_id_3: int | None | Unset = UNSET
    rd_id_4: int | None | Unset = UNSET
    remarks: None | str | Unset = UNSET
    last_upd_date_v: Any | Unset = UNSET
    building_address: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        run_in_out_id = self.run_in_out_id

        run_in_out_type: int | None | Unset
        if isinstance(self.run_in_out_type, Unset):
            run_in_out_type = UNSET
        else:
            run_in_out_type = self.run_in_out_type

        parking_id: None | str | Unset
        if isinstance(self.parking_id, Unset):
            parking_id = UNSET
        else:
            parking_id = self.parking_id

        building_ename: None | str | Unset
        if isinstance(self.building_ename, Unset):
            building_ename = UNSET
        else:
            building_ename = self.building_ename

        building_cname: None | str | Unset
        if isinstance(self.building_cname, Unset):
            building_cname = UNSET
        else:
            building_cname = self.building_cname

        cre_date = self.cre_date

        rd_id_1: int | None | Unset
        if isinstance(self.rd_id_1, Unset):
            rd_id_1 = UNSET
        else:
            rd_id_1 = self.rd_id_1

        rd_id_2: int | None | Unset
        if isinstance(self.rd_id_2, Unset):
            rd_id_2 = UNSET
        else:
            rd_id_2 = self.rd_id_2

        rd_id_3: int | None | Unset
        if isinstance(self.rd_id_3, Unset):
            rd_id_3 = UNSET
        else:
            rd_id_3 = self.rd_id_3

        rd_id_4: int | None | Unset
        if isinstance(self.rd_id_4, Unset):
            rd_id_4 = UNSET
        else:
            rd_id_4 = self.rd_id_4

        remarks: None | str | Unset
        if isinstance(self.remarks, Unset):
            remarks = UNSET
        else:
            remarks = self.remarks

        last_upd_date_v = self.last_upd_date_v

        building_address: None | str | Unset
        if isinstance(self.building_address, Unset):
            building_address = UNSET
        else:
            building_address = self.building_address

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if run_in_out_id is not UNSET:
            field_dict["RUN_IN_OUT_ID"] = run_in_out_id
        if run_in_out_type is not UNSET:
            field_dict["RUN_IN_OUT_TYPE"] = run_in_out_type
        if parking_id is not UNSET:
            field_dict["PARKING_ID"] = parking_id
        if building_ename is not UNSET:
            field_dict["BUILDING_ENAME"] = building_ename
        if building_cname is not UNSET:
            field_dict["BUILDING_CNAME"] = building_cname
        if cre_date is not UNSET:
            field_dict["CRE_DATE"] = cre_date
        if rd_id_1 is not UNSET:
            field_dict["RD_ID_1"] = rd_id_1
        if rd_id_2 is not UNSET:
            field_dict["RD_ID_2"] = rd_id_2
        if rd_id_3 is not UNSET:
            field_dict["RD_ID_3"] = rd_id_3
        if rd_id_4 is not UNSET:
            field_dict["RD_ID_4"] = rd_id_4
        if remarks is not UNSET:
            field_dict["REMARKS"] = remarks
        if last_upd_date_v is not UNSET:
            field_dict["LAST_UPD_DATE_V"] = last_upd_date_v
        if building_address is not UNSET:
            field_dict["BUILDING_ADDRESS"] = building_address

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        run_in_out_id = d.pop("RUN_IN_OUT_ID", UNSET)

        def _parse_run_in_out_type(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        run_in_out_type = _parse_run_in_out_type(d.pop("RUN_IN_OUT_TYPE", UNSET))

        def _parse_parking_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parking_id = _parse_parking_id(d.pop("PARKING_ID", UNSET))

        def _parse_building_ename(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        building_ename = _parse_building_ename(d.pop("BUILDING_ENAME", UNSET))

        def _parse_building_cname(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        building_cname = _parse_building_cname(d.pop("BUILDING_CNAME", UNSET))

        cre_date = d.pop("CRE_DATE", UNSET)

        def _parse_rd_id_1(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        rd_id_1 = _parse_rd_id_1(d.pop("RD_ID_1", UNSET))

        def _parse_rd_id_2(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        rd_id_2 = _parse_rd_id_2(d.pop("RD_ID_2", UNSET))

        def _parse_rd_id_3(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        rd_id_3 = _parse_rd_id_3(d.pop("RD_ID_3", UNSET))

        def _parse_rd_id_4(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        rd_id_4 = _parse_rd_id_4(d.pop("RD_ID_4", UNSET))

        def _parse_remarks(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remarks = _parse_remarks(d.pop("REMARKS", UNSET))

        last_upd_date_v = d.pop("LAST_UPD_DATE_V", UNSET)

        def _parse_building_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        building_address = _parse_building_address(d.pop("BUILDING_ADDRESS", UNSET))

        arcgis_feature_server_arcgis_layer_3_attributes = cls(
            objectid=objectid,
            run_in_out_id=run_in_out_id,
            run_in_out_type=run_in_out_type,
            parking_id=parking_id,
            building_ename=building_ename,
            building_cname=building_cname,
            cre_date=cre_date,
            rd_id_1=rd_id_1,
            rd_id_2=rd_id_2,
            rd_id_3=rd_id_3,
            rd_id_4=rd_id_4,
            remarks=remarks,
            last_upd_date_v=last_upd_date_v,
            building_address=building_address,
        )

        arcgis_feature_server_arcgis_layer_3_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_3_attributes

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
