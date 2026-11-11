from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Tile")


@_attrs_define
class Tile:
    """
    Attributes:
        fid (int | Unset): ID.
        file_url (str | Unset): Path of file.
        grid_name (str | Unset): Index grid name.
        loc_en (str | Unset): Location name in English.
        loc_sc (str | Unset): Location name in Simplified Chinese.
        loc_tc (str | Unset): Location name in Traditional Chinese.
        modi_date (str | Unset): Modification date. The legacy dictionary spells the field Modi_date and specifies
            DD/MM/YYYY; its example and a bounded observation use modi_date, and the observation includes a time component.
    """

    fid: int | Unset = UNSET
    file_url: str | Unset = UNSET
    grid_name: str | Unset = UNSET
    loc_en: str | Unset = UNSET
    loc_sc: str | Unset = UNSET
    loc_tc: str | Unset = UNSET
    modi_date: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fid = self.fid

        file_url = self.file_url

        grid_name = self.grid_name

        loc_en = self.loc_en

        loc_sc = self.loc_sc

        loc_tc = self.loc_tc

        modi_date = self.modi_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fid is not UNSET:
            field_dict["fid"] = fid
        if file_url is not UNSET:
            field_dict["file_url"] = file_url
        if grid_name is not UNSET:
            field_dict["grid_name"] = grid_name
        if loc_en is not UNSET:
            field_dict["loc_en"] = loc_en
        if loc_sc is not UNSET:
            field_dict["loc_sc"] = loc_sc
        if loc_tc is not UNSET:
            field_dict["loc_tc"] = loc_tc
        if modi_date is not UNSET:
            field_dict["modi_date"] = modi_date

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        fid = d.pop("fid", UNSET)

        file_url = d.pop("file_url", UNSET)

        grid_name = d.pop("grid_name", UNSET)

        loc_en = d.pop("loc_en", UNSET)

        loc_sc = d.pop("loc_sc", UNSET)

        loc_tc = d.pop("loc_tc", UNSET)

        modi_date = d.pop("modi_date", UNSET)

        tile = cls(
            fid=fid,
            file_url=file_url,
            grid_name=grid_name,
            loc_en=loc_en,
            loc_sc=loc_sc,
            loc_tc=loc_tc,
            modi_date=modi_date,
        )

        tile.additional_properties = d
        return tile

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
