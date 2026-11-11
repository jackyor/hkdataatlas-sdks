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
        lp_num (None | str | Unset): Publisher field type: esriFieldTypeString
        gm_north (float | None | Unset): Publisher field type: esriFieldTypeDouble
        gm_east (float | None | Unset): Publisher field type: esriFieldTypeDouble
        gm_id (None | str | Unset): Publisher field type: esriFieldTypeString
        gm_hgt (float | None | Unset): Publisher field type: esriFieldTypeDouble
        gm_url (None | str | Unset): Publisher field type: esriFieldTypeString
    """

    objectid: int | Unset = UNSET
    lp_num: None | str | Unset = UNSET
    gm_north: float | None | Unset = UNSET
    gm_east: float | None | Unset = UNSET
    gm_id: None | str | Unset = UNSET
    gm_hgt: float | None | Unset = UNSET
    gm_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        lp_num: None | str | Unset
        if isinstance(self.lp_num, Unset):
            lp_num = UNSET
        else:
            lp_num = self.lp_num

        gm_north: float | None | Unset
        if isinstance(self.gm_north, Unset):
            gm_north = UNSET
        else:
            gm_north = self.gm_north

        gm_east: float | None | Unset
        if isinstance(self.gm_east, Unset):
            gm_east = UNSET
        else:
            gm_east = self.gm_east

        gm_id: None | str | Unset
        if isinstance(self.gm_id, Unset):
            gm_id = UNSET
        else:
            gm_id = self.gm_id

        gm_hgt: float | None | Unset
        if isinstance(self.gm_hgt, Unset):
            gm_hgt = UNSET
        else:
            gm_hgt = self.gm_hgt

        gm_url: None | str | Unset
        if isinstance(self.gm_url, Unset):
            gm_url = UNSET
        else:
            gm_url = self.gm_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if lp_num is not UNSET:
            field_dict["LP_NUM"] = lp_num
        if gm_north is not UNSET:
            field_dict["GM_NORTH"] = gm_north
        if gm_east is not UNSET:
            field_dict["GM_EAST"] = gm_east
        if gm_id is not UNSET:
            field_dict["GM_ID"] = gm_id
        if gm_hgt is not UNSET:
            field_dict["GM_HGT"] = gm_hgt
        if gm_url is not UNSET:
            field_dict["GM_URL"] = gm_url

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_lp_num(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lp_num = _parse_lp_num(d.pop("LP_NUM", UNSET))

        def _parse_gm_north(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        gm_north = _parse_gm_north(d.pop("GM_NORTH", UNSET))

        def _parse_gm_east(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        gm_east = _parse_gm_east(d.pop("GM_EAST", UNSET))

        def _parse_gm_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gm_id = _parse_gm_id(d.pop("GM_ID", UNSET))

        def _parse_gm_hgt(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        gm_hgt = _parse_gm_hgt(d.pop("GM_HGT", UNSET))

        def _parse_gm_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gm_url = _parse_gm_url(d.pop("GM_URL", UNSET))

        arcgis_feature_server_arcgis_layer_1000_attributes = cls(
            objectid=objectid,
            lp_num=lp_num,
            gm_north=gm_north,
            gm_east=gm_east,
            gm_id=gm_id,
            gm_hgt=gm_hgt,
            gm_url=gm_url,
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
