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
        class_4 (None | str | Unset): Publisher field type: esriFieldTypeString
        class_5 (None | str | Unset): Publisher field type: esriFieldTypeString
        company_address_chinese (None | str | Unset): Publisher field type: esriFieldTypeString
        company_address_english (None | str | Unset): Publisher field type: esriFieldTypeString
        contractor_chinese (None | str | Unset): Publisher field type: esriFieldTypeString
        contractor_english (None | str | Unset): Publisher field type: esriFieldTypeString
        gsc_no (float | None | Unset): Publisher field type: esriFieldTypeDouble
        tel_no (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    class_4: None | str | Unset = UNSET
    class_5: None | str | Unset = UNSET
    company_address_chinese: None | str | Unset = UNSET
    company_address_english: None | str | Unset = UNSET
    contractor_chinese: None | str | Unset = UNSET
    contractor_english: None | str | Unset = UNSET
    gsc_no: float | None | Unset = UNSET
    tel_no: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        class_4: None | str | Unset
        if isinstance(self.class_4, Unset):
            class_4 = UNSET
        else:
            class_4 = self.class_4

        class_5: None | str | Unset
        if isinstance(self.class_5, Unset):
            class_5 = UNSET
        else:
            class_5 = self.class_5

        company_address_chinese: None | str | Unset
        if isinstance(self.company_address_chinese, Unset):
            company_address_chinese = UNSET
        else:
            company_address_chinese = self.company_address_chinese

        company_address_english: None | str | Unset
        if isinstance(self.company_address_english, Unset):
            company_address_english = UNSET
        else:
            company_address_english = self.company_address_english

        contractor_chinese: None | str | Unset
        if isinstance(self.contractor_chinese, Unset):
            contractor_chinese = UNSET
        else:
            contractor_chinese = self.contractor_chinese

        contractor_english: None | str | Unset
        if isinstance(self.contractor_english, Unset):
            contractor_english = UNSET
        else:
            contractor_english = self.contractor_english

        gsc_no: float | None | Unset
        if isinstance(self.gsc_no, Unset):
            gsc_no = UNSET
        else:
            gsc_no = self.gsc_no

        tel_no: None | str | Unset
        if isinstance(self.tel_no, Unset):
            tel_no = UNSET
        else:
            tel_no = self.tel_no

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if class_4 is not UNSET:
            field_dict["Class4"] = class_4
        if class_5 is not UNSET:
            field_dict["Class5"] = class_5
        if company_address_chinese is not UNSET:
            field_dict["Company_Address_Chinese"] = company_address_chinese
        if company_address_english is not UNSET:
            field_dict["Company_Address_English"] = company_address_english
        if contractor_chinese is not UNSET:
            field_dict["Contractor_Chinese"] = contractor_chinese
        if contractor_english is not UNSET:
            field_dict["Contractor_English"] = contractor_english
        if gsc_no is not UNSET:
            field_dict["GSC_No"] = gsc_no
        if tel_no is not UNSET:
            field_dict["Tel_No"] = tel_no
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_class_4(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        class_4 = _parse_class_4(d.pop("Class4", UNSET))

        def _parse_class_5(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        class_5 = _parse_class_5(d.pop("Class5", UNSET))

        def _parse_company_address_chinese(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_address_chinese = _parse_company_address_chinese(
            d.pop("Company_Address_Chinese", UNSET)
        )

        def _parse_company_address_english(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_address_english = _parse_company_address_english(
            d.pop("Company_Address_English", UNSET)
        )

        def _parse_contractor_chinese(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contractor_chinese = _parse_contractor_chinese(
            d.pop("Contractor_Chinese", UNSET)
        )

        def _parse_contractor_english(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contractor_english = _parse_contractor_english(
            d.pop("Contractor_English", UNSET)
        )

        def _parse_gsc_no(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        gsc_no = _parse_gsc_no(d.pop("GSC_No", UNSET))

        def _parse_tel_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tel_no = _parse_tel_no(d.pop("Tel_No", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            class_4=class_4,
            class_5=class_5,
            company_address_chinese=company_address_chinese,
            company_address_english=company_address_english,
            contractor_chinese=contractor_chinese,
            contractor_english=contractor_english,
            gsc_no=gsc_no,
            tel_no=tel_no,
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
