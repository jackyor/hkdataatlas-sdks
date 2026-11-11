from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsPilotBoardingStnAttributes")


@_attrs_define
class WfsMapServerWfsPilotBoardingStnAttributes:
    """
    Attributes:
        objnam (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        inform (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:MultiPointPropertyType; JSON geometry is not inferred from its
            XML type.
    """

    objnam: None | str | Unset = UNSET
    inform: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objnam: None | str | Unset
        if isinstance(self.objnam, Unset):
            objnam = UNSET
        else:
            objnam = self.objnam

        inform: None | str | Unset
        if isinstance(self.inform, Unset):
            inform = UNSET
        else:
            inform = self.inform

        objectid = self.objectid

        shape = self.shape

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objnam is not UNSET:
            field_dict["OBJNAM"] = objnam
        if inform is not UNSET:
            field_dict["INFORM"] = inform
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["SHAPE"] = shape

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_objnam(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        objnam = _parse_objnam(d.pop("OBJNAM", UNSET))

        def _parse_inform(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        inform = _parse_inform(d.pop("INFORM", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("SHAPE", UNSET)

        wfs_map_server_wfs_pilot_boarding_stn_attributes = cls(
            objnam=objnam,
            inform=inform,
            objectid=objectid,
            shape=shape,
        )

        wfs_map_server_wfs_pilot_boarding_stn_attributes.additional_properties = d
        return wfs_map_server_wfs_pilot_boarding_stn_attributes

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
