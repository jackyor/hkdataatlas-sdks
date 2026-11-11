from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsRoadCentreLineAttributes")


@_attrs_define
class WfsMapServerWfsRoadCentreLineAttributes:
    """
    Attributes:
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:MultiCurvePropertyType; JSON geometry is not inferred from its
            XML type.
        streetcentrelineid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence
            into all JSON queries.
        streetcode (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all
            JSON queries.
        streettype (str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        englishstreetname (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        chinesestreetname (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        lastupdatedate (str | Unset): Native XSD type xsd:dateTime. Requiredness is not projected from XML occurrence
            into all JSON queries.
        shape_length (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
    """

    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    streetcentrelineid: int | Unset = UNSET
    streetcode: int | Unset = UNSET
    streettype: str | Unset = UNSET
    englishstreetname: None | str | Unset = UNSET
    chinesestreetname: None | str | Unset = UNSET
    lastupdatedate: str | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        shape = self.shape

        streetcentrelineid = self.streetcentrelineid

        streetcode = self.streetcode

        streettype = self.streettype

        englishstreetname: None | str | Unset
        if isinstance(self.englishstreetname, Unset):
            englishstreetname = UNSET
        else:
            englishstreetname = self.englishstreetname

        chinesestreetname: None | str | Unset
        if isinstance(self.chinesestreetname, Unset):
            chinesestreetname = UNSET
        else:
            chinesestreetname = self.chinesestreetname

        lastupdatedate = self.lastupdatedate

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
        if streetcentrelineid is not UNSET:
            field_dict["STREETCENTRELINEID"] = streetcentrelineid
        if streetcode is not UNSET:
            field_dict["STREETCODE"] = streetcode
        if streettype is not UNSET:
            field_dict["STREETTYPE"] = streettype
        if englishstreetname is not UNSET:
            field_dict["ENGLISHSTREETNAME"] = englishstreetname
        if chinesestreetname is not UNSET:
            field_dict["CHINESESTREETNAME"] = chinesestreetname
        if lastupdatedate is not UNSET:
            field_dict["LASTUPDATEDATE"] = lastupdatedate
        if shape_length is not UNSET:
            field_dict["SHAPE_Length"] = shape_length

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("SHAPE", UNSET)

        streetcentrelineid = d.pop("STREETCENTRELINEID", UNSET)

        streetcode = d.pop("STREETCODE", UNSET)

        streettype = d.pop("STREETTYPE", UNSET)

        def _parse_englishstreetname(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        englishstreetname = _parse_englishstreetname(d.pop("ENGLISHSTREETNAME", UNSET))

        def _parse_chinesestreetname(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        chinesestreetname = _parse_chinesestreetname(d.pop("CHINESESTREETNAME", UNSET))

        lastupdatedate = d.pop("LASTUPDATEDATE", UNSET)

        def _parse_shape_length(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_length = _parse_shape_length(d.pop("SHAPE_Length", UNSET))

        wfs_map_server_wfs_road_centre_line_attributes = cls(
            objectid=objectid,
            shape=shape,
            streetcentrelineid=streetcentrelineid,
            streetcode=streetcode,
            streettype=streettype,
            englishstreetname=englishstreetname,
            chinesestreetname=chinesestreetname,
            lastupdatedate=lastupdatedate,
            shape_length=shape_length,
        )

        wfs_map_server_wfs_road_centre_line_attributes.additional_properties = d
        return wfs_map_server_wfs_road_centre_line_attributes

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
