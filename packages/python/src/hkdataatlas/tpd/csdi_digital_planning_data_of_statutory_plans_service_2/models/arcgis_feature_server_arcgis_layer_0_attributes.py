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
        plan_no (None | str | Unset): Publisher field type: esriFieldTypeString
        name_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        name_cht (None | str | Unset): Publisher field type: esriFieldTypeString
        pub_date (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains unknown.
        aprv_date (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains unknown.
        sect_no (None | str | Unset): Publisher field type: esriFieldTypeString
        plan_scale (int | None | Unset): Publisher field type: esriFieldTypeInteger
        geojson_link (None | str | Unset): Publisher field type: esriFieldTypeString
        gml_link (None | str | Unset): Publisher field type: esriFieldTypeString
        shp_link (None | str | Unset): Publisher field type: esriFieldTypeString
        name_chs (None | str | Unset): Publisher field type: esriFieldTypeString
        shape_area (float | None | Unset): Publisher field type: esriFieldTypeDouble
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    objectid: int | Unset = UNSET
    plan_no: None | str | Unset = UNSET
    name_eng: None | str | Unset = UNSET
    name_cht: None | str | Unset = UNSET
    pub_date: Any | Unset = UNSET
    aprv_date: Any | Unset = UNSET
    sect_no: None | str | Unset = UNSET
    plan_scale: int | None | Unset = UNSET
    geojson_link: None | str | Unset = UNSET
    gml_link: None | str | Unset = UNSET
    shp_link: None | str | Unset = UNSET
    name_chs: None | str | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        plan_no: None | str | Unset
        if isinstance(self.plan_no, Unset):
            plan_no = UNSET
        else:
            plan_no = self.plan_no

        name_eng: None | str | Unset
        if isinstance(self.name_eng, Unset):
            name_eng = UNSET
        else:
            name_eng = self.name_eng

        name_cht: None | str | Unset
        if isinstance(self.name_cht, Unset):
            name_cht = UNSET
        else:
            name_cht = self.name_cht

        pub_date = self.pub_date

        aprv_date = self.aprv_date

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

        name_chs: None | str | Unset
        if isinstance(self.name_chs, Unset):
            name_chs = UNSET
        else:
            name_chs = self.name_chs

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
        if plan_no is not UNSET:
            field_dict["PLAN_NO"] = plan_no
        if name_eng is not UNSET:
            field_dict["NAME_ENG"] = name_eng
        if name_cht is not UNSET:
            field_dict["NAME_CHT"] = name_cht
        if pub_date is not UNSET:
            field_dict["PUB_DATE"] = pub_date
        if aprv_date is not UNSET:
            field_dict["APRV_DATE"] = aprv_date
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
        if name_chs is not UNSET:
            field_dict["NAME_CHS"] = name_chs
        if shape_area is not UNSET:
            field_dict["Shape__Area"] = shape_area
        if shape_length is not UNSET:
            field_dict["Shape__Length"] = shape_length

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_plan_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        plan_no = _parse_plan_no(d.pop("PLAN_NO", UNSET))

        def _parse_name_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_eng = _parse_name_eng(d.pop("NAME_ENG", UNSET))

        def _parse_name_cht(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_cht = _parse_name_cht(d.pop("NAME_CHT", UNSET))

        pub_date = d.pop("PUB_DATE", UNSET)

        aprv_date = d.pop("APRV_DATE", UNSET)

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

        def _parse_name_chs(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_chs = _parse_name_chs(d.pop("NAME_CHS", UNSET))

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

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            objectid=objectid,
            plan_no=plan_no,
            name_eng=name_eng,
            name_cht=name_cht,
            pub_date=pub_date,
            aprv_date=aprv_date,
            sect_no=sect_no,
            plan_scale=plan_scale,
            geojson_link=geojson_link,
            gml_link=gml_link,
            shp_link=shp_link,
            name_chs=name_chs,
            shape_area=shape_area,
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
