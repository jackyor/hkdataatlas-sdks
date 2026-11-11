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
        en_property_name (None | str | Unset): Publisher field type: esriFieldTypeString
        tc_property_name (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_property_name (None | str | Unset): Publisher field type: esriFieldTypeString
        en_property_address (None | str | Unset): Publisher field type: esriFieldTypeString
        tc_property_address (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_property_address (None | str | Unset): Publisher field type: esriFieldTypeString
        en_district (None | str | Unset): Publisher field type: esriFieldTypeString
        tc_district (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_district (None | str | Unset): Publisher field type: esriFieldTypeString
        en_opening_hours (None | str | Unset): Publisher field type: esriFieldTypeString
        tc_opening_hours (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_opening_hours (None | str | Unset): Publisher field type: esriFieldTypeString
        en_number_of_car_parking_spaces_by_type (None | str | Unset): Publisher field type: esriFieldTypeString
        tc_number_of_car_parking_spaces_by_type (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_number_of_car_parking_spaces_by_type (None | str | Unset): Publisher field type: esriFieldTypeString
        tc_parking_fee_information (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_parking_fee_information (None | str | Unset): Publisher field type: esriFieldTypeString
        en_parking_fee_information (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    en_property_name: None | str | Unset = UNSET
    tc_property_name: None | str | Unset = UNSET
    sc_property_name: None | str | Unset = UNSET
    en_property_address: None | str | Unset = UNSET
    tc_property_address: None | str | Unset = UNSET
    sc_property_address: None | str | Unset = UNSET
    en_district: None | str | Unset = UNSET
    tc_district: None | str | Unset = UNSET
    sc_district: None | str | Unset = UNSET
    en_opening_hours: None | str | Unset = UNSET
    tc_opening_hours: None | str | Unset = UNSET
    sc_opening_hours: None | str | Unset = UNSET
    en_number_of_car_parking_spaces_by_type: None | str | Unset = UNSET
    tc_number_of_car_parking_spaces_by_type: None | str | Unset = UNSET
    sc_number_of_car_parking_spaces_by_type: None | str | Unset = UNSET
    tc_parking_fee_information: None | str | Unset = UNSET
    sc_parking_fee_information: None | str | Unset = UNSET
    en_parking_fee_information: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        en_property_name: None | str | Unset
        if isinstance(self.en_property_name, Unset):
            en_property_name = UNSET
        else:
            en_property_name = self.en_property_name

        tc_property_name: None | str | Unset
        if isinstance(self.tc_property_name, Unset):
            tc_property_name = UNSET
        else:
            tc_property_name = self.tc_property_name

        sc_property_name: None | str | Unset
        if isinstance(self.sc_property_name, Unset):
            sc_property_name = UNSET
        else:
            sc_property_name = self.sc_property_name

        en_property_address: None | str | Unset
        if isinstance(self.en_property_address, Unset):
            en_property_address = UNSET
        else:
            en_property_address = self.en_property_address

        tc_property_address: None | str | Unset
        if isinstance(self.tc_property_address, Unset):
            tc_property_address = UNSET
        else:
            tc_property_address = self.tc_property_address

        sc_property_address: None | str | Unset
        if isinstance(self.sc_property_address, Unset):
            sc_property_address = UNSET
        else:
            sc_property_address = self.sc_property_address

        en_district: None | str | Unset
        if isinstance(self.en_district, Unset):
            en_district = UNSET
        else:
            en_district = self.en_district

        tc_district: None | str | Unset
        if isinstance(self.tc_district, Unset):
            tc_district = UNSET
        else:
            tc_district = self.tc_district

        sc_district: None | str | Unset
        if isinstance(self.sc_district, Unset):
            sc_district = UNSET
        else:
            sc_district = self.sc_district

        en_opening_hours: None | str | Unset
        if isinstance(self.en_opening_hours, Unset):
            en_opening_hours = UNSET
        else:
            en_opening_hours = self.en_opening_hours

        tc_opening_hours: None | str | Unset
        if isinstance(self.tc_opening_hours, Unset):
            tc_opening_hours = UNSET
        else:
            tc_opening_hours = self.tc_opening_hours

        sc_opening_hours: None | str | Unset
        if isinstance(self.sc_opening_hours, Unset):
            sc_opening_hours = UNSET
        else:
            sc_opening_hours = self.sc_opening_hours

        en_number_of_car_parking_spaces_by_type: None | str | Unset
        if isinstance(self.en_number_of_car_parking_spaces_by_type, Unset):
            en_number_of_car_parking_spaces_by_type = UNSET
        else:
            en_number_of_car_parking_spaces_by_type = (
                self.en_number_of_car_parking_spaces_by_type
            )

        tc_number_of_car_parking_spaces_by_type: None | str | Unset
        if isinstance(self.tc_number_of_car_parking_spaces_by_type, Unset):
            tc_number_of_car_parking_spaces_by_type = UNSET
        else:
            tc_number_of_car_parking_spaces_by_type = (
                self.tc_number_of_car_parking_spaces_by_type
            )

        sc_number_of_car_parking_spaces_by_type: None | str | Unset
        if isinstance(self.sc_number_of_car_parking_spaces_by_type, Unset):
            sc_number_of_car_parking_spaces_by_type = UNSET
        else:
            sc_number_of_car_parking_spaces_by_type = (
                self.sc_number_of_car_parking_spaces_by_type
            )

        tc_parking_fee_information: None | str | Unset
        if isinstance(self.tc_parking_fee_information, Unset):
            tc_parking_fee_information = UNSET
        else:
            tc_parking_fee_information = self.tc_parking_fee_information

        sc_parking_fee_information: None | str | Unset
        if isinstance(self.sc_parking_fee_information, Unset):
            sc_parking_fee_information = UNSET
        else:
            sc_parking_fee_information = self.sc_parking_fee_information

        en_parking_fee_information: None | str | Unset
        if isinstance(self.en_parking_fee_information, Unset):
            en_parking_fee_information = UNSET
        else:
            en_parking_fee_information = self.en_parking_fee_information

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if en_property_name is not UNSET:
            field_dict["en_property_name"] = en_property_name
        if tc_property_name is not UNSET:
            field_dict["tc_property_name"] = tc_property_name
        if sc_property_name is not UNSET:
            field_dict["sc_property_name"] = sc_property_name
        if en_property_address is not UNSET:
            field_dict["en_property_address"] = en_property_address
        if tc_property_address is not UNSET:
            field_dict["tc_property_address"] = tc_property_address
        if sc_property_address is not UNSET:
            field_dict["sc_property_address"] = sc_property_address
        if en_district is not UNSET:
            field_dict["en_district"] = en_district
        if tc_district is not UNSET:
            field_dict["tc_district"] = tc_district
        if sc_district is not UNSET:
            field_dict["sc_district"] = sc_district
        if en_opening_hours is not UNSET:
            field_dict["en_opening_hours"] = en_opening_hours
        if tc_opening_hours is not UNSET:
            field_dict["tc_opening_hours"] = tc_opening_hours
        if sc_opening_hours is not UNSET:
            field_dict["sc_opening_hours"] = sc_opening_hours
        if en_number_of_car_parking_spaces_by_type is not UNSET:
            field_dict["en_number_of_car_parking_spaces_by_type"] = (
                en_number_of_car_parking_spaces_by_type
            )
        if tc_number_of_car_parking_spaces_by_type is not UNSET:
            field_dict["tc_number_of_car_parking_spaces_by_type"] = (
                tc_number_of_car_parking_spaces_by_type
            )
        if sc_number_of_car_parking_spaces_by_type is not UNSET:
            field_dict["sc_number_of_car_parking_spaces_by_type"] = (
                sc_number_of_car_parking_spaces_by_type
            )
        if tc_parking_fee_information is not UNSET:
            field_dict["tc_parking_fee_information"] = tc_parking_fee_information
        if sc_parking_fee_information is not UNSET:
            field_dict["sc_parking_fee_information"] = sc_parking_fee_information
        if en_parking_fee_information is not UNSET:
            field_dict["en_parking_fee_information"] = en_parking_fee_information
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_en_property_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        en_property_name = _parse_en_property_name(d.pop("en_property_name", UNSET))

        def _parse_tc_property_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tc_property_name = _parse_tc_property_name(d.pop("tc_property_name", UNSET))

        def _parse_sc_property_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_property_name = _parse_sc_property_name(d.pop("sc_property_name", UNSET))

        def _parse_en_property_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        en_property_address = _parse_en_property_address(
            d.pop("en_property_address", UNSET)
        )

        def _parse_tc_property_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tc_property_address = _parse_tc_property_address(
            d.pop("tc_property_address", UNSET)
        )

        def _parse_sc_property_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_property_address = _parse_sc_property_address(
            d.pop("sc_property_address", UNSET)
        )

        def _parse_en_district(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        en_district = _parse_en_district(d.pop("en_district", UNSET))

        def _parse_tc_district(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tc_district = _parse_tc_district(d.pop("tc_district", UNSET))

        def _parse_sc_district(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_district = _parse_sc_district(d.pop("sc_district", UNSET))

        def _parse_en_opening_hours(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        en_opening_hours = _parse_en_opening_hours(d.pop("en_opening_hours", UNSET))

        def _parse_tc_opening_hours(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tc_opening_hours = _parse_tc_opening_hours(d.pop("tc_opening_hours", UNSET))

        def _parse_sc_opening_hours(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_opening_hours = _parse_sc_opening_hours(d.pop("sc_opening_hours", UNSET))

        def _parse_en_number_of_car_parking_spaces_by_type(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        en_number_of_car_parking_spaces_by_type = (
            _parse_en_number_of_car_parking_spaces_by_type(
                d.pop("en_number_of_car_parking_spaces_by_type", UNSET)
            )
        )

        def _parse_tc_number_of_car_parking_spaces_by_type(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tc_number_of_car_parking_spaces_by_type = (
            _parse_tc_number_of_car_parking_spaces_by_type(
                d.pop("tc_number_of_car_parking_spaces_by_type", UNSET)
            )
        )

        def _parse_sc_number_of_car_parking_spaces_by_type(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_number_of_car_parking_spaces_by_type = (
            _parse_sc_number_of_car_parking_spaces_by_type(
                d.pop("sc_number_of_car_parking_spaces_by_type", UNSET)
            )
        )

        def _parse_tc_parking_fee_information(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tc_parking_fee_information = _parse_tc_parking_fee_information(
            d.pop("tc_parking_fee_information", UNSET)
        )

        def _parse_sc_parking_fee_information(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_parking_fee_information = _parse_sc_parking_fee_information(
            d.pop("sc_parking_fee_information", UNSET)
        )

        def _parse_en_parking_fee_information(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        en_parking_fee_information = _parse_en_parking_fee_information(
            d.pop("en_parking_fee_information", UNSET)
        )

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            en_property_name=en_property_name,
            tc_property_name=tc_property_name,
            sc_property_name=sc_property_name,
            en_property_address=en_property_address,
            tc_property_address=tc_property_address,
            sc_property_address=sc_property_address,
            en_district=en_district,
            tc_district=tc_district,
            sc_district=sc_district,
            en_opening_hours=en_opening_hours,
            tc_opening_hours=tc_opening_hours,
            sc_opening_hours=sc_opening_hours,
            en_number_of_car_parking_spaces_by_type=en_number_of_car_parking_spaces_by_type,
            tc_number_of_car_parking_spaces_by_type=tc_number_of_car_parking_spaces_by_type,
            sc_number_of_car_parking_spaces_by_type=sc_number_of_car_parking_spaces_by_type,
            tc_parking_fee_information=tc_parking_fee_information,
            sc_parking_fee_information=sc_parking_fee_information,
            en_parking_fee_information=en_parking_fee_information,
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
