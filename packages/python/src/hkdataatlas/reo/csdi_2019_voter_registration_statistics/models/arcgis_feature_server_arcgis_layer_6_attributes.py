from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer6Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer6Attributes:
    """
    Attributes:
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        cacode (None | str | Unset): Publisher field type: esriFieldTypeString
        ename (None | str | Unset): Publisher field type: esriFieldTypeString
        cname (None | str | Unset): Publisher field type: esriFieldTypeString
        district_t (None | str | Unset): Publisher field type: esriFieldTypeString
        district_e (None | str | Unset): Publisher field type: esriFieldTypeString
        f_18_20 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        f_21_25 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        f_26_30 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        f_31_35 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        f_36_40 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        f_41_45 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        f_46_50 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        f_51_55 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        f_56_60 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        f_61_65 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        f_66_70 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        f_71plus (float | None | Unset): Publisher field type: esriFieldTypeDouble
        m_18_20 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        m_21_25 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        m_26_30 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        m_31_35 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        m_36_40 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        m_41_45 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        m_46_50 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        m_51_55 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        m_56_60 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        m_61_65 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        m_66_70 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        m_71plus (float | None | Unset): Publisher field type: esriFieldTypeDouble
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
        shape_area (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    objectid: int | Unset = UNSET
    cacode: None | str | Unset = UNSET
    ename: None | str | Unset = UNSET
    cname: None | str | Unset = UNSET
    district_t: None | str | Unset = UNSET
    district_e: None | str | Unset = UNSET
    f_18_20: float | None | Unset = UNSET
    f_21_25: float | None | Unset = UNSET
    f_26_30: float | None | Unset = UNSET
    f_31_35: float | None | Unset = UNSET
    f_36_40: float | None | Unset = UNSET
    f_41_45: float | None | Unset = UNSET
    f_46_50: float | None | Unset = UNSET
    f_51_55: float | None | Unset = UNSET
    f_56_60: float | None | Unset = UNSET
    f_61_65: float | None | Unset = UNSET
    f_66_70: float | None | Unset = UNSET
    f_71plus: float | None | Unset = UNSET
    m_18_20: float | None | Unset = UNSET
    m_21_25: float | None | Unset = UNSET
    m_26_30: float | None | Unset = UNSET
    m_31_35: float | None | Unset = UNSET
    m_36_40: float | None | Unset = UNSET
    m_41_45: float | None | Unset = UNSET
    m_46_50: float | None | Unset = UNSET
    m_51_55: float | None | Unset = UNSET
    m_56_60: float | None | Unset = UNSET
    m_61_65: float | None | Unset = UNSET
    m_66_70: float | None | Unset = UNSET
    m_71plus: float | None | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        cacode: None | str | Unset
        if isinstance(self.cacode, Unset):
            cacode = UNSET
        else:
            cacode = self.cacode

        ename: None | str | Unset
        if isinstance(self.ename, Unset):
            ename = UNSET
        else:
            ename = self.ename

        cname: None | str | Unset
        if isinstance(self.cname, Unset):
            cname = UNSET
        else:
            cname = self.cname

        district_t: None | str | Unset
        if isinstance(self.district_t, Unset):
            district_t = UNSET
        else:
            district_t = self.district_t

        district_e: None | str | Unset
        if isinstance(self.district_e, Unset):
            district_e = UNSET
        else:
            district_e = self.district_e

        f_18_20: float | None | Unset
        if isinstance(self.f_18_20, Unset):
            f_18_20 = UNSET
        else:
            f_18_20 = self.f_18_20

        f_21_25: float | None | Unset
        if isinstance(self.f_21_25, Unset):
            f_21_25 = UNSET
        else:
            f_21_25 = self.f_21_25

        f_26_30: float | None | Unset
        if isinstance(self.f_26_30, Unset):
            f_26_30 = UNSET
        else:
            f_26_30 = self.f_26_30

        f_31_35: float | None | Unset
        if isinstance(self.f_31_35, Unset):
            f_31_35 = UNSET
        else:
            f_31_35 = self.f_31_35

        f_36_40: float | None | Unset
        if isinstance(self.f_36_40, Unset):
            f_36_40 = UNSET
        else:
            f_36_40 = self.f_36_40

        f_41_45: float | None | Unset
        if isinstance(self.f_41_45, Unset):
            f_41_45 = UNSET
        else:
            f_41_45 = self.f_41_45

        f_46_50: float | None | Unset
        if isinstance(self.f_46_50, Unset):
            f_46_50 = UNSET
        else:
            f_46_50 = self.f_46_50

        f_51_55: float | None | Unset
        if isinstance(self.f_51_55, Unset):
            f_51_55 = UNSET
        else:
            f_51_55 = self.f_51_55

        f_56_60: float | None | Unset
        if isinstance(self.f_56_60, Unset):
            f_56_60 = UNSET
        else:
            f_56_60 = self.f_56_60

        f_61_65: float | None | Unset
        if isinstance(self.f_61_65, Unset):
            f_61_65 = UNSET
        else:
            f_61_65 = self.f_61_65

        f_66_70: float | None | Unset
        if isinstance(self.f_66_70, Unset):
            f_66_70 = UNSET
        else:
            f_66_70 = self.f_66_70

        f_71plus: float | None | Unset
        if isinstance(self.f_71plus, Unset):
            f_71plus = UNSET
        else:
            f_71plus = self.f_71plus

        m_18_20: float | None | Unset
        if isinstance(self.m_18_20, Unset):
            m_18_20 = UNSET
        else:
            m_18_20 = self.m_18_20

        m_21_25: float | None | Unset
        if isinstance(self.m_21_25, Unset):
            m_21_25 = UNSET
        else:
            m_21_25 = self.m_21_25

        m_26_30: float | None | Unset
        if isinstance(self.m_26_30, Unset):
            m_26_30 = UNSET
        else:
            m_26_30 = self.m_26_30

        m_31_35: float | None | Unset
        if isinstance(self.m_31_35, Unset):
            m_31_35 = UNSET
        else:
            m_31_35 = self.m_31_35

        m_36_40: float | None | Unset
        if isinstance(self.m_36_40, Unset):
            m_36_40 = UNSET
        else:
            m_36_40 = self.m_36_40

        m_41_45: float | None | Unset
        if isinstance(self.m_41_45, Unset):
            m_41_45 = UNSET
        else:
            m_41_45 = self.m_41_45

        m_46_50: float | None | Unset
        if isinstance(self.m_46_50, Unset):
            m_46_50 = UNSET
        else:
            m_46_50 = self.m_46_50

        m_51_55: float | None | Unset
        if isinstance(self.m_51_55, Unset):
            m_51_55 = UNSET
        else:
            m_51_55 = self.m_51_55

        m_56_60: float | None | Unset
        if isinstance(self.m_56_60, Unset):
            m_56_60 = UNSET
        else:
            m_56_60 = self.m_56_60

        m_61_65: float | None | Unset
        if isinstance(self.m_61_65, Unset):
            m_61_65 = UNSET
        else:
            m_61_65 = self.m_61_65

        m_66_70: float | None | Unset
        if isinstance(self.m_66_70, Unset):
            m_66_70 = UNSET
        else:
            m_66_70 = self.m_66_70

        m_71plus: float | None | Unset
        if isinstance(self.m_71plus, Unset):
            m_71plus = UNSET
        else:
            m_71plus = self.m_71plus

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
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if cacode is not UNSET:
            field_dict["CACODE"] = cacode
        if ename is not UNSET:
            field_dict["ENAME"] = ename
        if cname is not UNSET:
            field_dict["CNAME"] = cname
        if district_t is not UNSET:
            field_dict["DISTRICT_T"] = district_t
        if district_e is not UNSET:
            field_dict["DISTRICT_E"] = district_e
        if f_18_20 is not UNSET:
            field_dict["F_18_20"] = f_18_20
        if f_21_25 is not UNSET:
            field_dict["F_21_25"] = f_21_25
        if f_26_30 is not UNSET:
            field_dict["F_26_30"] = f_26_30
        if f_31_35 is not UNSET:
            field_dict["F_31_35"] = f_31_35
        if f_36_40 is not UNSET:
            field_dict["F_36_40"] = f_36_40
        if f_41_45 is not UNSET:
            field_dict["F_41_45"] = f_41_45
        if f_46_50 is not UNSET:
            field_dict["F_46_50"] = f_46_50
        if f_51_55 is not UNSET:
            field_dict["F_51_55"] = f_51_55
        if f_56_60 is not UNSET:
            field_dict["F_56_60"] = f_56_60
        if f_61_65 is not UNSET:
            field_dict["F_61_65"] = f_61_65
        if f_66_70 is not UNSET:
            field_dict["F_66_70"] = f_66_70
        if f_71plus is not UNSET:
            field_dict["F_71PLUS"] = f_71plus
        if m_18_20 is not UNSET:
            field_dict["M_18_20"] = m_18_20
        if m_21_25 is not UNSET:
            field_dict["M_21_25"] = m_21_25
        if m_26_30 is not UNSET:
            field_dict["M_26_30"] = m_26_30
        if m_31_35 is not UNSET:
            field_dict["M_31_35"] = m_31_35
        if m_36_40 is not UNSET:
            field_dict["M_36_40"] = m_36_40
        if m_41_45 is not UNSET:
            field_dict["M_41_45"] = m_41_45
        if m_46_50 is not UNSET:
            field_dict["M_46_50"] = m_46_50
        if m_51_55 is not UNSET:
            field_dict["M_51_55"] = m_51_55
        if m_56_60 is not UNSET:
            field_dict["M_56_60"] = m_56_60
        if m_61_65 is not UNSET:
            field_dict["M_61_65"] = m_61_65
        if m_66_70 is not UNSET:
            field_dict["M_66_70"] = m_66_70
        if m_71plus is not UNSET:
            field_dict["M_71PLUS"] = m_71plus
        if shape_length is not UNSET:
            field_dict["Shape__Length"] = shape_length
        if shape_area is not UNSET:
            field_dict["Shape__Area"] = shape_area

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_cacode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cacode = _parse_cacode(d.pop("CACODE", UNSET))

        def _parse_ename(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ename = _parse_ename(d.pop("ENAME", UNSET))

        def _parse_cname(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cname = _parse_cname(d.pop("CNAME", UNSET))

        def _parse_district_t(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_t = _parse_district_t(d.pop("DISTRICT_T", UNSET))

        def _parse_district_e(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_e = _parse_district_e(d.pop("DISTRICT_E", UNSET))

        def _parse_f_18_20(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        f_18_20 = _parse_f_18_20(d.pop("F_18_20", UNSET))

        def _parse_f_21_25(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        f_21_25 = _parse_f_21_25(d.pop("F_21_25", UNSET))

        def _parse_f_26_30(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        f_26_30 = _parse_f_26_30(d.pop("F_26_30", UNSET))

        def _parse_f_31_35(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        f_31_35 = _parse_f_31_35(d.pop("F_31_35", UNSET))

        def _parse_f_36_40(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        f_36_40 = _parse_f_36_40(d.pop("F_36_40", UNSET))

        def _parse_f_41_45(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        f_41_45 = _parse_f_41_45(d.pop("F_41_45", UNSET))

        def _parse_f_46_50(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        f_46_50 = _parse_f_46_50(d.pop("F_46_50", UNSET))

        def _parse_f_51_55(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        f_51_55 = _parse_f_51_55(d.pop("F_51_55", UNSET))

        def _parse_f_56_60(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        f_56_60 = _parse_f_56_60(d.pop("F_56_60", UNSET))

        def _parse_f_61_65(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        f_61_65 = _parse_f_61_65(d.pop("F_61_65", UNSET))

        def _parse_f_66_70(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        f_66_70 = _parse_f_66_70(d.pop("F_66_70", UNSET))

        def _parse_f_71plus(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        f_71plus = _parse_f_71plus(d.pop("F_71PLUS", UNSET))

        def _parse_m_18_20(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        m_18_20 = _parse_m_18_20(d.pop("M_18_20", UNSET))

        def _parse_m_21_25(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        m_21_25 = _parse_m_21_25(d.pop("M_21_25", UNSET))

        def _parse_m_26_30(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        m_26_30 = _parse_m_26_30(d.pop("M_26_30", UNSET))

        def _parse_m_31_35(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        m_31_35 = _parse_m_31_35(d.pop("M_31_35", UNSET))

        def _parse_m_36_40(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        m_36_40 = _parse_m_36_40(d.pop("M_36_40", UNSET))

        def _parse_m_41_45(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        m_41_45 = _parse_m_41_45(d.pop("M_41_45", UNSET))

        def _parse_m_46_50(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        m_46_50 = _parse_m_46_50(d.pop("M_46_50", UNSET))

        def _parse_m_51_55(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        m_51_55 = _parse_m_51_55(d.pop("M_51_55", UNSET))

        def _parse_m_56_60(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        m_56_60 = _parse_m_56_60(d.pop("M_56_60", UNSET))

        def _parse_m_61_65(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        m_61_65 = _parse_m_61_65(d.pop("M_61_65", UNSET))

        def _parse_m_66_70(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        m_66_70 = _parse_m_66_70(d.pop("M_66_70", UNSET))

        def _parse_m_71plus(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        m_71plus = _parse_m_71plus(d.pop("M_71PLUS", UNSET))

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

        arcgis_feature_server_arcgis_layer_6_attributes = cls(
            objectid=objectid,
            cacode=cacode,
            ename=ename,
            cname=cname,
            district_t=district_t,
            district_e=district_e,
            f_18_20=f_18_20,
            f_21_25=f_21_25,
            f_26_30=f_26_30,
            f_31_35=f_31_35,
            f_36_40=f_36_40,
            f_41_45=f_41_45,
            f_46_50=f_46_50,
            f_51_55=f_51_55,
            f_56_60=f_56_60,
            f_61_65=f_61_65,
            f_66_70=f_66_70,
            f_71plus=f_71plus,
            m_18_20=m_18_20,
            m_21_25=m_21_25,
            m_26_30=m_26_30,
            m_31_35=m_31_35,
            m_36_40=m_36_40,
            m_41_45=m_41_45,
            m_46_50=m_46_50,
            m_51_55=m_51_55,
            m_56_60=m_56_60,
            m_61_65=m_61_65,
            m_66_70=m_66_70,
            m_71plus=m_71plus,
            shape_length=shape_length,
            shape_area=shape_area,
        )

        arcgis_feature_server_arcgis_layer_6_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_6_attributes

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
