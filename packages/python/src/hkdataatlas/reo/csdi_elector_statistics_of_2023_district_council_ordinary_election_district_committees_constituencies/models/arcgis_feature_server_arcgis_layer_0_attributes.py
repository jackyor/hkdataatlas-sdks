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
        eng_name (None | str | Unset): Publisher field type: esriFieldTypeString
        chn_name (None | str | Unset): Publisher field type: esriFieldTypeString
        district_fight_crime_committee (float | None | Unset): Publisher field type: esriFieldTypeDouble
        district_fire_safety_committee (float | None | Unset): Publisher field type: esriFieldTypeDouble
        area_committee (float | None | Unset): Publisher field type: esriFieldTypeDouble
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
        shape_area (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    objectid: int | Unset = UNSET
    eng_name: None | str | Unset = UNSET
    chn_name: None | str | Unset = UNSET
    district_fight_crime_committee: float | None | Unset = UNSET
    district_fire_safety_committee: float | None | Unset = UNSET
    area_committee: float | None | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        eng_name: None | str | Unset
        if isinstance(self.eng_name, Unset):
            eng_name = UNSET
        else:
            eng_name = self.eng_name

        chn_name: None | str | Unset
        if isinstance(self.chn_name, Unset):
            chn_name = UNSET
        else:
            chn_name = self.chn_name

        district_fight_crime_committee: float | None | Unset
        if isinstance(self.district_fight_crime_committee, Unset):
            district_fight_crime_committee = UNSET
        else:
            district_fight_crime_committee = self.district_fight_crime_committee

        district_fire_safety_committee: float | None | Unset
        if isinstance(self.district_fire_safety_committee, Unset):
            district_fire_safety_committee = UNSET
        else:
            district_fire_safety_committee = self.district_fire_safety_committee

        area_committee: float | None | Unset
        if isinstance(self.area_committee, Unset):
            area_committee = UNSET
        else:
            area_committee = self.area_committee

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
        if eng_name is not UNSET:
            field_dict["ENG_NAME"] = eng_name
        if chn_name is not UNSET:
            field_dict["CHN_NAME"] = chn_name
        if district_fight_crime_committee is not UNSET:
            field_dict["DISTRICT_FIGHT_CRIME_COMMITTEE"] = (
                district_fight_crime_committee
            )
        if district_fire_safety_committee is not UNSET:
            field_dict["DISTRICT_FIRE_SAFETY_COMMITTEE"] = (
                district_fire_safety_committee
            )
        if area_committee is not UNSET:
            field_dict["AREA_COMMITTEE"] = area_committee
        if shape_length is not UNSET:
            field_dict["Shape__Length"] = shape_length
        if shape_area is not UNSET:
            field_dict["Shape__Area"] = shape_area

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_eng_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        eng_name = _parse_eng_name(d.pop("ENG_NAME", UNSET))

        def _parse_chn_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        chn_name = _parse_chn_name(d.pop("CHN_NAME", UNSET))

        def _parse_district_fight_crime_committee(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        district_fight_crime_committee = _parse_district_fight_crime_committee(
            d.pop("DISTRICT_FIGHT_CRIME_COMMITTEE", UNSET)
        )

        def _parse_district_fire_safety_committee(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        district_fire_safety_committee = _parse_district_fire_safety_committee(
            d.pop("DISTRICT_FIRE_SAFETY_COMMITTEE", UNSET)
        )

        def _parse_area_committee(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        area_committee = _parse_area_committee(d.pop("AREA_COMMITTEE", UNSET))

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
            objectid=objectid,
            eng_name=eng_name,
            chn_name=chn_name,
            district_fight_crime_committee=district_fight_crime_committee,
            district_fire_safety_committee=district_fire_safety_committee,
            area_committee=area_committee,
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
