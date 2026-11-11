from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsTable8BAttributes")


@_attrs_define
class WfsMapServerWfsTable8BAttributes:
    """
    Attributes:
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        aa_code (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        aa_title (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        low_rent_owner_occupier (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from
            XML occurrence into all JSON queries.
        good_ib_condition_management (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected
            from XML occurrence into all JSON queries.
        good_facility_transport (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from
            XML occurrence into all JSON queries.
        no_alternative_location (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from
            XML occurrence into all JSON queries.
        others (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        no_decision_yet (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
    """

    objectid: int | Unset = UNSET
    aa_code: None | str | Unset = UNSET
    aa_title: None | str | Unset = UNSET
    low_rent_owner_occupier: float | None | Unset = UNSET
    good_ib_condition_management: float | None | Unset = UNSET
    good_facility_transport: float | None | Unset = UNSET
    no_alternative_location: float | None | Unset = UNSET
    others: float | None | Unset = UNSET
    no_decision_yet: float | None | Unset = UNSET
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

        low_rent_owner_occupier: float | None | Unset
        if isinstance(self.low_rent_owner_occupier, Unset):
            low_rent_owner_occupier = UNSET
        else:
            low_rent_owner_occupier = self.low_rent_owner_occupier

        good_ib_condition_management: float | None | Unset
        if isinstance(self.good_ib_condition_management, Unset):
            good_ib_condition_management = UNSET
        else:
            good_ib_condition_management = self.good_ib_condition_management

        good_facility_transport: float | None | Unset
        if isinstance(self.good_facility_transport, Unset):
            good_facility_transport = UNSET
        else:
            good_facility_transport = self.good_facility_transport

        no_alternative_location: float | None | Unset
        if isinstance(self.no_alternative_location, Unset):
            no_alternative_location = UNSET
        else:
            no_alternative_location = self.no_alternative_location

        others: float | None | Unset
        if isinstance(self.others, Unset):
            others = UNSET
        else:
            others = self.others

        no_decision_yet: float | None | Unset
        if isinstance(self.no_decision_yet, Unset):
            no_decision_yet = UNSET
        else:
            no_decision_yet = self.no_decision_yet

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if aa_code is not UNSET:
            field_dict["AA_Code"] = aa_code
        if aa_title is not UNSET:
            field_dict["AA_Title"] = aa_title
        if low_rent_owner_occupier is not UNSET:
            field_dict["Low_rent_Owner_occupier"] = low_rent_owner_occupier
        if good_ib_condition_management is not UNSET:
            field_dict["Good_IB_condition_management"] = good_ib_condition_management
        if good_facility_transport is not UNSET:
            field_dict["Good_facility_transport"] = good_facility_transport
        if no_alternative_location is not UNSET:
            field_dict["No_alternative_location"] = no_alternative_location
        if others is not UNSET:
            field_dict["Others_"] = others
        if no_decision_yet is not UNSET:
            field_dict["No_decision_yet"] = no_decision_yet

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

        def _parse_low_rent_owner_occupier(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        low_rent_owner_occupier = _parse_low_rent_owner_occupier(
            d.pop("Low_rent_Owner_occupier", UNSET)
        )

        def _parse_good_ib_condition_management(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        good_ib_condition_management = _parse_good_ib_condition_management(
            d.pop("Good_IB_condition_management", UNSET)
        )

        def _parse_good_facility_transport(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        good_facility_transport = _parse_good_facility_transport(
            d.pop("Good_facility_transport", UNSET)
        )

        def _parse_no_alternative_location(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        no_alternative_location = _parse_no_alternative_location(
            d.pop("No_alternative_location", UNSET)
        )

        def _parse_others(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        others = _parse_others(d.pop("Others_", UNSET))

        def _parse_no_decision_yet(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        no_decision_yet = _parse_no_decision_yet(d.pop("No_decision_yet", UNSET))

        wfs_map_server_wfs_table_8b_attributes = cls(
            objectid=objectid,
            aa_code=aa_code,
            aa_title=aa_title,
            low_rent_owner_occupier=low_rent_owner_occupier,
            good_ib_condition_management=good_ib_condition_management,
            good_facility_transport=good_facility_transport,
            no_alternative_location=no_alternative_location,
            others=others,
            no_decision_yet=no_decision_yet,
        )

        wfs_map_server_wfs_table_8b_attributes.additional_properties = d
        return wfs_map_server_wfs_table_8b_attributes

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
