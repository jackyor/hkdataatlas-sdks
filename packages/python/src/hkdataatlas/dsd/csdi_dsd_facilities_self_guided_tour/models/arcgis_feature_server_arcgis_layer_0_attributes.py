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
        district_en (None | str | Unset): Publisher field type: esriFieldTypeString
        district_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        district_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        intro_en (None | str | Unset): Publisher field type: esriFieldTypeString
        intro_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        intro_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        location_en (None | str | Unset): Publisher field type: esriFieldTypeString
        location_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        location_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        record_id (int | None | Unset): Publisher field type: esriFieldTypeSmallInteger
        tour_en (None | str | Unset): Publisher field type: esriFieldTypeString
        tour_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        tour_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
        shape_area (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    district_en: None | str | Unset = UNSET
    district_sc: None | str | Unset = UNSET
    district_tc: None | str | Unset = UNSET
    intro_en: None | str | Unset = UNSET
    intro_sc: None | str | Unset = UNSET
    intro_tc: None | str | Unset = UNSET
    location_en: None | str | Unset = UNSET
    location_sc: None | str | Unset = UNSET
    location_tc: None | str | Unset = UNSET
    record_id: int | None | Unset = UNSET
    tour_en: None | str | Unset = UNSET
    tour_sc: None | str | Unset = UNSET
    tour_tc: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        district_en: None | str | Unset
        if isinstance(self.district_en, Unset):
            district_en = UNSET
        else:
            district_en = self.district_en

        district_sc: None | str | Unset
        if isinstance(self.district_sc, Unset):
            district_sc = UNSET
        else:
            district_sc = self.district_sc

        district_tc: None | str | Unset
        if isinstance(self.district_tc, Unset):
            district_tc = UNSET
        else:
            district_tc = self.district_tc

        intro_en: None | str | Unset
        if isinstance(self.intro_en, Unset):
            intro_en = UNSET
        else:
            intro_en = self.intro_en

        intro_sc: None | str | Unset
        if isinstance(self.intro_sc, Unset):
            intro_sc = UNSET
        else:
            intro_sc = self.intro_sc

        intro_tc: None | str | Unset
        if isinstance(self.intro_tc, Unset):
            intro_tc = UNSET
        else:
            intro_tc = self.intro_tc

        location_en: None | str | Unset
        if isinstance(self.location_en, Unset):
            location_en = UNSET
        else:
            location_en = self.location_en

        location_sc: None | str | Unset
        if isinstance(self.location_sc, Unset):
            location_sc = UNSET
        else:
            location_sc = self.location_sc

        location_tc: None | str | Unset
        if isinstance(self.location_tc, Unset):
            location_tc = UNSET
        else:
            location_tc = self.location_tc

        record_id: int | None | Unset
        if isinstance(self.record_id, Unset):
            record_id = UNSET
        else:
            record_id = self.record_id

        tour_en: None | str | Unset
        if isinstance(self.tour_en, Unset):
            tour_en = UNSET
        else:
            tour_en = self.tour_en

        tour_sc: None | str | Unset
        if isinstance(self.tour_sc, Unset):
            tour_sc = UNSET
        else:
            tour_sc = self.tour_sc

        tour_tc: None | str | Unset
        if isinstance(self.tour_tc, Unset):
            tour_tc = UNSET
        else:
            tour_tc = self.tour_tc

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
        if district_en is not UNSET:
            field_dict["DISTRICT_EN"] = district_en
        if district_sc is not UNSET:
            field_dict["DISTRICT_SC"] = district_sc
        if district_tc is not UNSET:
            field_dict["DISTRICT_TC"] = district_tc
        if intro_en is not UNSET:
            field_dict["INTRO_EN"] = intro_en
        if intro_sc is not UNSET:
            field_dict["INTRO_SC"] = intro_sc
        if intro_tc is not UNSET:
            field_dict["INTRO_TC"] = intro_tc
        if location_en is not UNSET:
            field_dict["LOCATION_EN"] = location_en
        if location_sc is not UNSET:
            field_dict["LOCATION_SC"] = location_sc
        if location_tc is not UNSET:
            field_dict["LOCATION_TC"] = location_tc
        if record_id is not UNSET:
            field_dict["RECORD_ID"] = record_id
        if tour_en is not UNSET:
            field_dict["TOUR_EN"] = tour_en
        if tour_sc is not UNSET:
            field_dict["TOUR_SC"] = tour_sc
        if tour_tc is not UNSET:
            field_dict["TOUR_TC"] = tour_tc
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

        def _parse_district_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_en = _parse_district_en(d.pop("DISTRICT_EN", UNSET))

        def _parse_district_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_sc = _parse_district_sc(d.pop("DISTRICT_SC", UNSET))

        def _parse_district_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_tc = _parse_district_tc(d.pop("DISTRICT_TC", UNSET))

        def _parse_intro_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        intro_en = _parse_intro_en(d.pop("INTRO_EN", UNSET))

        def _parse_intro_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        intro_sc = _parse_intro_sc(d.pop("INTRO_SC", UNSET))

        def _parse_intro_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        intro_tc = _parse_intro_tc(d.pop("INTRO_TC", UNSET))

        def _parse_location_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_en = _parse_location_en(d.pop("LOCATION_EN", UNSET))

        def _parse_location_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_sc = _parse_location_sc(d.pop("LOCATION_SC", UNSET))

        def _parse_location_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_tc = _parse_location_tc(d.pop("LOCATION_TC", UNSET))

        def _parse_record_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        record_id = _parse_record_id(d.pop("RECORD_ID", UNSET))

        def _parse_tour_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tour_en = _parse_tour_en(d.pop("TOUR_EN", UNSET))

        def _parse_tour_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tour_sc = _parse_tour_sc(d.pop("TOUR_SC", UNSET))

        def _parse_tour_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tour_tc = _parse_tour_tc(d.pop("TOUR_TC", UNSET))

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
            district_en=district_en,
            district_sc=district_sc,
            district_tc=district_tc,
            intro_en=intro_en,
            intro_sc=intro_sc,
            intro_tc=intro_tc,
            location_en=location_en,
            location_sc=location_sc,
            location_tc=location_tc,
            record_id=record_id,
            tour_en=tour_en,
            tour_sc=tour_sc,
            tour_tc=tour_tc,
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
