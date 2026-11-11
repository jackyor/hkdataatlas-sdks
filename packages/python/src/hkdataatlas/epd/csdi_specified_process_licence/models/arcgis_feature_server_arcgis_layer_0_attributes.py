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
        public_register_a (None | str | Unset): Publisher field type: esriFieldTypeString
        public_register_r_l (None | str | Unset): Publisher field type: esriFieldTypeString
        licence_number (None | str | Unset): Publisher field type: esriFieldTypeString
        trade_code_description_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        trade_code_description_chi (None | str | Unset): Publisher field type: esriFieldTypeString
        applicant_name_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        applicant_name_chi (None | str | Unset): Publisher field type: esriFieldTypeString
        premises_address_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        premises_address_chi (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    public_register_a: None | str | Unset = UNSET
    public_register_r_l: None | str | Unset = UNSET
    licence_number: None | str | Unset = UNSET
    trade_code_description_eng: None | str | Unset = UNSET
    trade_code_description_chi: None | str | Unset = UNSET
    applicant_name_eng: None | str | Unset = UNSET
    applicant_name_chi: None | str | Unset = UNSET
    premises_address_eng: None | str | Unset = UNSET
    premises_address_chi: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        public_register_a: None | str | Unset
        if isinstance(self.public_register_a, Unset):
            public_register_a = UNSET
        else:
            public_register_a = self.public_register_a

        public_register_r_l: None | str | Unset
        if isinstance(self.public_register_r_l, Unset):
            public_register_r_l = UNSET
        else:
            public_register_r_l = self.public_register_r_l

        licence_number: None | str | Unset
        if isinstance(self.licence_number, Unset):
            licence_number = UNSET
        else:
            licence_number = self.licence_number

        trade_code_description_eng: None | str | Unset
        if isinstance(self.trade_code_description_eng, Unset):
            trade_code_description_eng = UNSET
        else:
            trade_code_description_eng = self.trade_code_description_eng

        trade_code_description_chi: None | str | Unset
        if isinstance(self.trade_code_description_chi, Unset):
            trade_code_description_chi = UNSET
        else:
            trade_code_description_chi = self.trade_code_description_chi

        applicant_name_eng: None | str | Unset
        if isinstance(self.applicant_name_eng, Unset):
            applicant_name_eng = UNSET
        else:
            applicant_name_eng = self.applicant_name_eng

        applicant_name_chi: None | str | Unset
        if isinstance(self.applicant_name_chi, Unset):
            applicant_name_chi = UNSET
        else:
            applicant_name_chi = self.applicant_name_chi

        premises_address_eng: None | str | Unset
        if isinstance(self.premises_address_eng, Unset):
            premises_address_eng = UNSET
        else:
            premises_address_eng = self.premises_address_eng

        premises_address_chi: None | str | Unset
        if isinstance(self.premises_address_chi, Unset):
            premises_address_chi = UNSET
        else:
            premises_address_chi = self.premises_address_chi

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if public_register_a is not UNSET:
            field_dict["Public_Register_A"] = public_register_a
        if public_register_r_l is not UNSET:
            field_dict["Public_Register_R_L"] = public_register_r_l
        if licence_number is not UNSET:
            field_dict["Licence_Number"] = licence_number
        if trade_code_description_eng is not UNSET:
            field_dict["Trade_Code_Description_Eng"] = trade_code_description_eng
        if trade_code_description_chi is not UNSET:
            field_dict["Trade_Code_Description_Chi"] = trade_code_description_chi
        if applicant_name_eng is not UNSET:
            field_dict["Applicant_Name_Eng"] = applicant_name_eng
        if applicant_name_chi is not UNSET:
            field_dict["Applicant_Name_Chi"] = applicant_name_chi
        if premises_address_eng is not UNSET:
            field_dict["Premises_Address_Eng"] = premises_address_eng
        if premises_address_chi is not UNSET:
            field_dict["Premises_Address_Chi"] = premises_address_chi
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_public_register_a(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        public_register_a = _parse_public_register_a(d.pop("Public_Register_A", UNSET))

        def _parse_public_register_r_l(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        public_register_r_l = _parse_public_register_r_l(
            d.pop("Public_Register_R_L", UNSET)
        )

        def _parse_licence_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        licence_number = _parse_licence_number(d.pop("Licence_Number", UNSET))

        def _parse_trade_code_description_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        trade_code_description_eng = _parse_trade_code_description_eng(
            d.pop("Trade_Code_Description_Eng", UNSET)
        )

        def _parse_trade_code_description_chi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        trade_code_description_chi = _parse_trade_code_description_chi(
            d.pop("Trade_Code_Description_Chi", UNSET)
        )

        def _parse_applicant_name_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        applicant_name_eng = _parse_applicant_name_eng(
            d.pop("Applicant_Name_Eng", UNSET)
        )

        def _parse_applicant_name_chi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        applicant_name_chi = _parse_applicant_name_chi(
            d.pop("Applicant_Name_Chi", UNSET)
        )

        def _parse_premises_address_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        premises_address_eng = _parse_premises_address_eng(
            d.pop("Premises_Address_Eng", UNSET)
        )

        def _parse_premises_address_chi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        premises_address_chi = _parse_premises_address_chi(
            d.pop("Premises_Address_Chi", UNSET)
        )

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            public_register_a=public_register_a,
            public_register_r_l=public_register_r_l,
            licence_number=licence_number,
            trade_code_description_eng=trade_code_description_eng,
            trade_code_description_chi=trade_code_description_chi,
            applicant_name_eng=applicant_name_eng,
            applicant_name_chi=applicant_name_chi,
            premises_address_eng=premises_address_eng,
            premises_address_chi=premises_address_chi,
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
