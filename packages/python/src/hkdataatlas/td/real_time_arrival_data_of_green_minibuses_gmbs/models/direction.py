from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.headway import Headway


T = TypeVar("T", bound="Direction")


@_attrs_define
class Direction:
    """
    Attributes:
        data_timestamp (datetime.datetime | Unset): Last updated timestamp of direction.
        dest_en (str | Unset): English destination name.
        dest_sc (str | Unset): Simplified Chinese destination name.
        dest_tc (str | Unset): Traditional Chinese destination name.
        headways (list[Headway] | Unset): Headways of a direction.
        orig_en (str | Unset): English origin name.
        orig_sc (str | Unset): Simplified Chinese origin name.
        orig_tc (str | Unset): Traditional Chinese origin name.
        remarks_en (None | str | Unset): English remarks for service amendment.
        remarks_sc (None | str | Unset): Simplified Chinese remarks for service amendment.
        remarks_tc (None | str | Unset): Traditional Chinese remarks for service amendment.
        route_seq (int | Unset): Route sequence.
    """

    data_timestamp: datetime.datetime | Unset = UNSET
    dest_en: str | Unset = UNSET
    dest_sc: str | Unset = UNSET
    dest_tc: str | Unset = UNSET
    headways: list[Headway] | Unset = UNSET
    orig_en: str | Unset = UNSET
    orig_sc: str | Unset = UNSET
    orig_tc: str | Unset = UNSET
    remarks_en: None | str | Unset = UNSET
    remarks_sc: None | str | Unset = UNSET
    remarks_tc: None | str | Unset = UNSET
    route_seq: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data_timestamp: str | Unset = UNSET
        if not isinstance(self.data_timestamp, Unset):
            data_timestamp = self.data_timestamp.isoformat()

        dest_en = self.dest_en

        dest_sc = self.dest_sc

        dest_tc = self.dest_tc

        headways: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.headways, Unset):
            headways = []
            for headways_item_data in self.headways:
                headways_item = headways_item_data.to_dict()
                headways.append(headways_item)

        orig_en = self.orig_en

        orig_sc = self.orig_sc

        orig_tc = self.orig_tc

        remarks_en: None | str | Unset
        if isinstance(self.remarks_en, Unset):
            remarks_en = UNSET
        else:
            remarks_en = self.remarks_en

        remarks_sc: None | str | Unset
        if isinstance(self.remarks_sc, Unset):
            remarks_sc = UNSET
        else:
            remarks_sc = self.remarks_sc

        remarks_tc: None | str | Unset
        if isinstance(self.remarks_tc, Unset):
            remarks_tc = UNSET
        else:
            remarks_tc = self.remarks_tc

        route_seq = self.route_seq

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data_timestamp is not UNSET:
            field_dict["data_timestamp"] = data_timestamp
        if dest_en is not UNSET:
            field_dict["dest_en"] = dest_en
        if dest_sc is not UNSET:
            field_dict["dest_sc"] = dest_sc
        if dest_tc is not UNSET:
            field_dict["dest_tc"] = dest_tc
        if headways is not UNSET:
            field_dict["headways"] = headways
        if orig_en is not UNSET:
            field_dict["orig_en"] = orig_en
        if orig_sc is not UNSET:
            field_dict["orig_sc"] = orig_sc
        if orig_tc is not UNSET:
            field_dict["orig_tc"] = orig_tc
        if remarks_en is not UNSET:
            field_dict["remarks_en"] = remarks_en
        if remarks_sc is not UNSET:
            field_dict["remarks_sc"] = remarks_sc
        if remarks_tc is not UNSET:
            field_dict["remarks_tc"] = remarks_tc
        if route_seq is not UNSET:
            field_dict["route_seq"] = route_seq

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.headway import Headway

        d = dict(src_dict)
        _data_timestamp = d.pop("data_timestamp", UNSET)
        data_timestamp: datetime.datetime | Unset
        if isinstance(_data_timestamp, Unset):
            data_timestamp = UNSET
        else:
            data_timestamp = datetime.datetime.fromisoformat(_data_timestamp)

        dest_en = d.pop("dest_en", UNSET)

        dest_sc = d.pop("dest_sc", UNSET)

        dest_tc = d.pop("dest_tc", UNSET)

        _headways = d.pop("headways", UNSET)
        headways: list[Headway] | Unset = UNSET
        if _headways is not UNSET:
            headways = []
            for headways_item_data in _headways:
                headways_item = Headway.from_dict(headways_item_data)

                headways.append(headways_item)

        orig_en = d.pop("orig_en", UNSET)

        orig_sc = d.pop("orig_sc", UNSET)

        orig_tc = d.pop("orig_tc", UNSET)

        def _parse_remarks_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remarks_en = _parse_remarks_en(d.pop("remarks_en", UNSET))

        def _parse_remarks_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remarks_sc = _parse_remarks_sc(d.pop("remarks_sc", UNSET))

        def _parse_remarks_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remarks_tc = _parse_remarks_tc(d.pop("remarks_tc", UNSET))

        route_seq = d.pop("route_seq", UNSET)

        direction = cls(
            data_timestamp=data_timestamp,
            dest_en=dest_en,
            dest_sc=dest_sc,
            dest_tc=dest_tc,
            headways=headways,
            orig_en=orig_en,
            orig_sc=orig_sc,
            orig_tc=orig_tc,
            remarks_en=remarks_en,
            remarks_sc=remarks_sc,
            remarks_tc=remarks_tc,
            route_seq=route_seq,
        )

        direction.additional_properties = d
        return direction

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
