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
        vpid (None | str | Unset): Publisher field type: esriFieldTypeString
        desc_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        desc_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        desc_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        x (int | None | Unset): Publisher field type: esriFieldTypeInteger
        y (int | None | Unset): Publisher field type: esriFieldTypeInteger
        z (float | None | Unset): Publisher field type: esriFieldTypeDouble
        orient_deg (int | None | Unset): Publisher field type: esriFieldTypeInteger
        lp_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        lp_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        lp_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        map_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        map_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        map_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        ortho_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        ortho_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        ortho_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        pan_e_tc_1 (None | str | Unset): Publisher field type: esriFieldTypeString
        pan_e_sc_1 (None | str | Unset): Publisher field type: esriFieldTypeString
        pan_e_tc_2 (None | str | Unset): Publisher field type: esriFieldTypeString
        pan_e_sc_2 (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    vpid: None | str | Unset = UNSET
    desc_eng: None | str | Unset = UNSET
    desc_tc: None | str | Unset = UNSET
    desc_sc: None | str | Unset = UNSET
    x: int | None | Unset = UNSET
    y: int | None | Unset = UNSET
    z: float | None | Unset = UNSET
    orient_deg: int | None | Unset = UNSET
    lp_eng: None | str | Unset = UNSET
    lp_tc: None | str | Unset = UNSET
    lp_sc: None | str | Unset = UNSET
    map_eng: None | str | Unset = UNSET
    map_tc: None | str | Unset = UNSET
    map_sc: None | str | Unset = UNSET
    ortho_eng: None | str | Unset = UNSET
    ortho_tc: None | str | Unset = UNSET
    ortho_sc: None | str | Unset = UNSET
    pan_e_tc_1: None | str | Unset = UNSET
    pan_e_sc_1: None | str | Unset = UNSET
    pan_e_tc_2: None | str | Unset = UNSET
    pan_e_sc_2: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vpid: None | str | Unset
        if isinstance(self.vpid, Unset):
            vpid = UNSET
        else:
            vpid = self.vpid

        desc_eng: None | str | Unset
        if isinstance(self.desc_eng, Unset):
            desc_eng = UNSET
        else:
            desc_eng = self.desc_eng

        desc_tc: None | str | Unset
        if isinstance(self.desc_tc, Unset):
            desc_tc = UNSET
        else:
            desc_tc = self.desc_tc

        desc_sc: None | str | Unset
        if isinstance(self.desc_sc, Unset):
            desc_sc = UNSET
        else:
            desc_sc = self.desc_sc

        x: int | None | Unset
        if isinstance(self.x, Unset):
            x = UNSET
        else:
            x = self.x

        y: int | None | Unset
        if isinstance(self.y, Unset):
            y = UNSET
        else:
            y = self.y

        z: float | None | Unset
        if isinstance(self.z, Unset):
            z = UNSET
        else:
            z = self.z

        orient_deg: int | None | Unset
        if isinstance(self.orient_deg, Unset):
            orient_deg = UNSET
        else:
            orient_deg = self.orient_deg

        lp_eng: None | str | Unset
        if isinstance(self.lp_eng, Unset):
            lp_eng = UNSET
        else:
            lp_eng = self.lp_eng

        lp_tc: None | str | Unset
        if isinstance(self.lp_tc, Unset):
            lp_tc = UNSET
        else:
            lp_tc = self.lp_tc

        lp_sc: None | str | Unset
        if isinstance(self.lp_sc, Unset):
            lp_sc = UNSET
        else:
            lp_sc = self.lp_sc

        map_eng: None | str | Unset
        if isinstance(self.map_eng, Unset):
            map_eng = UNSET
        else:
            map_eng = self.map_eng

        map_tc: None | str | Unset
        if isinstance(self.map_tc, Unset):
            map_tc = UNSET
        else:
            map_tc = self.map_tc

        map_sc: None | str | Unset
        if isinstance(self.map_sc, Unset):
            map_sc = UNSET
        else:
            map_sc = self.map_sc

        ortho_eng: None | str | Unset
        if isinstance(self.ortho_eng, Unset):
            ortho_eng = UNSET
        else:
            ortho_eng = self.ortho_eng

        ortho_tc: None | str | Unset
        if isinstance(self.ortho_tc, Unset):
            ortho_tc = UNSET
        else:
            ortho_tc = self.ortho_tc

        ortho_sc: None | str | Unset
        if isinstance(self.ortho_sc, Unset):
            ortho_sc = UNSET
        else:
            ortho_sc = self.ortho_sc

        pan_e_tc_1: None | str | Unset
        if isinstance(self.pan_e_tc_1, Unset):
            pan_e_tc_1 = UNSET
        else:
            pan_e_tc_1 = self.pan_e_tc_1

        pan_e_sc_1: None | str | Unset
        if isinstance(self.pan_e_sc_1, Unset):
            pan_e_sc_1 = UNSET
        else:
            pan_e_sc_1 = self.pan_e_sc_1

        pan_e_tc_2: None | str | Unset
        if isinstance(self.pan_e_tc_2, Unset):
            pan_e_tc_2 = UNSET
        else:
            pan_e_tc_2 = self.pan_e_tc_2

        pan_e_sc_2: None | str | Unset
        if isinstance(self.pan_e_sc_2, Unset):
            pan_e_sc_2 = UNSET
        else:
            pan_e_sc_2 = self.pan_e_sc_2

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if vpid is not UNSET:
            field_dict["VPID"] = vpid
        if desc_eng is not UNSET:
            field_dict["DESC_ENG"] = desc_eng
        if desc_tc is not UNSET:
            field_dict["DESC_TC"] = desc_tc
        if desc_sc is not UNSET:
            field_dict["DESC_SC"] = desc_sc
        if x is not UNSET:
            field_dict["X"] = x
        if y is not UNSET:
            field_dict["Y"] = y
        if z is not UNSET:
            field_dict["Z"] = z
        if orient_deg is not UNSET:
            field_dict["ORIENT_DEG"] = orient_deg
        if lp_eng is not UNSET:
            field_dict["LP_ENG"] = lp_eng
        if lp_tc is not UNSET:
            field_dict["LP_TC"] = lp_tc
        if lp_sc is not UNSET:
            field_dict["LP_SC"] = lp_sc
        if map_eng is not UNSET:
            field_dict["MAP_ENG"] = map_eng
        if map_tc is not UNSET:
            field_dict["MAP_TC"] = map_tc
        if map_sc is not UNSET:
            field_dict["MAP_SC"] = map_sc
        if ortho_eng is not UNSET:
            field_dict["ORTHO_ENG"] = ortho_eng
        if ortho_tc is not UNSET:
            field_dict["ORTHO_TC"] = ortho_tc
        if ortho_sc is not UNSET:
            field_dict["ORTHO_SC"] = ortho_sc
        if pan_e_tc_1 is not UNSET:
            field_dict["PAN_E_TC_1"] = pan_e_tc_1
        if pan_e_sc_1 is not UNSET:
            field_dict["PAN_E_SC_1"] = pan_e_sc_1
        if pan_e_tc_2 is not UNSET:
            field_dict["PAN_E_TC_2"] = pan_e_tc_2
        if pan_e_sc_2 is not UNSET:
            field_dict["PAN_E_SC_2"] = pan_e_sc_2
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_vpid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vpid = _parse_vpid(d.pop("VPID", UNSET))

        def _parse_desc_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        desc_eng = _parse_desc_eng(d.pop("DESC_ENG", UNSET))

        def _parse_desc_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        desc_tc = _parse_desc_tc(d.pop("DESC_TC", UNSET))

        def _parse_desc_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        desc_sc = _parse_desc_sc(d.pop("DESC_SC", UNSET))

        def _parse_x(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        x = _parse_x(d.pop("X", UNSET))

        def _parse_y(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        y = _parse_y(d.pop("Y", UNSET))

        def _parse_z(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        z = _parse_z(d.pop("Z", UNSET))

        def _parse_orient_deg(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        orient_deg = _parse_orient_deg(d.pop("ORIENT_DEG", UNSET))

        def _parse_lp_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lp_eng = _parse_lp_eng(d.pop("LP_ENG", UNSET))

        def _parse_lp_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lp_tc = _parse_lp_tc(d.pop("LP_TC", UNSET))

        def _parse_lp_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lp_sc = _parse_lp_sc(d.pop("LP_SC", UNSET))

        def _parse_map_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        map_eng = _parse_map_eng(d.pop("MAP_ENG", UNSET))

        def _parse_map_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        map_tc = _parse_map_tc(d.pop("MAP_TC", UNSET))

        def _parse_map_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        map_sc = _parse_map_sc(d.pop("MAP_SC", UNSET))

        def _parse_ortho_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ortho_eng = _parse_ortho_eng(d.pop("ORTHO_ENG", UNSET))

        def _parse_ortho_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ortho_tc = _parse_ortho_tc(d.pop("ORTHO_TC", UNSET))

        def _parse_ortho_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ortho_sc = _parse_ortho_sc(d.pop("ORTHO_SC", UNSET))

        def _parse_pan_e_tc_1(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pan_e_tc_1 = _parse_pan_e_tc_1(d.pop("PAN_E_TC_1", UNSET))

        def _parse_pan_e_sc_1(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pan_e_sc_1 = _parse_pan_e_sc_1(d.pop("PAN_E_SC_1", UNSET))

        def _parse_pan_e_tc_2(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pan_e_tc_2 = _parse_pan_e_tc_2(d.pop("PAN_E_TC_2", UNSET))

        def _parse_pan_e_sc_2(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pan_e_sc_2 = _parse_pan_e_sc_2(d.pop("PAN_E_SC_2", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            vpid=vpid,
            desc_eng=desc_eng,
            desc_tc=desc_tc,
            desc_sc=desc_sc,
            x=x,
            y=y,
            z=z,
            orient_deg=orient_deg,
            lp_eng=lp_eng,
            lp_tc=lp_tc,
            lp_sc=lp_sc,
            map_eng=map_eng,
            map_tc=map_tc,
            map_sc=map_sc,
            ortho_eng=ortho_eng,
            ortho_tc=ortho_tc,
            ortho_sc=ortho_sc,
            pan_e_tc_1=pan_e_tc_1,
            pan_e_sc_1=pan_e_sc_1,
            pan_e_tc_2=pan_e_tc_2,
            pan_e_sc_2=pan_e_sc_2,
            objectid=objectid,
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
