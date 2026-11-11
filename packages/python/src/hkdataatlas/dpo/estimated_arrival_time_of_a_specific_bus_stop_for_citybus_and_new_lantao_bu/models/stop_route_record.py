from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.stop_route_record_co import StopRouteRecordCo, check_stop_route_record_co
from ..models.stop_route_record_dir_type_1 import (
    StopRouteRecordDirType1,
    check_stop_route_record_dir_type_1,
)
from ..models.stop_route_record_dir_type_2_type_1 import (
    StopRouteRecordDirType2Type1,
    check_stop_route_record_dir_type_2_type_1,
)
from ..models.stop_route_record_dir_type_3_type_1 import (
    StopRouteRecordDirType3Type1,
    check_stop_route_record_dir_type_3_type_1,
)
from ..models.stop_route_record_overnight_route_type_1 import (
    StopRouteRecordOvernightRouteType1,
    check_stop_route_record_overnight_route_type_1,
)
from ..models.stop_route_record_overnight_route_type_2_type_1 import (
    StopRouteRecordOvernightRouteType2Type1,
    check_stop_route_record_overnight_route_type_2_type_1,
)
from ..models.stop_route_record_overnight_route_type_3_type_1 import (
    StopRouteRecordOvernightRouteType3Type1,
    check_stop_route_record_overnight_route_type_3_type_1,
)
from ..models.stop_route_record_special_route_type_1 import (
    StopRouteRecordSpecialRouteType1,
    check_stop_route_record_special_route_type_1,
)
from ..models.stop_route_record_special_route_type_2_type_1 import (
    StopRouteRecordSpecialRouteType2Type1,
    check_stop_route_record_special_route_type_2_type_1,
)
from ..models.stop_route_record_special_route_type_3_type_1 import (
    StopRouteRecordSpecialRouteType3Type1,
    check_stop_route_record_special_route_type_3_type_1,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="StopRouteRecord")


