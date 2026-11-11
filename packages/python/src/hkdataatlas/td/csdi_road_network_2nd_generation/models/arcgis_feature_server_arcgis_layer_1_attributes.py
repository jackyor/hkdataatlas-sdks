from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer1Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer1Attributes:
    """
    Attributes:
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        feature_type (int | None | Unset): Publisher field type: esriFieldTypeSmallInteger
        feature_id (int | Unset): Publisher field type: esriFieldTypeInteger
        cre_date (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains unknown.
        rd_id_1 (int | None | Unset): Publisher field type: esriFieldTypeInteger
        rd_id_2 (int | None | Unset): Publisher field type: esriFieldTypeInteger
        rd_id_3 (int | None | Unset): Publisher field type: esriFieldTypeInteger
        rd_id_4 (int | None | Unset): Publisher field type: esriFieldTypeInteger
        rd_id_5 (int | None | Unset): Publisher field type: esriFieldTypeInteger
        rd_id_6 (int | None | Unset): Publisher field type: esriFieldTypeInteger
        remarks (None | str | Unset): Publisher field type: esriFieldTypeString
        tun_bridge_id (int | None | Unset): Publisher field type: esriFieldTypeInteger
        last_upd_date_v (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains
            unknown.
        rd_id_7 (int | None | Unset): Publisher field type: esriFieldTypeInteger
        rd_id_8 (int | None | Unset): Publisher field type: esriFieldTypeInteger
        rd_id_9 (int | None | Unset): Publisher field type: esriFieldTypeInteger
    """

    objectid: int | Unset = UNSET
    feature_type: int | None | Unset = UNSET
    feature_id: int | Unset = UNSET
    cre_date: Any | Unset = UNSET
    rd_id_1: int | None | Unset = UNSET
    rd_id_2: int | None | Unset = UNSET
    rd_id_3: int | None | Unset = UNSET
    rd_id_4: int | None | Unset = UNSET
    rd_id_5: int | None | Unset = UNSET
    rd_id_6: int | None | Unset = UNSET
    remarks: None | str | Unset = UNSET
    tun_bridge_id: int | None | Unset = UNSET
    last_upd_date_v: Any | Unset = UNSET
    rd_id_7: int | None | Unset = UNSET
    rd_id_8: int | None | Unset = UNSET
    rd_id_9: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        feature_type: int | None | Unset
        if isinstance(self.feature_type, Unset):
            feature_type = UNSET
        else:
            feature_type = self.feature_type

        feature_id = self.feature_id

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

        rd_id_5: int | None | Unset
        if isinstance(self.rd_id_5, Unset):
            rd_id_5 = UNSET
        else:
            rd_id_5 = self.rd_id_5

        rd_id_6: int | None | Unset
        if isinstance(self.rd_id_6, Unset):
            rd_id_6 = UNSET
        else:
            rd_id_6 = self.rd_id_6

        remarks: None | str | Unset
        if isinstance(self.remarks, Unset):
            remarks = UNSET
        else:
            remarks = self.remarks

        tun_bridge_id: int | None | Unset
        if isinstance(self.tun_bridge_id, Unset):
            tun_bridge_id = UNSET
        else:
            tun_bridge_id = self.tun_bridge_id

        last_upd_date_v = self.last_upd_date_v

        rd_id_7: int | None | Unset
        if isinstance(self.rd_id_7, Unset):
            rd_id_7 = UNSET
        else:
            rd_id_7 = self.rd_id_7

        rd_id_8: int | None | Unset
        if isinstance(self.rd_id_8, Unset):
            rd_id_8 = UNSET
        else:
            rd_id_8 = self.rd_id_8

        rd_id_9: int | None | Unset
        if isinstance(self.rd_id_9, Unset):
            rd_id_9 = UNSET
        else:
            rd_id_9 = self.rd_id_9

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if feature_type is not UNSET:
            field_dict["FEATURE_TYPE"] = feature_type
        if feature_id is not UNSET:
            field_dict["FEATURE_ID"] = feature_id
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
        if rd_id_5 is not UNSET:
            field_dict["RD_ID_5"] = rd_id_5
        if rd_id_6 is not UNSET:
            field_dict["RD_ID_6"] = rd_id_6
        if remarks is not UNSET:
            field_dict["REMARKS"] = remarks
        if tun_bridge_id is not UNSET:
            field_dict["TUN_BRIDGE_ID"] = tun_bridge_id
        if last_upd_date_v is not UNSET:
            field_dict["LAST_UPD_DATE_V"] = last_upd_date_v
        if rd_id_7 is not UNSET:
            field_dict["RD_ID_7"] = rd_id_7
        if rd_id_8 is not UNSET:
            field_dict["RD_ID_8"] = rd_id_8
        if rd_id_9 is not UNSET:
            field_dict["RD_ID_9"] = rd_id_9

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_feature_type(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        feature_type = _parse_feature_type(d.pop("FEATURE_TYPE", UNSET))

        feature_id = d.pop("FEATURE_ID", UNSET)

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

        def _parse_rd_id_5(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        rd_id_5 = _parse_rd_id_5(d.pop("RD_ID_5", UNSET))

        def _parse_rd_id_6(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        rd_id_6 = _parse_rd_id_6(d.pop("RD_ID_6", UNSET))

        def _parse_remarks(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remarks = _parse_remarks(d.pop("REMARKS", UNSET))

        def _parse_tun_bridge_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        tun_bridge_id = _parse_tun_bridge_id(d.pop("TUN_BRIDGE_ID", UNSET))

        last_upd_date_v = d.pop("LAST_UPD_DATE_V", UNSET)

        def _parse_rd_id_7(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        rd_id_7 = _parse_rd_id_7(d.pop("RD_ID_7", UNSET))

        def _parse_rd_id_8(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        rd_id_8 = _parse_rd_id_8(d.pop("RD_ID_8", UNSET))

        def _parse_rd_id_9(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        rd_id_9 = _parse_rd_id_9(d.pop("RD_ID_9", UNSET))

        arcgis_feature_server_arcgis_layer_1_attributes = cls(
            objectid=objectid,
            feature_type=feature_type,
            feature_id=feature_id,
            cre_date=cre_date,
            rd_id_1=rd_id_1,
            rd_id_2=rd_id_2,
            rd_id_3=rd_id_3,
            rd_id_4=rd_id_4,
            rd_id_5=rd_id_5,
            rd_id_6=rd_id_6,
            remarks=remarks,
            tun_bridge_id=tun_bridge_id,
            last_upd_date_v=last_upd_date_v,
            rd_id_7=rd_id_7,
            rd_id_8=rd_id_8,
            rd_id_9=rd_id_9,
        )

        arcgis_feature_server_arcgis_layer_1_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_1_attributes

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
