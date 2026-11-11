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
        address (None | str | Unset): Publisher field type: esriFieldTypeString
        chinese_name (None | str | Unset): Publisher field type: esriFieldTypeString
        disciplinary_action_gazette_date_1 (None | str | Unset): Publisher field type: esriFieldTypeString
        english_name (None | str | Unset): Publisher field type: esriFieldTypeString
        expiry_date (None | str | Unset): Publisher field type: esriFieldTypeString
        gazette_id_1 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        government_notice_no_1 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        government_notice_url_chinese_1 (None | str | Unset): Publisher field type: esriFieldTypeString
        government_notice_url_english_1 (None | str | Unset): Publisher field type: esriFieldTypeString
        registered_electrical_contractor_no (float | None | Unset): Publisher field type: esriFieldTypeDouble
        telephone_no (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    address: None | str | Unset = UNSET
    chinese_name: None | str | Unset = UNSET
    disciplinary_action_gazette_date_1: None | str | Unset = UNSET
    english_name: None | str | Unset = UNSET
    expiry_date: None | str | Unset = UNSET
    gazette_id_1: float | None | Unset = UNSET
    government_notice_no_1: float | None | Unset = UNSET
    government_notice_url_chinese_1: None | str | Unset = UNSET
    government_notice_url_english_1: None | str | Unset = UNSET
    registered_electrical_contractor_no: float | None | Unset = UNSET
    telephone_no: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address: None | str | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        chinese_name: None | str | Unset
        if isinstance(self.chinese_name, Unset):
            chinese_name = UNSET
        else:
            chinese_name = self.chinese_name

        disciplinary_action_gazette_date_1: None | str | Unset
        if isinstance(self.disciplinary_action_gazette_date_1, Unset):
            disciplinary_action_gazette_date_1 = UNSET
        else:
            disciplinary_action_gazette_date_1 = self.disciplinary_action_gazette_date_1

        english_name: None | str | Unset
        if isinstance(self.english_name, Unset):
            english_name = UNSET
        else:
            english_name = self.english_name

        expiry_date: None | str | Unset
        if isinstance(self.expiry_date, Unset):
            expiry_date = UNSET
        else:
            expiry_date = self.expiry_date

        gazette_id_1: float | None | Unset
        if isinstance(self.gazette_id_1, Unset):
            gazette_id_1 = UNSET
        else:
            gazette_id_1 = self.gazette_id_1

        government_notice_no_1: float | None | Unset
        if isinstance(self.government_notice_no_1, Unset):
            government_notice_no_1 = UNSET
        else:
            government_notice_no_1 = self.government_notice_no_1

        government_notice_url_chinese_1: None | str | Unset
        if isinstance(self.government_notice_url_chinese_1, Unset):
            government_notice_url_chinese_1 = UNSET
        else:
            government_notice_url_chinese_1 = self.government_notice_url_chinese_1

        government_notice_url_english_1: None | str | Unset
        if isinstance(self.government_notice_url_english_1, Unset):
            government_notice_url_english_1 = UNSET
        else:
            government_notice_url_english_1 = self.government_notice_url_english_1

        registered_electrical_contractor_no: float | None | Unset
        if isinstance(self.registered_electrical_contractor_no, Unset):
            registered_electrical_contractor_no = UNSET
        else:
            registered_electrical_contractor_no = (
                self.registered_electrical_contractor_no
            )

        telephone_no: None | str | Unset
        if isinstance(self.telephone_no, Unset):
            telephone_no = UNSET
        else:
            telephone_no = self.telephone_no

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["Address"] = address
        if chinese_name is not UNSET:
            field_dict["Chinese_Name"] = chinese_name
        if disciplinary_action_gazette_date_1 is not UNSET:
            field_dict["Disciplinary_Action_Gazette_Date_1"] = (
                disciplinary_action_gazette_date_1
            )
        if english_name is not UNSET:
            field_dict["English_Name"] = english_name
        if expiry_date is not UNSET:
            field_dict["Expiry_Date"] = expiry_date
        if gazette_id_1 is not UNSET:
            field_dict["Gazette_ID_1"] = gazette_id_1
        if government_notice_no_1 is not UNSET:
            field_dict["Government_Notice_No_1"] = government_notice_no_1
        if government_notice_url_chinese_1 is not UNSET:
            field_dict["Government_Notice_URL_Chinese_1"] = (
                government_notice_url_chinese_1
            )
        if government_notice_url_english_1 is not UNSET:
            field_dict["Government_Notice_URL_English_1"] = (
                government_notice_url_english_1
            )
        if registered_electrical_contractor_no is not UNSET:
            field_dict["Registered_Electrical_Contractor_No"] = (
                registered_electrical_contractor_no
            )
        if telephone_no is not UNSET:
            field_dict["Telephone_No"] = telephone_no
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address = _parse_address(d.pop("Address", UNSET))

        def _parse_chinese_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        chinese_name = _parse_chinese_name(d.pop("Chinese_Name", UNSET))

        def _parse_disciplinary_action_gazette_date_1(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        disciplinary_action_gazette_date_1 = _parse_disciplinary_action_gazette_date_1(
            d.pop("Disciplinary_Action_Gazette_Date_1", UNSET)
        )

        def _parse_english_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        english_name = _parse_english_name(d.pop("English_Name", UNSET))

        def _parse_expiry_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        expiry_date = _parse_expiry_date(d.pop("Expiry_Date", UNSET))

        def _parse_gazette_id_1(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        gazette_id_1 = _parse_gazette_id_1(d.pop("Gazette_ID_1", UNSET))

        def _parse_government_notice_no_1(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        government_notice_no_1 = _parse_government_notice_no_1(
            d.pop("Government_Notice_No_1", UNSET)
        )

        def _parse_government_notice_url_chinese_1(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        government_notice_url_chinese_1 = _parse_government_notice_url_chinese_1(
            d.pop("Government_Notice_URL_Chinese_1", UNSET)
        )

        def _parse_government_notice_url_english_1(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        government_notice_url_english_1 = _parse_government_notice_url_english_1(
            d.pop("Government_Notice_URL_English_1", UNSET)
        )

        def _parse_registered_electrical_contractor_no(
            data: object,
        ) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        registered_electrical_contractor_no = (
            _parse_registered_electrical_contractor_no(
                d.pop("Registered_Electrical_Contractor_No", UNSET)
            )
        )

        def _parse_telephone_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        telephone_no = _parse_telephone_no(d.pop("Telephone_No", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            address=address,
            chinese_name=chinese_name,
            disciplinary_action_gazette_date_1=disciplinary_action_gazette_date_1,
            english_name=english_name,
            expiry_date=expiry_date,
            gazette_id_1=gazette_id_1,
            government_notice_no_1=government_notice_no_1,
            government_notice_url_chinese_1=government_notice_url_chinese_1,
            government_notice_url_english_1=government_notice_url_english_1,
            registered_electrical_contractor_no=registered_electrical_contractor_no,
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
