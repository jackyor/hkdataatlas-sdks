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
        district (None | str | Unset): Publisher field type: esriFieldTypeString
        ctl_cat (None | str | Unset): Publisher field type: esriFieldTypeString
        location (None | str | Unset): Publisher field type: esriFieldTypeString
        appro_e (int | None | Unset): Publisher field type: esriFieldTypeInteger
        appro_n (int | None | Unset): Publisher field type: esriFieldTypeInteger
        slope_no (None | str | Unset): Publisher field type: esriFieldTypeString
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
        shape_area (float | None | Unset): Publisher field type: esriFieldTypeDouble
        maint_part (None | str | Unset): Publisher field type: esriFieldTypeString
        overall_ht (float | None | Unset): Publisher field type: esriFieldTypeSingle
        overall_an (int | None | Unset): Publisher field type: esriFieldTypeSmallInteger
        crest_faci (None | str | Unset): Publisher field type: esriFieldTypeString
        crest_dist (float | None | Unset): Publisher field type: esriFieldTypeSingle
        toe_faci (None | str | Unset): Publisher field type: esriFieldTypeString
        toe_dist (float | None | Unset): Publisher field type: esriFieldTypeSingle
        slope1_ht (float | None | Unset): Publisher field type: esriFieldTypeSingle
        slope1_l (float | None | Unset): Publisher field type: esriFieldTypeSingle
        slope1_ang (int | None | Unset): Publisher field type: esriFieldTypeSmallInteger
        slope2_ht (float | None | Unset): Publisher field type: esriFieldTypeSingle
        slope2_l (float | None | Unset): Publisher field type: esriFieldTypeSingle
        slope2_ang (int | None | Unset): Publisher field type: esriFieldTypeSmallInteger
        slope3_ht (float | None | Unset): Publisher field type: esriFieldTypeSingle
        slope3_l (float | None | Unset): Publisher field type: esriFieldTypeSingle
        slope3_ang (int | None | Unset): Publisher field type: esriFieldTypeSmallInteger
        wall1_ht (float | None | Unset): Publisher field type: esriFieldTypeSingle
        wall1_l (float | None | Unset): Publisher field type: esriFieldTypeSingle
        wall1_ang (int | None | Unset): Publisher field type: esriFieldTypeSmallInteger
        wall2_ht (float | None | Unset): Publisher field type: esriFieldTypeSingle
        wall2_l (float | None | Unset): Publisher field type: esriFieldTypeSingle
        wall2_ang (int | None | Unset): Publisher field type: esriFieldTypeSmallInteger
        wall3_ht (float | None | Unset): Publisher field type: esriFieldTypeSingle
        wall3_l (float | None | Unset): Publisher field type: esriFieldTypeSingle
        wall3_ang (int | None | Unset): Publisher field type: esriFieldTypeSmallInteger
    """

    objectid: int | Unset = UNSET
    district: None | str | Unset = UNSET
    ctl_cat: None | str | Unset = UNSET
    location: None | str | Unset = UNSET
    appro_e: int | None | Unset = UNSET
    appro_n: int | None | Unset = UNSET
    slope_no: None | str | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    maint_part: None | str | Unset = UNSET
    overall_ht: float | None | Unset = UNSET
    overall_an: int | None | Unset = UNSET
    crest_faci: None | str | Unset = UNSET
    crest_dist: float | None | Unset = UNSET
    toe_faci: None | str | Unset = UNSET
    toe_dist: float | None | Unset = UNSET
    slope1_ht: float | None | Unset = UNSET
    slope1_l: float | None | Unset = UNSET
    slope1_ang: int | None | Unset = UNSET
    slope2_ht: float | None | Unset = UNSET
    slope2_l: float | None | Unset = UNSET
    slope2_ang: int | None | Unset = UNSET
    slope3_ht: float | None | Unset = UNSET
    slope3_l: float | None | Unset = UNSET
    slope3_ang: int | None | Unset = UNSET
    wall1_ht: float | None | Unset = UNSET
    wall1_l: float | None | Unset = UNSET
    wall1_ang: int | None | Unset = UNSET
    wall2_ht: float | None | Unset = UNSET
    wall2_l: float | None | Unset = UNSET
    wall2_ang: int | None | Unset = UNSET
    wall3_ht: float | None | Unset = UNSET
    wall3_l: float | None | Unset = UNSET
    wall3_ang: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        district: None | str | Unset
        if isinstance(self.district, Unset):
            district = UNSET
        else:
            district = self.district

        ctl_cat: None | str | Unset
        if isinstance(self.ctl_cat, Unset):
            ctl_cat = UNSET
        else:
            ctl_cat = self.ctl_cat

        location: None | str | Unset
        if isinstance(self.location, Unset):
            location = UNSET
        else:
            location = self.location

        appro_e: int | None | Unset
        if isinstance(self.appro_e, Unset):
            appro_e = UNSET
        else:
            appro_e = self.appro_e

        appro_n: int | None | Unset
        if isinstance(self.appro_n, Unset):
            appro_n = UNSET
        else:
            appro_n = self.appro_n

        slope_no: None | str | Unset
        if isinstance(self.slope_no, Unset):
            slope_no = UNSET
        else:
            slope_no = self.slope_no

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

        maint_part: None | str | Unset
        if isinstance(self.maint_part, Unset):
            maint_part = UNSET
        else:
            maint_part = self.maint_part

        overall_ht: float | None | Unset
        if isinstance(self.overall_ht, Unset):
            overall_ht = UNSET
        else:
            overall_ht = self.overall_ht

        overall_an: int | None | Unset
        if isinstance(self.overall_an, Unset):
            overall_an = UNSET
        else:
            overall_an = self.overall_an

        crest_faci: None | str | Unset
        if isinstance(self.crest_faci, Unset):
            crest_faci = UNSET
        else:
            crest_faci = self.crest_faci

        crest_dist: float | None | Unset
        if isinstance(self.crest_dist, Unset):
            crest_dist = UNSET
        else:
            crest_dist = self.crest_dist

        toe_faci: None | str | Unset
        if isinstance(self.toe_faci, Unset):
            toe_faci = UNSET
        else:
            toe_faci = self.toe_faci

        toe_dist: float | None | Unset
        if isinstance(self.toe_dist, Unset):
            toe_dist = UNSET
        else:
            toe_dist = self.toe_dist

        slope1_ht: float | None | Unset
        if isinstance(self.slope1_ht, Unset):
            slope1_ht = UNSET
        else:
            slope1_ht = self.slope1_ht

        slope1_l: float | None | Unset
        if isinstance(self.slope1_l, Unset):
            slope1_l = UNSET
        else:
            slope1_l = self.slope1_l

        slope1_ang: int | None | Unset
        if isinstance(self.slope1_ang, Unset):
            slope1_ang = UNSET
        else:
            slope1_ang = self.slope1_ang

        slope2_ht: float | None | Unset
        if isinstance(self.slope2_ht, Unset):
            slope2_ht = UNSET
        else:
            slope2_ht = self.slope2_ht

        slope2_l: float | None | Unset
        if isinstance(self.slope2_l, Unset):
            slope2_l = UNSET
        else:
            slope2_l = self.slope2_l

        slope2_ang: int | None | Unset
        if isinstance(self.slope2_ang, Unset):
            slope2_ang = UNSET
        else:
            slope2_ang = self.slope2_ang

        slope3_ht: float | None | Unset
        if isinstance(self.slope3_ht, Unset):
            slope3_ht = UNSET
        else:
            slope3_ht = self.slope3_ht

        slope3_l: float | None | Unset
        if isinstance(self.slope3_l, Unset):
            slope3_l = UNSET
        else:
            slope3_l = self.slope3_l

        slope3_ang: int | None | Unset
        if isinstance(self.slope3_ang, Unset):
            slope3_ang = UNSET
        else:
            slope3_ang = self.slope3_ang

        wall1_ht: float | None | Unset
        if isinstance(self.wall1_ht, Unset):
            wall1_ht = UNSET
        else:
            wall1_ht = self.wall1_ht

        wall1_l: float | None | Unset
        if isinstance(self.wall1_l, Unset):
            wall1_l = UNSET
        else:
            wall1_l = self.wall1_l

        wall1_ang: int | None | Unset
        if isinstance(self.wall1_ang, Unset):
            wall1_ang = UNSET
        else:
            wall1_ang = self.wall1_ang

        wall2_ht: float | None | Unset
        if isinstance(self.wall2_ht, Unset):
            wall2_ht = UNSET
        else:
            wall2_ht = self.wall2_ht

        wall2_l: float | None | Unset
        if isinstance(self.wall2_l, Unset):
            wall2_l = UNSET
        else:
            wall2_l = self.wall2_l

        wall2_ang: int | None | Unset
        if isinstance(self.wall2_ang, Unset):
            wall2_ang = UNSET
        else:
            wall2_ang = self.wall2_ang

        wall3_ht: float | None | Unset
        if isinstance(self.wall3_ht, Unset):
            wall3_ht = UNSET
        else:
            wall3_ht = self.wall3_ht

        wall3_l: float | None | Unset
        if isinstance(self.wall3_l, Unset):
            wall3_l = UNSET
        else:
            wall3_l = self.wall3_l

        wall3_ang: int | None | Unset
        if isinstance(self.wall3_ang, Unset):
            wall3_ang = UNSET
        else:
            wall3_ang = self.wall3_ang

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if district is not UNSET:
            field_dict["DISTRICT"] = district
        if ctl_cat is not UNSET:
            field_dict["CTL_CAT"] = ctl_cat
        if location is not UNSET:
            field_dict["LOCATION"] = location
        if appro_e is not UNSET:
            field_dict["APPRO_E"] = appro_e
        if appro_n is not UNSET:
            field_dict["APPRO_N"] = appro_n
        if slope_no is not UNSET:
            field_dict["SLOPE_NO"] = slope_no
        if shape_length is not UNSET:
            field_dict["Shape__Length"] = shape_length
        if shape_area is not UNSET:
            field_dict["Shape__Area"] = shape_area
        if maint_part is not UNSET:
            field_dict["MAINT_PART"] = maint_part
        if overall_ht is not UNSET:
            field_dict["OVERALL_HT"] = overall_ht
        if overall_an is not UNSET:
            field_dict["OVERALL_AN"] = overall_an
        if crest_faci is not UNSET:
            field_dict["CREST_FACI"] = crest_faci
        if crest_dist is not UNSET:
            field_dict["CREST_DIST"] = crest_dist
        if toe_faci is not UNSET:
            field_dict["TOE_FACI"] = toe_faci
        if toe_dist is not UNSET:
            field_dict["TOE_DIST"] = toe_dist
        if slope1_ht is not UNSET:
            field_dict["SLOPE1_HT"] = slope1_ht
        if slope1_l is not UNSET:
            field_dict["SLOPE1_L"] = slope1_l
        if slope1_ang is not UNSET:
            field_dict["SLOPE1_ANG"] = slope1_ang
        if slope2_ht is not UNSET:
            field_dict["SLOPE2_HT"] = slope2_ht
        if slope2_l is not UNSET:
            field_dict["SLOPE2_L"] = slope2_l
        if slope2_ang is not UNSET:
            field_dict["SLOPE2_ANG"] = slope2_ang
        if slope3_ht is not UNSET:
            field_dict["SLOPE3_HT"] = slope3_ht
        if slope3_l is not UNSET:
            field_dict["SLOPE3_L"] = slope3_l
        if slope3_ang is not UNSET:
            field_dict["SLOPE3_ANG"] = slope3_ang
        if wall1_ht is not UNSET:
            field_dict["WALL1_HT"] = wall1_ht
        if wall1_l is not UNSET:
            field_dict["WALL1_L"] = wall1_l
        if wall1_ang is not UNSET:
            field_dict["WALL1_ANG"] = wall1_ang
        if wall2_ht is not UNSET:
            field_dict["WALL2_HT"] = wall2_ht
        if wall2_l is not UNSET:
            field_dict["WALL2_L"] = wall2_l
        if wall2_ang is not UNSET:
            field_dict["WALL2_ANG"] = wall2_ang
        if wall3_ht is not UNSET:
            field_dict["WALL3_HT"] = wall3_ht
        if wall3_l is not UNSET:
            field_dict["WALL3_L"] = wall3_l
        if wall3_ang is not UNSET:
            field_dict["WALL3_ANG"] = wall3_ang

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_district(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district = _parse_district(d.pop("DISTRICT", UNSET))

        def _parse_ctl_cat(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ctl_cat = _parse_ctl_cat(d.pop("CTL_CAT", UNSET))

        def _parse_location(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location = _parse_location(d.pop("LOCATION", UNSET))

        def _parse_appro_e(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        appro_e = _parse_appro_e(d.pop("APPRO_E", UNSET))

        def _parse_appro_n(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        appro_n = _parse_appro_n(d.pop("APPRO_N", UNSET))

        def _parse_slope_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        slope_no = _parse_slope_no(d.pop("SLOPE_NO", UNSET))

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

        def _parse_maint_part(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        maint_part = _parse_maint_part(d.pop("MAINT_PART", UNSET))

        def _parse_overall_ht(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        overall_ht = _parse_overall_ht(d.pop("OVERALL_HT", UNSET))

        def _parse_overall_an(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        overall_an = _parse_overall_an(d.pop("OVERALL_AN", UNSET))

        def _parse_crest_faci(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        crest_faci = _parse_crest_faci(d.pop("CREST_FACI", UNSET))

        def _parse_crest_dist(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        crest_dist = _parse_crest_dist(d.pop("CREST_DIST", UNSET))

        def _parse_toe_faci(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        toe_faci = _parse_toe_faci(d.pop("TOE_FACI", UNSET))

        def _parse_toe_dist(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        toe_dist = _parse_toe_dist(d.pop("TOE_DIST", UNSET))

        def _parse_slope1_ht(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        slope1_ht = _parse_slope1_ht(d.pop("SLOPE1_HT", UNSET))

        def _parse_slope1_l(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        slope1_l = _parse_slope1_l(d.pop("SLOPE1_L", UNSET))

        def _parse_slope1_ang(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        slope1_ang = _parse_slope1_ang(d.pop("SLOPE1_ANG", UNSET))

        def _parse_slope2_ht(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        slope2_ht = _parse_slope2_ht(d.pop("SLOPE2_HT", UNSET))

        def _parse_slope2_l(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        slope2_l = _parse_slope2_l(d.pop("SLOPE2_L", UNSET))

        def _parse_slope2_ang(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        slope2_ang = _parse_slope2_ang(d.pop("SLOPE2_ANG", UNSET))

        def _parse_slope3_ht(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        slope3_ht = _parse_slope3_ht(d.pop("SLOPE3_HT", UNSET))

        def _parse_slope3_l(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        slope3_l = _parse_slope3_l(d.pop("SLOPE3_L", UNSET))

        def _parse_slope3_ang(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        slope3_ang = _parse_slope3_ang(d.pop("SLOPE3_ANG", UNSET))

        def _parse_wall1_ht(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        wall1_ht = _parse_wall1_ht(d.pop("WALL1_HT", UNSET))

        def _parse_wall1_l(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        wall1_l = _parse_wall1_l(d.pop("WALL1_L", UNSET))

        def _parse_wall1_ang(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        wall1_ang = _parse_wall1_ang(d.pop("WALL1_ANG", UNSET))

        def _parse_wall2_ht(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        wall2_ht = _parse_wall2_ht(d.pop("WALL2_HT", UNSET))

        def _parse_wall2_l(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        wall2_l = _parse_wall2_l(d.pop("WALL2_L", UNSET))

        def _parse_wall2_ang(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        wall2_ang = _parse_wall2_ang(d.pop("WALL2_ANG", UNSET))

        def _parse_wall3_ht(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        wall3_ht = _parse_wall3_ht(d.pop("WALL3_HT", UNSET))

        def _parse_wall3_l(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        wall3_l = _parse_wall3_l(d.pop("WALL3_L", UNSET))

        def _parse_wall3_ang(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        wall3_ang = _parse_wall3_ang(d.pop("WALL3_ANG", UNSET))

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            objectid=objectid,
            district=district,
            ctl_cat=ctl_cat,
            location=location,
            appro_e=appro_e,
            appro_n=appro_n,
            slope_no=slope_no,
            shape_length=shape_length,
            shape_area=shape_area,
            maint_part=maint_part,
            overall_ht=overall_ht,
            overall_an=overall_an,
            crest_faci=crest_faci,
            crest_dist=crest_dist,
            toe_faci=toe_faci,
            toe_dist=toe_dist,
            slope1_ht=slope1_ht,
            slope1_l=slope1_l,
            slope1_ang=slope1_ang,
            slope2_ht=slope2_ht,
            slope2_l=slope2_l,
            slope2_ang=slope2_ang,
            slope3_ht=slope3_ht,
            slope3_l=slope3_l,
            slope3_ang=slope3_ang,
            wall1_ht=wall1_ht,
            wall1_l=wall1_l,
            wall1_ang=wall1_ang,
            wall2_ht=wall2_ht,
            wall2_l=wall2_l,
            wall2_ang=wall2_ang,
            wall3_ht=wall3_ht,
            wall3_l=wall3_l,
            wall3_ang=wall3_ang,
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
