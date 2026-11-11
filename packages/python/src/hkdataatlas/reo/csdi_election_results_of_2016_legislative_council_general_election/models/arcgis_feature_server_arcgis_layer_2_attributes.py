from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer2Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer2Attributes:
    """
    Attributes:
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        pscode (None | str | Unset): Publisher field type: esriFieldTypeString
        ps_cname (None | str | Unset): Publisher field type: esriFieldTypeString
        ps_ename (None | str | Unset): Publisher field type: esriFieldTypeString
        addr_t (None | str | Unset): Publisher field type: esriFieldTypeString
        addr_e (None | str | Unset): Publisher field type: esriFieldTypeString
        accessible (None | str | Unset): Publisher field type: esriFieldTypeString
        list_num1 (None | str | Unset): Publisher field type: esriFieldTypeString
        list_num2 (None | str | Unset): Publisher field type: esriFieldTypeString
        list_num3 (None | str | Unset): Publisher field type: esriFieldTypeString
        list_num4 (None | str | Unset): Publisher field type: esriFieldTypeString
        list_num5 (None | str | Unset): Publisher field type: esriFieldTypeString
        list_num6 (None | str | Unset): Publisher field type: esriFieldTypeString
        list_num7 (None | str | Unset): Publisher field type: esriFieldTypeString
        list_num8 (None | str | Unset): Publisher field type: esriFieldTypeString
        list_num9 (None | str | Unset): Publisher field type: esriFieldTypeString
        list_num10 (None | str | Unset): Publisher field type: esriFieldTypeString
        list_num11 (None | str | Unset): Publisher field type: esriFieldTypeString
        list_num12 (None | str | Unset): Publisher field type: esriFieldTypeString
        list_num13 (None | str | Unset): Publisher field type: esriFieldTypeString
        list_num14 (None | str | Unset): Publisher field type: esriFieldTypeString
        list_num15 (None | str | Unset): Publisher field type: esriFieldTypeString
    """

    objectid: int | Unset = UNSET
    pscode: None | str | Unset = UNSET
    ps_cname: None | str | Unset = UNSET
    ps_ename: None | str | Unset = UNSET
    addr_t: None | str | Unset = UNSET
    addr_e: None | str | Unset = UNSET
    accessible: None | str | Unset = UNSET
    list_num1: None | str | Unset = UNSET
    list_num2: None | str | Unset = UNSET
    list_num3: None | str | Unset = UNSET
    list_num4: None | str | Unset = UNSET
    list_num5: None | str | Unset = UNSET
    list_num6: None | str | Unset = UNSET
    list_num7: None | str | Unset = UNSET
    list_num8: None | str | Unset = UNSET
    list_num9: None | str | Unset = UNSET
    list_num10: None | str | Unset = UNSET
    list_num11: None | str | Unset = UNSET
    list_num12: None | str | Unset = UNSET
    list_num13: None | str | Unset = UNSET
    list_num14: None | str | Unset = UNSET
    list_num15: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        pscode: None | str | Unset
        if isinstance(self.pscode, Unset):
            pscode = UNSET
        else:
            pscode = self.pscode

        ps_cname: None | str | Unset
        if isinstance(self.ps_cname, Unset):
            ps_cname = UNSET
        else:
            ps_cname = self.ps_cname

        ps_ename: None | str | Unset
        if isinstance(self.ps_ename, Unset):
            ps_ename = UNSET
        else:
            ps_ename = self.ps_ename

        addr_t: None | str | Unset
        if isinstance(self.addr_t, Unset):
            addr_t = UNSET
        else:
            addr_t = self.addr_t

        addr_e: None | str | Unset
        if isinstance(self.addr_e, Unset):
            addr_e = UNSET
        else:
            addr_e = self.addr_e

        accessible: None | str | Unset
        if isinstance(self.accessible, Unset):
            accessible = UNSET
        else:
            accessible = self.accessible

        list_num1: None | str | Unset
        if isinstance(self.list_num1, Unset):
            list_num1 = UNSET
        else:
            list_num1 = self.list_num1

        list_num2: None | str | Unset
        if isinstance(self.list_num2, Unset):
            list_num2 = UNSET
        else:
            list_num2 = self.list_num2

        list_num3: None | str | Unset
        if isinstance(self.list_num3, Unset):
            list_num3 = UNSET
        else:
            list_num3 = self.list_num3

        list_num4: None | str | Unset
        if isinstance(self.list_num4, Unset):
            list_num4 = UNSET
        else:
            list_num4 = self.list_num4

        list_num5: None | str | Unset
        if isinstance(self.list_num5, Unset):
            list_num5 = UNSET
        else:
            list_num5 = self.list_num5

        list_num6: None | str | Unset
        if isinstance(self.list_num6, Unset):
            list_num6 = UNSET
        else:
            list_num6 = self.list_num6

        list_num7: None | str | Unset
        if isinstance(self.list_num7, Unset):
            list_num7 = UNSET
        else:
            list_num7 = self.list_num7

        list_num8: None | str | Unset
        if isinstance(self.list_num8, Unset):
            list_num8 = UNSET
        else:
            list_num8 = self.list_num8

        list_num9: None | str | Unset
        if isinstance(self.list_num9, Unset):
            list_num9 = UNSET
        else:
            list_num9 = self.list_num9

        list_num10: None | str | Unset
        if isinstance(self.list_num10, Unset):
            list_num10 = UNSET
        else:
            list_num10 = self.list_num10

        list_num11: None | str | Unset
        if isinstance(self.list_num11, Unset):
            list_num11 = UNSET
        else:
            list_num11 = self.list_num11

        list_num12: None | str | Unset
        if isinstance(self.list_num12, Unset):
            list_num12 = UNSET
        else:
            list_num12 = self.list_num12

        list_num13: None | str | Unset
        if isinstance(self.list_num13, Unset):
            list_num13 = UNSET
        else:
            list_num13 = self.list_num13

        list_num14: None | str | Unset
        if isinstance(self.list_num14, Unset):
            list_num14 = UNSET
        else:
            list_num14 = self.list_num14

        list_num15: None | str | Unset
        if isinstance(self.list_num15, Unset):
            list_num15 = UNSET
        else:
            list_num15 = self.list_num15

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if pscode is not UNSET:
            field_dict["PSCODE"] = pscode
        if ps_cname is not UNSET:
            field_dict["PS_CNAME"] = ps_cname
        if ps_ename is not UNSET:
            field_dict["PS_ENAME"] = ps_ename
        if addr_t is not UNSET:
            field_dict["ADDR_T"] = addr_t
        if addr_e is not UNSET:
            field_dict["ADDR_E"] = addr_e
        if accessible is not UNSET:
            field_dict["ACCESSIBLE"] = accessible
        if list_num1 is not UNSET:
            field_dict["LIST_NUM1"] = list_num1
        if list_num2 is not UNSET:
            field_dict["LIST_NUM2"] = list_num2
        if list_num3 is not UNSET:
            field_dict["LIST_NUM3"] = list_num3
        if list_num4 is not UNSET:
            field_dict["LIST_NUM4"] = list_num4
        if list_num5 is not UNSET:
            field_dict["LIST_NUM5"] = list_num5
        if list_num6 is not UNSET:
            field_dict["LIST_NUM6"] = list_num6
        if list_num7 is not UNSET:
            field_dict["LIST_NUM7"] = list_num7
        if list_num8 is not UNSET:
            field_dict["LIST_NUM8"] = list_num8
        if list_num9 is not UNSET:
            field_dict["LIST_NUM9"] = list_num9
        if list_num10 is not UNSET:
            field_dict["LIST_NUM10"] = list_num10
        if list_num11 is not UNSET:
            field_dict["LIST_NUM11"] = list_num11
        if list_num12 is not UNSET:
            field_dict["LIST_NUM12"] = list_num12
        if list_num13 is not UNSET:
            field_dict["LIST_NUM13"] = list_num13
        if list_num14 is not UNSET:
            field_dict["LIST_NUM14"] = list_num14
        if list_num15 is not UNSET:
            field_dict["LIST_NUM15"] = list_num15

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_pscode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pscode = _parse_pscode(d.pop("PSCODE", UNSET))

        def _parse_ps_cname(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ps_cname = _parse_ps_cname(d.pop("PS_CNAME", UNSET))

        def _parse_ps_ename(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ps_ename = _parse_ps_ename(d.pop("PS_ENAME", UNSET))

        def _parse_addr_t(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        addr_t = _parse_addr_t(d.pop("ADDR_T", UNSET))

        def _parse_addr_e(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        addr_e = _parse_addr_e(d.pop("ADDR_E", UNSET))

        def _parse_accessible(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        accessible = _parse_accessible(d.pop("ACCESSIBLE", UNSET))

        def _parse_list_num1(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        list_num1 = _parse_list_num1(d.pop("LIST_NUM1", UNSET))

        def _parse_list_num2(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        list_num2 = _parse_list_num2(d.pop("LIST_NUM2", UNSET))

        def _parse_list_num3(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        list_num3 = _parse_list_num3(d.pop("LIST_NUM3", UNSET))

        def _parse_list_num4(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        list_num4 = _parse_list_num4(d.pop("LIST_NUM4", UNSET))

        def _parse_list_num5(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        list_num5 = _parse_list_num5(d.pop("LIST_NUM5", UNSET))

        def _parse_list_num6(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        list_num6 = _parse_list_num6(d.pop("LIST_NUM6", UNSET))

        def _parse_list_num7(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        list_num7 = _parse_list_num7(d.pop("LIST_NUM7", UNSET))

        def _parse_list_num8(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        list_num8 = _parse_list_num8(d.pop("LIST_NUM8", UNSET))

        def _parse_list_num9(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        list_num9 = _parse_list_num9(d.pop("LIST_NUM9", UNSET))

        def _parse_list_num10(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        list_num10 = _parse_list_num10(d.pop("LIST_NUM10", UNSET))

        def _parse_list_num11(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        list_num11 = _parse_list_num11(d.pop("LIST_NUM11", UNSET))

        def _parse_list_num12(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        list_num12 = _parse_list_num12(d.pop("LIST_NUM12", UNSET))

        def _parse_list_num13(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        list_num13 = _parse_list_num13(d.pop("LIST_NUM13", UNSET))

        def _parse_list_num14(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        list_num14 = _parse_list_num14(d.pop("LIST_NUM14", UNSET))

        def _parse_list_num15(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        list_num15 = _parse_list_num15(d.pop("LIST_NUM15", UNSET))

        arcgis_feature_server_arcgis_layer_2_attributes = cls(
            objectid=objectid,
            pscode=pscode,
            ps_cname=ps_cname,
            ps_ename=ps_ename,
            addr_t=addr_t,
            addr_e=addr_e,
            accessible=accessible,
            list_num1=list_num1,
            list_num2=list_num2,
            list_num3=list_num3,
            list_num4=list_num4,
            list_num5=list_num5,
            list_num6=list_num6,
            list_num7=list_num7,
            list_num8=list_num8,
            list_num9=list_num9,
            list_num10=list_num10,
            list_num11=list_num11,
            list_num12=list_num12,
            list_num13=list_num13,
            list_num14=list_num14,
            list_num15=list_num15,
        )

        arcgis_feature_server_arcgis_layer_2_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_2_attributes

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
