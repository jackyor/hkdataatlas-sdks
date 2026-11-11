from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TropicalCycloneListEntry")


@_attrs_define
class TropicalCycloneListEntry:
    """
    Attributes:
        tropical_cyclone_chinese_name (str | Unset): Chinese name of the tropical cyclone, if named. The dictionary
            identifies this as plain text in Traditional Chinese, UTF-8; its table layout does not reliably show the example
            value.
        tropical_cyclone_english_name (str | Unset): English name of the tropical cyclone, if named. If the tropical
            cyclone is not yet named, the latest intensity category may be given; possible categories are described in the
            track data dictionary.
        tropical_cyclone_id (int | str | Unset): Four-digit unique identifier assigned by HKO. The dictionary describes
            the format as Integer and gives example 1829; string representation is used in the file naming pattern.
        tropical_cyclone_url (str | Unset): URL of the tropical cyclone track data file. Example:
            https://www.weather.gov.hk/wxinfo/currwx/hko_tctrack_1829.xml.
    """

    tropical_cyclone_chinese_name: str | Unset = UNSET
    tropical_cyclone_english_name: str | Unset = UNSET
    tropical_cyclone_id: int | str | Unset = UNSET
    tropical_cyclone_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tropical_cyclone_chinese_name = self.tropical_cyclone_chinese_name

        tropical_cyclone_english_name = self.tropical_cyclone_english_name

        tropical_cyclone_id: int | str | Unset
        if isinstance(self.tropical_cyclone_id, Unset):
            tropical_cyclone_id = UNSET
        else:
            tropical_cyclone_id = self.tropical_cyclone_id

        tropical_cyclone_url = self.tropical_cyclone_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tropical_cyclone_chinese_name is not UNSET:
            field_dict["TropicalCycloneChineseName"] = tropical_cyclone_chinese_name
        if tropical_cyclone_english_name is not UNSET:
            field_dict["TropicalCycloneEnglishName"] = tropical_cyclone_english_name
        if tropical_cyclone_id is not UNSET:
            field_dict["TropicalCycloneID"] = tropical_cyclone_id
        if tropical_cyclone_url is not UNSET:
            field_dict["TropicalCycloneURL"] = tropical_cyclone_url

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        tropical_cyclone_chinese_name = d.pop("TropicalCycloneChineseName", UNSET)

        tropical_cyclone_english_name = d.pop("TropicalCycloneEnglishName", UNSET)

        def _parse_tropical_cyclone_id(data: object) -> int | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(int | str | Unset, data)

        tropical_cyclone_id = _parse_tropical_cyclone_id(
            d.pop("TropicalCycloneID", UNSET)
        )

        tropical_cyclone_url = d.pop("TropicalCycloneURL", UNSET)

        tropical_cyclone_list_entry = cls(
            tropical_cyclone_chinese_name=tropical_cyclone_chinese_name,
            tropical_cyclone_english_name=tropical_cyclone_english_name,
            tropical_cyclone_id=tropical_cyclone_id,
            tropical_cyclone_url=tropical_cyclone_url,
        )

        tropical_cyclone_list_entry.additional_properties = d
        return tropical_cyclone_list_entry

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
