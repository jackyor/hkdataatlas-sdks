from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.train_route import TrainRoute, check_train_route
from ..models.train_timetype import TrainTimetype, check_train_timetype
from ..types import UNSET, Unset

T = TypeVar("T", bound="Train")


@_attrs_define
class Train:
    """A train entry. The dictionary labels ttnt, valid, and source as Dummy/N/A; their sample representations are retained
    without asserting additional semantics. Dictionary numeric declarations for plat and seq conflict with string
    representations in examples; either representation is permitted.

        Attributes:
            dest (str | Unset): MTR station code in capital letters. Dictionary describes this as 3 characters.
            plat (float | str | Unset): Platform number for the departure/arrival train. Dictionary declares Numbers, while
                examples represent the value as a string.
            route (TrainRoute | Unset): Optional field documented for EAL only. Indicates a train to destination via
                Racecourse rather than Fo Tan: empty string = normal; RAC = via Racecourse station.
            seq (float | str | Unset): Sequence of upcoming trains; dictionary gives values 1, 2, 3, 4. The sample
                represents the sequence as a string, while the dictionary declares Numbers.
            source (str | Unset): Dictionary type: Dummy; description: N/A. The schedule example represents this value as
                "-".
            time (str | Unset): Estimated arrival or departure time of the train, in yyyy-MM-dd HH:mm:ss format.
            timetype (TrainTimetype | Unset): Optional field documented for EAL only. Indicates whether the train is
                arriving or departing: A = Arrival, D = Departure.
            ttnt (str | Unset): Dictionary type: Dummy; description: N/A. The schedule example represents this value as a
                string.
            valid (str | Unset): Dictionary type: Dummy; description: N/A. The schedule example represents this value as a
                string.
    """

    dest: str | Unset = UNSET
    plat: float | str | Unset = UNSET
    route: TrainRoute | Unset = UNSET
    seq: float | str | Unset = UNSET
    source: str | Unset = UNSET
    time: str | Unset = UNSET
    timetype: TrainTimetype | Unset = UNSET
    ttnt: str | Unset = UNSET
    valid: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dest = self.dest

        plat: float | str | Unset
        if isinstance(self.plat, Unset):
            plat = UNSET
        else:
            plat = self.plat

        route: str | Unset = UNSET
        if not isinstance(self.route, Unset):
            route = self.route

        seq: float | str | Unset
        if isinstance(self.seq, Unset):
            seq = UNSET
        else:
            seq = self.seq

        source = self.source

        time = self.time

        timetype: str | Unset = UNSET
        if not isinstance(self.timetype, Unset):
            timetype = self.timetype

        ttnt = self.ttnt

        valid = self.valid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dest is not UNSET:
            field_dict["dest"] = dest
        if plat is not UNSET:
            field_dict["plat"] = plat
        if route is not UNSET:
            field_dict["route"] = route
        if seq is not UNSET:
            field_dict["seq"] = seq
        if source is not UNSET:
            field_dict["source"] = source
        if time is not UNSET:
            field_dict["time"] = time
        if timetype is not UNSET:
            field_dict["timetype"] = timetype
        if ttnt is not UNSET:
            field_dict["ttnt"] = ttnt
        if valid is not UNSET:
            field_dict["valid"] = valid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        dest = d.pop("dest", UNSET)

        def _parse_plat(data: object) -> float | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(float | str | Unset, data)

        plat = _parse_plat(d.pop("plat", UNSET))

        _route = d.pop("route", UNSET)
        route: TrainRoute | Unset
        if isinstance(_route, Unset):
            route = UNSET
        else:
            route = check_train_route(_route)

        def _parse_seq(data: object) -> float | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(float | str | Unset, data)

        seq = _parse_seq(d.pop("seq", UNSET))

        source = d.pop("source", UNSET)

        time = d.pop("time", UNSET)

        _timetype = d.pop("timetype", UNSET)
        timetype: TrainTimetype | Unset
        if isinstance(_timetype, Unset):
            timetype = UNSET
        else:
            timetype = check_train_timetype(_timetype)

        ttnt = d.pop("ttnt", UNSET)

        valid = d.pop("valid", UNSET)

        train = cls(
            dest=dest,
            plat=plat,
            route=route,
            seq=seq,
            source=source,
            time=time,
            timetype=timetype,
            ttnt=ttnt,
            valid=valid,
        )

        train.additional_properties = d
        return train

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
