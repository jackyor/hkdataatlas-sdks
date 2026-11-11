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
        sect_no (None | str | Unset): Publisher field type: esriFieldTypeString
        plan_scale (int | None | Unset): Publisher field type: esriFieldTypeInteger
        geojson_link (None | str | Unset): Publisher field type: esriFieldTypeString
        gml_link (None | str | Unset): Publisher field type: esriFieldTypeString
        shp_link (None | str | Unset): Publisher field type: esriFieldTypeString
        ra_plan_no (None | str | Unset): Publisher field type: esriFieldTypeString
        ra_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        ra_cht (None | str | Unset): Publisher field type: esriFieldTypeString
        ra_chs (None | str | Unset): Publisher field type: esriFieldTypeString
        gaz_date (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains unknown.
        ozp_schm (None | str | Unset): Publisher field type: esriFieldTypeString
        sub_area (None | str | Unset): Publisher field type: esriFieldTypeString
        shape_area (float | None | Unset): Publisher field type: esriFieldTypeDouble
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    objectid: int | Unset = UNSET
    sect_no: None | str | Unset = UNSET
    plan_scale: int | None | Unset = UNSET
    geojson_link: None | str | Unset = UNSET
    gml_link: None | str | Unset = UNSET
    shp_link: None | str | Unset = UNSET
    ra_plan_no: None | str | Unset = UNSET
    ra_eng: None | str | Unset = UNSET
    ra_cht: None | str | Unset = UNSET
    ra_chs: None | str | Unset = UNSET
    gaz_date: Any | Unset = UNSET
    ozp_schm: None | str | Unset = UNSET
    sub_area: None | str | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        sect_no: None | str | Unset
        if isinstance(self.sect_no, Unset):
            sect_no = UNSET
        else:
            sect_no = self.sect_no

        plan_scale: int | None | Unset
        if isinstance(self.plan_scale, Unset):
            plan_scale = UNSET
        else:
            plan_scale = self.plan_scale

        geojson_link: None | str | Unset
        if isinstance(self.geojson_link, Unset):
            geojson_link = UNSET
        else:
            geojson_link = self.geojson_link

        gml_link: None | str | Unset
        if isinstance(self.gml_link, Unset):
            gml_link = UNSET
        else:
            gml_link = self.gml_link

        shp_link: None | str | Unset
        if isinstance(self.shp_link, Unset):
            shp_link = UNSET
        else:
            shp_link = self.shp_link

        ra_plan_no: None | str | Unset
        if isinstance(self.ra_plan_no, Unset):
            ra_plan_no = UNSET
        else:
            ra_plan_no = self.ra_plan_no

        ra_eng: None | str | Unset
        if isinstance(self.ra_eng, Unset):
            ra_eng = UNSET
        else:
            ra_eng = self.ra_eng

        ra_cht: None | str | Unset
        if isinstance(self.ra_cht, Unset):
            ra_cht = UNSET
        else:
            ra_cht = self.ra_cht

        ra_chs: None | str | Unset
        if isinstance(self.ra_chs, Unset):
            ra_chs = UNSET
        else:
            ra_chs = self.ra_chs

        gaz_date = self.gaz_date

        ozp_schm: None | str | Unset
        if isinstance(self.ozp_schm, Unset):
            ozp_schm = UNSET
        else:
            ozp_schm = self.ozp_schm

        sub_area: None | str | Unset
        if isinstance(self.sub_area, Unset):
            sub_area = UNSET
        else:
            sub_area = self.sub_area

        shape_area: float | None | Unset
        if isinstance(self.shape_area, Unset):
            shape_area = UNSET
        else:
            shape_area = self.shape_area

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
        if sect_no is not UNSET:
            field_dict["SECT_NO"] = sect_no
        if plan_scale is not UNSET:
            field_dict["PLAN_SCALE"] = plan_scale
        if geojson_link is not UNSET:
            field_dict["GEOJSON_LINK"] = geojson_link
        if gml_link is not UNSET:
            field_dict["GML_LINK"] = gml_link
        if shp_link is not UNSET:
            field_dict["SHP_LINK"] = shp_link
        if ra_plan_no is not UNSET:
            field_dict["RA_PLAN_NO"] = ra_plan_no
        if ra_eng is not UNSET:
            field_dict["RA_ENG"] = ra_eng
        if ra_cht is not UNSET:
            field_dict["RA_CHT"] = ra_cht
        if ra_chs is not UNSET:
            field_dict["RA_CHS"] = ra_chs
        if gaz_date is not UNSET:
            field_dict["GAZ_DATE"] = gaz_date
        if ozp_schm is not UNSET:
            field_dict["OZP_SCHM"] = ozp_schm
        if sub_area is not UNSET:
            field_dict["SUB_AREA"] = sub_area
        if shape_area is not UNSET:
            field_dict["Shape__Area"] = shape_area
        if shape_length is not UNSET:
            field_dict["Shape__Length"] = shape_length

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_sect_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sect_no = _parse_sect_no(d.pop("SECT_NO", UNSET))

        def _parse_plan_scale(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        plan_scale = _parse_plan_scale(d.pop("PLAN_SCALE", UNSET))

        def _parse_geojson_link(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        geojson_link = _parse_geojson_link(d.pop("GEOJSON_LINK", UNSET))

        def _parse_gml_link(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gml_link = _parse_gml_link(d.pop("GML_LINK", UNSET))

        def _parse_shp_link(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        shp_link = _parse_shp_link(d.pop("SHP_LINK", UNSET))

        def _parse_ra_plan_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ra_plan_no = _parse_ra_plan_no(d.pop("RA_PLAN_NO", UNSET))

        def _parse_ra_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ra_eng = _parse_ra_eng(d.pop("RA_ENG", UNSET))

        def _parse_ra_cht(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ra_cht = _parse_ra_cht(d.pop("RA_CHT", UNSET))

        def _parse_ra_chs(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ra_chs = _parse_ra_chs(d.pop("RA_CHS", UNSET))

        gaz_date = d.pop("GAZ_DATE", UNSET)

        def _parse_ozp_schm(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ozp_schm = _parse_ozp_schm(d.pop("OZP_SCHM", UNSET))

        def _parse_sub_area(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sub_area = _parse_sub_area(d.pop("SUB_AREA", UNSET))

        def _parse_shape_area(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_area = _parse_shape_area(d.pop("Shape__Area", UNSET))

        def _parse_shape_length(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_length = _parse_shape_length(d.pop("Shape__Length", UNSET))

        arcgis_feature_server_arcgis_layer_1_attributes = cls(
            objectid=objectid,
            sect_no=sect_no,
            plan_scale=plan_scale,
            geojson_link=geojson_link,
            gml_link=gml_link,
            shp_link=shp_link,
            ra_plan_no=ra_plan_no,
            ra_eng=ra_eng,
            ra_cht=ra_cht,
            ra_chs=ra_chs,
            gaz_date=gaz_date,
            ozp_schm=ozp_schm,
            sub_area=sub_area,
            shape_area=shape_area,
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
