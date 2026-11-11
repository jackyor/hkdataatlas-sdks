from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsDTADTSPOLELINEAttributes")


@_attrs_define
class WfsMapServerWfsDTADTSPOLELINEAttributes:
    """
    Attributes:
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:MultiCurvePropertyType; JSON geometry is not inferred from its
            XML type.
        refname (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        featureid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all
            JSON queries.
        completion_date (None | str | Unset): Native XSD type xsd:dateTime. Requiredness is not projected from XML
            occurrence into all JSON queries.
        gazette_date (None | str | Unset): Native XSD type xsd:dateTime. Requiredness is not projected from XML
            occurrence into all JSON queries.
        last_upd_date (str | Unset): Native XSD type xsd:dateTime. Requiredness is not projected from XML occurrence
            into all JSON queries.
        elevation (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        gg_name (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        poleid (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        type_ (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape_length (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
    """

    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    refname: None | str | Unset = UNSET
    featureid: int | Unset = UNSET
    completion_date: None | str | Unset = UNSET
    gazette_date: None | str | Unset = UNSET
    last_upd_date: str | Unset = UNSET
    elevation: None | str | Unset = UNSET
    gg_name: None | str | Unset = UNSET
    poleid: None | str | Unset = UNSET
    type_: None | str | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        shape = self.shape

        refname: None | str | Unset
        if isinstance(self.refname, Unset):
            refname = UNSET
        else:
            refname = self.refname

        featureid = self.featureid

        completion_date: None | str | Unset
        if isinstance(self.completion_date, Unset):
            completion_date = UNSET
        else:
            completion_date = self.completion_date

        gazette_date: None | str | Unset
        if isinstance(self.gazette_date, Unset):
            gazette_date = UNSET
        else:
            gazette_date = self.gazette_date

        last_upd_date = self.last_upd_date

        elevation: None | str | Unset
        if isinstance(self.elevation, Unset):
            elevation = UNSET
        else:
            elevation = self.elevation

        gg_name: None | str | Unset
        if isinstance(self.gg_name, Unset):
            gg_name = UNSET
        else:
            gg_name = self.gg_name

        poleid: None | str | Unset
        if isinstance(self.poleid, Unset):
            poleid = UNSET
        else:
            poleid = self.poleid

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

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
        if refname is not UNSET:
            field_dict["REFNAME"] = refname
        if featureid is not UNSET:
            field_dict["FEATUREID"] = featureid
        if completion_date is not UNSET:
            field_dict["COMPLETION_DATE"] = completion_date
        if gazette_date is not UNSET:
            field_dict["GAZETTE_DATE"] = gazette_date
        if last_upd_date is not UNSET:
            field_dict["LAST_UPD_DATE"] = last_upd_date
        if elevation is not UNSET:
            field_dict["ELEVATION"] = elevation
        if gg_name is not UNSET:
            field_dict["GG_NAME"] = gg_name
        if poleid is not UNSET:
            field_dict["POLEID"] = poleid
        if type_ is not UNSET:
            field_dict["TYPE"] = type_
        if shape_length is not UNSET:
            field_dict["SHAPE_Length"] = shape_length

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("SHAPE", UNSET)

        def _parse_refname(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        refname = _parse_refname(d.pop("REFNAME", UNSET))

        featureid = d.pop("FEATUREID", UNSET)

        def _parse_completion_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        completion_date = _parse_completion_date(d.pop("COMPLETION_DATE", UNSET))

        def _parse_gazette_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gazette_date = _parse_gazette_date(d.pop("GAZETTE_DATE", UNSET))

        last_upd_date = d.pop("LAST_UPD_DATE", UNSET)

        def _parse_elevation(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        elevation = _parse_elevation(d.pop("ELEVATION", UNSET))

        def _parse_gg_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gg_name = _parse_gg_name(d.pop("GG_NAME", UNSET))

        def _parse_poleid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        poleid = _parse_poleid(d.pop("POLEID", UNSET))

        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("TYPE", UNSET))

        def _parse_shape_length(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_length = _parse_shape_length(d.pop("SHAPE_Length", UNSET))

        wfs_map_server_wfs_dtadtspoleline_attributes = cls(
            objectid=objectid,
            shape=shape,
            refname=refname,
            featureid=featureid,
            completion_date=completion_date,
            gazette_date=gazette_date,
            last_upd_date=last_upd_date,
            elevation=elevation,
            gg_name=gg_name,
            poleid=poleid,
            type_=type_,
            shape_length=shape_length,
        )

        wfs_map_server_wfs_dtadtspoleline_attributes.additional_properties = d
        return wfs_map_server_wfs_dtadtspoleline_attributes

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
