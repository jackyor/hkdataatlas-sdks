from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.stop_coordinates import StopCoordinates


T = TypeVar("T", bound="Stop")


@_attrs_define
class Stop:
    """
    Attributes:
        coordinates (StopCoordinates | Unset): Stop position in different coordinate reference systems.
        data_timestamp (datetime.datetime | Unset): Last updated timestamp of stop.
        enabled (bool | Unset): True if the stop is in service; otherwise false.
        remarks_en (None | str | Unset): English remarks for service amendment; null if enabled is true.
        remarks_sc (None | str | Unset): Simplified Chinese remarks for service amendment; null if enabled is true.
        remarks_tc (None | str | Unset): Traditional Chinese remarks for service amendment; null if enabled is true.
    """

    coordinates: StopCoordinates | Unset = UNSET
    data_timestamp: datetime.datetime | Unset = UNSET
    enabled: bool | Unset = UNSET
    remarks_en: None | str | Unset = UNSET
    remarks_sc: None | str | Unset = UNSET
    remarks_tc: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        coordinates: dict[str, Any] | Unset = UNSET
        if not isinstance(self.coordinates, Unset):
            coordinates = self.coordinates.to_dict()

        data_timestamp: str | Unset = UNSET
        if not isinstance(self.data_timestamp, Unset):
            data_timestamp = self.data_timestamp.isoformat()

        enabled = self.enabled

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if coordinates is not UNSET:
            field_dict["coordinates"] = coordinates
        if data_timestamp is not UNSET:
            field_dict["data_timestamp"] = data_timestamp
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if remarks_en is not UNSET:
            field_dict["remarks_en"] = remarks_en
        if remarks_sc is not UNSET:
            field_dict["remarks_sc"] = remarks_sc
        if remarks_tc is not UNSET:
            field_dict["remarks_tc"] = remarks_tc

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.stop_coordinates import StopCoordinates

        d = dict(src_dict)
        _coordinates = d.pop("coordinates", UNSET)
        coordinates: StopCoordinates | Unset
        if isinstance(_coordinates, Unset):
            coordinates = UNSET
        else:
            coordinates = StopCoordinates.from_dict(_coordinates)

        _data_timestamp = d.pop("data_timestamp", UNSET)
        data_timestamp: datetime.datetime | Unset
        if isinstance(_data_timestamp, Unset):
            data_timestamp = UNSET
        else:
            data_timestamp = datetime.datetime.fromisoformat(_data_timestamp)

        enabled = d.pop("enabled", UNSET)

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

        stop = cls(
            coordinates=coordinates,
            data_timestamp=data_timestamp,
            enabled=enabled,
            remarks_en=remarks_en,
            remarks_sc=remarks_sc,
            remarks_tc=remarks_tc,
        )

        stop.additional_properties = d
        return stop

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
