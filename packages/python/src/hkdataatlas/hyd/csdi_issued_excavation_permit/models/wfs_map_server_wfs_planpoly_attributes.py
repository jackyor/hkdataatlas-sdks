from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsPLANPOLYAttributes")


@_attrs_define
class WfsMapServerWfsPLANPOLYAttributes:
    """
    Attributes:
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:MultiSurfacePropertyType; JSON geometry is not inferred from
            its XML type.
        plan_id (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        section_id (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        start_date (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        end_date (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        xp_purpose (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        poly_id (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        trnh_len (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        trnh_dep (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        trnh_wid (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        trnh_area (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        ref_id_1 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        xp_type (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        version (int | None | Unset): Native XSD type xsd:short. Requiredness is not projected from XML occurrence into
            all JSON queries.
        hp_lvl (int | None | Unset): Native XSD type xsd:short. Requiredness is not projected from XML occurrence into
            all JSON queries.
        is_ae (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape_length (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        shape_area (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
    """

    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    plan_id: None | str | Unset = UNSET
    section_id: None | str | Unset = UNSET
    start_date: None | str | Unset = UNSET
    end_date: None | str | Unset = UNSET
    xp_purpose: None | str | Unset = UNSET
    poly_id: float | None | Unset = UNSET
    trnh_len: float | None | Unset = UNSET
    trnh_dep: float | None | Unset = UNSET
    trnh_wid: float | None | Unset = UNSET
    trnh_area: float | None | Unset = UNSET
    ref_id_1: None | str | Unset = UNSET
    xp_type: None | str | Unset = UNSET
    version: int | None | Unset = UNSET
    hp_lvl: int | None | Unset = UNSET
    is_ae: None | str | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        shape = self.shape

        plan_id: None | str | Unset
        if isinstance(self.plan_id, Unset):
            plan_id = UNSET
        else:
            plan_id = self.plan_id

        section_id: None | str | Unset
        if isinstance(self.section_id, Unset):
            section_id = UNSET
        else:
            section_id = self.section_id

        start_date: None | str | Unset
        if isinstance(self.start_date, Unset):
            start_date = UNSET
        else:
            start_date = self.start_date

        end_date: None | str | Unset
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        else:
            end_date = self.end_date

        xp_purpose: None | str | Unset
        if isinstance(self.xp_purpose, Unset):
            xp_purpose = UNSET
        else:
            xp_purpose = self.xp_purpose

        poly_id: float | None | Unset
        if isinstance(self.poly_id, Unset):
            poly_id = UNSET
        else:
            poly_id = self.poly_id

        trnh_len: float | None | Unset
        if isinstance(self.trnh_len, Unset):
            trnh_len = UNSET
        else:
            trnh_len = self.trnh_len

        trnh_dep: float | None | Unset
        if isinstance(self.trnh_dep, Unset):
            trnh_dep = UNSET
        else:
            trnh_dep = self.trnh_dep

        trnh_wid: float | None | Unset
        if isinstance(self.trnh_wid, Unset):
            trnh_wid = UNSET
        else:
            trnh_wid = self.trnh_wid

        trnh_area: float | None | Unset
        if isinstance(self.trnh_area, Unset):
            trnh_area = UNSET
        else:
            trnh_area = self.trnh_area

        ref_id_1: None | str | Unset
        if isinstance(self.ref_id_1, Unset):
            ref_id_1 = UNSET
        else:
            ref_id_1 = self.ref_id_1

        xp_type: None | str | Unset
        if isinstance(self.xp_type, Unset):
            xp_type = UNSET
        else:
            xp_type = self.xp_type

        version: int | None | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        hp_lvl: int | None | Unset
        if isinstance(self.hp_lvl, Unset):
            hp_lvl = UNSET
        else:
            hp_lvl = self.hp_lvl

        is_ae: None | str | Unset
        if isinstance(self.is_ae, Unset):
            is_ae = UNSET
        else:
            is_ae = self.is_ae

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
        if shape is not UNSET:
            field_dict["Shape"] = shape
        if plan_id is not UNSET:
            field_dict["PLAN_ID"] = plan_id
        if section_id is not UNSET:
            field_dict["SECTION_ID"] = section_id
        if start_date is not UNSET:
            field_dict["Start_Date"] = start_date
        if end_date is not UNSET:
            field_dict["End_Date"] = end_date
        if xp_purpose is not UNSET:
            field_dict["XP_Purpose"] = xp_purpose
        if poly_id is not UNSET:
            field_dict["POLY_ID"] = poly_id
        if trnh_len is not UNSET:
            field_dict["trnh_len"] = trnh_len
        if trnh_dep is not UNSET:
            field_dict["trnh_dep"] = trnh_dep
        if trnh_wid is not UNSET:
            field_dict["trnh_wid"] = trnh_wid
        if trnh_area is not UNSET:
            field_dict["trnh_area"] = trnh_area
        if ref_id_1 is not UNSET:
            field_dict["REF_ID_1"] = ref_id_1
        if xp_type is not UNSET:
            field_dict["XP_TYPE"] = xp_type
        if version is not UNSET:
            field_dict["VERSION"] = version
        if hp_lvl is not UNSET:
            field_dict["HP_LVL"] = hp_lvl
        if is_ae is not UNSET:
            field_dict["IS_AE"] = is_ae
        if shape_length is not UNSET:
            field_dict["Shape_Length"] = shape_length
        if shape_area is not UNSET:
            field_dict["Shape_Area"] = shape_area

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("Shape", UNSET)

        def _parse_plan_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        plan_id = _parse_plan_id(d.pop("PLAN_ID", UNSET))

        def _parse_section_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        section_id = _parse_section_id(d.pop("SECTION_ID", UNSET))

        def _parse_start_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        start_date = _parse_start_date(d.pop("Start_Date", UNSET))

        def _parse_end_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        end_date = _parse_end_date(d.pop("End_Date", UNSET))

        def _parse_xp_purpose(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        xp_purpose = _parse_xp_purpose(d.pop("XP_Purpose", UNSET))

        def _parse_poly_id(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        poly_id = _parse_poly_id(d.pop("POLY_ID", UNSET))

        def _parse_trnh_len(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        trnh_len = _parse_trnh_len(d.pop("trnh_len", UNSET))

        def _parse_trnh_dep(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        trnh_dep = _parse_trnh_dep(d.pop("trnh_dep", UNSET))

        def _parse_trnh_wid(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        trnh_wid = _parse_trnh_wid(d.pop("trnh_wid", UNSET))

        def _parse_trnh_area(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        trnh_area = _parse_trnh_area(d.pop("trnh_area", UNSET))

        def _parse_ref_id_1(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ref_id_1 = _parse_ref_id_1(d.pop("REF_ID_1", UNSET))

        def _parse_xp_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        xp_type = _parse_xp_type(d.pop("XP_TYPE", UNSET))

        def _parse_version(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        version = _parse_version(d.pop("VERSION", UNSET))

        def _parse_hp_lvl(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        hp_lvl = _parse_hp_lvl(d.pop("HP_LVL", UNSET))

        def _parse_is_ae(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        is_ae = _parse_is_ae(d.pop("IS_AE", UNSET))

        def _parse_shape_length(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_length = _parse_shape_length(d.pop("Shape_Length", UNSET))

        def _parse_shape_area(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_area = _parse_shape_area(d.pop("Shape_Area", UNSET))

        wfs_map_server_wfs_planpoly_attributes = cls(
            objectid=objectid,
            shape=shape,
            plan_id=plan_id,
            section_id=section_id,
            start_date=start_date,
            end_date=end_date,
            xp_purpose=xp_purpose,
            poly_id=poly_id,
            trnh_len=trnh_len,
            trnh_dep=trnh_dep,
            trnh_wid=trnh_wid,
            trnh_area=trnh_area,
            ref_id_1=ref_id_1,
            xp_type=xp_type,
            version=version,
            hp_lvl=hp_lvl,
            is_ae=is_ae,
            shape_length=shape_length,
            shape_area=shape_area,
        )

        wfs_map_server_wfs_planpoly_attributes.additional_properties = d
        return wfs_map_server_wfs_planpoly_attributes

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
