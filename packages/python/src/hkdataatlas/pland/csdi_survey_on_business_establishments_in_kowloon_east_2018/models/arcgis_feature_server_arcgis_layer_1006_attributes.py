from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer1006Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer1006Attributes:
    """
    Attributes:
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        area_en (None | str | Unset): Publisher field type: esriFieldTypeString
        present_location_much_worse (int | None | Unset): Publisher field type: esriFieldTypeInteger
        present_location_little_worse (int | None | Unset): Publisher field type: esriFieldTypeInteger
        more_or_less_the_same (int | None | Unset): Publisher field type: esriFieldTypeInteger
        present_location_little_better (int | None | Unset): Publisher field type: esriFieldTypeInteger
        present_location_much_better (int | None | Unset): Publisher field type: esriFieldTypeInteger
    """

    objectid: int | Unset = UNSET
    area_en: None | str | Unset = UNSET
    present_location_much_worse: int | None | Unset = UNSET
    present_location_little_worse: int | None | Unset = UNSET
    more_or_less_the_same: int | None | Unset = UNSET
    present_location_little_better: int | None | Unset = UNSET
    present_location_much_better: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        area_en: None | str | Unset
        if isinstance(self.area_en, Unset):
            area_en = UNSET
        else:
            area_en = self.area_en

        present_location_much_worse: int | None | Unset
        if isinstance(self.present_location_much_worse, Unset):
            present_location_much_worse = UNSET
        else:
            present_location_much_worse = self.present_location_much_worse

        present_location_little_worse: int | None | Unset
        if isinstance(self.present_location_little_worse, Unset):
            present_location_little_worse = UNSET
        else:
            present_location_little_worse = self.present_location_little_worse

        more_or_less_the_same: int | None | Unset
        if isinstance(self.more_or_less_the_same, Unset):
            more_or_less_the_same = UNSET
        else:
            more_or_less_the_same = self.more_or_less_the_same

        present_location_little_better: int | None | Unset
        if isinstance(self.present_location_little_better, Unset):
            present_location_little_better = UNSET
        else:
            present_location_little_better = self.present_location_little_better

        present_location_much_better: int | None | Unset
        if isinstance(self.present_location_much_better, Unset):
            present_location_much_better = UNSET
        else:
            present_location_much_better = self.present_location_much_better

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if area_en is not UNSET:
            field_dict["Area_En"] = area_en
        if present_location_much_worse is not UNSET:
            field_dict["Present_location_much_worse"] = present_location_much_worse
        if present_location_little_worse is not UNSET:
            field_dict["Present_location_little_worse"] = present_location_little_worse
        if more_or_less_the_same is not UNSET:
            field_dict["More_or_less_the_same"] = more_or_less_the_same
        if present_location_little_better is not UNSET:
            field_dict["Present_location_little_better"] = (
                present_location_little_better
            )
        if present_location_much_better is not UNSET:
            field_dict["Present_location_much_better"] = present_location_much_better

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

        def _parse_present_location_much_worse(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        present_location_much_worse = _parse_present_location_much_worse(
            d.pop("Present_location_much_worse", UNSET)
        )

        def _parse_present_location_little_worse(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        present_location_little_worse = _parse_present_location_little_worse(
            d.pop("Present_location_little_worse", UNSET)
        )

        def _parse_more_or_less_the_same(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        more_or_less_the_same = _parse_more_or_less_the_same(
            d.pop("More_or_less_the_same", UNSET)
        )

        def _parse_present_location_little_better(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        present_location_little_better = _parse_present_location_little_better(
            d.pop("Present_location_little_better", UNSET)
        )

        def _parse_present_location_much_better(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        present_location_much_better = _parse_present_location_much_better(
            d.pop("Present_location_much_better", UNSET)
        )

        arcgis_feature_server_arcgis_layer_1006_attributes = cls(
            objectid=objectid,
            area_en=area_en,
            present_location_much_worse=present_location_much_worse,
            present_location_little_worse=present_location_little_worse,
            more_or_less_the_same=more_or_less_the_same,
            present_location_little_better=present_location_little_better,
            present_location_much_better=present_location_much_better,
        )

        arcgis_feature_server_arcgis_layer_1006_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_1006_attributes

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
