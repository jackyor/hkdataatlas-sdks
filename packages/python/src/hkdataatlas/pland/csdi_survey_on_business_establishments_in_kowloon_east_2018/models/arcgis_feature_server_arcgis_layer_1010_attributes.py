from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer1010Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer1010Attributes:
    """
    Attributes:
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        area_en (None | str | Unset): Publisher field type: esriFieldTypeString
        working_from_home_yes (int | None | Unset): Publisher field type: esriFieldTypeInteger
        working_from_home_no (int | None | Unset): Publisher field type: esriFieldTypeInteger
        practice_of_hot_desking_yes (int | None | Unset): Publisher field type: esriFieldTypeInteger
        practice_of_hot_desking_no (int | None | Unset): Publisher field type: esriFieldTypeInteger
        shared_office_yes (int | None | Unset): Publisher field type: esriFieldTypeInteger
        shared_office_no (int | None | Unset): Publisher field type: esriFieldTypeInteger
    """

    objectid: int | Unset = UNSET
    area_en: None | str | Unset = UNSET
    working_from_home_yes: int | None | Unset = UNSET
    working_from_home_no: int | None | Unset = UNSET
    practice_of_hot_desking_yes: int | None | Unset = UNSET
    practice_of_hot_desking_no: int | None | Unset = UNSET
    shared_office_yes: int | None | Unset = UNSET
    shared_office_no: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        area_en: None | str | Unset
        if isinstance(self.area_en, Unset):
            area_en = UNSET
        else:
            area_en = self.area_en

        working_from_home_yes: int | None | Unset
        if isinstance(self.working_from_home_yes, Unset):
            working_from_home_yes = UNSET
        else:
            working_from_home_yes = self.working_from_home_yes

        working_from_home_no: int | None | Unset
        if isinstance(self.working_from_home_no, Unset):
            working_from_home_no = UNSET
        else:
            working_from_home_no = self.working_from_home_no

        practice_of_hot_desking_yes: int | None | Unset
        if isinstance(self.practice_of_hot_desking_yes, Unset):
            practice_of_hot_desking_yes = UNSET
        else:
            practice_of_hot_desking_yes = self.practice_of_hot_desking_yes

        practice_of_hot_desking_no: int | None | Unset
        if isinstance(self.practice_of_hot_desking_no, Unset):
            practice_of_hot_desking_no = UNSET
        else:
            practice_of_hot_desking_no = self.practice_of_hot_desking_no

        shared_office_yes: int | None | Unset
        if isinstance(self.shared_office_yes, Unset):
            shared_office_yes = UNSET
        else:
            shared_office_yes = self.shared_office_yes

        shared_office_no: int | None | Unset
        if isinstance(self.shared_office_no, Unset):
            shared_office_no = UNSET
        else:
            shared_office_no = self.shared_office_no

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if area_en is not UNSET:
            field_dict["Area_En"] = area_en
        if working_from_home_yes is not UNSET:
            field_dict["Working_from_home_Yes"] = working_from_home_yes
        if working_from_home_no is not UNSET:
            field_dict["Working_from_home_No"] = working_from_home_no
        if practice_of_hot_desking_yes is not UNSET:
            field_dict["Practice_of_hot_desking_Yes"] = practice_of_hot_desking_yes
        if practice_of_hot_desking_no is not UNSET:
            field_dict["Practice_of_hot_desking_No"] = practice_of_hot_desking_no
        if shared_office_yes is not UNSET:
            field_dict["Shared_office_Yes"] = shared_office_yes
        if shared_office_no is not UNSET:
            field_dict["Shared_office_No"] = shared_office_no

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

        def _parse_working_from_home_yes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        working_from_home_yes = _parse_working_from_home_yes(
            d.pop("Working_from_home_Yes", UNSET)
        )

        def _parse_working_from_home_no(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        working_from_home_no = _parse_working_from_home_no(
            d.pop("Working_from_home_No", UNSET)
        )

        def _parse_practice_of_hot_desking_yes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        practice_of_hot_desking_yes = _parse_practice_of_hot_desking_yes(
            d.pop("Practice_of_hot_desking_Yes", UNSET)
        )

        def _parse_practice_of_hot_desking_no(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        practice_of_hot_desking_no = _parse_practice_of_hot_desking_no(
            d.pop("Practice_of_hot_desking_No", UNSET)
        )

        def _parse_shared_office_yes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        shared_office_yes = _parse_shared_office_yes(d.pop("Shared_office_Yes", UNSET))

        def _parse_shared_office_no(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        shared_office_no = _parse_shared_office_no(d.pop("Shared_office_No", UNSET))

        arcgis_feature_server_arcgis_layer_1010_attributes = cls(
            objectid=objectid,
            area_en=area_en,
            working_from_home_yes=working_from_home_yes,
            working_from_home_no=working_from_home_no,
            practice_of_hot_desking_yes=practice_of_hot_desking_yes,
            practice_of_hot_desking_no=practice_of_hot_desking_no,
            shared_office_yes=shared_office_yes,
            shared_office_no=shared_office_no,
        )

        arcgis_feature_server_arcgis_layer_1010_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_1010_attributes

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
