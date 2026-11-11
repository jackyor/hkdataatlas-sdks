from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer0Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer0Attributes:
    """
    Attributes:
        aud (float | None | Unset): Publisher field type: esriFieldTypeDouble
        cl_psy (float | None | Unset): Publisher field type: esriFieldTypeDouble
        diet (float | None | Unset): Publisher field type: esriFieldTypeDouble
        gc (float | None | Unset): Publisher field type: esriFieldTypeDouble
        msw (float | None | Unset): Publisher field type: esriFieldTypeDouble
        opt (float | None | Unset): Publisher field type: esriFieldTypeDouble
        orth (float | None | Unset): Publisher field type: esriFieldTypeDouble
        ot (float | None | Unset): Publisher field type: esriFieldTypeDouble
        overall (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pod (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pt (float | None | Unset): Publisher field type: esriFieldTypeDouble
        p_o (float | None | Unset): Publisher field type: esriFieldTypeDouble
        sp_th (float | None | Unset): Publisher field type: esriFieldTypeDouble
        facility_en (None | str | Unset): Publisher field type: esriFieldTypeString
        facility_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        facility_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        fin_yr (None | str | Unset): Publisher field type: esriFieldTypeString
        latitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        longitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    aud: float | None | Unset = UNSET
    cl_psy: float | None | Unset = UNSET
    diet: float | None | Unset = UNSET
    gc: float | None | Unset = UNSET
    msw: float | None | Unset = UNSET
    opt: float | None | Unset = UNSET
    orth: float | None | Unset = UNSET
    ot: float | None | Unset = UNSET
    overall: float | None | Unset = UNSET
    pod: float | None | Unset = UNSET
    pt: float | None | Unset = UNSET
    p_o: float | None | Unset = UNSET
    sp_th: float | None | Unset = UNSET
    facility_en: None | str | Unset = UNSET
    facility_sc: None | str | Unset = UNSET
    facility_tc: None | str | Unset = UNSET
    fin_yr: None | str | Unset = UNSET
    latitude: float | None | Unset = UNSET
    longitude: float | None | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aud: float | None | Unset
        if isinstance(self.aud, Unset):
            aud = UNSET
        else:
            aud = self.aud

        cl_psy: float | None | Unset
        if isinstance(self.cl_psy, Unset):
            cl_psy = UNSET
        else:
            cl_psy = self.cl_psy

        diet: float | None | Unset
        if isinstance(self.diet, Unset):
            diet = UNSET
        else:
            diet = self.diet

        gc: float | None | Unset
        if isinstance(self.gc, Unset):
            gc = UNSET
        else:
            gc = self.gc

        msw: float | None | Unset
        if isinstance(self.msw, Unset):
            msw = UNSET
        else:
            msw = self.msw

        opt: float | None | Unset
        if isinstance(self.opt, Unset):
            opt = UNSET
        else:
            opt = self.opt

        orth: float | None | Unset
        if isinstance(self.orth, Unset):
            orth = UNSET
        else:
            orth = self.orth

        ot: float | None | Unset
        if isinstance(self.ot, Unset):
            ot = UNSET
        else:
            ot = self.ot

        overall: float | None | Unset
        if isinstance(self.overall, Unset):
            overall = UNSET
        else:
            overall = self.overall

        pod: float | None | Unset
        if isinstance(self.pod, Unset):
            pod = UNSET
        else:
            pod = self.pod

        pt: float | None | Unset
        if isinstance(self.pt, Unset):
            pt = UNSET
        else:
            pt = self.pt

        p_o: float | None | Unset
        if isinstance(self.p_o, Unset):
            p_o = UNSET
        else:
            p_o = self.p_o

        sp_th: float | None | Unset
        if isinstance(self.sp_th, Unset):
            sp_th = UNSET
        else:
            sp_th = self.sp_th

        facility_en: None | str | Unset
        if isinstance(self.facility_en, Unset):
            facility_en = UNSET
        else:
            facility_en = self.facility_en

        facility_sc: None | str | Unset
        if isinstance(self.facility_sc, Unset):
            facility_sc = UNSET
        else:
            facility_sc = self.facility_sc

        facility_tc: None | str | Unset
        if isinstance(self.facility_tc, Unset):
            facility_tc = UNSET
        else:
            facility_tc = self.facility_tc

        fin_yr: None | str | Unset
        if isinstance(self.fin_yr, Unset):
            fin_yr = UNSET
        else:
            fin_yr = self.fin_yr

        latitude: float | None | Unset
        if isinstance(self.latitude, Unset):
            latitude = UNSET
        else:
            latitude = self.latitude

        longitude: float | None | Unset
        if isinstance(self.longitude, Unset):
            longitude = UNSET
        else:
            longitude = self.longitude

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aud is not UNSET:
            field_dict["AUD"] = aud
        if cl_psy is not UNSET:
            field_dict["CL_PSY"] = cl_psy
        if diet is not UNSET:
            field_dict["DIET"] = diet
        if gc is not UNSET:
            field_dict["GC"] = gc
        if msw is not UNSET:
            field_dict["MSW"] = msw
        if opt is not UNSET:
            field_dict["OPT"] = opt
        if orth is not UNSET:
            field_dict["ORTH"] = orth
        if ot is not UNSET:
            field_dict["OT"] = ot
        if overall is not UNSET:
            field_dict["Overall"] = overall
        if pod is not UNSET:
            field_dict["POD"] = pod
        if pt is not UNSET:
            field_dict["PT"] = pt
        if p_o is not UNSET:
            field_dict["P_O"] = p_o
        if sp_th is not UNSET:
            field_dict["SP_TH"] = sp_th
        if facility_en is not UNSET:
            field_dict["facility_en"] = facility_en
        if facility_sc is not UNSET:
            field_dict["facility_sc"] = facility_sc
        if facility_tc is not UNSET:
            field_dict["facility_tc"] = facility_tc
        if fin_yr is not UNSET:
            field_dict["fin_yr"] = fin_yr
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_aud(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        aud = _parse_aud(d.pop("AUD", UNSET))

        def _parse_cl_psy(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        cl_psy = _parse_cl_psy(d.pop("CL_PSY", UNSET))

        def _parse_diet(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        diet = _parse_diet(d.pop("DIET", UNSET))

        def _parse_gc(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        gc = _parse_gc(d.pop("GC", UNSET))

        def _parse_msw(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        msw = _parse_msw(d.pop("MSW", UNSET))

        def _parse_opt(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        opt = _parse_opt(d.pop("OPT", UNSET))

        def _parse_orth(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        orth = _parse_orth(d.pop("ORTH", UNSET))

        def _parse_ot(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        ot = _parse_ot(d.pop("OT", UNSET))

        def _parse_overall(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        overall = _parse_overall(d.pop("Overall", UNSET))

        def _parse_pod(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pod = _parse_pod(d.pop("POD", UNSET))

        def _parse_pt(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pt = _parse_pt(d.pop("PT", UNSET))

        def _parse_p_o(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        p_o = _parse_p_o(d.pop("P_O", UNSET))

        def _parse_sp_th(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        sp_th = _parse_sp_th(d.pop("SP_TH", UNSET))

        def _parse_facility_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        facility_en = _parse_facility_en(d.pop("facility_en", UNSET))

        def _parse_facility_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        facility_sc = _parse_facility_sc(d.pop("facility_sc", UNSET))

        def _parse_facility_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        facility_tc = _parse_facility_tc(d.pop("facility_tc", UNSET))

        def _parse_fin_yr(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fin_yr = _parse_fin_yr(d.pop("fin_yr", UNSET))

        def _parse_latitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        latitude = _parse_latitude(d.pop("latitude", UNSET))

        def _parse_longitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        longitude = _parse_longitude(d.pop("longitude", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            aud=aud,
            cl_psy=cl_psy,
            diet=diet,
            gc=gc,
            msw=msw,
            opt=opt,
            orth=orth,
            ot=ot,
            overall=overall,
            pod=pod,
            pt=pt,
            p_o=p_o,
            sp_th=sp_th,
            facility_en=facility_en,
            facility_sc=facility_sc,
            facility_tc=facility_tc,
            fin_yr=fin_yr,
            latitude=latitude,
            longitude=longitude,
            objectid=objectid,
        )

        arcgis_feature_server_arcgis_layer_0_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_0_attributes

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
