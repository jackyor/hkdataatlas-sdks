from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsLPGFillingStationsAttributes")


@_attrs_define
class WfsMapServerWfsLPGFillingStationsAttributes:
    """
    Attributes:
        company_english (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        company_traditional_chinese (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        dedicated_site_english (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        dedicated_site_traditional_chinese (None | str | Unset): Native XSD type . Requiredness is not projected from
            XML occurrence into all JSON queries.
        district_english (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        district_traditional_chinese (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        location_english (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        location_traditional_chinese (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        sequence_no (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        telephone_no (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
    """

    company_english: None | str | Unset = UNSET
    company_traditional_chinese: None | str | Unset = UNSET
    dedicated_site_english: None | str | Unset = UNSET
    dedicated_site_traditional_chinese: None | str | Unset = UNSET
    district_english: None | str | Unset = UNSET
    district_traditional_chinese: None | str | Unset = UNSET
    location_english: None | str | Unset = UNSET
    location_traditional_chinese: None | str | Unset = UNSET
    sequence_no: float | None | Unset = UNSET
    telephone_no: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company_english: None | str | Unset
        if isinstance(self.company_english, Unset):
            company_english = UNSET
        else:
            company_english = self.company_english

        company_traditional_chinese: None | str | Unset
        if isinstance(self.company_traditional_chinese, Unset):
            company_traditional_chinese = UNSET
        else:
            company_traditional_chinese = self.company_traditional_chinese

        dedicated_site_english: None | str | Unset
        if isinstance(self.dedicated_site_english, Unset):
            dedicated_site_english = UNSET
        else:
            dedicated_site_english = self.dedicated_site_english

        dedicated_site_traditional_chinese: None | str | Unset
        if isinstance(self.dedicated_site_traditional_chinese, Unset):
            dedicated_site_traditional_chinese = UNSET
        else:
            dedicated_site_traditional_chinese = self.dedicated_site_traditional_chinese

        district_english: None | str | Unset
        if isinstance(self.district_english, Unset):
            district_english = UNSET
        else:
            district_english = self.district_english

        district_traditional_chinese: None | str | Unset
        if isinstance(self.district_traditional_chinese, Unset):
            district_traditional_chinese = UNSET
        else:
            district_traditional_chinese = self.district_traditional_chinese

        location_english: None | str | Unset
        if isinstance(self.location_english, Unset):
            location_english = UNSET
        else:
            location_english = self.location_english

        location_traditional_chinese: None | str | Unset
        if isinstance(self.location_traditional_chinese, Unset):
            location_traditional_chinese = UNSET
        else:
            location_traditional_chinese = self.location_traditional_chinese

        sequence_no: float | None | Unset
        if isinstance(self.sequence_no, Unset):
            sequence_no = UNSET
        else:
            sequence_no = self.sequence_no

        telephone_no: None | str | Unset
        if isinstance(self.telephone_no, Unset):
            telephone_no = UNSET
        else:
            telephone_no = self.telephone_no

        objectid = self.objectid

        shape = self.shape

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if company_english is not UNSET:
            field_dict["Company_English"] = company_english
        if company_traditional_chinese is not UNSET:
            field_dict["Company_Traditional_Chinese"] = company_traditional_chinese
        if dedicated_site_english is not UNSET:
            field_dict["Dedicated_Site_English"] = dedicated_site_english
        if dedicated_site_traditional_chinese is not UNSET:
            field_dict["Dedicated_Site_Traditional_Chinese"] = (
                dedicated_site_traditional_chinese
            )
        if district_english is not UNSET:
            field_dict["District_English"] = district_english
        if district_traditional_chinese is not UNSET:
            field_dict["District_Traditional_Chinese"] = district_traditional_chinese
        if location_english is not UNSET:
            field_dict["Location_English"] = location_english
        if location_traditional_chinese is not UNSET:
            field_dict["Location_Traditional_Chinese"] = location_traditional_chinese
        if sequence_no is not UNSET:
            field_dict["Sequence_No"] = sequence_no
        if telephone_no is not UNSET:
            field_dict["Telephone_No"] = telephone_no
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["SHAPE"] = shape

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_company_english(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_english = _parse_company_english(d.pop("Company_English", UNSET))

        def _parse_company_traditional_chinese(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_traditional_chinese = _parse_company_traditional_chinese(
            d.pop("Company_Traditional_Chinese", UNSET)
        )

        def _parse_dedicated_site_english(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dedicated_site_english = _parse_dedicated_site_english(
            d.pop("Dedicated_Site_English", UNSET)
        )

        def _parse_dedicated_site_traditional_chinese(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dedicated_site_traditional_chinese = _parse_dedicated_site_traditional_chinese(
            d.pop("Dedicated_Site_Traditional_Chinese", UNSET)
        )

        def _parse_district_english(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_english = _parse_district_english(d.pop("District_English", UNSET))

        def _parse_district_traditional_chinese(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_traditional_chinese = _parse_district_traditional_chinese(
            d.pop("District_Traditional_Chinese", UNSET)
        )

        def _parse_location_english(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_english = _parse_location_english(d.pop("Location_English", UNSET))

        def _parse_location_traditional_chinese(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_traditional_chinese = _parse_location_traditional_chinese(
            d.pop("Location_Traditional_Chinese", UNSET)
        )

        def _parse_sequence_no(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        sequence_no = _parse_sequence_no(d.pop("Sequence_No", UNSET))

        def _parse_telephone_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        telephone_no = _parse_telephone_no(d.pop("Telephone_No", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("SHAPE", UNSET)

        wfs_map_server_wfs_lpg_filling_stations_attributes = cls(
            company_english=company_english,
            company_traditional_chinese=company_traditional_chinese,
            dedicated_site_english=dedicated_site_english,
            dedicated_site_traditional_chinese=dedicated_site_traditional_chinese,
            district_english=district_english,
            district_traditional_chinese=district_traditional_chinese,
            location_english=location_english,
            location_traditional_chinese=location_traditional_chinese,
            sequence_no=sequence_no,
            telephone_no=telephone_no,
            objectid=objectid,
            shape=shape,
        )

        wfs_map_server_wfs_lpg_filling_stations_attributes.additional_properties = d
        return wfs_map_server_wfs_lpg_filling_stations_attributes

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
