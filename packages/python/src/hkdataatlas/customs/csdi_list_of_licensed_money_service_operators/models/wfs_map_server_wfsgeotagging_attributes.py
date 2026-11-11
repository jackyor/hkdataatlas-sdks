from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsgeotaggingAttributes")


@_attrs_define
class WfsMapServerWfsgeotaggingAttributes:
    """
    Attributes:
        address_english_only (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        address_type_chinese (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        address_type_english (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        as_at_date (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        branch_name_chinese (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        branch_name_english (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        name_of_licensee_chinese (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        name_of_licensee_english (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        latitude (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        longitude (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
    """

    address_english_only: None | str | Unset = UNSET
    address_type_chinese: None | str | Unset = UNSET
    address_type_english: None | str | Unset = UNSET
    as_at_date: None | str | Unset = UNSET
    branch_name_chinese: None | str | Unset = UNSET
    branch_name_english: None | str | Unset = UNSET
    name_of_licensee_chinese: None | str | Unset = UNSET
    name_of_licensee_english: None | str | Unset = UNSET
    latitude: float | None | Unset = UNSET
    longitude: float | None | Unset = UNSET
    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address_english_only: None | str | Unset
        if isinstance(self.address_english_only, Unset):
            address_english_only = UNSET
        else:
            address_english_only = self.address_english_only

        address_type_chinese: None | str | Unset
        if isinstance(self.address_type_chinese, Unset):
            address_type_chinese = UNSET
        else:
            address_type_chinese = self.address_type_chinese

        address_type_english: None | str | Unset
        if isinstance(self.address_type_english, Unset):
            address_type_english = UNSET
        else:
            address_type_english = self.address_type_english

        as_at_date: None | str | Unset
        if isinstance(self.as_at_date, Unset):
            as_at_date = UNSET
        else:
            as_at_date = self.as_at_date

        branch_name_chinese: None | str | Unset
        if isinstance(self.branch_name_chinese, Unset):
            branch_name_chinese = UNSET
        else:
            branch_name_chinese = self.branch_name_chinese

        branch_name_english: None | str | Unset
        if isinstance(self.branch_name_english, Unset):
            branch_name_english = UNSET
        else:
            branch_name_english = self.branch_name_english

        name_of_licensee_chinese: None | str | Unset
        if isinstance(self.name_of_licensee_chinese, Unset):
            name_of_licensee_chinese = UNSET
        else:
            name_of_licensee_chinese = self.name_of_licensee_chinese

        name_of_licensee_english: None | str | Unset
        if isinstance(self.name_of_licensee_english, Unset):
            name_of_licensee_english = UNSET
        else:
            name_of_licensee_english = self.name_of_licensee_english

        latitude: float | None | Unset
        if isinstance(self.latitude, Unset):
            latitude = UNSET
        else:
            latitude = self.latitude

        longitude: float | None | Unset
        if isinstance(self.longitude, Unset):
            longitude = UNSET
        else:
            longitude = self.longitude

        objectid = self.objectid

        shape = self.shape

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address_english_only is not UNSET:
            field_dict["Address_English_only"] = address_english_only
        if address_type_chinese is not UNSET:
            field_dict["Address_Type_Chinese"] = address_type_chinese
        if address_type_english is not UNSET:
            field_dict["Address_Type_English"] = address_type_english
        if as_at_date is not UNSET:
            field_dict["As_at_Date"] = as_at_date
        if branch_name_chinese is not UNSET:
            field_dict["Branch_Name_Chinese"] = branch_name_chinese
        if branch_name_english is not UNSET:
            field_dict["Branch_Name_English"] = branch_name_english
        if name_of_licensee_chinese is not UNSET:
            field_dict["Name_of_Licensee_Chinese"] = name_of_licensee_chinese
        if name_of_licensee_english is not UNSET:
            field_dict["Name_of_Licensee_English"] = name_of_licensee_english
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["SHAPE"] = shape

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_address_english_only(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_english_only = _parse_address_english_only(
            d.pop("Address_English_only", UNSET)
        )

        def _parse_address_type_chinese(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_type_chinese = _parse_address_type_chinese(
            d.pop("Address_Type_Chinese", UNSET)
        )

        def _parse_address_type_english(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_type_english = _parse_address_type_english(
            d.pop("Address_Type_English", UNSET)
        )

        def _parse_as_at_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        as_at_date = _parse_as_at_date(d.pop("As_at_Date", UNSET))

        def _parse_branch_name_chinese(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        branch_name_chinese = _parse_branch_name_chinese(
            d.pop("Branch_Name_Chinese", UNSET)
        )

        def _parse_branch_name_english(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        branch_name_english = _parse_branch_name_english(
            d.pop("Branch_Name_English", UNSET)
        )

        def _parse_name_of_licensee_chinese(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_of_licensee_chinese = _parse_name_of_licensee_chinese(
            d.pop("Name_of_Licensee_Chinese", UNSET)
        )

        def _parse_name_of_licensee_english(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_of_licensee_english = _parse_name_of_licensee_english(
            d.pop("Name_of_Licensee_English", UNSET)
        )

        def _parse_latitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        latitude = _parse_latitude(d.pop("latitude", UNSET))

        def _parse_longitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        longitude = _parse_longitude(d.pop("longitude", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("SHAPE", UNSET)

        wfs_map_server_wfsgeotagging_attributes = cls(
            address_english_only=address_english_only,
            address_type_chinese=address_type_chinese,
            address_type_english=address_type_english,
            as_at_date=as_at_date,
            branch_name_chinese=branch_name_chinese,
            branch_name_english=branch_name_english,
            name_of_licensee_chinese=name_of_licensee_chinese,
            name_of_licensee_english=name_of_licensee_english,
            latitude=latitude,
            longitude=longitude,
            objectid=objectid,
            shape=shape,
        )

        wfs_map_server_wfsgeotagging_attributes.additional_properties = d
        return wfs_map_server_wfsgeotagging_attributes

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
