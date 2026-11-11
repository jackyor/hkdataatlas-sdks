from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AlternateRoute")


@_attrs_define
class AlternateRoute:
    """Alternate harbour route information.

    Attributes:
        dist_u (str | Unset): Total distance with unit.
        eta (str | Unset): Estimated journey time in hh:mm.
        name (str | Unset): Name/code of harbour tunnel (cht, wht, eht).
    """

    dist_u: str | Unset = UNSET
    eta: str | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dist_u = self.dist_u

        eta = self.eta

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dist_u is not UNSET:
            field_dict["distU"] = dist_u
        if eta is not UNSET:
            field_dict["eta"] = eta
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        dist_u = d.pop("distU", UNSET)

        eta = d.pop("eta", UNSET)

        name = d.pop("name", UNSET)

        alternate_route = cls(
            dist_u=dist_u,
            eta=eta,
            name=name,
        )

        alternate_route.additional_properties = d
        return alternate_route

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
