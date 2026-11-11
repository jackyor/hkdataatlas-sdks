from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Stop")


@_attrs_define
class Stop:
    """
    Attributes:
        fare (float | str | Unset): Fare from Monday to Saturday, except public holidays. Documented as Number; the
            sample represents it as a string.
        fare_holiday (float | str | Unset): Fare on Sundays and public holidays. Documented as Number; the sample
            represents it as a string.
        latitude (float | str | Unset): Documented as Number; the sample represents it as a string.
        longitude (float | str | Unset): Documented as Number; the sample represents it as a string.
        some_departure_observe_only (int | Unset): Indicates whether the stop of that route is some departure observe
            only: 1 if it is, otherwise 0.
        stop_id (int | str | Unset): Documented as Integer; the sample represents this identifier as a string.
        stop_location_c (str | Unset):
        stop_location_e (str | Unset):
        stop_location_s (str | Unset):
        stop_name_c (str | Unset):
        stop_name_e (str | Unset):
        stop_name_s (str | Unset):
    """

    fare: float | str | Unset = UNSET
    fare_holiday: float | str | Unset = UNSET
    latitude: float | str | Unset = UNSET
    longitude: float | str | Unset = UNSET
    some_departure_observe_only: int | Unset = UNSET
    stop_id: int | str | Unset = UNSET
    stop_location_c: str | Unset = UNSET
    stop_location_e: str | Unset = UNSET
    stop_location_s: str | Unset = UNSET
    stop_name_c: str | Unset = UNSET
    stop_name_e: str | Unset = UNSET
    stop_name_s: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fare: float | str | Unset
        if isinstance(self.fare, Unset):
            fare = UNSET
        else:
            fare = self.fare

        fare_holiday: float | str | Unset
        if isinstance(self.fare_holiday, Unset):
            fare_holiday = UNSET
        else:
            fare_holiday = self.fare_holiday

        latitude: float | str | Unset
        if isinstance(self.latitude, Unset):
            latitude = UNSET
        else:
            latitude = self.latitude

        longitude: float | str | Unset
        if isinstance(self.longitude, Unset):
            longitude = UNSET
        else:
            longitude = self.longitude

        some_departure_observe_only = self.some_departure_observe_only

        stop_id: int | str | Unset
        if isinstance(self.stop_id, Unset):
            stop_id = UNSET
        else:
            stop_id = self.stop_id

        stop_location_c = self.stop_location_c

        stop_location_e = self.stop_location_e

        stop_location_s = self.stop_location_s

        stop_name_c = self.stop_name_c

        stop_name_e = self.stop_name_e

        stop_name_s = self.stop_name_s

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fare is not UNSET:
            field_dict["fare"] = fare
        if fare_holiday is not UNSET:
            field_dict["fareHoliday"] = fare_holiday
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if some_departure_observe_only is not UNSET:
            field_dict["someDepartureObserveOnly"] = some_departure_observe_only
        if stop_id is not UNSET:
            field_dict["stopId"] = stop_id
        if stop_location_c is not UNSET:
            field_dict["stopLocation_c"] = stop_location_c
        if stop_location_e is not UNSET:
            field_dict["stopLocation_e"] = stop_location_e
        if stop_location_s is not UNSET:
            field_dict["stopLocation_s"] = stop_location_s
        if stop_name_c is not UNSET:
            field_dict["stopName_c"] = stop_name_c
        if stop_name_e is not UNSET:
            field_dict["stopName_e"] = stop_name_e
        if stop_name_s is not UNSET:
            field_dict["stopName_s"] = stop_name_s

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_fare(data: object) -> float | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(float | str | Unset, data)

        fare = _parse_fare(d.pop("fare", UNSET))

        def _parse_fare_holiday(data: object) -> float | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(float | str | Unset, data)

        fare_holiday = _parse_fare_holiday(d.pop("fareHoliday", UNSET))

        def _parse_latitude(data: object) -> float | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(float | str | Unset, data)

        latitude = _parse_latitude(d.pop("latitude", UNSET))

        def _parse_longitude(data: object) -> float | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(float | str | Unset, data)

        longitude = _parse_longitude(d.pop("longitude", UNSET))

        some_departure_observe_only = d.pop("someDepartureObserveOnly", UNSET)

        def _parse_stop_id(data: object) -> int | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(int | str | Unset, data)

        stop_id = _parse_stop_id(d.pop("stopId", UNSET))

        stop_location_c = d.pop("stopLocation_c", UNSET)

        stop_location_e = d.pop("stopLocation_e", UNSET)

        stop_location_s = d.pop("stopLocation_s", UNSET)

        stop_name_c = d.pop("stopName_c", UNSET)

        stop_name_e = d.pop("stopName_e", UNSET)

        stop_name_s = d.pop("stopName_s", UNSET)

        stop = cls(
            fare=fare,
            fare_holiday=fare_holiday,
            latitude=latitude,
            longitude=longitude,
            some_departure_observe_only=some_departure_observe_only,
            stop_id=stop_id,
            stop_location_c=stop_location_c,
            stop_location_e=stop_location_e,
            stop_location_s=stop_location_s,
            stop_name_c=stop_name_c,
            stop_name_e=stop_name_e,
            stop_name_s=stop_name_s,
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
