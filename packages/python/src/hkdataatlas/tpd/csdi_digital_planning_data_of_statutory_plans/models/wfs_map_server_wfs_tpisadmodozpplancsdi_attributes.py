from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsTPISADMODOZPPLANCSDIAttributes")


@_attrs_define
class WfsMapServerWfsTPISADMODOZPPLANCSDIAttributes:
    """
    Attributes:
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        plan_no (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        name_eng (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        name_cht (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        name_chs (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        pub_date (None | str | Unset): Native XSD type xsd:dateTime. Requiredness is not projected from XML occurrence
            into all JSON queries.
        aprv_date (None | str | Unset): Native XSD type xsd:dateTime. Requiredness is not projected from XML occurrence
            into all JSON queries.
        sect_no (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        plan_scale (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into
            all JSON queries.
        geojson_link (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        gml_link (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        shp_link (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:MultiSurfacePropertyType; JSON geometry is not inferred from
            its XML type.
        shape_st_area (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        shape_st_length (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
    """

    objectid: int | Unset = UNSET
    plan_no: None | str | Unset = UNSET
    name_eng: None | str | Unset = UNSET
    name_cht: None | str | Unset = UNSET
    name_chs: None | str | Unset = UNSET
    pub_date: None | str | Unset = UNSET
    aprv_date: None | str | Unset = UNSET
    sect_no: None | str | Unset = UNSET
    plan_scale: int | None | Unset = UNSET
    geojson_link: None | str | Unset = UNSET
    gml_link: None | str | Unset = UNSET
    shp_link: None | str | Unset = UNSET
    shape: Any | Unset = UNSET
    shape_st_area: float | None | Unset = UNSET
    shape_st_length: float | None | Unset = UNSET
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

        name_chs: None | str | Unset
        if isinstance(self.name_chs, Unset):
            name_chs = UNSET
        else:
            name_chs = self.name_chs

        pub_date: None | str | Unset
        if isinstance(self.pub_date, Unset):
            pub_date = UNSET
        else:
            pub_date = self.pub_date

        aprv_date: None | str | Unset
        if isinstance(self.aprv_date, Unset):
            aprv_date = UNSET
        else:
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

        shape = self.shape

        shape_st_area: float | None | Unset
        if isinstance(self.shape_st_area, Unset):
            shape_st_area = UNSET
        else:
            shape_st_area = self.shape_st_area

        shape_st_length: float | None | Unset
        if isinstance(self.shape_st_length, Unset):
            shape_st_length = UNSET
        else:
            shape_st_length = self.shape_st_length

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
        if name_chs is not UNSET:
            field_dict["NAME_CHS"] = name_chs
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
        if shape is not UNSET:
            field_dict["SHAPE"] = shape
        if shape_st_area is not UNSET:
            field_dict["SHAPE.STArea__"] = shape_st_area
        if shape_st_length is not UNSET:
            field_dict["SHAPE.STLength__"] = shape_st_length

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

        def _parse_name_chs(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_chs = _parse_name_chs(d.pop("NAME_CHS", UNSET))

        def _parse_pub_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pub_date = _parse_pub_date(d.pop("PUB_DATE", UNSET))

        def _parse_aprv_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        aprv_date = _parse_aprv_date(d.pop("APRV_DATE", UNSET))

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

        shape = d.pop("SHAPE", UNSET)

        def _parse_shape_st_area(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_st_area = _parse_shape_st_area(d.pop("SHAPE.STArea__", UNSET))

        def _parse_shape_st_length(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_st_length = _parse_shape_st_length(d.pop("SHAPE.STLength__", UNSET))

        wfs_map_server_wfs_tpisadmodozpplancsdi_attributes = cls(
            objectid=objectid,
            plan_no=plan_no,
            name_eng=name_eng,
            name_cht=name_cht,
            name_chs=name_chs,
            pub_date=pub_date,
            aprv_date=aprv_date,
            sect_no=sect_no,
            plan_scale=plan_scale,
            geojson_link=geojson_link,
            gml_link=gml_link,
            shp_link=shp_link,
            shape=shape,
            shape_st_area=shape_st_area,
            shape_st_length=shape_st_length,
        )

        wfs_map_server_wfs_tpisadmodozpplancsdi_attributes.additional_properties = d
        return wfs_map_server_wfs_tpisadmodozpplancsdi_attributes

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
