from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer0Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer0Attributes:
    """
    Attributes:
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        chainage (float | None | Unset): Publisher field type: esriFieldTypeDouble
        lvl (int | None | Unset): Publisher field type: esriFieldTypeInteger
        tun_code (None | str | Unset): Publisher field type: esriFieldTypeString
        tcm_id (None | str | Unset): Publisher field type: esriFieldTypeString
    """

    objectid: int | Unset = UNSET
    chainage: float | None | Unset = UNSET
    lvl: int | None | Unset = UNSET
    tun_code: None | str | Unset = UNSET
    tcm_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        chainage: float | None | Unset
        if isinstance(self.chainage, Unset):
            chainage = UNSET
        else:
            chainage = self.chainage

        lvl: int | None | Unset
        if isinstance(self.lvl, Unset):
            lvl = UNSET
        else:
            lvl = self.lvl

        tun_code: None | str | Unset
        if isinstance(self.tun_code, Unset):
            tun_code = UNSET
        else:
            tun_code = self.tun_code

        tcm_id: None | str | Unset
        if isinstance(self.tcm_id, Unset):
            tcm_id = UNSET
        else:
            tcm_id = self.tcm_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if chainage is not UNSET:
            field_dict["CHAINAGE"] = chainage
        if lvl is not UNSET:
            field_dict["LVL"] = lvl
        if tun_code is not UNSET:
            field_dict["TUN_CODE"] = tun_code
        if tcm_id is not UNSET:
            field_dict["TCM_ID"] = tcm_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_chainage(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        chainage = _parse_chainage(d.pop("CHAINAGE", UNSET))

        def _parse_lvl(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        lvl = _parse_lvl(d.pop("LVL", UNSET))

        def _parse_tun_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tun_code = _parse_tun_code(d.pop("TUN_CODE", UNSET))

        def _parse_tcm_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tcm_id = _parse_tcm_id(d.pop("TCM_ID", UNSET))

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            objectid=objectid,
            chainage=chainage,
            lvl=lvl,
            tun_code=tun_code,
            tcm_id=tcm_id,
        )

        arcgis_feature_server_arcgis_layer_0_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_0_attributes

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
