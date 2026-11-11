from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsOPAttributes")


@_attrs_define
class WfsMapServerWfsOPAttributes:
    """
    Attributes:
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        op_no (str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON queries.
        op_date (None | str | Unset): Native XSD type xsd:dateTime. Requiredness is not projected from XML occurrence
            into all JSON queries.
        domestic_gfa (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        non_domestic_gfa (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        gfa (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence into
            all JSON queries.
    """

    objectid: int | Unset = UNSET
    op_no: str | Unset = UNSET
    op_date: None | str | Unset = UNSET
    domestic_gfa: float | None | Unset = UNSET
    non_domestic_gfa: float | None | Unset = UNSET
    gfa: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        op_no = self.op_no

        op_date: None | str | Unset
        if isinstance(self.op_date, Unset):
            op_date = UNSET
        else:
            op_date = self.op_date

        domestic_gfa: float | None | Unset
        if isinstance(self.domestic_gfa, Unset):
            domestic_gfa = UNSET
        else:
            domestic_gfa = self.domestic_gfa

        non_domestic_gfa: float | None | Unset
        if isinstance(self.non_domestic_gfa, Unset):
            non_domestic_gfa = UNSET
        else:
            non_domestic_gfa = self.non_domestic_gfa

        gfa: float | None | Unset
        if isinstance(self.gfa, Unset):
            gfa = UNSET
        else:
            gfa = self.gfa

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if op_no is not UNSET:
            field_dict["OPNo"] = op_no
        if op_date is not UNSET:
            field_dict["OPDate"] = op_date
        if domestic_gfa is not UNSET:
            field_dict["DomesticGFA"] = domestic_gfa
        if non_domestic_gfa is not UNSET:
            field_dict["NonDomesticGFA"] = non_domestic_gfa
        if gfa is not UNSET:
            field_dict["GFA"] = gfa

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        op_no = d.pop("OPNo", UNSET)

        def _parse_op_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        op_date = _parse_op_date(d.pop("OPDate", UNSET))

        def _parse_domestic_gfa(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        domestic_gfa = _parse_domestic_gfa(d.pop("DomesticGFA", UNSET))

        def _parse_non_domestic_gfa(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        non_domestic_gfa = _parse_non_domestic_gfa(d.pop("NonDomesticGFA", UNSET))

        def _parse_gfa(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        gfa = _parse_gfa(d.pop("GFA", UNSET))

        wfs_map_server_wfs_op_attributes = cls(
            objectid=objectid,
            op_no=op_no,
            op_date=op_date,
            domestic_gfa=domestic_gfa,
            non_domestic_gfa=non_domestic_gfa,
            gfa=gfa,
        )

        wfs_map_server_wfs_op_attributes.additional_properties = d
        return wfs_map_server_wfs_op_attributes

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
