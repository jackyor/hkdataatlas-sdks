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
        area_chi (None | str | Unset): Publisher field type: esriFieldTypeString
        area_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        period (float | None | Unset): Publisher field type: esriFieldTypeDouble
        qtr_all (float | None | Unset): Publisher field type: esriFieldTypeDouble
        qtr_ph (float | None | Unset): Publisher field type: esriFieldTypeDouble
        qtr_ph_ndq (float | None | Unset): Publisher field type: esriFieldTypeDouble
        qtr_ph_prf (float | None | Unset): Publisher field type: esriFieldTypeDouble
        qtr_ph_sq (float | None | Unset): Publisher field type: esriFieldTypeDouble
        qtr_ph_sstv (float | None | Unset): Publisher field type: esriFieldTypeDouble
        qtr_ph_vbm (float | None | Unset): Publisher field type: esriFieldTypeDouble
        qtr_prh (float | None | Unset): Publisher field type: esriFieldTypeDouble
        qtr_prh_ha (float | None | Unset): Publisher field type: esriFieldTypeDouble
        qtr_prh_hs (float | None | Unset): Publisher field type: esriFieldTypeDouble
        qtr_ssf (float | None | Unset): Publisher field type: esriFieldTypeDouble
        qtr_ssf_ha (float | None | Unset): Publisher field type: esriFieldTypeDouble
        qtr_ssf_hs (float | None | Unset): Publisher field type: esriFieldTypeDouble
        qtr_ssf_ura (float | None | Unset): Publisher field type: esriFieldTypeDouble
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
        shape_area (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    area_chi: None | str | Unset = UNSET
    area_eng: None | str | Unset = UNSET
    period: float | None | Unset = UNSET
    qtr_all: float | None | Unset = UNSET
    qtr_ph: float | None | Unset = UNSET
    qtr_ph_ndq: float | None | Unset = UNSET
    qtr_ph_prf: float | None | Unset = UNSET
    qtr_ph_sq: float | None | Unset = UNSET
    qtr_ph_sstv: float | None | Unset = UNSET
    qtr_ph_vbm: float | None | Unset = UNSET
    qtr_prh: float | None | Unset = UNSET
    qtr_prh_ha: float | None | Unset = UNSET
    qtr_prh_hs: float | None | Unset = UNSET
    qtr_ssf: float | None | Unset = UNSET
    qtr_ssf_ha: float | None | Unset = UNSET
    qtr_ssf_hs: float | None | Unset = UNSET
    qtr_ssf_ura: float | None | Unset = UNSET
    objectid: int | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        area_chi: None | str | Unset
        if isinstance(self.area_chi, Unset):
            area_chi = UNSET
        else:
            area_chi = self.area_chi

        area_eng: None | str | Unset
        if isinstance(self.area_eng, Unset):
            area_eng = UNSET
        else:
            area_eng = self.area_eng

        period: float | None | Unset
        if isinstance(self.period, Unset):
            period = UNSET
        else:
            period = self.period

        qtr_all: float | None | Unset
        if isinstance(self.qtr_all, Unset):
            qtr_all = UNSET
        else:
            qtr_all = self.qtr_all

        qtr_ph: float | None | Unset
        if isinstance(self.qtr_ph, Unset):
            qtr_ph = UNSET
        else:
            qtr_ph = self.qtr_ph

        qtr_ph_ndq: float | None | Unset
        if isinstance(self.qtr_ph_ndq, Unset):
            qtr_ph_ndq = UNSET
        else:
            qtr_ph_ndq = self.qtr_ph_ndq

        qtr_ph_prf: float | None | Unset
        if isinstance(self.qtr_ph_prf, Unset):
            qtr_ph_prf = UNSET
        else:
            qtr_ph_prf = self.qtr_ph_prf

        qtr_ph_sq: float | None | Unset
        if isinstance(self.qtr_ph_sq, Unset):
            qtr_ph_sq = UNSET
        else:
            qtr_ph_sq = self.qtr_ph_sq

        qtr_ph_sstv: float | None | Unset
        if isinstance(self.qtr_ph_sstv, Unset):
            qtr_ph_sstv = UNSET
        else:
            qtr_ph_sstv = self.qtr_ph_sstv

        qtr_ph_vbm: float | None | Unset
        if isinstance(self.qtr_ph_vbm, Unset):
            qtr_ph_vbm = UNSET
        else:
            qtr_ph_vbm = self.qtr_ph_vbm

        qtr_prh: float | None | Unset
        if isinstance(self.qtr_prh, Unset):
            qtr_prh = UNSET
        else:
            qtr_prh = self.qtr_prh

        qtr_prh_ha: float | None | Unset
        if isinstance(self.qtr_prh_ha, Unset):
            qtr_prh_ha = UNSET
        else:
            qtr_prh_ha = self.qtr_prh_ha

        qtr_prh_hs: float | None | Unset
        if isinstance(self.qtr_prh_hs, Unset):
            qtr_prh_hs = UNSET
        else:
            qtr_prh_hs = self.qtr_prh_hs

        qtr_ssf: float | None | Unset
        if isinstance(self.qtr_ssf, Unset):
            qtr_ssf = UNSET
        else:
            qtr_ssf = self.qtr_ssf

        qtr_ssf_ha: float | None | Unset
        if isinstance(self.qtr_ssf_ha, Unset):
            qtr_ssf_ha = UNSET
        else:
            qtr_ssf_ha = self.qtr_ssf_ha

        qtr_ssf_hs: float | None | Unset
        if isinstance(self.qtr_ssf_hs, Unset):
            qtr_ssf_hs = UNSET
        else:
            qtr_ssf_hs = self.qtr_ssf_hs

        qtr_ssf_ura: float | None | Unset
        if isinstance(self.qtr_ssf_ura, Unset):
            qtr_ssf_ura = UNSET
        else:
            qtr_ssf_ura = self.qtr_ssf_ura

        objectid = self.objectid

        shape_length: float | None | Unset
        if isinstance(self.shape_length, Unset):
            shape_length = UNSET
        else:
            shape_length = self.shape_length

        shape_area: float | None | Unset
        if isinstance(self.shape_area, Unset):
            shape_area = UNSET
        else:
            shape_area = self.shape_area

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if area_chi is not UNSET:
            field_dict["AREA_CHI"] = area_chi
        if area_eng is not UNSET:
            field_dict["AREA_ENG"] = area_eng
        if period is not UNSET:
            field_dict["PERIOD"] = period
        if qtr_all is not UNSET:
            field_dict["QTR_ALL"] = qtr_all
        if qtr_ph is not UNSET:
            field_dict["QTR_PH"] = qtr_ph
        if qtr_ph_ndq is not UNSET:
            field_dict["QTR_PH_NDQ"] = qtr_ph_ndq
        if qtr_ph_prf is not UNSET:
            field_dict["QTR_PH_PRF"] = qtr_ph_prf
        if qtr_ph_sq is not UNSET:
            field_dict["QTR_PH_SQ"] = qtr_ph_sq
        if qtr_ph_sstv is not UNSET:
            field_dict["QTR_PH_SSTV"] = qtr_ph_sstv
        if qtr_ph_vbm is not UNSET:
            field_dict["QTR_PH_VBM"] = qtr_ph_vbm
        if qtr_prh is not UNSET:
            field_dict["QTR_PRH"] = qtr_prh
        if qtr_prh_ha is not UNSET:
            field_dict["QTR_PRH_HA"] = qtr_prh_ha
        if qtr_prh_hs is not UNSET:
            field_dict["QTR_PRH_HS"] = qtr_prh_hs
        if qtr_ssf is not UNSET:
            field_dict["QTR_SSF"] = qtr_ssf
        if qtr_ssf_ha is not UNSET:
            field_dict["QTR_SSF_HA"] = qtr_ssf_ha
        if qtr_ssf_hs is not UNSET:
            field_dict["QTR_SSF_HS"] = qtr_ssf_hs
        if qtr_ssf_ura is not UNSET:
            field_dict["QTR_SSF_URA"] = qtr_ssf_ura
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape_length is not UNSET:
            field_dict["Shape__Length"] = shape_length
        if shape_area is not UNSET:
            field_dict["Shape__Area"] = shape_area

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_area_chi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        area_chi = _parse_area_chi(d.pop("AREA_CHI", UNSET))

        def _parse_area_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        area_eng = _parse_area_eng(d.pop("AREA_ENG", UNSET))

        def _parse_period(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        period = _parse_period(d.pop("PERIOD", UNSET))

        def _parse_qtr_all(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        qtr_all = _parse_qtr_all(d.pop("QTR_ALL", UNSET))

        def _parse_qtr_ph(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        qtr_ph = _parse_qtr_ph(d.pop("QTR_PH", UNSET))

        def _parse_qtr_ph_ndq(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        qtr_ph_ndq = _parse_qtr_ph_ndq(d.pop("QTR_PH_NDQ", UNSET))

        def _parse_qtr_ph_prf(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        qtr_ph_prf = _parse_qtr_ph_prf(d.pop("QTR_PH_PRF", UNSET))

        def _parse_qtr_ph_sq(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        qtr_ph_sq = _parse_qtr_ph_sq(d.pop("QTR_PH_SQ", UNSET))

        def _parse_qtr_ph_sstv(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        qtr_ph_sstv = _parse_qtr_ph_sstv(d.pop("QTR_PH_SSTV", UNSET))

        def _parse_qtr_ph_vbm(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        qtr_ph_vbm = _parse_qtr_ph_vbm(d.pop("QTR_PH_VBM", UNSET))

        def _parse_qtr_prh(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        qtr_prh = _parse_qtr_prh(d.pop("QTR_PRH", UNSET))

        def _parse_qtr_prh_ha(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        qtr_prh_ha = _parse_qtr_prh_ha(d.pop("QTR_PRH_HA", UNSET))

        def _parse_qtr_prh_hs(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        qtr_prh_hs = _parse_qtr_prh_hs(d.pop("QTR_PRH_HS", UNSET))

        def _parse_qtr_ssf(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        qtr_ssf = _parse_qtr_ssf(d.pop("QTR_SSF", UNSET))

        def _parse_qtr_ssf_ha(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        qtr_ssf_ha = _parse_qtr_ssf_ha(d.pop("QTR_SSF_HA", UNSET))

        def _parse_qtr_ssf_hs(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        qtr_ssf_hs = _parse_qtr_ssf_hs(d.pop("QTR_SSF_HS", UNSET))

        def _parse_qtr_ssf_ura(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        qtr_ssf_ura = _parse_qtr_ssf_ura(d.pop("QTR_SSF_URA", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        def _parse_shape_length(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_length = _parse_shape_length(d.pop("Shape__Length", UNSET))

        def _parse_shape_area(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_area = _parse_shape_area(d.pop("Shape__Area", UNSET))

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            area_chi=area_chi,
            area_eng=area_eng,
            period=period,
            qtr_all=qtr_all,
            qtr_ph=qtr_ph,
            qtr_ph_ndq=qtr_ph_ndq,
            qtr_ph_prf=qtr_ph_prf,
            qtr_ph_sq=qtr_ph_sq,
            qtr_ph_sstv=qtr_ph_sstv,
            qtr_ph_vbm=qtr_ph_vbm,
            qtr_prh=qtr_prh,
            qtr_prh_ha=qtr_prh_ha,
            qtr_prh_hs=qtr_prh_hs,
            qtr_ssf=qtr_ssf,
            qtr_ssf_ha=qtr_ssf_ha,
            qtr_ssf_hs=qtr_ssf_hs,
            qtr_ssf_ura=qtr_ssf_ura,
            objectid=objectid,
            shape_length=shape_length,
            shape_area=shape_area,
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
