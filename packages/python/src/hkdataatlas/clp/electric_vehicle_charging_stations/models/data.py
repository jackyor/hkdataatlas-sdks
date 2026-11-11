from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.geo_location_result import GeoLocationResult


T = TypeVar("T", bound="Data")


@_attrs_define
class Data:
    """
    Attributes:
        geo_location_result (list[GeoLocationResult] | Unset):
        total_search_result (int | Unset): Number of geoLocationResult objects.
    """

    geo_location_result: list[GeoLocationResult] | Unset = UNSET
    total_search_result: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        geo_location_result: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.geo_location_result, Unset):
            geo_location_result = []
            for geo_location_result_item_data in self.geo_location_result:
                geo_location_result_item = geo_location_result_item_data.to_dict()
                geo_location_result.append(geo_location_result_item)

        total_search_result = self.total_search_result

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if geo_location_result is not UNSET:
            field_dict["geoLocationResult"] = geo_location_result
        if total_search_result is not UNSET:
            field_dict["totalSearchResult"] = total_search_result

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.geo_location_result import GeoLocationResult

        d = dict(src_dict)
        _geo_location_result = d.pop("geoLocationResult", UNSET)
        geo_location_result: list[GeoLocationResult] | Unset = UNSET
        if _geo_location_result is not UNSET:
            geo_location_result = []
            for geo_location_result_item_data in _geo_location_result:
                geo_location_result_item = GeoLocationResult.from_dict(
                    geo_location_result_item_data
                )

                geo_location_result.append(geo_location_result_item)

        total_search_result = d.pop("totalSearchResult", UNSET)

        data = cls(
            geo_location_result=geo_location_result,
            total_search_result=total_search_result,
        )

        data.additional_properties = d
        return data

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
