from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Charger")


@_attrs_define
class Charger:
    """
    Attributes:
        charger_type (str | Unset): Documented values: Quick, SemiQuick. The sample spells a value as "Semi-Quick",
            which differs from the dictionary spelling.
        cp_no (str | Unset): Unique identifier for the charger.
        cp_status (str | Unset): Documented values: Charging_Not_Available, Status_Not_Available, Charging_Available,
            Charger_Out_of_Service.
        item_id (str | Unset): Unique identifier for the charger, as described by the dictionary.
        last_update (str | Unset): Last update timestamp. The dictionary labels this as date and gives an example with a
            timezone offset; the sample uses a space-separated timestamp without an offset. No format is asserted.
        point_name (str | Unset): Name of the charging point; the sample includes an empty string.
        provider (str | Unset): Documented value: CLP.
    """

    charger_type: str | Unset = UNSET
    cp_no: str | Unset = UNSET
    cp_status: str | Unset = UNSET
    item_id: str | Unset = UNSET
    last_update: str | Unset = UNSET
    point_name: str | Unset = UNSET
    provider: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        charger_type = self.charger_type

        cp_no = self.cp_no

        cp_status = self.cp_status

        item_id = self.item_id

        last_update = self.last_update

        point_name = self.point_name

        provider = self.provider

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if charger_type is not UNSET:
            field_dict["chargerType"] = charger_type
        if cp_no is not UNSET:
            field_dict["cpNo"] = cp_no
        if cp_status is not UNSET:
            field_dict["cpStatus"] = cp_status
        if item_id is not UNSET:
            field_dict["itemId"] = item_id
        if last_update is not UNSET:
            field_dict["lastUpdate"] = last_update
        if point_name is not UNSET:
            field_dict["pointName"] = point_name
        if provider is not UNSET:
            field_dict["provider"] = provider

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        charger_type = d.pop("chargerType", UNSET)

        cp_no = d.pop("cpNo", UNSET)

        cp_status = d.pop("cpStatus", UNSET)

        item_id = d.pop("itemId", UNSET)

        last_update = d.pop("lastUpdate", UNSET)

        point_name = d.pop("pointName", UNSET)

        provider = d.pop("provider", UNSET)

        charger = cls(
            charger_type=charger_type,
            cp_no=cp_no,
            cp_status=cp_status,
            item_id=item_id,
            last_update=last_update,
            point_name=point_name,
            provider=provider,
        )

        charger.additional_properties = d
        return charger

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
