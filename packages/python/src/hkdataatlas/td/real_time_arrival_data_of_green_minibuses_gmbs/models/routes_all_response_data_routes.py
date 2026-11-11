from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RoutesAllResponseDataRoutes")


@_attrs_define
class RoutesAllResponseDataRoutes:
    """Route codes grouped by region.

    Attributes:
        hki (list[str] | Unset): Route codes for Hong Kong Island.
        kln (list[str] | Unset): Route codes for Kowloon.
        nt (list[str] | Unset): Route codes for the New Territories.
    """

    hki: list[str] | Unset = UNSET
    kln: list[str] | Unset = UNSET
    nt: list[str] | Unset = UNSET
    additional_properties: dict[str, list[str]] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hki: list[str] | Unset = UNSET
        if not isinstance(self.hki, Unset):
            hki = self.hki

        kln: list[str] | Unset = UNSET
        if not isinstance(self.kln, Unset):
            kln = self.kln

        nt: list[str] | Unset = UNSET
        if not isinstance(self.nt, Unset):
            nt = self.nt

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop

        field_dict.update({})
        if hki is not UNSET:
            field_dict["HKI"] = hki
        if kln is not UNSET:
            field_dict["KLN"] = kln
        if nt is not UNSET:
            field_dict["NT"] = nt

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        hki = cast(list[str], d.pop("HKI", UNSET))

        kln = cast(list[str], d.pop("KLN", UNSET))

        nt = cast(list[str], d.pop("NT", UNSET))

        routes_all_response_data_routes = cls(
            hki=hki,
            kln=kln,
            nt=nt,
        )

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = cast(list[str], prop_dict)

            additional_properties[prop_name] = additional_property

        routes_all_response_data_routes.additional_properties = additional_properties
        return routes_all_response_data_routes

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> list[str]:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: list[str]) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
