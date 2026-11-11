from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TradeRecord")


@_attrs_define
class TradeRecord:
    """Trade data record illustrated in the documented response. The documented example encodes `ttype` as an integer
    although request trade-type values are shown as codes; `figure` is shown as a string. Language-dependent description
    and unit property names vary with the selected language.

        Attributes:
            cc (str | Unset): Consignment code.
            cc_desc_en (str | Unset): Consignment description; language suffix varies with `lang`.
            cc_region (str | Unset):
            cc_region_dsec_en (str | Unset): Consignment-region description; language suffix varies with `lang`.
            co (str | Unset): Origin code, if present.
            co_desc_en (str | Unset): Origin description; language suffix varies with `lang`.
            co_region (str | Unset):
            co_region_dsec_en (str | Unset): Origin-region description; language suffix varies with `lang`.
            code (str | Unset): Commodity code.
            code_dsec_en (str | Unset): Commodity description; language suffix varies with `lang`.
            codeclass (str | Unset): Commodity classification code.
            figure (str | Unset): Statistical value, represented as a string in the documented response sample.
            freq (str | Unset): Frequency code.
            period (str | Unset): Annual or monthly period code.
            sv (str | Unset): Statistics selection code.
            sv_desc_en (str | Unset): Statistics description; language suffix varies with `lang`.
            tm (str | Unset):
            tm_dsec_en (str | Unset): Transport mode description; language suffix varies with `lang`.
            ttype (int | str | Unset): Trade type; the documented response sample uses an integer while request values are
                codes.
            ttype_desc_en (str | Unset): Trade type description in English; language-specific suffix varies with `lang`.
            unit_en (str | Unset): Unit; language suffix varies with `lang`.
    """

    cc: str | Unset = UNSET
    cc_desc_en: str | Unset = UNSET
    cc_region: str | Unset = UNSET
    cc_region_dsec_en: str | Unset = UNSET
    co: str | Unset = UNSET
    co_desc_en: str | Unset = UNSET
    co_region: str | Unset = UNSET
    co_region_dsec_en: str | Unset = UNSET
    code: str | Unset = UNSET
    code_dsec_en: str | Unset = UNSET
    codeclass: str | Unset = UNSET
    figure: str | Unset = UNSET
    freq: str | Unset = UNSET
    period: str | Unset = UNSET
    sv: str | Unset = UNSET
    sv_desc_en: str | Unset = UNSET
    tm: str | Unset = UNSET
    tm_dsec_en: str | Unset = UNSET
    ttype: int | str | Unset = UNSET
    ttype_desc_en: str | Unset = UNSET
    unit_en: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cc = self.cc

        cc_desc_en = self.cc_desc_en

        cc_region = self.cc_region

        cc_region_dsec_en = self.cc_region_dsec_en

        co = self.co

        co_desc_en = self.co_desc_en

        co_region = self.co_region

        co_region_dsec_en = self.co_region_dsec_en

        code = self.code

        code_dsec_en = self.code_dsec_en

        codeclass = self.codeclass

        figure = self.figure

        freq = self.freq

        period = self.period

        sv = self.sv

        sv_desc_en = self.sv_desc_en

        tm = self.tm

        tm_dsec_en = self.tm_dsec_en

        ttype: int | str | Unset
        if isinstance(self.ttype, Unset):
            ttype = UNSET
        else:
            ttype = self.ttype

        ttype_desc_en = self.ttype_desc_en

        unit_en = self.unit_en

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cc is not UNSET:
            field_dict["cc"] = cc
        if cc_desc_en is not UNSET:
            field_dict["ccDescEN"] = cc_desc_en
        if cc_region is not UNSET:
            field_dict["ccRegion"] = cc_region
        if cc_region_dsec_en is not UNSET:
            field_dict["ccRegionDsecEN"] = cc_region_dsec_en
        if co is not UNSET:
            field_dict["co"] = co
        if co_desc_en is not UNSET:
            field_dict["coDescEN"] = co_desc_en
        if co_region is not UNSET:
            field_dict["coRegion"] = co_region
        if co_region_dsec_en is not UNSET:
            field_dict["coRegionDsecEN"] = co_region_dsec_en
        if code is not UNSET:
            field_dict["code"] = code
        if code_dsec_en is not UNSET:
            field_dict["codeDsecEN"] = code_dsec_en
        if codeclass is not UNSET:
            field_dict["codeclass"] = codeclass
        if figure is not UNSET:
            field_dict["figure"] = figure
        if freq is not UNSET:
            field_dict["freq"] = freq
        if period is not UNSET:
            field_dict["period"] = period
        if sv is not UNSET:
            field_dict["sv"] = sv
        if sv_desc_en is not UNSET:
            field_dict["svDescEN"] = sv_desc_en
        if tm is not UNSET:
            field_dict["tm"] = tm
        if tm_dsec_en is not UNSET:
            field_dict["tmDsecEN"] = tm_dsec_en
        if ttype is not UNSET:
            field_dict["ttype"] = ttype
        if ttype_desc_en is not UNSET:
            field_dict["ttypeDescEN"] = ttype_desc_en
        if unit_en is not UNSET:
            field_dict["unitEN"] = unit_en

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        cc = d.pop("cc", UNSET)

        cc_desc_en = d.pop("ccDescEN", UNSET)

        cc_region = d.pop("ccRegion", UNSET)

        cc_region_dsec_en = d.pop("ccRegionDsecEN", UNSET)

        co = d.pop("co", UNSET)

        co_desc_en = d.pop("coDescEN", UNSET)

        co_region = d.pop("coRegion", UNSET)

        co_region_dsec_en = d.pop("coRegionDsecEN", UNSET)

        code = d.pop("code", UNSET)

        code_dsec_en = d.pop("codeDsecEN", UNSET)

        codeclass = d.pop("codeclass", UNSET)

        figure = d.pop("figure", UNSET)

        freq = d.pop("freq", UNSET)

        period = d.pop("period", UNSET)

        sv = d.pop("sv", UNSET)

        sv_desc_en = d.pop("svDescEN", UNSET)

        tm = d.pop("tm", UNSET)

        tm_dsec_en = d.pop("tmDsecEN", UNSET)

        def _parse_ttype(data: object) -> int | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(int | str | Unset, data)

        ttype = _parse_ttype(d.pop("ttype", UNSET))

        ttype_desc_en = d.pop("ttypeDescEN", UNSET)

        unit_en = d.pop("unitEN", UNSET)

        trade_record = cls(
            cc=cc,
            cc_desc_en=cc_desc_en,
            cc_region=cc_region,
            cc_region_dsec_en=cc_region_dsec_en,
            co=co,
            co_desc_en=co_desc_en,
            co_region=co_region,
            co_region_dsec_en=co_region_dsec_en,
            code=code,
            code_dsec_en=code_dsec_en,
            codeclass=codeclass,
            figure=figure,
            freq=freq,
            period=period,
            sv=sv,
            sv_desc_en=sv_desc_en,
            tm=tm,
            tm_dsec_en=tm_dsec_en,
            ttype=ttype,
            ttype_desc_en=ttype_desc_en,
            unit_en=unit_en,
        )

        trade_record.additional_properties = d
        return trade_record

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
