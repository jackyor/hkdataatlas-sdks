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
        id (int | None | Unset): Publisher field type: esriFieldTypeInteger
        isl_name_c (None | str | Unset): Publisher field type: esriFieldTypeString
        isl_name_e (None | str | Unset): Publisher field type: esriFieldTypeString
        fcz (None | str | Unset): Publisher field type: esriFieldTypeString
        siteplan (None | str | Unset): Publisher field type: esriFieldTypeString
        fcz_id (int | None | Unset): Publisher field type: esriFieldTypeInteger
        name_c (None | str | Unset): Publisher field type: esriFieldTypeString
        name_e (None | str | Unset): Publisher field type: esriFieldTypeString
        fcz_id2 (int | None | Unset): Publisher field type: esriFieldTypeInteger
        fcz_sz (None | str | Unset): Publisher field type: esriFieldTypeString
        sz_c (None | str | Unset): Publisher field type: esriFieldTypeString
        sz_e (None | str | Unset): Publisher field type: esriFieldTypeString
        masterplan (None | str | Unset): Publisher field type: esriFieldTypeString
        zarea_sqm (int | None | Unset): Publisher field type: esriFieldTypeInteger
        shape_leng (float | None | Unset): Publisher field type: esriFieldTypeDouble
        ogr_fid (int | None | Unset): Publisher field type: esriFieldTypeInteger
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
        shape_area (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    id: int | None | Unset = UNSET
    isl_name_c: None | str | Unset = UNSET
    isl_name_e: None | str | Unset = UNSET
    fcz: None | str | Unset = UNSET
    siteplan: None | str | Unset = UNSET
    fcz_id: int | None | Unset = UNSET
    name_c: None | str | Unset = UNSET
    name_e: None | str | Unset = UNSET
    fcz_id2: int | None | Unset = UNSET
    fcz_sz: None | str | Unset = UNSET
    sz_c: None | str | Unset = UNSET
    sz_e: None | str | Unset = UNSET
    masterplan: None | str | Unset = UNSET
    zarea_sqm: int | None | Unset = UNSET
    shape_leng: float | None | Unset = UNSET
    ogr_fid: int | None | Unset = UNSET
    objectid: int | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: int | None | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        isl_name_c: None | str | Unset
        if isinstance(self.isl_name_c, Unset):
            isl_name_c = UNSET
        else:
            isl_name_c = self.isl_name_c

        isl_name_e: None | str | Unset
        if isinstance(self.isl_name_e, Unset):
            isl_name_e = UNSET
        else:
            isl_name_e = self.isl_name_e

        fcz: None | str | Unset
        if isinstance(self.fcz, Unset):
            fcz = UNSET
        else:
            fcz = self.fcz

        siteplan: None | str | Unset
        if isinstance(self.siteplan, Unset):
            siteplan = UNSET
        else:
            siteplan = self.siteplan

        fcz_id: int | None | Unset
        if isinstance(self.fcz_id, Unset):
            fcz_id = UNSET
        else:
            fcz_id = self.fcz_id

        name_c: None | str | Unset
        if isinstance(self.name_c, Unset):
            name_c = UNSET
        else:
            name_c = self.name_c

        name_e: None | str | Unset
        if isinstance(self.name_e, Unset):
            name_e = UNSET
        else:
            name_e = self.name_e

        fcz_id2: int | None | Unset
        if isinstance(self.fcz_id2, Unset):
            fcz_id2 = UNSET
        else:
            fcz_id2 = self.fcz_id2

        fcz_sz: None | str | Unset
        if isinstance(self.fcz_sz, Unset):
            fcz_sz = UNSET
        else:
            fcz_sz = self.fcz_sz

        sz_c: None | str | Unset
        if isinstance(self.sz_c, Unset):
            sz_c = UNSET
        else:
            sz_c = self.sz_c

        sz_e: None | str | Unset
        if isinstance(self.sz_e, Unset):
            sz_e = UNSET
        else:
            sz_e = self.sz_e

        masterplan: None | str | Unset
        if isinstance(self.masterplan, Unset):
            masterplan = UNSET
        else:
            masterplan = self.masterplan

        zarea_sqm: int | None | Unset
        if isinstance(self.zarea_sqm, Unset):
            zarea_sqm = UNSET
        else:
            zarea_sqm = self.zarea_sqm

        shape_leng: float | None | Unset
        if isinstance(self.shape_leng, Unset):
            shape_leng = UNSET
        else:
            shape_leng = self.shape_leng

        ogr_fid: int | None | Unset
        if isinstance(self.ogr_fid, Unset):
            ogr_fid = UNSET
        else:
            ogr_fid = self.ogr_fid

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
        if id is not UNSET:
            field_dict["ID"] = id
        if isl_name_c is not UNSET:
            field_dict["ISL_NAME_C"] = isl_name_c
        if isl_name_e is not UNSET:
            field_dict["ISL_NAME_E"] = isl_name_e
        if fcz is not UNSET:
            field_dict["FCZ"] = fcz
        if siteplan is not UNSET:
            field_dict["SITEPLAN"] = siteplan
        if fcz_id is not UNSET:
            field_dict["FCZ_ID"] = fcz_id
        if name_c is not UNSET:
            field_dict["NAME_C"] = name_c
        if name_e is not UNSET:
            field_dict["NAME_E"] = name_e
        if fcz_id2 is not UNSET:
            field_dict["FCZ_ID2"] = fcz_id2
        if fcz_sz is not UNSET:
            field_dict["FCZ_SZ"] = fcz_sz
        if sz_c is not UNSET:
            field_dict["SZ_C"] = sz_c
        if sz_e is not UNSET:
            field_dict["SZ_E"] = sz_e
        if masterplan is not UNSET:
            field_dict["MASTERPLAN"] = masterplan
        if zarea_sqm is not UNSET:
            field_dict["ZAREA_SQM"] = zarea_sqm
        if shape_leng is not UNSET:
            field_dict["SHAPE_Leng"] = shape_leng
        if ogr_fid is not UNSET:
            field_dict["OGR_FID"] = ogr_fid
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

        def _parse_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        id = _parse_id(d.pop("ID", UNSET))

        def _parse_isl_name_c(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        isl_name_c = _parse_isl_name_c(d.pop("ISL_NAME_C", UNSET))

        def _parse_isl_name_e(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        isl_name_e = _parse_isl_name_e(d.pop("ISL_NAME_E", UNSET))

        def _parse_fcz(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fcz = _parse_fcz(d.pop("FCZ", UNSET))

        def _parse_siteplan(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        siteplan = _parse_siteplan(d.pop("SITEPLAN", UNSET))

        def _parse_fcz_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        fcz_id = _parse_fcz_id(d.pop("FCZ_ID", UNSET))

        def _parse_name_c(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_c = _parse_name_c(d.pop("NAME_C", UNSET))

        def _parse_name_e(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_e = _parse_name_e(d.pop("NAME_E", UNSET))

        def _parse_fcz_id2(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        fcz_id2 = _parse_fcz_id2(d.pop("FCZ_ID2", UNSET))

        def _parse_fcz_sz(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fcz_sz = _parse_fcz_sz(d.pop("FCZ_SZ", UNSET))

        def _parse_sz_c(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sz_c = _parse_sz_c(d.pop("SZ_C", UNSET))

        def _parse_sz_e(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sz_e = _parse_sz_e(d.pop("SZ_E", UNSET))

        def _parse_masterplan(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        masterplan = _parse_masterplan(d.pop("MASTERPLAN", UNSET))

        def _parse_zarea_sqm(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        zarea_sqm = _parse_zarea_sqm(d.pop("ZAREA_SQM", UNSET))

        def _parse_shape_leng(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_leng = _parse_shape_leng(d.pop("SHAPE_Leng", UNSET))

        def _parse_ogr_fid(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        ogr_fid = _parse_ogr_fid(d.pop("OGR_FID", UNSET))

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
            id=id,
            isl_name_c=isl_name_c,
            isl_name_e=isl_name_e,
            fcz=fcz,
            siteplan=siteplan,
            fcz_id=fcz_id,
            name_c=name_c,
            name_e=name_e,
            fcz_id2=fcz_id2,
            fcz_sz=fcz_sz,
            sz_c=sz_c,
            sz_e=sz_e,
            masterplan=masterplan,
            zarea_sqm=zarea_sqm,
            shape_leng=shape_leng,
            ogr_fid=ogr_fid,
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
