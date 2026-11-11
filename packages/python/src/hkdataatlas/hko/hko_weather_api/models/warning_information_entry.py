from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WarningInformationEntry")


@_attrs_define
class WarningInformationEntry:
    """
    Attributes:
        contents (list[str] | Unset): Warning message contents.
        subtype (str | Unset): Subtype is documented only for fire danger, tropical cyclone and rainstorm warnings.
            WFIRE: WFIREY (Yellow Fire), WFIRER (Red Fire). WRAIN: WRAINA (Amber), WRAINR (Red), WRAINB (Black). WTCSGNL:
            TC1 (No. 1), TC3 (No. 3), TC8NE (No. 8 North East), TC8SE (No. 8 South East), TC8SW (No. 8 South West), TC8NW
            (No. 8 North West), TC9 (No. 9), TC10 (No. 10), CANCEL (Cancel All Signals).
        update_time (str | Unset): Timestamp examples use YYYY-MM-DD'T'hh:mm:ssZ notation and include the +08:00 offset.
        warning_statement_code (str | Unset): Warning statement code. Documented codes: WFIRE (Fire Danger Warning),
            WFROST (Frost Warning), WHOT (Hot Weather Warning), WCOLD (Cold Weather Warning), WMSGNL (Strong Monsoon
            Signal), WTCPRE8 (Pre-no.8 Special Announcement), WRAIN (Rainstorm Warning Signal), WFNTSA (Special Announcement
            on Flooding in the northern New Territories), WL (Landslip Warning), WTCSGNL (Tropical Cyclone Warning Signal),
            WTMW (Tsunami Warning), WTS (Thunderstorm Warning).
    """

    contents: list[str] | Unset = UNSET
    subtype: str | Unset = UNSET
    update_time: str | Unset = UNSET
    warning_statement_code: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        contents: list[str] | Unset = UNSET
        if not isinstance(self.contents, Unset):
            contents = self.contents

        subtype = self.subtype

        update_time = self.update_time

        warning_statement_code = self.warning_statement_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if contents is not UNSET:
            field_dict["contents"] = contents
        if subtype is not UNSET:
            field_dict["subtype"] = subtype
        if update_time is not UNSET:
            field_dict["updateTime"] = update_time
        if warning_statement_code is not UNSET:
            field_dict["warningStatementCode"] = warning_statement_code

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        contents = cast(list[str], d.pop("contents", UNSET))

        subtype = d.pop("subtype", UNSET)

        update_time = d.pop("updateTime", UNSET)

        warning_statement_code = d.pop("warningStatementCode", UNSET)

        warning_information_entry = cls(
            contents=contents,
            subtype=subtype,
            update_time=update_time,
            warning_statement_code=warning_statement_code,
        )

        warning_information_entry.additional_properties = d
        return warning_information_entry

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
