from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer1000Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer1000Attributes:
    """
    Attributes:
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        slope_no (str | Unset): Publisher field type: esriFieldTypeString
        sub_div_no (int | Unset): Publisher field type: esriFieldTypeInteger
        resp_pty (None | str | Unset): Publisher field type: esriFieldTypeString
        maint_agent (None | str | Unset): Publisher field type: esriFieldTypeString
    """

    objectid: int | Unset = UNSET
    slope_no: str | Unset = UNSET
    sub_div_no: int | Unset = UNSET
    resp_pty: None | str | Unset = UNSET
    maint_agent: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        slope_no = self.slope_no

        sub_div_no = self.sub_div_no

        resp_pty: None | str | Unset
        if isinstance(self.resp_pty, Unset):
            resp_pty = UNSET
        else:
            resp_pty = self.resp_pty

        maint_agent: None | str | Unset
        if isinstance(self.maint_agent, Unset):
            maint_agent = UNSET
        else:
            maint_agent = self.maint_agent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if slope_no is not UNSET:
            field_dict["SLOPE_NO"] = slope_no
        if sub_div_no is not UNSET:
            field_dict["SUB_DIV_NO"] = sub_div_no
        if resp_pty is not UNSET:
            field_dict["RESP_PTY"] = resp_pty
        if maint_agent is not UNSET:
            field_dict["MAINT_AGENT"] = maint_agent

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        slope_no = d.pop("SLOPE_NO", UNSET)

        sub_div_no = d.pop("SUB_DIV_NO", UNSET)

        def _parse_resp_pty(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resp_pty = _parse_resp_pty(d.pop("RESP_PTY", UNSET))

        def _parse_maint_agent(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        maint_agent = _parse_maint_agent(d.pop("MAINT_AGENT", UNSET))

        arcgis_feature_server_arcgis_layer_1000_attributes = cls(
            objectid=objectid,
            slope_no=slope_no,
            sub_div_no=sub_div_no,
            resp_pty=resp_pty,
            maint_agent=maint_agent,
        )

        arcgis_feature_server_arcgis_layer_1000_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_1000_attributes

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
