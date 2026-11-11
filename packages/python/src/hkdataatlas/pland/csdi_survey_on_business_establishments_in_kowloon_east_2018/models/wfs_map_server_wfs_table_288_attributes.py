from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsTable288Attributes")


@_attrs_define
class WfsMapServerWfsTable288Attributes:
    """
    Attributes:
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        area_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        very_unlikely (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence
            into all JSON queries.
        quite_unlikely (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence
            into all JSON queries.
        quite_likely (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence
            into all JSON queries.
        very_likely (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence
            into all JSON queries.
        uncertain (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into
            all JSON queries.
    """

    objectid: int | Unset = UNSET
    area_en: None | str | Unset = UNSET
    very_unlikely: int | None | Unset = UNSET
    quite_unlikely: int | None | Unset = UNSET
    quite_likely: int | None | Unset = UNSET
    very_likely: int | None | Unset = UNSET
    uncertain: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        area_en: None | str | Unset
        if isinstance(self.area_en, Unset):
            area_en = UNSET
        else:
            area_en = self.area_en

        very_unlikely: int | None | Unset
        if isinstance(self.very_unlikely, Unset):
            very_unlikely = UNSET
        else:
            very_unlikely = self.very_unlikely

        quite_unlikely: int | None | Unset
        if isinstance(self.quite_unlikely, Unset):
            quite_unlikely = UNSET
        else:
            quite_unlikely = self.quite_unlikely

        quite_likely: int | None | Unset
        if isinstance(self.quite_likely, Unset):
            quite_likely = UNSET
        else:
            quite_likely = self.quite_likely

        very_likely: int | None | Unset
        if isinstance(self.very_likely, Unset):
            very_likely = UNSET
        else:
            very_likely = self.very_likely

        uncertain: int | None | Unset
        if isinstance(self.uncertain, Unset):
            uncertain = UNSET
        else:
            uncertain = self.uncertain

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if area_en is not UNSET:
            field_dict["Area_En"] = area_en
        if very_unlikely is not UNSET:
            field_dict["Very_unlikely"] = very_unlikely
        if quite_unlikely is not UNSET:
            field_dict["Quite_unlikely"] = quite_unlikely
        if quite_likely is not UNSET:
            field_dict["Quite_likely"] = quite_likely
        if very_likely is not UNSET:
            field_dict["Very_likely"] = very_likely
        if uncertain is not UNSET:
            field_dict["Uncertain"] = uncertain

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

        def _parse_very_unlikely(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        very_unlikely = _parse_very_unlikely(d.pop("Very_unlikely", UNSET))

        def _parse_quite_unlikely(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        quite_unlikely = _parse_quite_unlikely(d.pop("Quite_unlikely", UNSET))

        def _parse_quite_likely(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        quite_likely = _parse_quite_likely(d.pop("Quite_likely", UNSET))

        def _parse_very_likely(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        very_likely = _parse_very_likely(d.pop("Very_likely", UNSET))

        def _parse_uncertain(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        uncertain = _parse_uncertain(d.pop("Uncertain", UNSET))

        wfs_map_server_wfs_table_288_attributes = cls(
            objectid=objectid,
            area_en=area_en,
            very_unlikely=very_unlikely,
            quite_unlikely=quite_unlikely,
            quite_likely=quite_likely,
            very_likely=very_likely,
            uncertain=uncertain,
        )

        wfs_map_server_wfs_table_288_attributes.additional_properties = d
        return wfs_map_server_wfs_table_288_attributes

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
