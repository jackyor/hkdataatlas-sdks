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
        street_no (None | str | Unset): Publisher field type: esriFieldTypeString
        eng_building (None | str | Unset): Publisher field type: esriFieldTypeString
        eng_estate (None | str | Unset): Publisher field type: esriFieldTypeString
        eng_street (None | str | Unset): Publisher field type: esriFieldTypeString
        eng_district (None | str | Unset): Publisher field type: esriFieldTypeString
        chi_building (None | str | Unset): Publisher field type: esriFieldTypeString
        chi_estate (None | str | Unset): Publisher field type: esriFieldTypeString
        chi_street (None | str | Unset): Publisher field type: esriFieldTypeString
        chi_district (None | str | Unset): Publisher field type: esriFieldTypeString
        dtt_coverage_estimate (None | str | Unset): Publisher field type: esriFieldTypeString
        latitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        longitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    street_no: None | str | Unset = UNSET
    eng_building: None | str | Unset = UNSET
    eng_estate: None | str | Unset = UNSET
    eng_street: None | str | Unset = UNSET
    eng_district: None | str | Unset = UNSET
    chi_building: None | str | Unset = UNSET
    chi_estate: None | str | Unset = UNSET
    chi_street: None | str | Unset = UNSET
    chi_district: None | str | Unset = UNSET
    dtt_coverage_estimate: None | str | Unset = UNSET
    latitude: float | None | Unset = UNSET
    longitude: float | None | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        street_no: None | str | Unset
        if isinstance(self.street_no, Unset):
            street_no = UNSET
        else:
            street_no = self.street_no

        eng_building: None | str | Unset
        if isinstance(self.eng_building, Unset):
            eng_building = UNSET
        else:
            eng_building = self.eng_building

        eng_estate: None | str | Unset
        if isinstance(self.eng_estate, Unset):
            eng_estate = UNSET
        else:
            eng_estate = self.eng_estate

        eng_street: None | str | Unset
        if isinstance(self.eng_street, Unset):
            eng_street = UNSET
        else:
            eng_street = self.eng_street

        eng_district: None | str | Unset
        if isinstance(self.eng_district, Unset):
            eng_district = UNSET
        else:
            eng_district = self.eng_district

        chi_building: None | str | Unset
        if isinstance(self.chi_building, Unset):
            chi_building = UNSET
        else:
            chi_building = self.chi_building

        chi_estate: None | str | Unset
        if isinstance(self.chi_estate, Unset):
            chi_estate = UNSET
        else:
            chi_estate = self.chi_estate

        chi_street: None | str | Unset
        if isinstance(self.chi_street, Unset):
            chi_street = UNSET
        else:
            chi_street = self.chi_street

        chi_district: None | str | Unset
        if isinstance(self.chi_district, Unset):
            chi_district = UNSET
        else:
            chi_district = self.chi_district

        dtt_coverage_estimate: None | str | Unset
        if isinstance(self.dtt_coverage_estimate, Unset):
            dtt_coverage_estimate = UNSET
        else:
            dtt_coverage_estimate = self.dtt_coverage_estimate

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if street_no is not UNSET:
            field_dict["Street_No"] = street_no
        if eng_building is not UNSET:
            field_dict["Eng_Building"] = eng_building
        if eng_estate is not UNSET:
            field_dict["Eng_Estate"] = eng_estate
        if eng_street is not UNSET:
            field_dict["Eng_Street"] = eng_street
        if eng_district is not UNSET:
            field_dict["Eng_District"] = eng_district
        if chi_building is not UNSET:
            field_dict["Chi_Building"] = chi_building
        if chi_estate is not UNSET:
            field_dict["Chi_Estate"] = chi_estate
        if chi_street is not UNSET:
            field_dict["Chi_Street"] = chi_street
        if chi_district is not UNSET:
            field_dict["Chi_District"] = chi_district
        if dtt_coverage_estimate is not UNSET:
            field_dict["DTT_Coverage_Estimate"] = dtt_coverage_estimate
        if latitude is not UNSET:
            field_dict["Latitude"] = latitude
        if longitude is not UNSET:
            field_dict["Longitude"] = longitude
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_street_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        street_no = _parse_street_no(d.pop("Street_No", UNSET))

        def _parse_eng_building(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        eng_building = _parse_eng_building(d.pop("Eng_Building", UNSET))

        def _parse_eng_estate(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        eng_estate = _parse_eng_estate(d.pop("Eng_Estate", UNSET))

        def _parse_eng_street(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        eng_street = _parse_eng_street(d.pop("Eng_Street", UNSET))

        def _parse_eng_district(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        eng_district = _parse_eng_district(d.pop("Eng_District", UNSET))

        def _parse_chi_building(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        chi_building = _parse_chi_building(d.pop("Chi_Building", UNSET))

        def _parse_chi_estate(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        chi_estate = _parse_chi_estate(d.pop("Chi_Estate", UNSET))

        def _parse_chi_street(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        chi_street = _parse_chi_street(d.pop("Chi_Street", UNSET))

        def _parse_chi_district(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        chi_district = _parse_chi_district(d.pop("Chi_District", UNSET))

        def _parse_dtt_coverage_estimate(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dtt_coverage_estimate = _parse_dtt_coverage_estimate(
            d.pop("DTT_Coverage_Estimate", UNSET)
        )

        def _parse_latitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        latitude = _parse_latitude(d.pop("Latitude", UNSET))

        def _parse_longitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        longitude = _parse_longitude(d.pop("Longitude", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            street_no=street_no,
            eng_building=eng_building,
            eng_estate=eng_estate,
            eng_street=eng_street,
            eng_district=eng_district,
            chi_building=chi_building,
            chi_estate=chi_estate,
            chi_street=chi_street,
            chi_district=chi_district,
            dtt_coverage_estimate=dtt_coverage_estimate,
            latitude=latitude,
            longitude=longitude,
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
