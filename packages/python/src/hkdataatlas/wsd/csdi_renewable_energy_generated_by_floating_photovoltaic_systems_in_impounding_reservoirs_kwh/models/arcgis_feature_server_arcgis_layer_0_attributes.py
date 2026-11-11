from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer0Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer0Attributes:
    """
    Attributes:
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        reservoir (None | str | Unset): Publisher field type: esriFieldTypeString
        financial_year (None | str | Unset): Publisher field type: esriFieldTypeString
        renewable_energy (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    objectid: int | Unset = UNSET
    reservoir: None | str | Unset = UNSET
    financial_year: None | str | Unset = UNSET
    renewable_energy: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        reservoir: None | str | Unset
        if isinstance(self.reservoir, Unset):
            reservoir = UNSET
        else:
            reservoir = self.reservoir

        financial_year: None | str | Unset
        if isinstance(self.financial_year, Unset):
            financial_year = UNSET
        else:
            financial_year = self.financial_year

        renewable_energy: float | None | Unset
        if isinstance(self.renewable_energy, Unset):
            renewable_energy = UNSET
        else:
            renewable_energy = self.renewable_energy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if reservoir is not UNSET:
            field_dict["RESERVOIR"] = reservoir
        if financial_year is not UNSET:
            field_dict["FINANCIAL_YEAR"] = financial_year
        if renewable_energy is not UNSET:
            field_dict["RENEWABLE_ENERGY"] = renewable_energy

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_reservoir(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reservoir = _parse_reservoir(d.pop("RESERVOIR", UNSET))

        def _parse_financial_year(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        financial_year = _parse_financial_year(d.pop("FINANCIAL_YEAR", UNSET))

        def _parse_renewable_energy(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        renewable_energy = _parse_renewable_energy(d.pop("RENEWABLE_ENERGY", UNSET))

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            objectid=objectid,
            reservoir=reservoir,
            financial_year=financial_year,
            renewable_energy=renewable_energy,
        )

        arcgis_feature_server_arcgis_layer_0_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_0_attributes

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
