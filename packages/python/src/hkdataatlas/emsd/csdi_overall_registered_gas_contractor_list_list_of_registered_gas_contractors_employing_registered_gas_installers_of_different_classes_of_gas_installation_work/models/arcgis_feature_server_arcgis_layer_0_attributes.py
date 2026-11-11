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
        address_chinese (None | str | Unset): Publisher field type: esriFieldTypeString
        address_english (None | str | Unset): Publisher field type: esriFieldTypeString
        chinese_company_name (None | str | Unset): Publisher field type: esriFieldTypeString
        chinese_district_name (None | str | Unset): Publisher field type: esriFieldTypeString
        class_1 (None | str | Unset): Publisher field type: esriFieldTypeString
        class_2 (None | str | Unset): Publisher field type: esriFieldTypeString
        class_3 (None | str | Unset): Publisher field type: esriFieldTypeString
        class_4 (None | str | Unset): Publisher field type: esriFieldTypeString
        class_5 (None | str | Unset): Publisher field type: esriFieldTypeString
        class_6 (None | str | Unset): Publisher field type: esriFieldTypeString
        class_7 (None | str | Unset): Publisher field type: esriFieldTypeString
        class_8 (None | str | Unset): Publisher field type: esriFieldTypeString
        english_company_name (None | str | Unset): Publisher field type: esriFieldTypeString
        english_district_name (None | str | Unset): Publisher field type: esriFieldTypeString
        rgc_no (None | str | Unset): Publisher field type: esriFieldTypeString
        telephone_no (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    address_chinese: None | str | Unset = UNSET
    address_english: None | str | Unset = UNSET
    chinese_company_name: None | str | Unset = UNSET
    chinese_district_name: None | str | Unset = UNSET
    class_1: None | str | Unset = UNSET
    class_2: None | str | Unset = UNSET
    class_3: None | str | Unset = UNSET
    class_4: None | str | Unset = UNSET
    class_5: None | str | Unset = UNSET
    class_6: None | str | Unset = UNSET
    class_7: None | str | Unset = UNSET
    class_8: None | str | Unset = UNSET
    english_company_name: None | str | Unset = UNSET
    english_district_name: None | str | Unset = UNSET
    rgc_no: None | str | Unset = UNSET
    telephone_no: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
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

        chinese_company_name: None | str | Unset
        if isinstance(self.chinese_company_name, Unset):
            chinese_company_name = UNSET
        else:
            chinese_company_name = self.chinese_company_name

        chinese_district_name: None | str | Unset
        if isinstance(self.chinese_district_name, Unset):
            chinese_district_name = UNSET
        else:
            chinese_district_name = self.chinese_district_name

        class_1: None | str | Unset
        if isinstance(self.class_1, Unset):
            class_1 = UNSET
        else:
            class_1 = self.class_1

        class_2: None | str | Unset
        if isinstance(self.class_2, Unset):
            class_2 = UNSET
        else:
            class_2 = self.class_2

        class_3: None | str | Unset
        if isinstance(self.class_3, Unset):
            class_3 = UNSET
        else:
            class_3 = self.class_3

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

        class_6: None | str | Unset
        if isinstance(self.class_6, Unset):
            class_6 = UNSET
        else:
            class_6 = self.class_6

        class_7: None | str | Unset
        if isinstance(self.class_7, Unset):
            class_7 = UNSET
        else:
            class_7 = self.class_7

        class_8: None | str | Unset
        if isinstance(self.class_8, Unset):
            class_8 = UNSET
        else:
            class_8 = self.class_8

        english_company_name: None | str | Unset
        if isinstance(self.english_company_name, Unset):
            english_company_name = UNSET
        else:
            english_company_name = self.english_company_name

        english_district_name: None | str | Unset
        if isinstance(self.english_district_name, Unset):
            english_district_name = UNSET
        else:
            english_district_name = self.english_district_name

        rgc_no: None | str | Unset
        if isinstance(self.rgc_no, Unset):
            rgc_no = UNSET
        else:
            rgc_no = self.rgc_no

        telephone_no: None | str | Unset
        if isinstance(self.telephone_no, Unset):
            telephone_no = UNSET
        else:
            telephone_no = self.telephone_no

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address_chinese is not UNSET:
            field_dict["Address_Chinese"] = address_chinese
        if address_english is not UNSET:
            field_dict["Address_English"] = address_english
        if chinese_company_name is not UNSET:
            field_dict["Chinese_Company_Name"] = chinese_company_name
        if chinese_district_name is not UNSET:
            field_dict["Chinese_District_Name"] = chinese_district_name
        if class_1 is not UNSET:
            field_dict["Class_1"] = class_1
        if class_2 is not UNSET:
            field_dict["Class_2"] = class_2
        if class_3 is not UNSET:
            field_dict["Class_3"] = class_3
        if class_4 is not UNSET:
            field_dict["Class_4"] = class_4
        if class_5 is not UNSET:
            field_dict["Class_5"] = class_5
        if class_6 is not UNSET:
            field_dict["Class_6"] = class_6
        if class_7 is not UNSET:
            field_dict["Class_7"] = class_7
        if class_8 is not UNSET:
            field_dict["Class_8"] = class_8
        if english_company_name is not UNSET:
            field_dict["English_Company_Name"] = english_company_name
        if english_district_name is not UNSET:
            field_dict["English_District_Name"] = english_district_name
        if rgc_no is not UNSET:
            field_dict["RGC_No"] = rgc_no
        if telephone_no is not UNSET:
            field_dict["Telephone_No"] = telephone_no
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

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

        def _parse_chinese_company_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        chinese_company_name = _parse_chinese_company_name(
            d.pop("Chinese_Company_Name", UNSET)
        )

        def _parse_chinese_district_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        chinese_district_name = _parse_chinese_district_name(
            d.pop("Chinese_District_Name", UNSET)
        )

        def _parse_class_1(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        class_1 = _parse_class_1(d.pop("Class_1", UNSET))

        def _parse_class_2(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        class_2 = _parse_class_2(d.pop("Class_2", UNSET))

        def _parse_class_3(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        class_3 = _parse_class_3(d.pop("Class_3", UNSET))

        def _parse_class_4(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        class_4 = _parse_class_4(d.pop("Class_4", UNSET))

        def _parse_class_5(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        class_5 = _parse_class_5(d.pop("Class_5", UNSET))

        def _parse_class_6(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        class_6 = _parse_class_6(d.pop("Class_6", UNSET))

        def _parse_class_7(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        class_7 = _parse_class_7(d.pop("Class_7", UNSET))

        def _parse_class_8(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        class_8 = _parse_class_8(d.pop("Class_8", UNSET))

        def _parse_english_company_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        english_company_name = _parse_english_company_name(
            d.pop("English_Company_Name", UNSET)
        )

        def _parse_english_district_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        english_district_name = _parse_english_district_name(
            d.pop("English_District_Name", UNSET)
        )

        def _parse_rgc_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rgc_no = _parse_rgc_no(d.pop("RGC_No", UNSET))

        def _parse_telephone_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        telephone_no = _parse_telephone_no(d.pop("Telephone_No", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            address_chinese=address_chinese,
            address_english=address_english,
            chinese_company_name=chinese_company_name,
            chinese_district_name=chinese_district_name,
            class_1=class_1,
            class_2=class_2,
            class_3=class_3,
            class_4=class_4,
            class_5=class_5,
            class_6=class_6,
            class_7=class_7,
            class_8=class_8,
            english_company_name=english_company_name,
            english_district_name=english_district_name,
            rgc_no=rgc_no,
            telephone_no=telephone_no,
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
