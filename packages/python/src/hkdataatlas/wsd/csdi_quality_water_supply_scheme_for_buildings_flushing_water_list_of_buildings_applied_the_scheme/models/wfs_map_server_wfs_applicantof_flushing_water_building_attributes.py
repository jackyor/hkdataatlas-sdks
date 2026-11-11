from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsApplicantofFlushingWaterBuildingAttributes")


@_attrs_define
class WfsMapServerWfsApplicantofFlushingWaterBuildingAttributes:
    """
    Attributes:
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
        name (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        name_chinese (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        address (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        address_chinese (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        applicant (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        applicant_chinese (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        district (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        district_chinese (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
    """

    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    name: None | str | Unset = UNSET
    name_chinese: None | str | Unset = UNSET
    address: None | str | Unset = UNSET
    address_chinese: None | str | Unset = UNSET
    applicant: None | str | Unset = UNSET
    applicant_chinese: None | str | Unset = UNSET
    district: None | str | Unset = UNSET
    district_chinese: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        shape = self.shape

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        name_chinese: None | str | Unset
        if isinstance(self.name_chinese, Unset):
            name_chinese = UNSET
        else:
            name_chinese = self.name_chinese

        address: None | str | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        address_chinese: None | str | Unset
        if isinstance(self.address_chinese, Unset):
            address_chinese = UNSET
        else:
            address_chinese = self.address_chinese

        applicant: None | str | Unset
        if isinstance(self.applicant, Unset):
            applicant = UNSET
        else:
            applicant = self.applicant

        applicant_chinese: None | str | Unset
        if isinstance(self.applicant_chinese, Unset):
            applicant_chinese = UNSET
        else:
            applicant_chinese = self.applicant_chinese

        district: None | str | Unset
        if isinstance(self.district, Unset):
            district = UNSET
        else:
            district = self.district

        district_chinese: None | str | Unset
        if isinstance(self.district_chinese, Unset):
            district_chinese = UNSET
        else:
            district_chinese = self.district_chinese

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["Shape"] = shape
        if name is not UNSET:
            field_dict["NAME"] = name
        if name_chinese is not UNSET:
            field_dict["NAME_CHINESE"] = name_chinese
        if address is not UNSET:
            field_dict["ADDRESS"] = address
        if address_chinese is not UNSET:
            field_dict["ADDRESS_CHINESE"] = address_chinese
        if applicant is not UNSET:
            field_dict["APPLICANT"] = applicant
        if applicant_chinese is not UNSET:
            field_dict["APPLICANT_CHINESE"] = applicant_chinese
        if district is not UNSET:
            field_dict["DISTRICT"] = district
        if district_chinese is not UNSET:
            field_dict["DISTRICT_CHINESE"] = district_chinese

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("Shape", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("NAME", UNSET))

        def _parse_name_chinese(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_chinese = _parse_name_chinese(d.pop("NAME_CHINESE", UNSET))

        def _parse_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address = _parse_address(d.pop("ADDRESS", UNSET))

        def _parse_address_chinese(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_chinese = _parse_address_chinese(d.pop("ADDRESS_CHINESE", UNSET))

        def _parse_applicant(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        applicant = _parse_applicant(d.pop("APPLICANT", UNSET))

        def _parse_applicant_chinese(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        applicant_chinese = _parse_applicant_chinese(d.pop("APPLICANT_CHINESE", UNSET))

        def _parse_district(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district = _parse_district(d.pop("DISTRICT", UNSET))

        def _parse_district_chinese(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_chinese = _parse_district_chinese(d.pop("DISTRICT_CHINESE", UNSET))

        wfs_map_server_wfs_applicantof_flushing_water_building_attributes = cls(
            objectid=objectid,
            shape=shape,
            name=name,
            name_chinese=name_chinese,
            address=address,
            address_chinese=address_chinese,
            applicant=applicant,
            applicant_chinese=applicant_chinese,
            district=district,
            district_chinese=district_chinese,
        )

        wfs_map_server_wfs_applicantof_flushing_water_building_attributes.additional_properties = d
        return wfs_map_server_wfs_applicantof_flushing_water_building_attributes

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
