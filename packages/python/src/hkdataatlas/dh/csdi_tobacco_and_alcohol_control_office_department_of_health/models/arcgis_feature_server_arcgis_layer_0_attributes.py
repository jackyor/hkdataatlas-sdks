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
        ename (None | str | Unset): Publisher field type: esriFieldTypeString
        cname (None | str | Unset): Publisher field type: esriFieldTypeString
        district (None | str | Unset): Publisher field type: esriFieldTypeString
        district_c (None | str | Unset): Publisher field type: esriFieldTypeString
        usagetype (None | str | Unset): Publisher field type: esriFieldTypeString
        usagetype_c (None | str | Unset): Publisher field type: esriFieldTypeString
        structuretype (None | str | Unset): Publisher field type: esriFieldTypeString
        structuretype_c (None | str | Unset): Publisher field type: esriFieldTypeString
        planno (None | str | Unset): Publisher field type: esriFieldTypeString
        rev_date (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains unknown.
        url (None | str | Unset): Publisher field type: esriFieldTypeString
        remarks (None | str | Unset): Publisher field type: esriFieldTypeString
        remarks_c (None | str | Unset): Publisher field type: esriFieldTypeString
        nsa_id (None | str | Unset): Publisher field type: esriFieldTypeString
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
        shape_area (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    objectid: int | Unset = UNSET
    ename: None | str | Unset = UNSET
    cname: None | str | Unset = UNSET
    district: None | str | Unset = UNSET
    district_c: None | str | Unset = UNSET
    usagetype: None | str | Unset = UNSET
    usagetype_c: None | str | Unset = UNSET
    structuretype: None | str | Unset = UNSET
    structuretype_c: None | str | Unset = UNSET
    planno: None | str | Unset = UNSET
    rev_date: Any | Unset = UNSET
    url: None | str | Unset = UNSET
    remarks: None | str | Unset = UNSET
    remarks_c: None | str | Unset = UNSET
    nsa_id: None | str | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        ename: None | str | Unset
        if isinstance(self.ename, Unset):
            ename = UNSET
        else:
            ename = self.ename

        cname: None | str | Unset
        if isinstance(self.cname, Unset):
            cname = UNSET
        else:
            cname = self.cname

        district: None | str | Unset
        if isinstance(self.district, Unset):
            district = UNSET
        else:
            district = self.district

        district_c: None | str | Unset
        if isinstance(self.district_c, Unset):
            district_c = UNSET
        else:
            district_c = self.district_c

        usagetype: None | str | Unset
        if isinstance(self.usagetype, Unset):
            usagetype = UNSET
        else:
            usagetype = self.usagetype

        usagetype_c: None | str | Unset
        if isinstance(self.usagetype_c, Unset):
            usagetype_c = UNSET
        else:
            usagetype_c = self.usagetype_c

        structuretype: None | str | Unset
        if isinstance(self.structuretype, Unset):
            structuretype = UNSET
        else:
            structuretype = self.structuretype

        structuretype_c: None | str | Unset
        if isinstance(self.structuretype_c, Unset):
            structuretype_c = UNSET
        else:
            structuretype_c = self.structuretype_c

        planno: None | str | Unset
        if isinstance(self.planno, Unset):
            planno = UNSET
        else:
            planno = self.planno

        rev_date = self.rev_date

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        remarks: None | str | Unset
        if isinstance(self.remarks, Unset):
            remarks = UNSET
        else:
            remarks = self.remarks

        remarks_c: None | str | Unset
        if isinstance(self.remarks_c, Unset):
            remarks_c = UNSET
        else:
            remarks_c = self.remarks_c

        nsa_id: None | str | Unset
        if isinstance(self.nsa_id, Unset):
            nsa_id = UNSET
        else:
            nsa_id = self.nsa_id

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
        if ename is not UNSET:
            field_dict["ENAME"] = ename
        if cname is not UNSET:
            field_dict["CNAME"] = cname
        if district is not UNSET:
            field_dict["DISTRICT"] = district
        if district_c is not UNSET:
            field_dict["DISTRICT_C"] = district_c
        if usagetype is not UNSET:
            field_dict["USAGETYPE"] = usagetype
        if usagetype_c is not UNSET:
            field_dict["USAGETYPE_C"] = usagetype_c
        if structuretype is not UNSET:
            field_dict["STRUCTURETYPE"] = structuretype
        if structuretype_c is not UNSET:
            field_dict["STRUCTURETYPE_C"] = structuretype_c
        if planno is not UNSET:
            field_dict["PLANNO"] = planno
        if rev_date is not UNSET:
            field_dict["REV_DATE"] = rev_date
        if url is not UNSET:
            field_dict["URL"] = url
        if remarks is not UNSET:
            field_dict["REMARKS"] = remarks
        if remarks_c is not UNSET:
            field_dict["REMARKS_C"] = remarks_c
        if nsa_id is not UNSET:
            field_dict["NSA_ID"] = nsa_id
        if shape_length is not UNSET:
            field_dict["Shape__Length"] = shape_length
        if shape_area is not UNSET:
            field_dict["Shape__Area"] = shape_area

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_ename(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ename = _parse_ename(d.pop("ENAME", UNSET))

        def _parse_cname(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cname = _parse_cname(d.pop("CNAME", UNSET))

        def _parse_district(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district = _parse_district(d.pop("DISTRICT", UNSET))

        def _parse_district_c(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_c = _parse_district_c(d.pop("DISTRICT_C", UNSET))

        def _parse_usagetype(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        usagetype = _parse_usagetype(d.pop("USAGETYPE", UNSET))

        def _parse_usagetype_c(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        usagetype_c = _parse_usagetype_c(d.pop("USAGETYPE_C", UNSET))

        def _parse_structuretype(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        structuretype = _parse_structuretype(d.pop("STRUCTURETYPE", UNSET))

        def _parse_structuretype_c(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        structuretype_c = _parse_structuretype_c(d.pop("STRUCTURETYPE_C", UNSET))

        def _parse_planno(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        planno = _parse_planno(d.pop("PLANNO", UNSET))

        rev_date = d.pop("REV_DATE", UNSET)

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("URL", UNSET))

        def _parse_remarks(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remarks = _parse_remarks(d.pop("REMARKS", UNSET))

        def _parse_remarks_c(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remarks_c = _parse_remarks_c(d.pop("REMARKS_C", UNSET))

        def _parse_nsa_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nsa_id = _parse_nsa_id(d.pop("NSA_ID", UNSET))

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
            objectid=objectid,
            ename=ename,
            cname=cname,
            district=district,
            district_c=district_c,
            usagetype=usagetype,
            usagetype_c=usagetype_c,
            structuretype=structuretype,
            structuretype_c=structuretype_c,
            planno=planno,
            rev_date=rev_date,
            url=url,
            remarks=remarks,
            remarks_c=remarks_c,
            nsa_id=nsa_id,
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
