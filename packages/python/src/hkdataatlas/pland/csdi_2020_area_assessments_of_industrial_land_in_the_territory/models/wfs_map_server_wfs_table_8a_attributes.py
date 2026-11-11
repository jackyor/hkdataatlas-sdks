from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsTable8AAttributes")


@_attrs_define
class WfsMapServerWfsTable8AAttributes:
    """
    Attributes:
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        aa_code (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        aa_title (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        intended_to_relocate (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        not_intended_to_relocate (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from
            XML occurrence into all JSON queries.
    """

    objectid: int | Unset = UNSET
    aa_code: None | str | Unset = UNSET
    aa_title: None | str | Unset = UNSET
    intended_to_relocate: float | None | Unset = UNSET
    not_intended_to_relocate: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        aa_code: None | str | Unset
        if isinstance(self.aa_code, Unset):
            aa_code = UNSET
        else:
            aa_code = self.aa_code

        aa_title: None | str | Unset
        if isinstance(self.aa_title, Unset):
            aa_title = UNSET
        else:
            aa_title = self.aa_title

        intended_to_relocate: float | None | Unset
        if isinstance(self.intended_to_relocate, Unset):
            intended_to_relocate = UNSET
        else:
            intended_to_relocate = self.intended_to_relocate

        not_intended_to_relocate: float | None | Unset
        if isinstance(self.not_intended_to_relocate, Unset):
            not_intended_to_relocate = UNSET
        else:
            not_intended_to_relocate = self.not_intended_to_relocate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if aa_code is not UNSET:
            field_dict["AA_Code"] = aa_code
        if aa_title is not UNSET:
            field_dict["AA_Title"] = aa_title
        if intended_to_relocate is not UNSET:
            field_dict["Intended_to_relocate"] = intended_to_relocate
        if not_intended_to_relocate is not UNSET:
            field_dict["Not_intended_to_relocate"] = not_intended_to_relocate

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_aa_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        aa_code = _parse_aa_code(d.pop("AA_Code", UNSET))

        def _parse_aa_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        aa_title = _parse_aa_title(d.pop("AA_Title", UNSET))

        def _parse_intended_to_relocate(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        intended_to_relocate = _parse_intended_to_relocate(
            d.pop("Intended_to_relocate", UNSET)
        )

        def _parse_not_intended_to_relocate(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        not_intended_to_relocate = _parse_not_intended_to_relocate(
            d.pop("Not_intended_to_relocate", UNSET)
        )

        wfs_map_server_wfs_table_8a_attributes = cls(
            objectid=objectid,
            aa_code=aa_code,
            aa_title=aa_title,
            intended_to_relocate=intended_to_relocate,
            not_intended_to_relocate=not_intended_to_relocate,
        )

        wfs_map_server_wfs_table_8a_attributes.additional_properties = d
        return wfs_map_server_wfs_table_8a_attributes

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
