from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer1Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer1Attributes:
    """
    Attributes:
        category_of_persons_in_custody (None | str | Unset): Publisher field type: esriFieldTypeString
        name_of_institution (None | str | Unset): Publisher field type: esriFieldTypeString
        notes (None | str | Unset): Publisher field type: esriFieldTypeString
        number_of_persons_in_custody (None | str | Unset): Publisher field type: esriFieldTypeString
        reference_date (None | str | Unset): Publisher field type: esriFieldTypeString
        type_of_institution (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    category_of_persons_in_custody: None | str | Unset = UNSET
    name_of_institution: None | str | Unset = UNSET
    notes: None | str | Unset = UNSET
    number_of_persons_in_custody: None | str | Unset = UNSET
    reference_date: None | str | Unset = UNSET
    type_of_institution: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category_of_persons_in_custody: None | str | Unset
        if isinstance(self.category_of_persons_in_custody, Unset):
            category_of_persons_in_custody = UNSET
        else:
            category_of_persons_in_custody = self.category_of_persons_in_custody

        name_of_institution: None | str | Unset
        if isinstance(self.name_of_institution, Unset):
            name_of_institution = UNSET
        else:
            name_of_institution = self.name_of_institution

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        number_of_persons_in_custody: None | str | Unset
        if isinstance(self.number_of_persons_in_custody, Unset):
            number_of_persons_in_custody = UNSET
        else:
            number_of_persons_in_custody = self.number_of_persons_in_custody

        reference_date: None | str | Unset
        if isinstance(self.reference_date, Unset):
            reference_date = UNSET
        else:
            reference_date = self.reference_date

        type_of_institution: None | str | Unset
        if isinstance(self.type_of_institution, Unset):
            type_of_institution = UNSET
        else:
            type_of_institution = self.type_of_institution

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category_of_persons_in_custody is not UNSET:
            field_dict["Category_of_persons_in_custody"] = (
                category_of_persons_in_custody
            )
        if name_of_institution is not UNSET:
            field_dict["Name_of_institution"] = name_of_institution
        if notes is not UNSET:
            field_dict["Notes"] = notes
        if number_of_persons_in_custody is not UNSET:
            field_dict["Number_of_persons_in_custody"] = number_of_persons_in_custody
        if reference_date is not UNSET:
            field_dict["Reference_date"] = reference_date
        if type_of_institution is not UNSET:
            field_dict["Type_of_institution"] = type_of_institution
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_category_of_persons_in_custody(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category_of_persons_in_custody = _parse_category_of_persons_in_custody(
            d.pop("Category_of_persons_in_custody", UNSET)
        )

        def _parse_name_of_institution(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_of_institution = _parse_name_of_institution(
            d.pop("Name_of_institution", UNSET)
        )

        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("Notes", UNSET))

        def _parse_number_of_persons_in_custody(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        number_of_persons_in_custody = _parse_number_of_persons_in_custody(
            d.pop("Number_of_persons_in_custody", UNSET)
        )

        def _parse_reference_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reference_date = _parse_reference_date(d.pop("Reference_date", UNSET))

        def _parse_type_of_institution(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_of_institution = _parse_type_of_institution(
            d.pop("Type_of_institution", UNSET)
        )

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_1_attributes = cls(
            category_of_persons_in_custody=category_of_persons_in_custody,
            name_of_institution=name_of_institution,
            notes=notes,
            number_of_persons_in_custody=number_of_persons_in_custody,
            reference_date=reference_date,
            type_of_institution=type_of_institution,
            objectid=objectid,
        )

        arcgis_feature_server_arcgis_layer_1_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_1_attributes

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
