from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsMAJORMINESAttributes")


@_attrs_define
class WfsMapServerWfsMAJORMINESAttributes:
    """
    Attributes:
        mineral (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        m_code (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:MultiPointPropertyType; JSON geometry is not inferred from its
            XML type.
    """

    mineral: None | str | Unset = UNSET
    m_code: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mineral: None | str | Unset
        if isinstance(self.mineral, Unset):
            mineral = UNSET
        else:
            mineral = self.mineral

        m_code: None | str | Unset
        if isinstance(self.m_code, Unset):
            m_code = UNSET
        else:
            m_code = self.m_code

        objectid = self.objectid

        shape = self.shape

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mineral is not UNSET:
            field_dict["MINERAL"] = mineral
        if m_code is not UNSET:
            field_dict["M_Code"] = m_code
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["SHAPE"] = shape

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_mineral(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mineral = _parse_mineral(d.pop("MINERAL", UNSET))

        def _parse_m_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        m_code = _parse_m_code(d.pop("M_Code", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("SHAPE", UNSET)

        wfs_map_server_wfs_majormines_attributes = cls(
            mineral=mineral,
            m_code=m_code,
            objectid=objectid,
            shape=shape,
        )

        wfs_map_server_wfs_majormines_attributes.additional_properties = d
        return wfs_map_server_wfs_majormines_attributes

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
