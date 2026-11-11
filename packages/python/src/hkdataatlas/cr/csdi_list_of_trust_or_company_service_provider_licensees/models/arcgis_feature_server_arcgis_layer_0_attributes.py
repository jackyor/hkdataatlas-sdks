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
        business_address (None | str | Unset): Publisher field type: esriFieldTypeString
        latitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        licence_no (None | str | Unset): Publisher field type: esriFieldTypeString
        longitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        name_of_tcsp_licensee_in_chinese (None | str | Unset): Publisher field type: esriFieldTypeString
        name_of_tcsp_licensee_in_english (None | str | Unset): Publisher field type: esriFieldTypeString
        remarks_in_chinese (None | str | Unset): Publisher field type: esriFieldTypeString
        remarks_in_english (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    business_address: None | str | Unset = UNSET
    latitude: float | None | Unset = UNSET
    licence_no: None | str | Unset = UNSET
    longitude: float | None | Unset = UNSET
    name_of_tcsp_licensee_in_chinese: None | str | Unset = UNSET
    name_of_tcsp_licensee_in_english: None | str | Unset = UNSET
    remarks_in_chinese: None | str | Unset = UNSET
    remarks_in_english: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        business_address: None | str | Unset
        if isinstance(self.business_address, Unset):
            business_address = UNSET
        else:
            business_address = self.business_address

        latitude: float | None | Unset
        if isinstance(self.latitude, Unset):
            latitude = UNSET
        else:
            latitude = self.latitude

        licence_no: None | str | Unset
        if isinstance(self.licence_no, Unset):
            licence_no = UNSET
        else:
            licence_no = self.licence_no

        longitude: float | None | Unset
        if isinstance(self.longitude, Unset):
            longitude = UNSET
        else:
            longitude = self.longitude

        name_of_tcsp_licensee_in_chinese: None | str | Unset
        if isinstance(self.name_of_tcsp_licensee_in_chinese, Unset):
            name_of_tcsp_licensee_in_chinese = UNSET
        else:
            name_of_tcsp_licensee_in_chinese = self.name_of_tcsp_licensee_in_chinese

        name_of_tcsp_licensee_in_english: None | str | Unset
        if isinstance(self.name_of_tcsp_licensee_in_english, Unset):
            name_of_tcsp_licensee_in_english = UNSET
        else:
            name_of_tcsp_licensee_in_english = self.name_of_tcsp_licensee_in_english

        remarks_in_chinese: None | str | Unset
        if isinstance(self.remarks_in_chinese, Unset):
            remarks_in_chinese = UNSET
        else:
            remarks_in_chinese = self.remarks_in_chinese

        remarks_in_english: None | str | Unset
        if isinstance(self.remarks_in_english, Unset):
            remarks_in_english = UNSET
        else:
            remarks_in_english = self.remarks_in_english

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if business_address is not UNSET:
            field_dict["Business_Address"] = business_address
        if latitude is not UNSET:
            field_dict["Latitude"] = latitude
        if licence_no is not UNSET:
            field_dict["Licence_No"] = licence_no
        if longitude is not UNSET:
            field_dict["Longitude"] = longitude
        if name_of_tcsp_licensee_in_chinese is not UNSET:
            field_dict["Name_of_TCSP_Licensee_in_Chinese"] = (
                name_of_tcsp_licensee_in_chinese
            )
        if name_of_tcsp_licensee_in_english is not UNSET:
            field_dict["Name_of_TCSP_Licensee_in_English"] = (
                name_of_tcsp_licensee_in_english
            )
        if remarks_in_chinese is not UNSET:
            field_dict["Remarks_in_Chinese"] = remarks_in_chinese
        if remarks_in_english is not UNSET:
            field_dict["Remarks_in_English"] = remarks_in_english
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_business_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        business_address = _parse_business_address(d.pop("Business_Address", UNSET))

        def _parse_latitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        latitude = _parse_latitude(d.pop("Latitude", UNSET))

        def _parse_licence_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        licence_no = _parse_licence_no(d.pop("Licence_No", UNSET))

        def _parse_longitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        longitude = _parse_longitude(d.pop("Longitude", UNSET))

        def _parse_name_of_tcsp_licensee_in_chinese(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_of_tcsp_licensee_in_chinese = _parse_name_of_tcsp_licensee_in_chinese(
            d.pop("Name_of_TCSP_Licensee_in_Chinese", UNSET)
        )

        def _parse_name_of_tcsp_licensee_in_english(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_of_tcsp_licensee_in_english = _parse_name_of_tcsp_licensee_in_english(
            d.pop("Name_of_TCSP_Licensee_in_English", UNSET)
        )

        def _parse_remarks_in_chinese(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remarks_in_chinese = _parse_remarks_in_chinese(
            d.pop("Remarks_in_Chinese", UNSET)
        )

        def _parse_remarks_in_english(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remarks_in_english = _parse_remarks_in_english(
            d.pop("Remarks_in_English", UNSET)
        )

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            business_address=business_address,
            latitude=latitude,
            licence_no=licence_no,
            longitude=longitude,
            name_of_tcsp_licensee_in_chinese=name_of_tcsp_licensee_in_chinese,
            name_of_tcsp_licensee_in_english=name_of_tcsp_licensee_in_english,
            remarks_in_chinese=remarks_in_chinese,
            remarks_in_english=remarks_in_english,
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
