from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsUsePermitofLiftsAttributes")


@_attrs_define
class WfsMapServerWfsUsePermitofLiftsAttributes:
    """
    Attributes:
        address_chinese (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        address_english (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        date_of_expiry (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        date_of_issue (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        lift_no (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        location_id (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
    """

    address_chinese: None | str | Unset = UNSET
    address_english: None | str | Unset = UNSET
    date_of_expiry: None | str | Unset = UNSET
    date_of_issue: None | str | Unset = UNSET
    lift_no: None | str | Unset = UNSET
    location_id: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address_chinese: None | str | Unset
        if isinstance(self.address_chinese, Unset):
            address_chinese = UNSET
        else:
            address_chinese = self.address_chinese

        address_english: None | str | Unset
        if isinstance(self.address_english, Unset):
            address_english = UNSET
        else:
            address_english = self.address_english

        date_of_expiry: None | str | Unset
        if isinstance(self.date_of_expiry, Unset):
            date_of_expiry = UNSET
        else:
            date_of_expiry = self.date_of_expiry

        date_of_issue: None | str | Unset
        if isinstance(self.date_of_issue, Unset):
            date_of_issue = UNSET
        else:
            date_of_issue = self.date_of_issue

        lift_no: None | str | Unset
        if isinstance(self.lift_no, Unset):
            lift_no = UNSET
        else:
            lift_no = self.lift_no

        location_id: None | str | Unset
        if isinstance(self.location_id, Unset):
            location_id = UNSET
        else:
            location_id = self.location_id

        objectid = self.objectid

        shape = self.shape

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address_chinese is not UNSET:
            field_dict["Address_Chinese"] = address_chinese
        if address_english is not UNSET:
            field_dict["Address_English"] = address_english
        if date_of_expiry is not UNSET:
            field_dict["Date_of_Expiry"] = date_of_expiry
        if date_of_issue is not UNSET:
            field_dict["Date_of_Issue"] = date_of_issue
        if lift_no is not UNSET:
            field_dict["Lift_No"] = lift_no
        if location_id is not UNSET:
            field_dict["Location_ID"] = location_id
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["SHAPE"] = shape

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_address_chinese(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_chinese = _parse_address_chinese(d.pop("Address_Chinese", UNSET))

        def _parse_address_english(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_english = _parse_address_english(d.pop("Address_English", UNSET))

        def _parse_date_of_expiry(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date_of_expiry = _parse_date_of_expiry(d.pop("Date_of_Expiry", UNSET))

        def _parse_date_of_issue(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date_of_issue = _parse_date_of_issue(d.pop("Date_of_Issue", UNSET))

        def _parse_lift_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lift_no = _parse_lift_no(d.pop("Lift_No", UNSET))

        def _parse_location_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_id = _parse_location_id(d.pop("Location_ID", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("SHAPE", UNSET)

        wfs_map_server_wfs_use_permitof_lifts_attributes = cls(
            address_chinese=address_chinese,
            address_english=address_english,
            date_of_expiry=date_of_expiry,
            date_of_issue=date_of_issue,
            lift_no=lift_no,
            location_id=location_id,
            objectid=objectid,
            shape=shape,
        )

        wfs_map_server_wfs_use_permitof_lifts_attributes.additional_properties = d
        return wfs_map_server_wfs_use_permitof_lifts_attributes

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
