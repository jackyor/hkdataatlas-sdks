from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsVR2022GCFULLAttributes")


@_attrs_define
class WfsMapServerWfsVR2022GCFULLAttributes:
    """
    Attributes:
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        cname (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        ename (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        district_t (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        district_e (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        count (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence into
            all JSON queries.
        shape (Any | Unset): Native geometry property gml:MultiSurfacePropertyType; JSON geometry is not inferred from
            its XML type.
        shape_length (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        shape_area (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
    """

    objectid: int | Unset = UNSET
    cname: None | str | Unset = UNSET
    ename: None | str | Unset = UNSET
    district_t: None | str | Unset = UNSET
    district_e: None | str | Unset = UNSET
    count: float | None | Unset = UNSET
    shape: Any | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        cname: None | str | Unset
        if isinstance(self.cname, Unset):
            cname = UNSET
        else:
            cname = self.cname

        ename: None | str | Unset
        if isinstance(self.ename, Unset):
            ename = UNSET
        else:
            ename = self.ename

        district_t: None | str | Unset
        if isinstance(self.district_t, Unset):
            district_t = UNSET
        else:
            district_t = self.district_t

        district_e: None | str | Unset
        if isinstance(self.district_e, Unset):
            district_e = UNSET
        else:
            district_e = self.district_e

        count: float | None | Unset
        if isinstance(self.count, Unset):
            count = UNSET
        else:
            count = self.count

        shape = self.shape

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
        if cname is not UNSET:
            field_dict["CNAME"] = cname
        if ename is not UNSET:
            field_dict["ENAME"] = ename
        if district_t is not UNSET:
            field_dict["DISTRICT_T"] = district_t
        if district_e is not UNSET:
            field_dict["DISTRICT_E"] = district_e
        if count is not UNSET:
            field_dict["COUNT"] = count
        if shape is not UNSET:
            field_dict["SHAPE"] = shape
        if shape_length is not UNSET:
            field_dict["SHAPE_Length"] = shape_length
        if shape_area is not UNSET:
            field_dict["SHAPE_Area"] = shape_area

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_cname(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cname = _parse_cname(d.pop("CNAME", UNSET))

        def _parse_ename(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ename = _parse_ename(d.pop("ENAME", UNSET))

        def _parse_district_t(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_t = _parse_district_t(d.pop("DISTRICT_T", UNSET))

        def _parse_district_e(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_e = _parse_district_e(d.pop("DISTRICT_E", UNSET))

        def _parse_count(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        count = _parse_count(d.pop("COUNT", UNSET))

        shape = d.pop("SHAPE", UNSET)

        def _parse_shape_length(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_length = _parse_shape_length(d.pop("SHAPE_Length", UNSET))

        def _parse_shape_area(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_area = _parse_shape_area(d.pop("SHAPE_Area", UNSET))

        wfs_map_server_wfs_vr2022gcfull_attributes = cls(
            objectid=objectid,
            cname=cname,
            ename=ename,
            district_t=district_t,
            district_e=district_e,
            count=count,
            shape=shape,
            shape_length=shape_length,
            shape_area=shape_area,
        )

        wfs_map_server_wfs_vr2022gcfull_attributes.additional_properties = d
        return wfs_map_server_wfs_vr2022gcfull_attributes

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
