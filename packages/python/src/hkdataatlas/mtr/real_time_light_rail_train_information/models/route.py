from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Route")


@_attrs_define
class Route:
    """Train and route information. For regular routes, the route number is obtained from route_no. For special routes,
    special is 1 and the route number should be obtained from additionalInfo1, not route_no.

        Attributes:
            additional_info_1 (str | Unset): Route number information for a special route. Examples in the dictionary
                include values such as 751P* and SPR; SPR means Special/特別車. The API example also shows 507*.
            arrival_departure (str | Unset): A means the time acts as remaining arrival time for a normal station; D means
                the time acts as remaining departure time for a terminal station.
            dest_ch (str | Unset): Destination of the route in Chinese.
            dest_en (str | Unset): Destination of the route in English.
            route_remark_chi_2 (None | str | Unset): Remark for this route in Traditional Chinese.
            route_remark_eng_2 (None | str | Unset): Remark for the route in English.
            route_no (str | Unset): Route number.
            special (int | Unset): Indicates whether the route is special: 0 is regular; 1 is special.
            stop (int | Unset): Indicates whether the line is stopped.
            time_ch (str | Unset): Arrival/departure time in Chinese. '正在離開' means the train is departing from the terminus
                soon; '即將抵達' means the train is arriving soon; '-' means the train is arriving or departing.
            time_en (str | Unset): Arrival/departure time in English. 'departing' means the train is departing from the
                terminus soon; 'arriving' means the train is arriving soon; '-' means the train is arriving or departing.
            train_length (int | Unset): Length of the train.
    """

    additional_info_1: str | Unset = UNSET
    arrival_departure: str | Unset = UNSET
    dest_ch: str | Unset = UNSET
    dest_en: str | Unset = UNSET
    route_remark_chi_2: None | str | Unset = UNSET
    route_remark_eng_2: None | str | Unset = UNSET
    route_no: str | Unset = UNSET
    special: int | Unset = UNSET
    stop: int | Unset = UNSET
    time_ch: str | Unset = UNSET
    time_en: str | Unset = UNSET
    train_length: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        additional_info_1 = self.additional_info_1

        arrival_departure = self.arrival_departure

        dest_ch = self.dest_ch

        dest_en = self.dest_en

        route_remark_chi_2: None | str | Unset
        if isinstance(self.route_remark_chi_2, Unset):
            route_remark_chi_2 = UNSET
        else:
            route_remark_chi_2 = self.route_remark_chi_2

        route_remark_eng_2: None | str | Unset
        if isinstance(self.route_remark_eng_2, Unset):
            route_remark_eng_2 = UNSET
        else:
            route_remark_eng_2 = self.route_remark_eng_2

        route_no = self.route_no

        special = self.special

        stop = self.stop

        time_ch = self.time_ch

        time_en = self.time_en

        train_length = self.train_length

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if additional_info_1 is not UNSET:
            field_dict["additionalInfo1"] = additional_info_1
        if arrival_departure is not UNSET:
            field_dict["arrival_departure"] = arrival_departure
        if dest_ch is not UNSET:
            field_dict["dest_ch"] = dest_ch
        if dest_en is not UNSET:
            field_dict["dest_en"] = dest_en
        if route_remark_chi_2 is not UNSET:
            field_dict["routeRemarkChi2"] = route_remark_chi_2
        if route_remark_eng_2 is not UNSET:
            field_dict["routeRemarkEng2"] = route_remark_eng_2
        if route_no is not UNSET:
            field_dict["route_no"] = route_no
        if special is not UNSET:
            field_dict["special"] = special
        if stop is not UNSET:
            field_dict["stop"] = stop
        if time_ch is not UNSET:
            field_dict["time_ch"] = time_ch
        if time_en is not UNSET:
            field_dict["time_en"] = time_en
        if train_length is not UNSET:
            field_dict["train_length"] = train_length

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        additional_info_1 = d.pop("additionalInfo1", UNSET)

        arrival_departure = d.pop("arrival_departure", UNSET)

        dest_ch = d.pop("dest_ch", UNSET)

        dest_en = d.pop("dest_en", UNSET)

        def _parse_route_remark_chi_2(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        route_remark_chi_2 = _parse_route_remark_chi_2(d.pop("routeRemarkChi2", UNSET))

        def _parse_route_remark_eng_2(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        route_remark_eng_2 = _parse_route_remark_eng_2(d.pop("routeRemarkEng2", UNSET))

        route_no = d.pop("route_no", UNSET)

        special = d.pop("special", UNSET)

        stop = d.pop("stop", UNSET)

        time_ch = d.pop("time_ch", UNSET)

        time_en = d.pop("time_en", UNSET)

        train_length = d.pop("train_length", UNSET)

        route = cls(
            additional_info_1=additional_info_1,
            arrival_departure=arrival_departure,
            dest_ch=dest_ch,
            dest_en=dest_en,
            route_remark_chi_2=route_remark_chi_2,
            route_remark_eng_2=route_remark_eng_2,
            route_no=route_no,
            special=special,
            stop=stop,
            time_ch=time_ch,
            time_en=time_en,
            train_length=train_length,
        )

        route.additional_properties = d
        return route

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
