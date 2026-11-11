from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfspointsAttributes")


@_attrs_define
class WfsMapServerWfspointsAttributes:
    """
    Attributes:
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
        name (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        popup_info (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
    """

    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    name: None | str | Unset = UNSET
    popup_info: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        shape = self.shape

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        popup_info: None | str | Unset
        if isinstance(self.popup_info, Unset):
            popup_info = UNSET
        else:
            popup_info = self.popup_info

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["Shape"] = shape
        if name is not UNSET:
            field_dict["Name"] = name
        if popup_info is not UNSET:
            field_dict["PopupInfo"] = popup_info

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("Shape", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("Name", UNSET))

        def _parse_popup_info(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        popup_info = _parse_popup_info(d.pop("PopupInfo", UNSET))

        wfs_map_server_wfspoints_attributes = cls(
            objectid=objectid,
            shape=shape,
            name=name,
            popup_info=popup_info,
        )

        wfs_map_server_wfspoints_attributes.additional_properties = d
        return wfs_map_server_wfspoints_attributes

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
