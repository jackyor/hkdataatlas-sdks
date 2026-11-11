from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsGRATINGGULLYEMMSMMSAttributes")


@_attrs_define
class WfsMapServerWfsGRATINGGULLYEMMSMMSAttributes:
    """
    Attributes:
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
        lvl (int | None | Unset): Native XSD type xsd:short. Requiredness is not projected from XML occurrence into all
            JSON queries.
        gr_uid (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
    """

    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    lvl: int | None | Unset = UNSET
    gr_uid: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        shape = self.shape

        lvl: int | None | Unset
        if isinstance(self.lvl, Unset):
            lvl = UNSET
        else:
            lvl = self.lvl

        gr_uid: None | str | Unset
        if isinstance(self.gr_uid, Unset):
            gr_uid = UNSET
        else:
            gr_uid = self.gr_uid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["Shape"] = shape
        if lvl is not UNSET:
            field_dict["LVL"] = lvl
        if gr_uid is not UNSET:
            field_dict["GR_UID"] = gr_uid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("Shape", UNSET)

        def _parse_lvl(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        lvl = _parse_lvl(d.pop("LVL", UNSET))

        def _parse_gr_uid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gr_uid = _parse_gr_uid(d.pop("GR_UID", UNSET))

        wfs_map_server_wfs_gratinggullyemmsmms_attributes = cls(
            objectid=objectid,
            shape=shape,
            lvl=lvl,
            gr_uid=gr_uid,
        )

        wfs_map_server_wfs_gratinggullyemmsmms_attributes.additional_properties = d
        return wfs_map_server_wfs_gratinggullyemmsmms_attributes

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