@_attrs_define
class StopRouteRecord:
    """A route record for a requested stop. Field applicability differs by company; null indicates a field is not
    applicable for the respective company.

        Attributes:
            co (StopRouteRecordCo | Unset): Company code. Documented codes: CTB (Citybus Limited) and NLB (New Lantao Bus
                Company Limited).
            data_timestamp (datetime.datetime | Unset): Timestamp when data was initially prepared from the origin server,
                with time zone in ISO 8601 format.
            dir_ (None | StopRouteRecordDirType1 | StopRouteRecordDirType2Type1 | StopRouteRecordDirType3Type1 | Unset):
                Route direction; not applicable for NLB. I means inbound; O means outbound.
            overnight_route (None | StopRouteRecordOvernightRouteType1 | StopRouteRecordOvernightRouteType2Type1 |
                StopRouteRecordOvernightRouteType3Type1 | Unset): Indicator of an overnight route; not applicable for CTB. 0
                means not an overnight route; 1 means an overnight route.
            route (str | Unset): Route number of the requested company.
            route_id (None | str | Unset): Route ID of the respective company's route; not applicable for CTB.
            route_name (None | str | Unset): Name of a route; not applicable for CTB.
            seq (int | Unset): Stop sequence number of a bus route; not applicable for NLB. The dictionary documents a
                numeric type. The API sample shows this as a number (for example, 11), while a data-dictionary example shows a
                string representation (for example, "10").
            special_route (None | StopRouteRecordSpecialRouteType1 | StopRouteRecordSpecialRouteType2Type1 |
                StopRouteRecordSpecialRouteType3Type1 | Unset): Indicator of a special route; not applicable for CTB. 0 means
                not a special route; 1 means a special route.
            stop (str | Unset): Bus stop ID.
    """

    co: StopRouteRecordCo | Unset = UNSET
    data_timestamp: datetime.datetime | Unset = UNSET
    dir_: (
        None
        | StopRouteRecordDirType1
        | StopRouteRecordDirType2Type1
        | StopRouteRecordDirType3Type1
        | Unset
    ) = UNSET
    overnight_route: (
        None
        | StopRouteRecordOvernightRouteType1
        | StopRouteRecordOvernightRouteType2Type1
        | StopRouteRecordOvernightRouteType3Type1
        | Unset
    ) = UNSET
    route: str | Unset = UNSET
    route_id: None | str | Unset = UNSET
    route_name: None | str | Unset = UNSET
    seq: int | Unset = UNSET
    special_route: (
        None
        | StopRouteRecordSpecialRouteType1
        | StopRouteRecordSpecialRouteType2Type1
        | StopRouteRecordSpecialRouteType3Type1
        | Unset
    ) = UNSET
    stop: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        co: str | Unset = UNSET
        if not isinstance(self.co, Unset):
            co = self.co

        data_timestamp: str | Unset = UNSET
        if not isinstance(self.data_timestamp, Unset):
            data_timestamp = self.data_timestamp.isoformat()

        dir_: None | str | Unset
        if isinstance(self.dir_, Unset):
            dir_ = UNSET
        elif (
            isinstance(self.dir_, str)
            or isinstance(self.dir_, str)
            or isinstance(self.dir_, str)
        ):
            dir_ = self.dir_
        else:
            dir_ = self.dir_

        overnight_route: int | None | Unset
        if isinstance(self.overnight_route, Unset):
            overnight_route = UNSET
        elif (
            isinstance(self.overnight_route, int)
            or isinstance(self.overnight_route, int)
            or isinstance(self.overnight_route, int)
        ):
            overnight_route = self.overnight_route
        else:
            overnight_route = self.overnight_route

        route = self.route

        route_id: None | str | Unset
        if isinstance(self.route_id, Unset):
            route_id = UNSET
        else:
            route_id = self.route_id

        route_name: None | str | Unset
        if isinstance(self.route_name, Unset):
            route_name = UNSET
        else:
            route_name = self.route_name

        seq = self.seq

        special_route: int | None | Unset
        if isinstance(self.special_route, Unset):
            special_route = UNSET
        elif (
            isinstance(self.special_route, int)
            or isinstance(self.special_route, int)
            or isinstance(self.special_route, int)
        ):
            special_route = self.special_route
        else:
            special_route = self.special_route

        stop = self.stop

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if co is not UNSET:
            field_dict["co"] = co
        if data_timestamp is not UNSET:
            field_dict["data_timestamp"] = data_timestamp
        if dir_ is not UNSET:
            field_dict["dir"] = dir_
        if overnight_route is not UNSET:
            field_dict["overnightRoute"] = overnight_route
        if route is not UNSET:
            field_dict["route"] = route
        if route_id is not UNSET:
            field_dict["routeId"] = route_id
        if route_name is not UNSET:
            field_dict["routeName"] = route_name
        if seq is not UNSET:
            field_dict["seq"] = seq
        if special_route is not UNSET:
            field_dict["specialRoute"] = special_route
        if stop is not UNSET:
            field_dict["stop"] = stop

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _co = d.pop("co", UNSET)
        co: StopRouteRecordCo | Unset
        if isinstance(_co, Unset):
            co = UNSET
        else:
            co = check_stop_route_record_co(_co)

        _data_timestamp = d.pop("data_timestamp", UNSET)
        data_timestamp: datetime.datetime | Unset
        if isinstance(_data_timestamp, Unset):
            data_timestamp = UNSET
        else:
            data_timestamp = datetime.datetime.fromisoformat(_data_timestamp)

        def _parse_dir_(
            data: object,
        ) -> (
            None
            | StopRouteRecordDirType1
            | StopRouteRecordDirType2Type1
            | StopRouteRecordDirType3Type1
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                dir_type_1 = check_stop_route_record_dir_type_1(data)

                return dir_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                dir_type_2_type_1 = check_stop_route_record_dir_type_2_type_1(data)

                return dir_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                dir_type_3_type_1 = check_stop_route_record_dir_type_3_type_1(data)

                return dir_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | StopRouteRecordDirType1
                | StopRouteRecordDirType2Type1
                | StopRouteRecordDirType3Type1
                | Unset,
                data,
            )

        dir_ = _parse_dir_(d.pop("dir", UNSET))

        def _parse_overnight_route(
            data: object,
        ) -> (
            None
            | StopRouteRecordOvernightRouteType1
            | StopRouteRecordOvernightRouteType2Type1
            | StopRouteRecordOvernightRouteType3Type1
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, int):
                    raise TypeError()
                overnight_route_type_1 = check_stop_route_record_overnight_route_type_1(
                    data
                )

                return overnight_route_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                overnight_route_type_2_type_1 = (
                    check_stop_route_record_overnight_route_type_2_type_1(data)
                )

                return overnight_route_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                overnight_route_type_3_type_1 = (
                    check_stop_route_record_overnight_route_type_3_type_1(data)
                )

                return overnight_route_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | StopRouteRecordOvernightRouteType1
                | StopRouteRecordOvernightRouteType2Type1
                | StopRouteRecordOvernightRouteType3Type1
                | Unset,
                data,
            )

        overnight_route = _parse_overnight_route(d.pop("overnightRoute", UNSET))

        route = d.pop("route", UNSET)

        def _parse_route_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        route_id = _parse_route_id(d.pop("routeId", UNSET))

        def _parse_route_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        route_name = _parse_route_name(d.pop("routeName", UNSET))

        seq = d.pop("seq", UNSET)

        def _parse_special_route(
            data: object,
        ) -> (
            None
            | StopRouteRecordSpecialRouteType1
            | StopRouteRecordSpecialRouteType2Type1
            | StopRouteRecordSpecialRouteType3Type1
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, int):
                    raise TypeError()
                special_route_type_1 = check_stop_route_record_special_route_type_1(
                    data
                )

                return special_route_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                special_route_type_2_type_1 = (
                    check_stop_route_record_special_route_type_2_type_1(data)
                )

                return special_route_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                special_route_type_3_type_1 = (
                    check_stop_route_record_special_route_type_3_type_1(data)
                )

                return special_route_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | StopRouteRecordSpecialRouteType1
                | StopRouteRecordSpecialRouteType2Type1
                | StopRouteRecordSpecialRouteType3Type1
                | Unset,
                data,
            )

        special_route = _parse_special_route(d.pop("specialRoute", UNSET))

        stop = d.pop("stop", UNSET)

        stop_route_record = cls(
            co=co,
            data_timestamp=data_timestamp,
            dir_=dir_,
            overnight_route=overnight_route,
            route=route,
            route_id=route_id,
            route_name=route_name,
            seq=seq,
            special_route=special_route,
            stop=stop,
        )

        stop_route_record.additional_properties = d
        return stop_route_record

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
