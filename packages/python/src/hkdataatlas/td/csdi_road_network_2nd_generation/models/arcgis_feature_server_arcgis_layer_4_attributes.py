from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer4Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer4Attributes:
    """
    Attributes:
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        cre_date (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains unknown.
        r_about_id (int | Unset): Publisher field type: esriFieldTypeInteger
        r_about_ename (None | str | Unset): Publisher field type: esriFieldTypeString
        r_about_cname (None | str | Unset): Publisher field type: esriFieldTypeString
        r_about_type (int | None | Unset): Publisher field type: esriFieldTypeSmallInteger
        graded (None | str | Unset): Publisher field type: esriFieldTypeString
        signalized (None | str | Unset): Publisher field type: esriFieldTypeString
        no_of_arm (int | None | Unset): Publisher field type: esriFieldTypeSmallInteger
        rd_id_1 (int | None | Unset): Publisher field type: esriFieldTypeInteger
        rd_id_2 (int | None | Unset): Publisher field type: esriFieldTypeInteger
        rd_id_3 (int | None | Unset): Publisher field type: esriFieldTypeInteger
        rd_id_4 (int | None | Unset): Publisher field type: esriFieldTypeInteger
        rd_id_5 (int | None | Unset): Publisher field type: esriFieldTypeInteger
        rd_id_6 (int | None | Unset): Publisher field type: esriFieldTypeInteger
        rd_id_7 (int | None | Unset): Publisher field type: esriFieldTypeInteger
        rd_id_8 (int | None | Unset): Publisher field type: esriFieldTypeInteger
        rd_id_9 (int | None | Unset): Publisher field type: esriFieldTypeInteger
        rd_id_10 (int | None | Unset): Publisher field type: esriFieldTypeInteger
        remarks (None | str | Unset): Publisher field type: esriFieldTypeString
        last_upd_date_v (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains
            unknown.
    """

    objectid: int | Unset = UNSET
    cre_date: Any | Unset = UNSET
    r_about_id: int | Unset = UNSET
    r_about_ename: None | str | Unset = UNSET
    r_about_cname: None | str | Unset = UNSET
    r_about_type: int | None | Unset = UNSET
    graded: None | str | Unset = UNSET
    signalized: None | str | Unset = UNSET
    no_of_arm: int | None | Unset = UNSET
    rd_id_1: int | None | Unset = UNSET
    rd_id_2: int | None | Unset = UNSET
    rd_id_3: int | None | Unset = UNSET
    rd_id_4: int | None | Unset = UNSET
    rd_id_5: int | None | Unset = UNSET
    rd_id_6: int | None | Unset = UNSET
    rd_id_7: int | None | Unset = UNSET
    rd_id_8: int | None | Unset = UNSET
    rd_id_9: int | None | Unset = UNSET
    rd_id_10: int | None | Unset = UNSET
    remarks: None | str | Unset = UNSET
    last_upd_date_v: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        cre_date = self.cre_date

        r_about_id = self.r_about_id

        r_about_ename: None | str | Unset
        if isinstance(self.r_about_ename, Unset):
            r_about_ename = UNSET
        else:
            r_about_ename = self.r_about_ename

        r_about_cname: None | str | Unset
        if isinstance(self.r_about_cname, Unset):
            r_about_cname = UNSET
        else:
            r_about_cname = self.r_about_cname

        r_about_type: int | None | Unset
        if isinstance(self.r_about_type, Unset):
            r_about_type = UNSET
        else:
            r_about_type = self.r_about_type

        graded: None | str | Unset
        if isinstance(self.graded, Unset):
            graded = UNSET
        else:
            graded = self.graded

        signalized: None | str | Unset
        if isinstance(self.signalized, Unset):
            signalized = UNSET
        else:
            signalized = self.signalized

        no_of_arm: int | None | Unset
        if isinstance(self.no_of_arm, Unset):
            no_of_arm = UNSET
        else:
            no_of_arm = self.no_of_arm

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

        rd_id_10: int | None | Unset
        if isinstance(self.rd_id_10, Unset):
            rd_id_10 = UNSET
        else:
            rd_id_10 = self.rd_id_10

        remarks: None | str | Unset
        if isinstance(self.remarks, Unset):
            remarks = UNSET
        else:
            remarks = self.remarks

        last_upd_date_v = self.last_upd_date_v

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if cre_date is not UNSET:
            field_dict["CRE_DATE"] = cre_date
        if r_about_id is not UNSET:
            field_dict["R_ABOUT_ID"] = r_about_id
        if r_about_ename is not UNSET:
            field_dict["R_ABOUT_ENAME"] = r_about_ename
        if r_about_cname is not UNSET:
            field_dict["R_ABOUT_CNAME"] = r_about_cname
        if r_about_type is not UNSET:
            field_dict["R_ABOUT_TYPE"] = r_about_type
        if graded is not UNSET:
            field_dict["GRADED"] = graded
        if signalized is not UNSET:
            field_dict["SIGNALIZED"] = signalized
        if no_of_arm is not UNSET:
            field_dict["NO_OF_ARM"] = no_of_arm
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
        if rd_id_7 is not UNSET:
            field_dict["RD_ID_7"] = rd_id_7
        if rd_id_8 is not UNSET:
            field_dict["RD_ID_8"] = rd_id_8
        if rd_id_9 is not UNSET:
            field_dict["RD_ID_9"] = rd_id_9
        if rd_id_10 is not UNSET:
            field_dict["RD_ID_10"] = rd_id_10
        if remarks is not UNSET:
            field_dict["REMARKS"] = remarks
        if last_upd_date_v is not UNSET:
            field_dict["LAST_UPD_DATE_V"] = last_upd_date_v

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        cre_date = d.pop("CRE_DATE", UNSET)

        r_about_id = d.pop("R_ABOUT_ID", UNSET)

        def _parse_r_about_ename(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        r_about_ename = _parse_r_about_ename(d.pop("R_ABOUT_ENAME", UNSET))

        def _parse_r_about_cname(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        r_about_cname = _parse_r_about_cname(d.pop("R_ABOUT_CNAME", UNSET))

        def _parse_r_about_type(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        r_about_type = _parse_r_about_type(d.pop("R_ABOUT_TYPE", UNSET))

        def _parse_graded(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        graded = _parse_graded(d.pop("GRADED", UNSET))

        def _parse_signalized(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        signalized = _parse_signalized(d.pop("SIGNALIZED", UNSET))

        def _parse_no_of_arm(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        no_of_arm = _parse_no_of_arm(d.pop("NO_OF_ARM", UNSET))

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

        def _parse_rd_id_10(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        rd_id_10 = _parse_rd_id_10(d.pop("RD_ID_10", UNSET))

        def _parse_remarks(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remarks = _parse_remarks(d.pop("REMARKS", UNSET))

        last_upd_date_v = d.pop("LAST_UPD_DATE_V", UNSET)

        arcgis_feature_server_arcgis_layer_4_attributes = cls(
            objectid=objectid,
            cre_date=cre_date,
            r_about_id=r_about_id,
            r_about_ename=r_about_ename,
            r_about_cname=r_about_cname,
            r_about_type=r_about_type,
            graded=graded,
            signalized=signalized,
            no_of_arm=no_of_arm,
            rd_id_1=rd_id_1,
            rd_id_2=rd_id_2,
            rd_id_3=rd_id_3,
            rd_id_4=rd_id_4,
            rd_id_5=rd_id_5,
            rd_id_6=rd_id_6,
            rd_id_7=rd_id_7,
            rd_id_8=rd_id_8,
            rd_id_9=rd_id_9,
            rd_id_10=rd_id_10,
            remarks=remarks,
            last_upd_date_v=last_upd_date_v,
        )

        arcgis_feature_server_arcgis_layer_4_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_4_attributes

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
