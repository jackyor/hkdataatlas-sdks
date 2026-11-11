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
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        registered_address_en (None | str | Unset): Publisher field type: esriFieldTypeString
        registered_address_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        registered_address_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        registration_number_class_1 (None | str | Unset): Publisher field type: esriFieldTypeString
        registration_number_class_2 (None | str | Unset): Publisher field type: esriFieldTypeString
        registration_number_class_3 (None | str | Unset): Publisher field type: esriFieldTypeString
        northing (float | None | Unset): Publisher field type: esriFieldTypeDouble
        easting (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    objectid: int | Unset = UNSET
    registered_address_en: None | str | Unset = UNSET
    registered_address_tc: None | str | Unset = UNSET
    registered_address_sc: None | str | Unset = UNSET
    registration_number_class_1: None | str | Unset = UNSET
    registration_number_class_2: None | str | Unset = UNSET
    registration_number_class_3: None | str | Unset = UNSET
    northing: float | None | Unset = UNSET
    easting: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        registered_address_en: None | str | Unset
        if isinstance(self.registered_address_en, Unset):
            registered_address_en = UNSET
        else:
            registered_address_en = self.registered_address_en

        registered_address_tc: None | str | Unset
        if isinstance(self.registered_address_tc, Unset):
            registered_address_tc = UNSET
        else:
            registered_address_tc = self.registered_address_tc

        registered_address_sc: None | str | Unset
        if isinstance(self.registered_address_sc, Unset):
            registered_address_sc = UNSET
        else:
            registered_address_sc = self.registered_address_sc

        registration_number_class_1: None | str | Unset
        if isinstance(self.registration_number_class_1, Unset):
            registration_number_class_1 = UNSET
        else:
            registration_number_class_1 = self.registration_number_class_1

        registration_number_class_2: None | str | Unset
        if isinstance(self.registration_number_class_2, Unset):
            registration_number_class_2 = UNSET
        else:
            registration_number_class_2 = self.registration_number_class_2

        registration_number_class_3: None | str | Unset
        if isinstance(self.registration_number_class_3, Unset):
            registration_number_class_3 = UNSET
        else:
            registration_number_class_3 = self.registration_number_class_3

        northing: float | None | Unset
        if isinstance(self.northing, Unset):
            northing = UNSET
        else:
            northing = self.northing

        easting: float | None | Unset
        if isinstance(self.easting, Unset):
            easting = UNSET
        else:
            easting = self.easting

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if registered_address_en is not UNSET:
            field_dict["Registered_Address_en_"] = registered_address_en
        if registered_address_tc is not UNSET:
            field_dict["Registered_Address_tc_"] = registered_address_tc
        if registered_address_sc is not UNSET:
            field_dict["Registered_Address_sc_"] = registered_address_sc
        if registration_number_class_1 is not UNSET:
            field_dict["Registration_Number__Class_1_"] = registration_number_class_1
        if registration_number_class_2 is not UNSET:
            field_dict["Registration_Number__Class_2_"] = registration_number_class_2
        if registration_number_class_3 is not UNSET:
            field_dict["Registration_Number__Class_3_"] = registration_number_class_3
        if northing is not UNSET:
            field_dict["Northing"] = northing
        if easting is not UNSET:
            field_dict["Easting"] = easting

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_registered_address_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        registered_address_en = _parse_registered_address_en(
            d.pop("Registered_Address_en_", UNSET)
        )

        def _parse_registered_address_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        registered_address_tc = _parse_registered_address_tc(
            d.pop("Registered_Address_tc_", UNSET)
        )

        def _parse_registered_address_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        registered_address_sc = _parse_registered_address_sc(
            d.pop("Registered_Address_sc_", UNSET)
        )

        def _parse_registration_number_class_1(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        registration_number_class_1 = _parse_registration_number_class_1(
            d.pop("Registration_Number__Class_1_", UNSET)
        )

        def _parse_registration_number_class_2(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        registration_number_class_2 = _parse_registration_number_class_2(
            d.pop("Registration_Number__Class_2_", UNSET)
        )

        def _parse_registration_number_class_3(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        registration_number_class_3 = _parse_registration_number_class_3(
            d.pop("Registration_Number__Class_3_", UNSET)
        )

        def _parse_northing(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        northing = _parse_northing(d.pop("Northing", UNSET))

        def _parse_easting(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        easting = _parse_easting(d.pop("Easting", UNSET))

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            objectid=objectid,
            registered_address_en=registered_address_en,
            registered_address_tc=registered_address_tc,
            registered_address_sc=registered_address_sc,
            registration_number_class_1=registration_number_class_1,
            registration_number_class_2=registration_number_class_2,
            registration_number_class_3=registration_number_class_3,
            northing=northing,
            easting=easting,
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
