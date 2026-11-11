from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsDTADRDMARKSYMPTAttributes")


@_attrs_define
class WfsMapServerWfsDTADRDMARKSYMPTAttributes:
    """
    Attributes:
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
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
        angle (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence into
            all JSON queries.
        elevation (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        symbol_size (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        ruleid (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all
            JSON queries.
        ruleid_1 (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into
            all JSON queries.
    """

    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    refname: None | str | Unset = UNSET
    featureid: int | Unset = UNSET
    completion_date: None | str | Unset = UNSET
    gazette_date: None | str | Unset = UNSET
    last_upd_date: str | Unset = UNSET
    angle: float | None | Unset = UNSET
    elevation: None | str | Unset = UNSET
    symbol_size: float | None | Unset = UNSET
    ruleid: int | None | Unset = UNSET
    ruleid_1: int | None | Unset = UNSET
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

        angle: float | None | Unset
        if isinstance(self.angle, Unset):
            angle = UNSET
        else:
            angle = self.angle

        elevation: None | str | Unset
        if isinstance(self.elevation, Unset):
            elevation = UNSET
        else:
            elevation = self.elevation

        symbol_size: float | None | Unset
        if isinstance(self.symbol_size, Unset):
            symbol_size = UNSET
        else:
            symbol_size = self.symbol_size

        ruleid: int | None | Unset
        if isinstance(self.ruleid, Unset):
            ruleid = UNSET
        else:
            ruleid = self.ruleid

        ruleid_1: int | None | Unset
        if isinstance(self.ruleid_1, Unset):
            ruleid_1 = UNSET
        else:
            ruleid_1 = self.ruleid_1

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
        if angle is not UNSET:
            field_dict["ANGLE"] = angle
        if elevation is not UNSET:
            field_dict["ELEVATION"] = elevation
        if symbol_size is not UNSET:
            field_dict["SYMBOL_SIZE"] = symbol_size
        if ruleid is not UNSET:
            field_dict["RULEID"] = ruleid
        if ruleid_1 is not UNSET:
            field_dict["RULEID_1"] = ruleid_1

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

        def _parse_angle(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        angle = _parse_angle(d.pop("ANGLE", UNSET))

        def _parse_elevation(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        elevation = _parse_elevation(d.pop("ELEVATION", UNSET))

        def _parse_symbol_size(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        symbol_size = _parse_symbol_size(d.pop("SYMBOL_SIZE", UNSET))

        def _parse_ruleid(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        ruleid = _parse_ruleid(d.pop("RULEID", UNSET))

        def _parse_ruleid_1(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        ruleid_1 = _parse_ruleid_1(d.pop("RULEID_1", UNSET))

        wfs_map_server_wfs_dtadrdmarksympt_attributes = cls(
            objectid=objectid,
            shape=shape,
            refname=refname,
            featureid=featureid,
            completion_date=completion_date,
            gazette_date=gazette_date,
            last_upd_date=last_upd_date,
            angle=angle,
            elevation=elevation,
            symbol_size=symbol_size,
            ruleid=ruleid,
            ruleid_1=ruleid_1,
        )

        wfs_map_server_wfs_dtadrdmarksympt_attributes.additional_properties = d
        return wfs_map_server_wfs_dtadrdmarksympt_attributes

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
