from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsTable2AAttributes")


@_attrs_define
class WfsMapServerWfsTable2AAttributes:
    """
    Attributes:
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        aa_code (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        aa_title (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        no_of_i_bs_before_1987 (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from
            XML occurrence into all JSON queries.
        gfa_in_i_bs_before_1987 (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from
            XML occurrence into all JSON queries.
        no_of_i_bs_in_after_1987 (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from
            XML occurrence into all JSON queries.
        gfa_in_i_bs_in_after_1987 (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from
            XML occurrence into all JSON queries.
    """

    objectid: int | Unset = UNSET
    aa_code: None | str | Unset = UNSET
    aa_title: None | str | Unset = UNSET
    no_of_i_bs_before_1987: float | None | Unset = UNSET
    gfa_in_i_bs_before_1987: float | None | Unset = UNSET
    no_of_i_bs_in_after_1987: float | None | Unset = UNSET
    gfa_in_i_bs_in_after_1987: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        aa_code: None | str | Unset
        if isinstance(self.aa_code, Unset):
            aa_code = UNSET
        else:
            aa_code = self.aa_code

        aa_title: None | str | Unset
        if isinstance(self.aa_title, Unset):
            aa_title = UNSET
        else:
            aa_title = self.aa_title

        no_of_i_bs_before_1987: float | None | Unset
        if isinstance(self.no_of_i_bs_before_1987, Unset):
            no_of_i_bs_before_1987 = UNSET
        else:
            no_of_i_bs_before_1987 = self.no_of_i_bs_before_1987

        gfa_in_i_bs_before_1987: float | None | Unset
        if isinstance(self.gfa_in_i_bs_before_1987, Unset):
            gfa_in_i_bs_before_1987 = UNSET
        else:
            gfa_in_i_bs_before_1987 = self.gfa_in_i_bs_before_1987

        no_of_i_bs_in_after_1987: float | None | Unset
        if isinstance(self.no_of_i_bs_in_after_1987, Unset):
            no_of_i_bs_in_after_1987 = UNSET
        else:
            no_of_i_bs_in_after_1987 = self.no_of_i_bs_in_after_1987

        gfa_in_i_bs_in_after_1987: float | None | Unset
        if isinstance(self.gfa_in_i_bs_in_after_1987, Unset):
            gfa_in_i_bs_in_after_1987 = UNSET
        else:
            gfa_in_i_bs_in_after_1987 = self.gfa_in_i_bs_in_after_1987

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if aa_code is not UNSET:
            field_dict["AA_Code"] = aa_code
        if aa_title is not UNSET:
            field_dict["AA_Title"] = aa_title
        if no_of_i_bs_before_1987 is not UNSET:
            field_dict["No_of_IBs_before_1987"] = no_of_i_bs_before_1987
        if gfa_in_i_bs_before_1987 is not UNSET:
            field_dict["GFA_in_IBs_before_1987"] = gfa_in_i_bs_before_1987
        if no_of_i_bs_in_after_1987 is not UNSET:
            field_dict["No_of_IBs_in_after_1987"] = no_of_i_bs_in_after_1987
        if gfa_in_i_bs_in_after_1987 is not UNSET:
            field_dict["GFA_in_IBs_in_after_1987"] = gfa_in_i_bs_in_after_1987

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_aa_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        aa_code = _parse_aa_code(d.pop("AA_Code", UNSET))

        def _parse_aa_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        aa_title = _parse_aa_title(d.pop("AA_Title", UNSET))

        def _parse_no_of_i_bs_before_1987(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        no_of_i_bs_before_1987 = _parse_no_of_i_bs_before_1987(
            d.pop("No_of_IBs_before_1987", UNSET)
        )

        def _parse_gfa_in_i_bs_before_1987(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        gfa_in_i_bs_before_1987 = _parse_gfa_in_i_bs_before_1987(
            d.pop("GFA_in_IBs_before_1987", UNSET)
        )

        def _parse_no_of_i_bs_in_after_1987(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        no_of_i_bs_in_after_1987 = _parse_no_of_i_bs_in_after_1987(
            d.pop("No_of_IBs_in_after_1987", UNSET)
        )

        def _parse_gfa_in_i_bs_in_after_1987(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        gfa_in_i_bs_in_after_1987 = _parse_gfa_in_i_bs_in_after_1987(
            d.pop("GFA_in_IBs_in_after_1987", UNSET)
        )

        wfs_map_server_wfs_table_2a_attributes = cls(
            objectid=objectid,
            aa_code=aa_code,
            aa_title=aa_title,
            no_of_i_bs_before_1987=no_of_i_bs_before_1987,
            gfa_in_i_bs_before_1987=gfa_in_i_bs_before_1987,
            no_of_i_bs_in_after_1987=no_of_i_bs_in_after_1987,
            gfa_in_i_bs_in_after_1987=gfa_in_i_bs_in_after_1987,
        )

        wfs_map_server_wfs_table_2a_attributes.additional_properties = d
        return wfs_map_server_wfs_table_2a_attributes

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
