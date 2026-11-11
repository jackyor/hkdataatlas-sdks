from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsTable270Attributes")


@_attrs_define
class WfsMapServerWfsTable270Attributes:
    """
    Attributes:
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        area_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        very_satisfied (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence
            into all JSON queries.
        quite_satisfied (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence
            into all JSON queries.
        neutral (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into
            all JSON queries.
        quite_dissatisfied (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML
            occurrence into all JSON queries.
        very_dissatisfied (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML
            occurrence into all JSON queries.
    """

    objectid: int | Unset = UNSET
    area_en: None | str | Unset = UNSET
    very_satisfied: int | None | Unset = UNSET
    quite_satisfied: int | None | Unset = UNSET
    neutral: int | None | Unset = UNSET
    quite_dissatisfied: int | None | Unset = UNSET
    very_dissatisfied: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        area_en: None | str | Unset
        if isinstance(self.area_en, Unset):
            area_en = UNSET
        else:
            area_en = self.area_en

        very_satisfied: int | None | Unset
        if isinstance(self.very_satisfied, Unset):
            very_satisfied = UNSET
        else:
            very_satisfied = self.very_satisfied

        quite_satisfied: int | None | Unset
        if isinstance(self.quite_satisfied, Unset):
            quite_satisfied = UNSET
        else:
            quite_satisfied = self.quite_satisfied

        neutral: int | None | Unset
        if isinstance(self.neutral, Unset):
            neutral = UNSET
        else:
            neutral = self.neutral

        quite_dissatisfied: int | None | Unset
        if isinstance(self.quite_dissatisfied, Unset):
            quite_dissatisfied = UNSET
        else:
            quite_dissatisfied = self.quite_dissatisfied

        very_dissatisfied: int | None | Unset
        if isinstance(self.very_dissatisfied, Unset):
            very_dissatisfied = UNSET
        else:
            very_dissatisfied = self.very_dissatisfied

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if area_en is not UNSET:
            field_dict["Area_En"] = area_en
        if very_satisfied is not UNSET:
            field_dict["Very_satisfied"] = very_satisfied
        if quite_satisfied is not UNSET:
            field_dict["Quite_satisfied"] = quite_satisfied
        if neutral is not UNSET:
            field_dict["Neutral"] = neutral
        if quite_dissatisfied is not UNSET:
            field_dict["Quite_dissatisfied"] = quite_dissatisfied
        if very_dissatisfied is not UNSET:
            field_dict["Very_dissatisfied"] = very_dissatisfied

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_area_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        area_en = _parse_area_en(d.pop("Area_En", UNSET))

        def _parse_very_satisfied(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        very_satisfied = _parse_very_satisfied(d.pop("Very_satisfied", UNSET))

        def _parse_quite_satisfied(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        quite_satisfied = _parse_quite_satisfied(d.pop("Quite_satisfied", UNSET))

        def _parse_neutral(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        neutral = _parse_neutral(d.pop("Neutral", UNSET))

        def _parse_quite_dissatisfied(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        quite_dissatisfied = _parse_quite_dissatisfied(
            d.pop("Quite_dissatisfied", UNSET)
        )

        def _parse_very_dissatisfied(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        very_dissatisfied = _parse_very_dissatisfied(d.pop("Very_dissatisfied", UNSET))

        wfs_map_server_wfs_table_270_attributes = cls(
            objectid=objectid,
            area_en=area_en,
            very_satisfied=very_satisfied,
            quite_satisfied=quite_satisfied,
            neutral=neutral,
            quite_dissatisfied=quite_dissatisfied,
            very_dissatisfied=very_dissatisfied,
        )

        wfs_map_server_wfs_table_270_attributes.additional_properties = d
        return wfs_map_server_wfs_table_270_attributes

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
