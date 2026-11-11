from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsDTADRUNINOUTLINEAttributes")


@_attrs_define
class WfsMapServerWfsDTADRUNINOUTLINEAttributes:
    """
    Attributes:
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:MultiCurvePropertyType; JSON geometry is not inferred from its
            XML type.
        last_upd_date (str | Unset): Native XSD type xsd:dateTime. Requiredness is not projected from XML occurrence
            into all JSON queries.
        type_ (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        elevation (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        refname (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        gazette_date (None | str | Unset): Native XSD type xsd:dateTime. Requiredness is not projected from XML
            occurrence into all JSON queries.
        featureid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all
            JSON queries.
        shape_length (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
    """

    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    last_upd_date: str | Unset = UNSET
    type_: None | str | Unset = UNSET
    elevation: None | str | Unset = UNSET
    refname: None | str | Unset = UNSET
    gazette_date: None | str | Unset = UNSET
    featureid: int | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        shape = self.shape

        last_upd_date = self.last_upd_date

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        elevation: None | str | Unset
        if isinstance(self.elevation, Unset):
            elevation = UNSET
        else:
            elevation = self.elevation

        refname: None | str | Unset
        if isinstance(self.refname, Unset):
            refname = UNSET
        else:
            refname = self.refname

        gazette_date: None | str | Unset
        if isinstance(self.gazette_date, Unset):
            gazette_date = UNSET
        else:
            gazette_date = self.gazette_date

        featureid = self.featureid

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
        if shape is not UNSET:
            field_dict["SHAPE"] = shape
        if last_upd_date is not UNSET:
            field_dict["LAST_UPD_DATE"] = last_upd_date
        if type_ is not UNSET:
            field_dict["TYPE"] = type_
        if elevation is not UNSET:
            field_dict["ELEVATION"] = elevation
        if refname is not UNSET:
            field_dict["REFNAME"] = refname
        if gazette_date is not UNSET:
            field_dict["GAZETTE_DATE"] = gazette_date
        if featureid is not UNSET:
            field_dict["FEATUREID"] = featureid
        if shape_length is not UNSET:
            field_dict["SHAPE_Length"] = shape_length

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("SHAPE", UNSET)

        last_upd_date = d.pop("LAST_UPD_DATE", UNSET)

        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("TYPE", UNSET))

        def _parse_elevation(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        elevation = _parse_elevation(d.pop("ELEVATION", UNSET))

        def _parse_refname(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        refname = _parse_refname(d.pop("REFNAME", UNSET))

        def _parse_gazette_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gazette_date = _parse_gazette_date(d.pop("GAZETTE_DATE", UNSET))

        featureid = d.pop("FEATUREID", UNSET)

        def _parse_shape_length(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_length = _parse_shape_length(d.pop("SHAPE_Length", UNSET))

        wfs_map_server_wfs_dtadruninoutline_attributes = cls(
            objectid=objectid,
            shape=shape,
            last_upd_date=last_upd_date,
            type_=type_,
            elevation=elevation,
            refname=refname,
            gazette_date=gazette_date,
            featureid=featureid,
            shape_length=shape_length,
        )

        wfs_map_server_wfs_dtadruninoutline_attributes.additional_properties = d
        return wfs_map_server_wfs_dtadruninoutline_attributes

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
