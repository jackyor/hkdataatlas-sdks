from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.stop_eta_record_co import StopEtaRecordCo, check_stop_eta_record_co
from ..models.stop_eta_record_dir_type_1 import (
    StopEtaRecordDirType1,
    check_stop_eta_record_dir_type_1,
)
from ..models.stop_eta_record_dir_type_2_type_1 import (
    StopEtaRecordDirType2Type1,
    check_stop_eta_record_dir_type_2_type_1,
)
from ..models.stop_eta_record_dir_type_3_type_1 import (
    StopEtaRecordDirType3Type1,
    check_stop_eta_record_dir_type_3_type_1,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="StopEtaRecord")


@_attrs_define
class StopEtaRecord:
    """An estimated-arrival record. Some fields are not applicable for a particular company, as noted individually.

    Attributes:
        co (StopEtaRecordCo | Unset): Company code. Documented codes: CTB (Citybus Limited) and NLB (New Lantao Bus
            Company Limited).
        data_timestamp (datetime.datetime | Unset): Timestamp when data was initially prepared from the origin server,
            with time zone in ISO 8601 format.
        departed (int | None | str | Unset): Preserves documented integer/null indicator and retained official empty-
            string representation for non-applicable company fields; lexical constraints are undocumented and no coercion is
            applied.
        dest (str | Unset): Destination of a route. Dictionary example uses the related dest_en label; it documents this
            field as a string.
        dir_ (None | StopEtaRecordDirType1 | StopEtaRecordDirType2Type1 | StopEtaRecordDirType3Type1 | Unset): Route
            direction; not applicable for NLB. I means inbound; O means outbound.
        eta (str | Unset): Timestamp of the next ETA, with time zone in ISO 8601 format. Retained publisherETA is also
            an empty string when not applicable; preserve published timestamp strings without requiring every string to be a
            strictRFC3339 value.
        eta_seq (int | None | Unset): ETA sequence number: 1 represents the next ETA, 2 the ETA after the first, and so
            on. Not applicable for NLB. Dictionary describes a numeric value; NLB example includes null.
        no_gps (int | None | str | Unset): Preserves documented integer/null indicator and retained official empty-
            string representation for non-applicable company fields; lexical constraints are undocumented and no coercion is
            applied.
        rmk (str | Unset): Remark of an ETA.
        route (str | Unset): Route number of the requested company.
        route_variant_name (None | str | Unset): Supplementary route name; not applicable for CTB.
        seq (int | None | Unset): Stop sequence number of a bus route; not applicable for NLB.
        stop (str | Unset): Bus stop ID.
        wheel_chair (int | None | str | Unset): Preserves documented integer/null indicator and retained official empty-
            string representation for non-applicable company fields; lexical constraints are undocumented and no coercion is
            applied.
    """

    co: StopEtaRecordCo | Unset = UNSET
    data_timestamp: datetime.datetime | Unset = UNSET
    departed: int | None | str | Unset = UNSET
    dest: str | Unset = UNSET
    dir_: (
        None
        | StopEtaRecordDirType1
        | StopEtaRecordDirType2Type1
        | StopEtaRecordDirType3Type1
        | Unset
    ) = UNSET
    eta: str | Unset = UNSET
    eta_seq: int | None | Unset = UNSET
    no_gps: int | None | str | Unset = UNSET
    rmk: str | Unset = UNSET
    route: str | Unset = UNSET
    route_variant_name: None | str | Unset = UNSET
    seq: int | None | Unset = UNSET
    stop: str | Unset = UNSET
    wheel_chair: int | None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        co: str | Unset = UNSET
        if not isinstance(self.co, Unset):
            co = self.co

        data_timestamp: str | Unset = UNSET
        if not isinstance(self.data_timestamp, Unset):
            data_timestamp = self.data_timestamp.isoformat()

        departed: int | None | str | Unset
        if isinstance(self.departed, Unset):
            departed = UNSET
        else:
            departed = self.departed

        dest = self.dest

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

        eta = self.eta

        eta_seq: int | None | Unset
        if isinstance(self.eta_seq, Unset):
            eta_seq = UNSET
        else:
            eta_seq = self.eta_seq

        no_gps: int | None | str | Unset
        if isinstance(self.no_gps, Unset):
            no_gps = UNSET
        else:
            no_gps = self.no_gps

        rmk = self.rmk

        route = self.route

        route_variant_name: None | str | Unset
        if isinstance(self.route_variant_name, Unset):
            route_variant_name = UNSET
        else:
            route_variant_name = self.route_variant_name

        seq: int | None | Unset
        if isinstance(self.seq, Unset):
            seq = UNSET
        else:
            seq = self.seq

        stop = self.stop

        wheel_chair: int | None | str | Unset
        if isinstance(self.wheel_chair, Unset):
            wheel_chair = UNSET
        else:
            wheel_chair = self.wheel_chair

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if co is not UNSET:
            field_dict["co"] = co
        if data_timestamp is not UNSET:
            field_dict["data_timestamp"] = data_timestamp
        if departed is not UNSET:
            field_dict["departed"] = departed
        if dest is not UNSET:
            field_dict["dest"] = dest
        if dir_ is not UNSET:
            field_dict["dir"] = dir_
        if eta is not UNSET:
            field_dict["eta"] = eta
        if eta_seq is not UNSET:
            field_dict["eta_seq"] = eta_seq
        if no_gps is not UNSET:
            field_dict["noGPS"] = no_gps
        if rmk is not UNSET:
            field_dict["rmk"] = rmk
        if route is not UNSET:
            field_dict["route"] = route
        if route_variant_name is not UNSET:
            field_dict["routeVariantName"] = route_variant_name
        if seq is not UNSET:
            field_dict["seq"] = seq
        if stop is not UNSET:
            field_dict["stop"] = stop
        if wheel_chair is not UNSET:
            field_dict["wheelChair"] = wheel_chair

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _co = d.pop("co", UNSET)
        co: StopEtaRecordCo | Unset
        if isinstance(_co, Unset):
            co = UNSET
        else:
            co = check_stop_eta_record_co(_co)

        _data_timestamp = d.pop("data_timestamp", UNSET)
        data_timestamp: datetime.datetime | Unset
        if isinstance(_data_timestamp, Unset):
            data_timestamp = UNSET
        else:
            data_timestamp = datetime.datetime.fromisoformat(_data_timestamp)

        def _parse_departed(data: object) -> int | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | str | Unset, data)

        departed = _parse_departed(d.pop("departed", UNSET))

        dest = d.pop("dest", UNSET)

        def _parse_dir_(
            data: object,
        ) -> (
            None
            | StopEtaRecordDirType1
            | StopEtaRecordDirType2Type1
            | StopEtaRecordDirType3Type1
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                dir_type_1 = check_stop_eta_record_dir_type_1(data)

                return dir_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                dir_type_2_type_1 = check_stop_eta_record_dir_type_2_type_1(data)

                return dir_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                dir_type_3_type_1 = check_stop_eta_record_dir_type_3_type_1(data)

                return dir_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | StopEtaRecordDirType1
                | StopEtaRecordDirType2Type1
                | StopEtaRecordDirType3Type1
                | Unset,
                data,
            )

        dir_ = _parse_dir_(d.pop("dir", UNSET))

        eta = d.pop("eta", UNSET)

        def _parse_eta_seq(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        eta_seq = _parse_eta_seq(d.pop("eta_seq", UNSET))

        def _parse_no_gps(data: object) -> int | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | str | Unset, data)

        no_gps = _parse_no_gps(d.pop("noGPS", UNSET))

        rmk = d.pop("rmk", UNSET)

        route = d.pop("route", UNSET)

        def _parse_route_variant_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        route_variant_name = _parse_route_variant_name(d.pop("routeVariantName", UNSET))

        def _parse_seq(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        seq = _parse_seq(d.pop("seq", UNSET))

        stop = d.pop("stop", UNSET)

        def _parse_wheel_chair(data: object) -> int | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | str | Unset, data)

        wheel_chair = _parse_wheel_chair(d.pop("wheelChair", UNSET))

        stop_eta_record = cls(
            co=co,
            data_timestamp=data_timestamp,
            departed=departed,
            dest=dest,
            dir_=dir_,
            eta=eta,
            eta_seq=eta_seq,
            no_gps=no_gps,
            rmk=rmk,
            route=route,
            route_variant_name=route_variant_name,
            seq=seq,
            stop=stop,
            wheel_chair=wheel_chair,
        )

        stop_eta_record.additional_properties = d
        return stop_eta_record

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
