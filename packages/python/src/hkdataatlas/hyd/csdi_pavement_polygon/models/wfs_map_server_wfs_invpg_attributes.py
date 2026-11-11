from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsINVPGAttributes")


@_attrs_define
class WfsMapServerWfsINVPGAttributes:
    """
    Attributes:
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:MultiSurfacePropertyType; JSON geometry is not inferred from
            its XML type.
        pg_uid (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        feat_type (int | None | Unset): Native XSD type xsd:short. Requiredness is not projected from XML occurrence
            into all JSON queries.
        sur_type_1 (int | None | Unset): Native XSD type xsd:short. Requiredness is not projected from XML occurrence
            into all JSON queries.
        paver_type (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        lvl (int | None | Unset): Native XSD type xsd:short. Requiredness is not projected from XML occurrence into all
            JSON queries.
        shape_length (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        shape_area (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
    """

    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    pg_uid: None | str | Unset = UNSET
    feat_type: int | None | Unset = UNSET
    sur_type_1: int | None | Unset = UNSET
    paver_type: None | str | Unset = UNSET
    lvl: int | None | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        shape = self.shape

        pg_uid: None | str | Unset
        if isinstance(self.pg_uid, Unset):
            pg_uid = UNSET
        else:
            pg_uid = self.pg_uid

        feat_type: int | None | Unset
        if isinstance(self.feat_type, Unset):
            feat_type = UNSET
        else:
            feat_type = self.feat_type

        sur_type_1: int | None | Unset
        if isinstance(self.sur_type_1, Unset):
            sur_type_1 = UNSET
        else:
            sur_type_1 = self.sur_type_1

        paver_type: None | str | Unset
        if isinstance(self.paver_type, Unset):
            paver_type = UNSET
        else:
            paver_type = self.paver_type

        lvl: int | None | Unset
        if isinstance(self.lvl, Unset):
            lvl = UNSET
        else:
            lvl = self.lvl

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
        if pg_uid is not UNSET:
            field_dict["PG_UID"] = pg_uid
        if feat_type is not UNSET:
            field_dict["FEAT_TYPE"] = feat_type
        if sur_type_1 is not UNSET:
            field_dict["SUR_TYPE_1"] = sur_type_1
        if paver_type is not UNSET:
            field_dict["PAVER_TYPE"] = paver_type
        if lvl is not UNSET:
            field_dict["LVL"] = lvl
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

        def _parse_pg_uid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pg_uid = _parse_pg_uid(d.pop("PG_UID", UNSET))

        def _parse_feat_type(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        feat_type = _parse_feat_type(d.pop("FEAT_TYPE", UNSET))

        def _parse_sur_type_1(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sur_type_1 = _parse_sur_type_1(d.pop("SUR_TYPE_1", UNSET))

        def _parse_paver_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        paver_type = _parse_paver_type(d.pop("PAVER_TYPE", UNSET))

        def _parse_lvl(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        lvl = _parse_lvl(d.pop("LVL", UNSET))

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

        wfs_map_server_wfs_invpg_attributes = cls(
            objectid=objectid,
            shape=shape,
            pg_uid=pg_uid,
            feat_type=feat_type,
            sur_type_1=sur_type_1,
            paver_type=paver_type,
            lvl=lvl,
            shape_length=shape_length,
            shape_area=shape_area,
        )

        wfs_map_server_wfs_invpg_attributes.additional_properties = d
        return wfs_map_server_wfs_invpg_attributes

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
