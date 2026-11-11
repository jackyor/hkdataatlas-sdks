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
        pscode (None | str | Unset): Publisher field type: esriFieldTypeString
        ps_cname (None | str | Unset): Publisher field type: esriFieldTypeString
        ps_ename (None | str | Unset): Publisher field type: esriFieldTypeString
        addr_t (None | str | Unset): Publisher field type: esriFieldTypeString
        addr_e (None | str | Unset): Publisher field type: esriFieldTypeString
        accessible (None | str | Unset): Publisher field type: esriFieldTypeString
        candidate_num1 (None | str | Unset): Publisher field type: esriFieldTypeString
        candidate_num2 (None | str | Unset): Publisher field type: esriFieldTypeString
        candidate_num3 (None | str | Unset): Publisher field type: esriFieldTypeString
        candidate_num4 (None | str | Unset): Publisher field type: esriFieldTypeString
        candidate_num5 (None | str | Unset): Publisher field type: esriFieldTypeString
    """

    objectid: int | Unset = UNSET
    pscode: None | str | Unset = UNSET
    ps_cname: None | str | Unset = UNSET
    ps_ename: None | str | Unset = UNSET
    addr_t: None | str | Unset = UNSET
    addr_e: None | str | Unset = UNSET
    accessible: None | str | Unset = UNSET
    candidate_num1: None | str | Unset = UNSET
    candidate_num2: None | str | Unset = UNSET
    candidate_num3: None | str | Unset = UNSET
    candidate_num4: None | str | Unset = UNSET
    candidate_num5: None | str | Unset = UNSET
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

        candidate_num1: None | str | Unset
        if isinstance(self.candidate_num1, Unset):
            candidate_num1 = UNSET
        else:
            candidate_num1 = self.candidate_num1

        candidate_num2: None | str | Unset
        if isinstance(self.candidate_num2, Unset):
            candidate_num2 = UNSET
        else:
            candidate_num2 = self.candidate_num2

        candidate_num3: None | str | Unset
        if isinstance(self.candidate_num3, Unset):
            candidate_num3 = UNSET
        else:
            candidate_num3 = self.candidate_num3

        candidate_num4: None | str | Unset
        if isinstance(self.candidate_num4, Unset):
            candidate_num4 = UNSET
        else:
            candidate_num4 = self.candidate_num4

        candidate_num5: None | str | Unset
        if isinstance(self.candidate_num5, Unset):
            candidate_num5 = UNSET
        else:
            candidate_num5 = self.candidate_num5

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
        if candidate_num1 is not UNSET:
            field_dict["CANDIDATE_NUM1"] = candidate_num1
        if candidate_num2 is not UNSET:
            field_dict["CANDIDATE_NUM2"] = candidate_num2
        if candidate_num3 is not UNSET:
            field_dict["CANDIDATE_NUM3"] = candidate_num3
        if candidate_num4 is not UNSET:
            field_dict["CANDIDATE_NUM4"] = candidate_num4
        if candidate_num5 is not UNSET:
            field_dict["CANDIDATE_NUM5"] = candidate_num5

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

        def _parse_candidate_num1(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        candidate_num1 = _parse_candidate_num1(d.pop("CANDIDATE_NUM1", UNSET))

        def _parse_candidate_num2(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        candidate_num2 = _parse_candidate_num2(d.pop("CANDIDATE_NUM2", UNSET))

        def _parse_candidate_num3(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        candidate_num3 = _parse_candidate_num3(d.pop("CANDIDATE_NUM3", UNSET))

        def _parse_candidate_num4(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        candidate_num4 = _parse_candidate_num4(d.pop("CANDIDATE_NUM4", UNSET))

        def _parse_candidate_num5(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        candidate_num5 = _parse_candidate_num5(d.pop("CANDIDATE_NUM5", UNSET))

        arcgis_feature_server_arcgis_layer_7_attributes = cls(
            objectid=objectid,
            pscode=pscode,
            ps_cname=ps_cname,
            ps_ename=ps_ename,
            addr_t=addr_t,
            addr_e=addr_e,
            accessible=accessible,
            candidate_num1=candidate_num1,
            candidate_num2=candidate_num2,
            candidate_num3=candidate_num3,
            candidate_num4=candidate_num4,
            candidate_num5=candidate_num5,
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
