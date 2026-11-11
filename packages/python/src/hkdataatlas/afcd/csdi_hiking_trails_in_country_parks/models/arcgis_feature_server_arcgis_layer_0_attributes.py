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
        trail_id (None | str | Unset): Publisher field type: esriFieldTypeString
        trail_name_en (None | str | Unset): Publisher field type: esriFieldTypeString
        trail_name_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        section_no (None | str | Unset): Publisher field type: esriFieldTypeString
        measure_len (None | str | Unset): Publisher field type: esriFieldTypeString
        star_tpt_en (None | str | Unset): Publisher field type: esriFieldTypeString
        star_tpt_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        finis_hpt_en (None | str | Unset): Publisher field type: esriFieldTypeString
        finis_hpt_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        type_en (None | str | Unset): Publisher field type: esriFieldTypeString
        type_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        difficulty_en (None | str | Unset): Publisher field type: esriFieldTypeString
        difficulty_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        region_en (None | str | Unset): Publisher field type: esriFieldTypeString
        region_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        tel (None | str | Unset): Publisher field type: esriFieldTypeString
        website (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    trail_id: None | str | Unset = UNSET
    trail_name_en: None | str | Unset = UNSET
    trail_name_tc: None | str | Unset = UNSET
    section_no: None | str | Unset = UNSET
    measure_len: None | str | Unset = UNSET
    star_tpt_en: None | str | Unset = UNSET
    star_tpt_tc: None | str | Unset = UNSET
    finis_hpt_en: None | str | Unset = UNSET
    finis_hpt_tc: None | str | Unset = UNSET
    type_en: None | str | Unset = UNSET
    type_tc: None | str | Unset = UNSET
    difficulty_en: None | str | Unset = UNSET
    difficulty_tc: None | str | Unset = UNSET
    region_en: None | str | Unset = UNSET
    region_tc: None | str | Unset = UNSET
    tel: None | str | Unset = UNSET
    website: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        trail_id: None | str | Unset
        if isinstance(self.trail_id, Unset):
            trail_id = UNSET
        else:
            trail_id = self.trail_id

        trail_name_en: None | str | Unset
        if isinstance(self.trail_name_en, Unset):
            trail_name_en = UNSET
        else:
            trail_name_en = self.trail_name_en

        trail_name_tc: None | str | Unset
        if isinstance(self.trail_name_tc, Unset):
            trail_name_tc = UNSET
        else:
            trail_name_tc = self.trail_name_tc

        section_no: None | str | Unset
        if isinstance(self.section_no, Unset):
            section_no = UNSET
        else:
            section_no = self.section_no

        measure_len: None | str | Unset
        if isinstance(self.measure_len, Unset):
            measure_len = UNSET
        else:
            measure_len = self.measure_len

        star_tpt_en: None | str | Unset
        if isinstance(self.star_tpt_en, Unset):
            star_tpt_en = UNSET
        else:
            star_tpt_en = self.star_tpt_en

        star_tpt_tc: None | str | Unset
        if isinstance(self.star_tpt_tc, Unset):
            star_tpt_tc = UNSET
        else:
            star_tpt_tc = self.star_tpt_tc

        finis_hpt_en: None | str | Unset
        if isinstance(self.finis_hpt_en, Unset):
            finis_hpt_en = UNSET
        else:
            finis_hpt_en = self.finis_hpt_en

        finis_hpt_tc: None | str | Unset
        if isinstance(self.finis_hpt_tc, Unset):
            finis_hpt_tc = UNSET
        else:
            finis_hpt_tc = self.finis_hpt_tc

        type_en: None | str | Unset
        if isinstance(self.type_en, Unset):
            type_en = UNSET
        else:
            type_en = self.type_en

        type_tc: None | str | Unset
        if isinstance(self.type_tc, Unset):
            type_tc = UNSET
        else:
            type_tc = self.type_tc

        difficulty_en: None | str | Unset
        if isinstance(self.difficulty_en, Unset):
            difficulty_en = UNSET
        else:
            difficulty_en = self.difficulty_en

        difficulty_tc: None | str | Unset
        if isinstance(self.difficulty_tc, Unset):
            difficulty_tc = UNSET
        else:
            difficulty_tc = self.difficulty_tc

        region_en: None | str | Unset
        if isinstance(self.region_en, Unset):
            region_en = UNSET
        else:
            region_en = self.region_en

        region_tc: None | str | Unset
        if isinstance(self.region_tc, Unset):
            region_tc = UNSET
        else:
            region_tc = self.region_tc

        tel: None | str | Unset
        if isinstance(self.tel, Unset):
            tel = UNSET
        else:
            tel = self.tel

        website: None | str | Unset
        if isinstance(self.website, Unset):
            website = UNSET
        else:
            website = self.website

        objectid = self.objectid

        shape_length: float | None | Unset
        if isinstance(self.shape_length, Unset):
            shape_length = UNSET
        else:
            shape_length = self.shape_length

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if trail_id is not UNSET:
            field_dict["TRAIL_ID"] = trail_id
        if trail_name_en is not UNSET:
            field_dict["TRAIL_NAME_EN"] = trail_name_en
        if trail_name_tc is not UNSET:
            field_dict["TRAIL_NAME_TC"] = trail_name_tc
        if section_no is not UNSET:
            field_dict["SECTION_NO"] = section_no
        if measure_len is not UNSET:
            field_dict["MEASURE_LEN"] = measure_len
        if star_tpt_en is not UNSET:
            field_dict["STARTpt_EN"] = star_tpt_en
        if star_tpt_tc is not UNSET:
            field_dict["STARTpt_TC"] = star_tpt_tc
        if finis_hpt_en is not UNSET:
            field_dict["FINISHpt_EN"] = finis_hpt_en
        if finis_hpt_tc is not UNSET:
            field_dict["FINISHpt_TC"] = finis_hpt_tc
        if type_en is not UNSET:
            field_dict["TYPE_EN"] = type_en
        if type_tc is not UNSET:
            field_dict["TYPE_TC"] = type_tc
        if difficulty_en is not UNSET:
            field_dict["DIFFICULTY_EN"] = difficulty_en
        if difficulty_tc is not UNSET:
            field_dict["DIFFICULTY_TC"] = difficulty_tc
        if region_en is not UNSET:
            field_dict["REGION_EN"] = region_en
        if region_tc is not UNSET:
            field_dict["REGION_TC"] = region_tc
        if tel is not UNSET:
            field_dict["TEL"] = tel
        if website is not UNSET:
            field_dict["WEBSITE"] = website
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape_length is not UNSET:
            field_dict["Shape__Length"] = shape_length

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_trail_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        trail_id = _parse_trail_id(d.pop("TRAIL_ID", UNSET))

        def _parse_trail_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        trail_name_en = _parse_trail_name_en(d.pop("TRAIL_NAME_EN", UNSET))

        def _parse_trail_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        trail_name_tc = _parse_trail_name_tc(d.pop("TRAIL_NAME_TC", UNSET))

        def _parse_section_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        section_no = _parse_section_no(d.pop("SECTION_NO", UNSET))

        def _parse_measure_len(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        measure_len = _parse_measure_len(d.pop("MEASURE_LEN", UNSET))

        def _parse_star_tpt_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        star_tpt_en = _parse_star_tpt_en(d.pop("STARTpt_EN", UNSET))

        def _parse_star_tpt_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        star_tpt_tc = _parse_star_tpt_tc(d.pop("STARTpt_TC", UNSET))

        def _parse_finis_hpt_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        finis_hpt_en = _parse_finis_hpt_en(d.pop("FINISHpt_EN", UNSET))

        def _parse_finis_hpt_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        finis_hpt_tc = _parse_finis_hpt_tc(d.pop("FINISHpt_TC", UNSET))

        def _parse_type_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_en = _parse_type_en(d.pop("TYPE_EN", UNSET))

        def _parse_type_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_tc = _parse_type_tc(d.pop("TYPE_TC", UNSET))

        def _parse_difficulty_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        difficulty_en = _parse_difficulty_en(d.pop("DIFFICULTY_EN", UNSET))

        def _parse_difficulty_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        difficulty_tc = _parse_difficulty_tc(d.pop("DIFFICULTY_TC", UNSET))

        def _parse_region_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_en = _parse_region_en(d.pop("REGION_EN", UNSET))

        def _parse_region_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_tc = _parse_region_tc(d.pop("REGION_TC", UNSET))

        def _parse_tel(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tel = _parse_tel(d.pop("TEL", UNSET))

        def _parse_website(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website = _parse_website(d.pop("WEBSITE", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        def _parse_shape_length(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_length = _parse_shape_length(d.pop("Shape__Length", UNSET))

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            trail_id=trail_id,
            trail_name_en=trail_name_en,
            trail_name_tc=trail_name_tc,
            section_no=section_no,
            measure_len=measure_len,
            star_tpt_en=star_tpt_en,
            star_tpt_tc=star_tpt_tc,
            finis_hpt_en=finis_hpt_en,
            finis_hpt_tc=finis_hpt_tc,
            type_en=type_en,
            type_tc=type_tc,
            difficulty_en=difficulty_en,
            difficulty_tc=difficulty_tc,
            region_en=region_en,
            region_tc=region_tc,
            tel=tel,
            website=website,
            objectid=objectid,
            shape_length=shape_length,
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
