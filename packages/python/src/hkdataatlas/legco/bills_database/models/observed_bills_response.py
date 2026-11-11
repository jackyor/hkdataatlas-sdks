from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.observed_bill_record import ObservedBillRecord


T = TypeVar("T", bound="ObservedBillsResponse")


@_attrs_define
class ObservedBillsResponse:
    """Envelope observed in one complete successful retained publisher JSON response. The PDF defines record fields but
    does not define this envelope. Properties remain optional; no universal response guarantee is implied.

        Attributes:
            odata_metadata (str | Unset):
            odata_count (str | Unset): Observed string representation; no numeric coercion or undocumented lexical
                restriction.
            value (list[ObservedBillRecord] | Unset):
    """

    odata_metadata: str | Unset = UNSET
    odata_count: str | Unset = UNSET
    value: list[ObservedBillRecord] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        odata_metadata = self.odata_metadata

        odata_count = self.odata_count

        value: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.value, Unset):
            value = []
            for value_item_data in self.value:
                value_item = value_item_data.to_dict()
                value.append(value_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if odata_metadata is not UNSET:
            field_dict["odata.metadata"] = odata_metadata
        if odata_count is not UNSET:
            field_dict["odata.count"] = odata_count
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.observed_bill_record import ObservedBillRecord

        d = dict(src_dict)
        odata_metadata = d.pop("odata.metadata", UNSET)

        odata_count = d.pop("odata.count", UNSET)

        _value = d.pop("value", UNSET)
        value: list[ObservedBillRecord] | Unset = UNSET
        if _value is not UNSET:
            value = []
            for value_item_data in _value:
                value_item = ObservedBillRecord.from_dict(value_item_data)

                value.append(value_item)

        observed_bills_response = cls(
            odata_metadata=odata_metadata,
            odata_count=odata_count,
            value=value,
        )

        observed_bills_response.additional_properties = d
        return observed_bills_response

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
