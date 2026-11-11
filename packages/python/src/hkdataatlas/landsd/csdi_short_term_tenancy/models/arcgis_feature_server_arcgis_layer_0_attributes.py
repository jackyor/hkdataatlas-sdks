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
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
        shape_area (float | None | Unset): Publisher field type: esriFieldTypeDouble
        stt_no (str | Unset): Publisher field type: esriFieldTypeString
        dc_district (str | Unset): Publisher field type: esriFieldTypeString
        area (float | None | Unset): Publisher field type: esriFieldTypeDouble
        user_en (None | str | Unset): Publisher field type: esriFieldTypeString
        user_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        grant_type (None | str | Unset): Publisher field type: esriFieldTypeString
        commencement_date (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains
            unknown.
        term_en (None | str | Unset): Publisher field type: esriFieldTypeString
        term_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        lbs_info (None | str | Unset): Publisher field type: esriFieldTypeString
        rent_en (None | str | Unset): Publisher field type: esriFieldTypeString
        rent_tc (None | str | Unset): Publisher field type: esriFieldTypeString
    """

    objectid: int | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    stt_no: str | Unset = UNSET
    dc_district: str | Unset = UNSET
    area: float | None | Unset = UNSET
    user_en: None | str | Unset = UNSET
    user_tc: None | str | Unset = UNSET
    grant_type: None | str | Unset = UNSET
    commencement_date: Any | Unset = UNSET
    term_en: None | str | Unset = UNSET
    term_tc: None | str | Unset = UNSET
    lbs_info: None | str | Unset = UNSET
    rent_en: None | str | Unset = UNSET
    rent_tc: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        stt_no = self.stt_no

        dc_district = self.dc_district

        area: float | None | Unset
        if isinstance(self.area, Unset):
            area = UNSET
        else:
            area = self.area

        user_en: None | str | Unset
        if isinstance(self.user_en, Unset):
            user_en = UNSET
        else:
            user_en = self.user_en

        user_tc: None | str | Unset
        if isinstance(self.user_tc, Unset):
            user_tc = UNSET
        else:
            user_tc = self.user_tc

        grant_type: None | str | Unset
        if isinstance(self.grant_type, Unset):
            grant_type = UNSET
        else:
            grant_type = self.grant_type

        commencement_date = self.commencement_date

        term_en: None | str | Unset
        if isinstance(self.term_en, Unset):
            term_en = UNSET
        else:
            term_en = self.term_en

        term_tc: None | str | Unset
        if isinstance(self.term_tc, Unset):
            term_tc = UNSET
        else:
            term_tc = self.term_tc

        lbs_info: None | str | Unset
        if isinstance(self.lbs_info, Unset):
            lbs_info = UNSET
        else:
            lbs_info = self.lbs_info

        rent_en: None | str | Unset
        if isinstance(self.rent_en, Unset):
            rent_en = UNSET
        else:
            rent_en = self.rent_en

        rent_tc: None | str | Unset
        if isinstance(self.rent_tc, Unset):
            rent_tc = UNSET
        else:
            rent_tc = self.rent_tc

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape_length is not UNSET:
            field_dict["Shape__Length"] = shape_length
        if shape_area is not UNSET:
            field_dict["Shape__Area"] = shape_area
        if stt_no is not UNSET:
            field_dict["STTNo"] = stt_no
        if dc_district is not UNSET:
            field_dict["DCDistrict"] = dc_district
        if area is not UNSET:
            field_dict["Area"] = area
        if user_en is not UNSET:
            field_dict["UserEN"] = user_en
        if user_tc is not UNSET:
            field_dict["UserTC"] = user_tc
        if grant_type is not UNSET:
            field_dict["GrantType"] = grant_type
        if commencement_date is not UNSET:
            field_dict["CommencementDate"] = commencement_date
        if term_en is not UNSET:
            field_dict["TermEN"] = term_en
        if term_tc is not UNSET:
            field_dict["TermTC"] = term_tc
        if lbs_info is not UNSET:
            field_dict["LBSInfo"] = lbs_info
        if rent_en is not UNSET:
            field_dict["RentEN"] = rent_en
        if rent_tc is not UNSET:
            field_dict["RentTC"] = rent_tc

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
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

        stt_no = d.pop("STTNo", UNSET)

        dc_district = d.pop("DCDistrict", UNSET)

        def _parse_area(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        area = _parse_area(d.pop("Area", UNSET))

        def _parse_user_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_en = _parse_user_en(d.pop("UserEN", UNSET))

        def _parse_user_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_tc = _parse_user_tc(d.pop("UserTC", UNSET))

        def _parse_grant_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        grant_type = _parse_grant_type(d.pop("GrantType", UNSET))

        commencement_date = d.pop("CommencementDate", UNSET)

        def _parse_term_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        term_en = _parse_term_en(d.pop("TermEN", UNSET))

        def _parse_term_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        term_tc = _parse_term_tc(d.pop("TermTC", UNSET))

        def _parse_lbs_info(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lbs_info = _parse_lbs_info(d.pop("LBSInfo", UNSET))

        def _parse_rent_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rent_en = _parse_rent_en(d.pop("RentEN", UNSET))

        def _parse_rent_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rent_tc = _parse_rent_tc(d.pop("RentTC", UNSET))

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            objectid=objectid,
            shape_length=shape_length,
            shape_area=shape_area,
            stt_no=stt_no,
            dc_district=dc_district,
            area=area,
            user_en=user_en,
            user_tc=user_tc,
            grant_type=grant_type,
            commencement_date=commencement_date,
            term_en=term_en,
            term_tc=term_tc,
            lbs_info=lbs_info,
            rent_en=rent_en,
            rent_tc=rent_tc,
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
