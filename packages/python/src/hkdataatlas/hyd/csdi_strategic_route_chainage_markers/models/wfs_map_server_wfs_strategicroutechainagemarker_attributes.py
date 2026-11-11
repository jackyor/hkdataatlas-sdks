from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsSTRATEGICROUTECHAINAGEMARKERAttributes")


@_attrs_define
class WfsMapServerWfsSTRATEGICROUTECHAINAGEMARKERAttributes:
    """
    Attributes:
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
        chainage (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        lvl (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all
            JSON queries.
        route_no (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into
            all JSON queries.
        ecm_id (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
    """

    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    chainage: float | None | Unset = UNSET
    lvl: int | None | Unset = UNSET
    route_no: int | None | Unset = UNSET
    ecm_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        shape = self.shape

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

        route_no: int | None | Unset
        if isinstance(self.route_no, Unset):
            route_no = UNSET
        else:
            route_no = self.route_no

        ecm_id: None | str | Unset
        if isinstance(self.ecm_id, Unset):
            ecm_id = UNSET
        else:
            ecm_id = self.ecm_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["Shape"] = shape
        if chainage is not UNSET:
            field_dict["CHAINAGE"] = chainage
        if lvl is not UNSET:
            field_dict["LVL"] = lvl
        if route_no is not UNSET:
            field_dict["ROUTE_NO"] = route_no
        if ecm_id is not UNSET:
            field_dict["ECM_ID"] = ecm_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("Shape", UNSET)

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

        def _parse_route_no(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        route_no = _parse_route_no(d.pop("ROUTE_NO", UNSET))

        def _parse_ecm_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ecm_id = _parse_ecm_id(d.pop("ECM_ID", UNSET))

        wfs_map_server_wfs_strategicroutechainagemarker_attributes = cls(
            objectid=objectid,
            shape=shape,
            chainage=chainage,
            lvl=lvl,
            route_no=route_no,
            ecm_id=ecm_id,
        )

        wfs_map_server_wfs_strategicroutechainagemarker_attributes.additional_properties = d
        return wfs_map_server_wfs_strategicroutechainagemarker_attributes

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
