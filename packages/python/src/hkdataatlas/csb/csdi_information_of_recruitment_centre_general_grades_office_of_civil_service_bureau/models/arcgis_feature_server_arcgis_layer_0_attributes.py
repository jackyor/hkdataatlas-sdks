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
        name_en (None | str | Unset): Publisher field type: esriFieldTypeString
        name_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        name_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        address_en (None | str | Unset): Publisher field type: esriFieldTypeString
        address_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        address_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        telephone (None | str | Unset): Publisher field type: esriFieldTypeString
        e_mail (None | str | Unset): Publisher field type: esriFieldTypeString
        opening_hours_en (None | str | Unset): Publisher field type: esriFieldTypeString
        opening_hours_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        opening_hours_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        recruitment_centre_commissioned_date_en (None | str | Unset): Publisher field type: esriFieldTypeString
        recruitment_centre_commissioned_date_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        recruitment_centre_commissioned_date_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    name_en: None | str | Unset = UNSET
    name_tc: None | str | Unset = UNSET
    name_sc: None | str | Unset = UNSET
    address_en: None | str | Unset = UNSET
    address_tc: None | str | Unset = UNSET
    address_sc: None | str | Unset = UNSET
    telephone: None | str | Unset = UNSET
    e_mail: None | str | Unset = UNSET
    opening_hours_en: None | str | Unset = UNSET
    opening_hours_tc: None | str | Unset = UNSET
    opening_hours_sc: None | str | Unset = UNSET
    recruitment_centre_commissioned_date_en: None | str | Unset = UNSET
    recruitment_centre_commissioned_date_tc: None | str | Unset = UNSET
    recruitment_centre_commissioned_date_sc: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name_en: None | str | Unset
        if isinstance(self.name_en, Unset):
            name_en = UNSET
        else:
            name_en = self.name_en

        name_tc: None | str | Unset
        if isinstance(self.name_tc, Unset):
            name_tc = UNSET
        else:
            name_tc = self.name_tc

        name_sc: None | str | Unset
        if isinstance(self.name_sc, Unset):
            name_sc = UNSET
        else:
            name_sc = self.name_sc

        address_en: None | str | Unset
        if isinstance(self.address_en, Unset):
            address_en = UNSET
        else:
            address_en = self.address_en

        address_tc: None | str | Unset
        if isinstance(self.address_tc, Unset):
            address_tc = UNSET
        else:
            address_tc = self.address_tc

        address_sc: None | str | Unset
        if isinstance(self.address_sc, Unset):
            address_sc = UNSET
        else:
            address_sc = self.address_sc

        telephone: None | str | Unset
        if isinstance(self.telephone, Unset):
            telephone = UNSET
        else:
            telephone = self.telephone

        e_mail: None | str | Unset
        if isinstance(self.e_mail, Unset):
            e_mail = UNSET
        else:
            e_mail = self.e_mail

        opening_hours_en: None | str | Unset
        if isinstance(self.opening_hours_en, Unset):
            opening_hours_en = UNSET
        else:
            opening_hours_en = self.opening_hours_en

        opening_hours_tc: None | str | Unset
        if isinstance(self.opening_hours_tc, Unset):
            opening_hours_tc = UNSET
        else:
            opening_hours_tc = self.opening_hours_tc

        opening_hours_sc: None | str | Unset
        if isinstance(self.opening_hours_sc, Unset):
            opening_hours_sc = UNSET
        else:
            opening_hours_sc = self.opening_hours_sc

        recruitment_centre_commissioned_date_en: None | str | Unset
        if isinstance(self.recruitment_centre_commissioned_date_en, Unset):
            recruitment_centre_commissioned_date_en = UNSET
        else:
            recruitment_centre_commissioned_date_en = (
                self.recruitment_centre_commissioned_date_en
            )

        recruitment_centre_commissioned_date_tc: None | str | Unset
        if isinstance(self.recruitment_centre_commissioned_date_tc, Unset):
            recruitment_centre_commissioned_date_tc = UNSET
        else:
            recruitment_centre_commissioned_date_tc = (
                self.recruitment_centre_commissioned_date_tc
            )

        recruitment_centre_commissioned_date_sc: None | str | Unset
        if isinstance(self.recruitment_centre_commissioned_date_sc, Unset):
            recruitment_centre_commissioned_date_sc = UNSET
        else:
            recruitment_centre_commissioned_date_sc = (
                self.recruitment_centre_commissioned_date_sc
            )

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name_en is not UNSET:
            field_dict["Name_EN"] = name_en
        if name_tc is not UNSET:
            field_dict["Name_TC"] = name_tc
        if name_sc is not UNSET:
            field_dict["Name_SC"] = name_sc
        if address_en is not UNSET:
            field_dict["Address_EN"] = address_en
        if address_tc is not UNSET:
            field_dict["Address_TC"] = address_tc
        if address_sc is not UNSET:
            field_dict["Address_SC"] = address_sc
        if telephone is not UNSET:
            field_dict["Telephone"] = telephone
        if e_mail is not UNSET:
            field_dict["E_mail"] = e_mail
        if opening_hours_en is not UNSET:
            field_dict["OpeningHours_EN"] = opening_hours_en
        if opening_hours_tc is not UNSET:
            field_dict["OpeningHours_TC"] = opening_hours_tc
        if opening_hours_sc is not UNSET:
            field_dict["OpeningHours_SC"] = opening_hours_sc
        if recruitment_centre_commissioned_date_en is not UNSET:
            field_dict["RecruitmentCentreCommissionedDate_EN"] = (
                recruitment_centre_commissioned_date_en
            )
        if recruitment_centre_commissioned_date_tc is not UNSET:
            field_dict["RecruitmentCentreCommissionedDate_TC"] = (
                recruitment_centre_commissioned_date_tc
            )
        if recruitment_centre_commissioned_date_sc is not UNSET:
            field_dict["RecruitmentCentreCommissionedDate_SC"] = (
                recruitment_centre_commissioned_date_sc
            )
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_en = _parse_name_en(d.pop("Name_EN", UNSET))

        def _parse_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_tc = _parse_name_tc(d.pop("Name_TC", UNSET))

        def _parse_name_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_sc = _parse_name_sc(d.pop("Name_SC", UNSET))

        def _parse_address_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_en = _parse_address_en(d.pop("Address_EN", UNSET))

        def _parse_address_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_tc = _parse_address_tc(d.pop("Address_TC", UNSET))

        def _parse_address_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_sc = _parse_address_sc(d.pop("Address_SC", UNSET))

        def _parse_telephone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        telephone = _parse_telephone(d.pop("Telephone", UNSET))

        def _parse_e_mail(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        e_mail = _parse_e_mail(d.pop("E_mail", UNSET))

        def _parse_opening_hours_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        opening_hours_en = _parse_opening_hours_en(d.pop("OpeningHours_EN", UNSET))

        def _parse_opening_hours_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        opening_hours_tc = _parse_opening_hours_tc(d.pop("OpeningHours_TC", UNSET))

        def _parse_opening_hours_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        opening_hours_sc = _parse_opening_hours_sc(d.pop("OpeningHours_SC", UNSET))

        def _parse_recruitment_centre_commissioned_date_en(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        recruitment_centre_commissioned_date_en = (
            _parse_recruitment_centre_commissioned_date_en(
                d.pop("RecruitmentCentreCommissionedDate_EN", UNSET)
            )
        )

        def _parse_recruitment_centre_commissioned_date_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        recruitment_centre_commissioned_date_tc = (
            _parse_recruitment_centre_commissioned_date_tc(
                d.pop("RecruitmentCentreCommissionedDate_TC", UNSET)
            )
        )

        def _parse_recruitment_centre_commissioned_date_sc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        recruitment_centre_commissioned_date_sc = (
            _parse_recruitment_centre_commissioned_date_sc(
                d.pop("RecruitmentCentreCommissionedDate_SC", UNSET)
            )
        )

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            name_en=name_en,
            name_tc=name_tc,
            name_sc=name_sc,
            address_en=address_en,
            address_tc=address_tc,
            address_sc=address_sc,
            telephone=telephone,
            e_mail=e_mail,
            opening_hours_en=opening_hours_en,
            opening_hours_tc=opening_hours_tc,
            opening_hours_sc=opening_hours_sc,
            recruitment_centre_commissioned_date_en=recruitment_centre_commissioned_date_en,
            recruitment_centre_commissioned_date_tc=recruitment_centre_commissioned_date_tc,
            recruitment_centre_commissioned_date_sc=recruitment_centre_commissioned_date_sc,
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
