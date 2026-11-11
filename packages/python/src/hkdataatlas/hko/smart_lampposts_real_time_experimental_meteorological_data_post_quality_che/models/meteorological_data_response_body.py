from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hko_meteorological_data import HkoMeteorologicalData


T = TypeVar("T", bound="MeteorologicalDataResponseBODY")


@_attrs_define
class MeteorologicalDataResponseBODY:
    """
    Attributes:
        hko (HkoMeteorologicalData | Unset): Meteorological payload fields documented for HKO. The data dictionary
            declares these values as strings; some examples are presented without quotation marks, so the schema allows
            either string or number for those fields to preserve the discrepancy.
    """

    hko: HkoMeteorologicalData | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hko: dict[str, Any] | Unset = UNSET
        if not isinstance(self.hko, Unset):
            hko = self.hko.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hko is not UNSET:
            field_dict["HKO"] = hko

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.hko_meteorological_data import HkoMeteorologicalData

        d = dict(src_dict)
        _hko = d.pop("HKO", UNSET)
        hko: HkoMeteorologicalData | Unset
        if isinstance(_hko, Unset):
            hko = UNSET
        else:
            hko = HkoMeteorologicalData.from_dict(_hko)

        meteorological_data_response_body = cls(
            hko=hko,
        )

        meteorological_data_response_body.additional_properties = d
        return meteorological_data_response_body

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
