from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HkoMeteorologicalData")


@_attrs_define
class HkoMeteorologicalData:
    """Meteorological payload fields documented for HKO. The data dictionary declares these values as strings; some
    examples are presented without quotation marks, so the schema allows either string or number for those fields to
    preserve the discrepancy.

        Attributes:
            dh (float | str | Unset): Device height, in m; resolution 1 m. Declared data type: String. The data dictionary
                example is the unquoted number 3, while the API response example uses the string "12"; both representations are
                allowed.
            rh (str | Unset): Relative humidity, in %; resolution 0.1 %. The data dictionary declares String. Example:
                "93.1"; "////" if quality control fails.
            t0 (str | Unset): Air temperature, in °C; resolution 0.1 °C. The data dictionary declares String. Example:
                "19.8"; "////" if quality control fails.
            tp (str | Unset): Data processed time in Hong Kong Time. Format: YYYYMMDDHHMMSS (described as ISO 8601
                notation). Example: 20230913174049.
            ts (str | Unset): Data measurement time in Hong Kong Time. Format: YYYYMMDDHHMMSS (described as ISO 8601
                notation). Example: 20230913174049.
            vn (str | Unset): Version number of the payload format. Resolution: 0.1. Example: 1.0.
            wd (float | str | Unset): 10-minute mean wind direction, in degrees; resolution 1°. Declared data type: String.
                The data dictionary's example is the unquoted number 108, while the API response example uses the string "143";
                both representations are allowed. "////" if quality control fails.
            ws (float | str | Unset): 10-minute mean wind speed, in km/h; resolution 1 km/h. Declared data type: String. The
                data dictionary's example is the unquoted number 3, while the API response example uses the string "4"; both
                representations are allowed. "////" if quality control fails.
    """

    dh: float | str | Unset = UNSET
    rh: str | Unset = UNSET
    t0: str | Unset = UNSET
    tp: str | Unset = UNSET
    ts: str | Unset = UNSET
    vn: str | Unset = UNSET
    wd: float | str | Unset = UNSET
    ws: float | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dh: float | str | Unset
        if isinstance(self.dh, Unset):
            dh = UNSET
        else:
            dh = self.dh

        rh = self.rh

        t0 = self.t0

        tp = self.tp

        ts = self.ts

        vn = self.vn

        wd: float | str | Unset
        if isinstance(self.wd, Unset):
            wd = UNSET
        else:
            wd = self.wd

        ws: float | str | Unset
        if isinstance(self.ws, Unset):
            ws = UNSET
        else:
            ws = self.ws

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dh is not UNSET:
            field_dict["DH"] = dh
        if rh is not UNSET:
            field_dict["RH"] = rh
        if t0 is not UNSET:
            field_dict["T0"] = t0
        if tp is not UNSET:
            field_dict["TP"] = tp
        if ts is not UNSET:
            field_dict["TS"] = ts
        if vn is not UNSET:
            field_dict["VN"] = vn
        if wd is not UNSET:
            field_dict["WD"] = wd
        if ws is not UNSET:
            field_dict["WS"] = ws

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_dh(data: object) -> float | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(float | str | Unset, data)

        dh = _parse_dh(d.pop("DH", UNSET))

        rh = d.pop("RH", UNSET)

        t0 = d.pop("T0", UNSET)

        tp = d.pop("TP", UNSET)

        ts = d.pop("TS", UNSET)

        vn = d.pop("VN", UNSET)

        def _parse_wd(data: object) -> float | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(float | str | Unset, data)

        wd = _parse_wd(d.pop("WD", UNSET))

        def _parse_ws(data: object) -> float | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(float | str | Unset, data)

        ws = _parse_ws(d.pop("WS", UNSET))

        hko_meteorological_data = cls(
            dh=dh,
            rh=rh,
            t0=t0,
            tp=tp,
            ts=ts,
            vn=vn,
            wd=wd,
            ws=ws,
        )

        hko_meteorological_data.additional_properties = d
        return hko_meteorological_data

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
