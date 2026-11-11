from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer1Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer1Attributes:
    """
    Attributes:
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        slide_type (None | str | Unset): Publisher field type: esriFieldTypeString
        m_width (float | None | Unset): Publisher field type: esriFieldTypeDouble
        s_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
        slope (float | None | Unset): Publisher field type: esriFieldTypeDouble
        cover (None | str | Unset): Publisher field type: esriFieldTypeString
        year_1 (None | str | Unset): Publisher field type: esriFieldTypeString
        headelev (float | None | Unset): Publisher field type: esriFieldTypeDouble
        tailelev (float | None | Unset): Publisher field type: esriFieldTypeDouble
        ele_diff (float | None | Unset): Publisher field type: esriFieldTypeDouble
        gully (None | str | Unset): Publisher field type: esriFieldTypeString
        easting (float | None | Unset): Publisher field type: esriFieldTypeDouble
        northing (float | None | Unset): Publisher field type: esriFieldTypeDouble
        class_ (None | str | Unset): Publisher field type: esriFieldTypeString
        entli_no (None | str | Unset): Publisher field type: esriFieldTypeString
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    objectid: int | Unset = UNSET
    slide_type: None | str | Unset = UNSET
    m_width: float | None | Unset = UNSET
    s_length: float | None | Unset = UNSET
    slope: float | None | Unset = UNSET
    cover: None | str | Unset = UNSET
    year_1: None | str | Unset = UNSET
    headelev: float | None | Unset = UNSET
    tailelev: float | None | Unset = UNSET
    ele_diff: float | None | Unset = UNSET
    gully: None | str | Unset = UNSET
    easting: float | None | Unset = UNSET
    northing: float | None | Unset = UNSET
    class_: None | str | Unset = UNSET
    entli_no: None | str | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        slide_type: None | str | Unset
        if isinstance(self.slide_type, Unset):
            slide_type = UNSET
        else:
            slide_type = self.slide_type

        m_width: float | None | Unset
        if isinstance(self.m_width, Unset):
            m_width = UNSET
        else:
            m_width = self.m_width

        s_length: float | None | Unset
        if isinstance(self.s_length, Unset):
            s_length = UNSET
        else:
            s_length = self.s_length

        slope: float | None | Unset
        if isinstance(self.slope, Unset):
            slope = UNSET
        else:
            slope = self.slope

        cover: None | str | Unset
        if isinstance(self.cover, Unset):
            cover = UNSET
        else:
            cover = self.cover

        year_1: None | str | Unset
        if isinstance(self.year_1, Unset):
            year_1 = UNSET
        else:
            year_1 = self.year_1

        headelev: float | None | Unset
        if isinstance(self.headelev, Unset):
            headelev = UNSET
        else:
            headelev = self.headelev

        tailelev: float | None | Unset
        if isinstance(self.tailelev, Unset):
            tailelev = UNSET
        else:
            tailelev = self.tailelev

        ele_diff: float | None | Unset
        if isinstance(self.ele_diff, Unset):
            ele_diff = UNSET
        else:
            ele_diff = self.ele_diff

        gully: None | str | Unset
        if isinstance(self.gully, Unset):
            gully = UNSET
        else:
            gully = self.gully

        easting: float | None | Unset
        if isinstance(self.easting, Unset):
            easting = UNSET
        else:
            easting = self.easting

        northing: float | None | Unset
        if isinstance(self.northing, Unset):
            northing = UNSET
        else:
            northing = self.northing

        class_: None | str | Unset
        if isinstance(self.class_, Unset):
            class_ = UNSET
        else:
            class_ = self.class_

        entli_no: None | str | Unset
        if isinstance(self.entli_no, Unset):
            entli_no = UNSET
        else:
            entli_no = self.entli_no

        shape_length: float | None | Unset
        if isinstance(self.shape_length, Unset):
            shape_length = UNSET
        else:
            shape_length = self.shape_length

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if slide_type is not UNSET:
            field_dict["SLIDE_TYPE"] = slide_type
        if m_width is not UNSET:
            field_dict["M_WIDTH"] = m_width
        if s_length is not UNSET:
            field_dict["S_LENGTH"] = s_length
        if slope is not UNSET:
            field_dict["SLOPE"] = slope
        if cover is not UNSET:
            field_dict["COVER"] = cover
        if year_1 is not UNSET:
            field_dict["YEAR_1"] = year_1
        if headelev is not UNSET:
            field_dict["HEADELEV"] = headelev
        if tailelev is not UNSET:
            field_dict["TAILELEV"] = tailelev
        if ele_diff is not UNSET:
            field_dict["ELE_DIFF"] = ele_diff
        if gully is not UNSET:
            field_dict["GULLY"] = gully
        if easting is not UNSET:
            field_dict["EASTING"] = easting
        if northing is not UNSET:
            field_dict["NORTHING"] = northing
        if class_ is not UNSET:
            field_dict["CLASS"] = class_
        if entli_no is not UNSET:
            field_dict["ENTLI_NO"] = entli_no
        if shape_length is not UNSET:
            field_dict["Shape__Length"] = shape_length

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_slide_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        slide_type = _parse_slide_type(d.pop("SLIDE_TYPE", UNSET))

        def _parse_m_width(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        m_width = _parse_m_width(d.pop("M_WIDTH", UNSET))

        def _parse_s_length(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        s_length = _parse_s_length(d.pop("S_LENGTH", UNSET))

        def _parse_slope(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        slope = _parse_slope(d.pop("SLOPE", UNSET))

        def _parse_cover(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cover = _parse_cover(d.pop("COVER", UNSET))

        def _parse_year_1(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        year_1 = _parse_year_1(d.pop("YEAR_1", UNSET))

        def _parse_headelev(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        headelev = _parse_headelev(d.pop("HEADELEV", UNSET))

        def _parse_tailelev(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        tailelev = _parse_tailelev(d.pop("TAILELEV", UNSET))

        def _parse_ele_diff(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        ele_diff = _parse_ele_diff(d.pop("ELE_DIFF", UNSET))

        def _parse_gully(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gully = _parse_gully(d.pop("GULLY", UNSET))

        def _parse_easting(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        easting = _parse_easting(d.pop("EASTING", UNSET))

        def _parse_northing(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        northing = _parse_northing(d.pop("NORTHING", UNSET))

        def _parse_class_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        class_ = _parse_class_(d.pop("CLASS", UNSET))

        def _parse_entli_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        entli_no = _parse_entli_no(d.pop("ENTLI_NO", UNSET))

        def _parse_shape_length(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_length = _parse_shape_length(d.pop("Shape__Length", UNSET))

        arcgis_feature_server_arcgis_layer_1_attributes = cls(
            objectid=objectid,
            slide_type=slide_type,
            m_width=m_width,
            s_length=s_length,
            slope=slope,
            cover=cover,
            year_1=year_1,
            headelev=headelev,
            tailelev=tailelev,
            ele_diff=ele_diff,
            gully=gully,
            easting=easting,
            northing=northing,
            class_=class_,
            entli_no=entli_no,
            shape_length=shape_length,
        )

        arcgis_feature_server_arcgis_layer_1_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_1_attributes

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
