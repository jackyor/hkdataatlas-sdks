from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer0Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer0Attributes:
    """
    Attributes:
        company_name (None | str | Unset): Publisher field type: esriFieldTypeString
        company_name_chi (None | str | Unset): Publisher field type: esriFieldTypeString
        part_chi (None | str | Unset): Publisher field type: esriFieldTypeString
        part_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        premises_details_address_01 (None | str | Unset): Publisher field type: esriFieldTypeString
        premises_details_address_02 (None | str | Unset): Publisher field type: esriFieldTypeString
        premises_details_district (None | str | Unset): Publisher field type: esriFieldTypeString
        premises_details_latitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        premises_details_longitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        premises_details_part (None | str | Unset): Publisher field type: esriFieldTypeString
        premises_details_region (None | str | Unset): Publisher field type: esriFieldTypeString
        premises_details_type (None | str | Unset): Publisher field type: esriFieldTypeString
        type_chi (None | str | Unset): Publisher field type: esriFieldTypeString
        type_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    company_name: None | str | Unset = UNSET
    company_name_chi: None | str | Unset = UNSET
    part_chi: None | str | Unset = UNSET
    part_eng: None | str | Unset = UNSET
    premises_details_address_01: None | str | Unset = UNSET
    premises_details_address_02: None | str | Unset = UNSET
    premises_details_district: None | str | Unset = UNSET
    premises_details_latitude: float | None | Unset = UNSET
    premises_details_longitude: float | None | Unset = UNSET
    premises_details_part: None | str | Unset = UNSET
    premises_details_region: None | str | Unset = UNSET
    premises_details_type: None | str | Unset = UNSET
    type_chi: None | str | Unset = UNSET
    type_eng: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company_name: None | str | Unset
        if isinstance(self.company_name, Unset):
            company_name = UNSET
        else:
            company_name = self.company_name

        company_name_chi: None | str | Unset
        if isinstance(self.company_name_chi, Unset):
            company_name_chi = UNSET
        else:
            company_name_chi = self.company_name_chi

        part_chi: None | str | Unset
        if isinstance(self.part_chi, Unset):
            part_chi = UNSET
        else:
            part_chi = self.part_chi

        part_eng: None | str | Unset
        if isinstance(self.part_eng, Unset):
            part_eng = UNSET
        else:
            part_eng = self.part_eng

        premises_details_address_01: None | str | Unset
        if isinstance(self.premises_details_address_01, Unset):
            premises_details_address_01 = UNSET
        else:
            premises_details_address_01 = self.premises_details_address_01

        premises_details_address_02: None | str | Unset
        if isinstance(self.premises_details_address_02, Unset):
            premises_details_address_02 = UNSET
        else:
            premises_details_address_02 = self.premises_details_address_02

        premises_details_district: None | str | Unset
        if isinstance(self.premises_details_district, Unset):
            premises_details_district = UNSET
        else:
            premises_details_district = self.premises_details_district

        premises_details_latitude: float | None | Unset
        if isinstance(self.premises_details_latitude, Unset):
            premises_details_latitude = UNSET
        else:
            premises_details_latitude = self.premises_details_latitude

        premises_details_longitude: float | None | Unset
        if isinstance(self.premises_details_longitude, Unset):
            premises_details_longitude = UNSET
        else:
            premises_details_longitude = self.premises_details_longitude

        premises_details_part: None | str | Unset
        if isinstance(self.premises_details_part, Unset):
            premises_details_part = UNSET
        else:
            premises_details_part = self.premises_details_part

        premises_details_region: None | str | Unset
        if isinstance(self.premises_details_region, Unset):
            premises_details_region = UNSET
        else:
            premises_details_region = self.premises_details_region

        premises_details_type: None | str | Unset
        if isinstance(self.premises_details_type, Unset):
            premises_details_type = UNSET
        else:
            premises_details_type = self.premises_details_type

        type_chi: None | str | Unset
        if isinstance(self.type_chi, Unset):
            type_chi = UNSET
        else:
            type_chi = self.type_chi

        type_eng: None | str | Unset
        if isinstance(self.type_eng, Unset):
            type_eng = UNSET
        else:
            type_eng = self.type_eng

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if company_name is not UNSET:
            field_dict["CompanyName"] = company_name
        if company_name_chi is not UNSET:
            field_dict["CompanyNameChi"] = company_name_chi
        if part_chi is not UNSET:
            field_dict["PartChi"] = part_chi
        if part_eng is not UNSET:
            field_dict["PartEng"] = part_eng
        if premises_details_address_01 is not UNSET:
            field_dict["PremisesDetailsAddress01"] = premises_details_address_01
        if premises_details_address_02 is not UNSET:
            field_dict["PremisesDetailsAddress02"] = premises_details_address_02
        if premises_details_district is not UNSET:
            field_dict["PremisesDetailsDistrict"] = premises_details_district
        if premises_details_latitude is not UNSET:
            field_dict["PremisesDetailsLatitude"] = premises_details_latitude
        if premises_details_longitude is not UNSET:
            field_dict["PremisesDetailsLongitude"] = premises_details_longitude
        if premises_details_part is not UNSET:
            field_dict["PremisesDetailsPart"] = premises_details_part
        if premises_details_region is not UNSET:
            field_dict["PremisesDetailsRegion"] = premises_details_region
        if premises_details_type is not UNSET:
            field_dict["PremisesDetailsType"] = premises_details_type
        if type_chi is not UNSET:
            field_dict["TypeChi"] = type_chi
        if type_eng is not UNSET:
            field_dict["TypeEng"] = type_eng
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_company_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_name = _parse_company_name(d.pop("CompanyName", UNSET))

        def _parse_company_name_chi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_name_chi = _parse_company_name_chi(d.pop("CompanyNameChi", UNSET))

        def _parse_part_chi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        part_chi = _parse_part_chi(d.pop("PartChi", UNSET))

        def _parse_part_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        part_eng = _parse_part_eng(d.pop("PartEng", UNSET))

        def _parse_premises_details_address_01(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        premises_details_address_01 = _parse_premises_details_address_01(
            d.pop("PremisesDetailsAddress01", UNSET)
        )

        def _parse_premises_details_address_02(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        premises_details_address_02 = _parse_premises_details_address_02(
            d.pop("PremisesDetailsAddress02", UNSET)
        )

        def _parse_premises_details_district(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        premises_details_district = _parse_premises_details_district(
            d.pop("PremisesDetailsDistrict", UNSET)
        )

        def _parse_premises_details_latitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        premises_details_latitude = _parse_premises_details_latitude(
            d.pop("PremisesDetailsLatitude", UNSET)
        )

        def _parse_premises_details_longitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        premises_details_longitude = _parse_premises_details_longitude(
            d.pop("PremisesDetailsLongitude", UNSET)
        )

        def _parse_premises_details_part(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        premises_details_part = _parse_premises_details_part(
            d.pop("PremisesDetailsPart", UNSET)
        )

        def _parse_premises_details_region(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        premises_details_region = _parse_premises_details_region(
            d.pop("PremisesDetailsRegion", UNSET)
        )

        def _parse_premises_details_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        premises_details_type = _parse_premises_details_type(
            d.pop("PremisesDetailsType", UNSET)
        )

        def _parse_type_chi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_chi = _parse_type_chi(d.pop("TypeChi", UNSET))

        def _parse_type_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_eng = _parse_type_eng(d.pop("TypeEng", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            company_name=company_name,
            company_name_chi=company_name_chi,
            part_chi=part_chi,
            part_eng=part_eng,
            premises_details_address_01=premises_details_address_01,
            premises_details_address_02=premises_details_address_02,
            premises_details_district=premises_details_district,
            premises_details_latitude=premises_details_latitude,
            premises_details_longitude=premises_details_longitude,
            premises_details_part=premises_details_part,
            premises_details_region=premises_details_region,
            premises_details_type=premises_details_type,
            type_chi=type_chi,
            type_eng=type_eng,
            objectid=objectid,
        )

        arcgis_feature_server_arcgis_layer_0_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_0_attributes

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
