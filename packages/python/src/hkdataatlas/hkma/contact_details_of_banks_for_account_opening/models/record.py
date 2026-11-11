from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Record")


@_attrs_define
class Record:
    """
    Attributes:
        bank_info_name (str | Unset):
        bank_info_url (None | str | Unset):
        bank_info_type (str | Unset):
        bank_info_remark (None | str | Unset):
        pa_service_url (None | str | Unset):
        pa_service_remark (None | str | Unset):
        pa_onlappl_url (None | str | Unset):
        pa_onlappl_remark (None | str | Unset):
        pa_onlappo_url (None | str | Unset):
        pa_onlappo_remark (None | str | Unset):
        pa_inforeq_url (None | str | Unset):
        pa_inforeq_remark (None | str | Unset):
        pa_acctopenbh_url (None | str | Unset):
        pa_acctopenbh_remark (None | str | Unset):
        pa_hotline_tel (None | str | Unset):
        pa_hotline_remark (None | str | Unset):
        pa_contact_person (None | str | Unset):
        pa_contact_email (None | str | Unset):
        pa_contact_tel (None | str | Unset):
        pa_contact_fax (None | str | Unset):
        pa_contact_mobile (None | str | Unset):
        pa_contact_url (None | str | Unset):
        pa_contact_remark (None | str | Unset):
        ba_service_url (None | str | Unset):
        ba_service_remark (None | str | Unset):
        ba_onlappl_url (None | str | Unset):
        ba_onlappl_remark (None | str | Unset):
        ba_onlappo_url (None | str | Unset):
        ba_onlappo_remark (None | str | Unset):
        ba_inforeq_url (None | str | Unset):
        ba_inforeq_remark (None | str | Unset):
        ba_acctopenbh_url (None | str | Unset):
        ba_acctopenbh_remark (None | str | Unset):
        ba_hotline_tel (None | str | Unset):
        ba_hotline_remark (None | str | Unset):
        ba_contact_person (None | str | Unset):
        ba_contact_email (None | str | Unset):
        ba_contact_tel (None | str | Unset):
        ba_contact_fax (None | str | Unset):
        ba_contact_mobile (None | str | Unset):
        ba_contact_url (None | str | Unset):
        ba_contact_remark (None | str | Unset):
    """

    bank_info_name: str | Unset = UNSET
    bank_info_url: None | str | Unset = UNSET
    bank_info_type: str | Unset = UNSET
    bank_info_remark: None | str | Unset = UNSET
    pa_service_url: None | str | Unset = UNSET
    pa_service_remark: None | str | Unset = UNSET
    pa_onlappl_url: None | str | Unset = UNSET
    pa_onlappl_remark: None | str | Unset = UNSET
    pa_onlappo_url: None | str | Unset = UNSET
    pa_onlappo_remark: None | str | Unset = UNSET
    pa_inforeq_url: None | str | Unset = UNSET
    pa_inforeq_remark: None | str | Unset = UNSET
    pa_acctopenbh_url: None | str | Unset = UNSET
    pa_acctopenbh_remark: None | str | Unset = UNSET
    pa_hotline_tel: None | str | Unset = UNSET
    pa_hotline_remark: None | str | Unset = UNSET
    pa_contact_person: None | str | Unset = UNSET
    pa_contact_email: None | str | Unset = UNSET
    pa_contact_tel: None | str | Unset = UNSET
    pa_contact_fax: None | str | Unset = UNSET
    pa_contact_mobile: None | str | Unset = UNSET
    pa_contact_url: None | str | Unset = UNSET
    pa_contact_remark: None | str | Unset = UNSET
    ba_service_url: None | str | Unset = UNSET
    ba_service_remark: None | str | Unset = UNSET
    ba_onlappl_url: None | str | Unset = UNSET
    ba_onlappl_remark: None | str | Unset = UNSET
    ba_onlappo_url: None | str | Unset = UNSET
    ba_onlappo_remark: None | str | Unset = UNSET
    ba_inforeq_url: None | str | Unset = UNSET
    ba_inforeq_remark: None | str | Unset = UNSET
    ba_acctopenbh_url: None | str | Unset = UNSET
    ba_acctopenbh_remark: None | str | Unset = UNSET
    ba_hotline_tel: None | str | Unset = UNSET
    ba_hotline_remark: None | str | Unset = UNSET
    ba_contact_person: None | str | Unset = UNSET
    ba_contact_email: None | str | Unset = UNSET
    ba_contact_tel: None | str | Unset = UNSET
    ba_contact_fax: None | str | Unset = UNSET
    ba_contact_mobile: None | str | Unset = UNSET
    ba_contact_url: None | str | Unset = UNSET
    ba_contact_remark: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bank_info_name = self.bank_info_name

        bank_info_url: None | str | Unset
        if isinstance(self.bank_info_url, Unset):
            bank_info_url = UNSET
        else:
            bank_info_url = self.bank_info_url

        bank_info_type = self.bank_info_type

        bank_info_remark: None | str | Unset
        if isinstance(self.bank_info_remark, Unset):
            bank_info_remark = UNSET
        else:
            bank_info_remark = self.bank_info_remark

        pa_service_url: None | str | Unset
        if isinstance(self.pa_service_url, Unset):
            pa_service_url = UNSET
        else:
            pa_service_url = self.pa_service_url

        pa_service_remark: None | str | Unset
        if isinstance(self.pa_service_remark, Unset):
            pa_service_remark = UNSET
        else:
            pa_service_remark = self.pa_service_remark

        pa_onlappl_url: None | str | Unset
        if isinstance(self.pa_onlappl_url, Unset):
            pa_onlappl_url = UNSET
        else:
            pa_onlappl_url = self.pa_onlappl_url

        pa_onlappl_remark: None | str | Unset
        if isinstance(self.pa_onlappl_remark, Unset):
            pa_onlappl_remark = UNSET
        else:
            pa_onlappl_remark = self.pa_onlappl_remark

        pa_onlappo_url: None | str | Unset
        if isinstance(self.pa_onlappo_url, Unset):
            pa_onlappo_url = UNSET
        else:
            pa_onlappo_url = self.pa_onlappo_url

        pa_onlappo_remark: None | str | Unset
        if isinstance(self.pa_onlappo_remark, Unset):
            pa_onlappo_remark = UNSET
        else:
            pa_onlappo_remark = self.pa_onlappo_remark

        pa_inforeq_url: None | str | Unset
        if isinstance(self.pa_inforeq_url, Unset):
            pa_inforeq_url = UNSET
        else:
            pa_inforeq_url = self.pa_inforeq_url

        pa_inforeq_remark: None | str | Unset
        if isinstance(self.pa_inforeq_remark, Unset):
            pa_inforeq_remark = UNSET
        else:
            pa_inforeq_remark = self.pa_inforeq_remark

        pa_acctopenbh_url: None | str | Unset
        if isinstance(self.pa_acctopenbh_url, Unset):
            pa_acctopenbh_url = UNSET
        else:
            pa_acctopenbh_url = self.pa_acctopenbh_url

        pa_acctopenbh_remark: None | str | Unset
        if isinstance(self.pa_acctopenbh_remark, Unset):
            pa_acctopenbh_remark = UNSET
        else:
            pa_acctopenbh_remark = self.pa_acctopenbh_remark

        pa_hotline_tel: None | str | Unset
        if isinstance(self.pa_hotline_tel, Unset):
            pa_hotline_tel = UNSET
        else:
            pa_hotline_tel = self.pa_hotline_tel

        pa_hotline_remark: None | str | Unset
        if isinstance(self.pa_hotline_remark, Unset):
            pa_hotline_remark = UNSET
        else:
            pa_hotline_remark = self.pa_hotline_remark

        pa_contact_person: None | str | Unset
        if isinstance(self.pa_contact_person, Unset):
            pa_contact_person = UNSET
        else:
            pa_contact_person = self.pa_contact_person

        pa_contact_email: None | str | Unset
        if isinstance(self.pa_contact_email, Unset):
            pa_contact_email = UNSET
        else:
            pa_contact_email = self.pa_contact_email

        pa_contact_tel: None | str | Unset
        if isinstance(self.pa_contact_tel, Unset):
            pa_contact_tel = UNSET
        else:
            pa_contact_tel = self.pa_contact_tel

        pa_contact_fax: None | str | Unset
        if isinstance(self.pa_contact_fax, Unset):
            pa_contact_fax = UNSET
        else:
            pa_contact_fax = self.pa_contact_fax

        pa_contact_mobile: None | str | Unset
        if isinstance(self.pa_contact_mobile, Unset):
            pa_contact_mobile = UNSET
        else:
            pa_contact_mobile = self.pa_contact_mobile

        pa_contact_url: None | str | Unset
        if isinstance(self.pa_contact_url, Unset):
            pa_contact_url = UNSET
        else:
            pa_contact_url = self.pa_contact_url

        pa_contact_remark: None | str | Unset
        if isinstance(self.pa_contact_remark, Unset):
            pa_contact_remark = UNSET
        else:
            pa_contact_remark = self.pa_contact_remark

        ba_service_url: None | str | Unset
        if isinstance(self.ba_service_url, Unset):
            ba_service_url = UNSET
        else:
            ba_service_url = self.ba_service_url

        ba_service_remark: None | str | Unset
        if isinstance(self.ba_service_remark, Unset):
            ba_service_remark = UNSET
        else:
            ba_service_remark = self.ba_service_remark

        ba_onlappl_url: None | str | Unset
        if isinstance(self.ba_onlappl_url, Unset):
            ba_onlappl_url = UNSET
        else:
            ba_onlappl_url = self.ba_onlappl_url

        ba_onlappl_remark: None | str | Unset
        if isinstance(self.ba_onlappl_remark, Unset):
            ba_onlappl_remark = UNSET
        else:
            ba_onlappl_remark = self.ba_onlappl_remark

        ba_onlappo_url: None | str | Unset
        if isinstance(self.ba_onlappo_url, Unset):
            ba_onlappo_url = UNSET
        else:
            ba_onlappo_url = self.ba_onlappo_url

        ba_onlappo_remark: None | str | Unset
        if isinstance(self.ba_onlappo_remark, Unset):
            ba_onlappo_remark = UNSET
        else:
            ba_onlappo_remark = self.ba_onlappo_remark

        ba_inforeq_url: None | str | Unset
        if isinstance(self.ba_inforeq_url, Unset):
            ba_inforeq_url = UNSET
        else:
            ba_inforeq_url = self.ba_inforeq_url

        ba_inforeq_remark: None | str | Unset
        if isinstance(self.ba_inforeq_remark, Unset):
            ba_inforeq_remark = UNSET
        else:
            ba_inforeq_remark = self.ba_inforeq_remark

        ba_acctopenbh_url: None | str | Unset
        if isinstance(self.ba_acctopenbh_url, Unset):
            ba_acctopenbh_url = UNSET
        else:
            ba_acctopenbh_url = self.ba_acctopenbh_url

        ba_acctopenbh_remark: None | str | Unset
        if isinstance(self.ba_acctopenbh_remark, Unset):
            ba_acctopenbh_remark = UNSET
        else:
            ba_acctopenbh_remark = self.ba_acctopenbh_remark

        ba_hotline_tel: None | str | Unset
        if isinstance(self.ba_hotline_tel, Unset):
            ba_hotline_tel = UNSET
        else:
            ba_hotline_tel = self.ba_hotline_tel

        ba_hotline_remark: None | str | Unset
        if isinstance(self.ba_hotline_remark, Unset):
            ba_hotline_remark = UNSET
        else:
            ba_hotline_remark = self.ba_hotline_remark

        ba_contact_person: None | str | Unset
        if isinstance(self.ba_contact_person, Unset):
            ba_contact_person = UNSET
        else:
            ba_contact_person = self.ba_contact_person

        ba_contact_email: None | str | Unset
        if isinstance(self.ba_contact_email, Unset):
            ba_contact_email = UNSET
        else:
            ba_contact_email = self.ba_contact_email

        ba_contact_tel: None | str | Unset
        if isinstance(self.ba_contact_tel, Unset):
            ba_contact_tel = UNSET
        else:
            ba_contact_tel = self.ba_contact_tel

        ba_contact_fax: None | str | Unset
        if isinstance(self.ba_contact_fax, Unset):
            ba_contact_fax = UNSET
        else:
            ba_contact_fax = self.ba_contact_fax

        ba_contact_mobile: None | str | Unset
        if isinstance(self.ba_contact_mobile, Unset):
            ba_contact_mobile = UNSET
        else:
            ba_contact_mobile = self.ba_contact_mobile

        ba_contact_url: None | str | Unset
        if isinstance(self.ba_contact_url, Unset):
            ba_contact_url = UNSET
        else:
            ba_contact_url = self.ba_contact_url

        ba_contact_remark: None | str | Unset
        if isinstance(self.ba_contact_remark, Unset):
            ba_contact_remark = UNSET
        else:
            ba_contact_remark = self.ba_contact_remark

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bank_info_name is not UNSET:
            field_dict["bank_info_name"] = bank_info_name
        if bank_info_url is not UNSET:
            field_dict["bank_info_url"] = bank_info_url
        if bank_info_type is not UNSET:
            field_dict["bank_info_type"] = bank_info_type
        if bank_info_remark is not UNSET:
            field_dict["bank_info_remark"] = bank_info_remark
        if pa_service_url is not UNSET:
            field_dict["pa_service_url"] = pa_service_url
        if pa_service_remark is not UNSET:
            field_dict["pa_service_remark"] = pa_service_remark
        if pa_onlappl_url is not UNSET:
            field_dict["pa_onlappl_url"] = pa_onlappl_url
        if pa_onlappl_remark is not UNSET:
            field_dict["pa_onlappl_remark"] = pa_onlappl_remark
        if pa_onlappo_url is not UNSET:
            field_dict["pa_onlappo_url"] = pa_onlappo_url
        if pa_onlappo_remark is not UNSET:
            field_dict["pa_onlappo_remark"] = pa_onlappo_remark
        if pa_inforeq_url is not UNSET:
            field_dict["pa_inforeq_url"] = pa_inforeq_url
        if pa_inforeq_remark is not UNSET:
            field_dict["pa_inforeq_remark"] = pa_inforeq_remark
        if pa_acctopenbh_url is not UNSET:
            field_dict["pa_acctopenbh_url"] = pa_acctopenbh_url
        if pa_acctopenbh_remark is not UNSET:
            field_dict["pa_acctopenbh_remark"] = pa_acctopenbh_remark
        if pa_hotline_tel is not UNSET:
            field_dict["pa_hotline_tel"] = pa_hotline_tel
        if pa_hotline_remark is not UNSET:
            field_dict["pa_hotline_remark"] = pa_hotline_remark
        if pa_contact_person is not UNSET:
            field_dict["pa_contact_person"] = pa_contact_person
        if pa_contact_email is not UNSET:
            field_dict["pa_contact_email"] = pa_contact_email
        if pa_contact_tel is not UNSET:
            field_dict["pa_contact_tel"] = pa_contact_tel
        if pa_contact_fax is not UNSET:
            field_dict["pa_contact_fax"] = pa_contact_fax
        if pa_contact_mobile is not UNSET:
            field_dict["pa_contact_mobile"] = pa_contact_mobile
        if pa_contact_url is not UNSET:
            field_dict["pa_contact_url"] = pa_contact_url
        if pa_contact_remark is not UNSET:
            field_dict["pa_contact_remark"] = pa_contact_remark
        if ba_service_url is not UNSET:
            field_dict["ba_service_url"] = ba_service_url
        if ba_service_remark is not UNSET:
            field_dict["ba_service_remark"] = ba_service_remark
        if ba_onlappl_url is not UNSET:
            field_dict["ba_onlappl_url"] = ba_onlappl_url
        if ba_onlappl_remark is not UNSET:
            field_dict["ba_onlappl_remark"] = ba_onlappl_remark
        if ba_onlappo_url is not UNSET:
            field_dict["ba_onlappo_url"] = ba_onlappo_url
        if ba_onlappo_remark is not UNSET:
            field_dict["ba_onlappo_remark"] = ba_onlappo_remark
        if ba_inforeq_url is not UNSET:
            field_dict["ba_inforeq_url"] = ba_inforeq_url
        if ba_inforeq_remark is not UNSET:
            field_dict["ba_inforeq_remark"] = ba_inforeq_remark
        if ba_acctopenbh_url is not UNSET:
            field_dict["ba_acctopenbh_url"] = ba_acctopenbh_url
        if ba_acctopenbh_remark is not UNSET:
            field_dict["ba_acctopenbh_remark"] = ba_acctopenbh_remark
        if ba_hotline_tel is not UNSET:
            field_dict["ba_hotline_tel"] = ba_hotline_tel
        if ba_hotline_remark is not UNSET:
            field_dict["ba_hotline_remark"] = ba_hotline_remark
        if ba_contact_person is not UNSET:
            field_dict["ba_contact_person"] = ba_contact_person
        if ba_contact_email is not UNSET:
            field_dict["ba_contact_email"] = ba_contact_email
        if ba_contact_tel is not UNSET:
            field_dict["ba_contact_tel"] = ba_contact_tel
        if ba_contact_fax is not UNSET:
            field_dict["ba_contact_fax"] = ba_contact_fax
        if ba_contact_mobile is not UNSET:
            field_dict["ba_contact_mobile"] = ba_contact_mobile
        if ba_contact_url is not UNSET:
            field_dict["ba_contact_url"] = ba_contact_url
        if ba_contact_remark is not UNSET:
            field_dict["ba_contact_remark"] = ba_contact_remark

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        bank_info_name = d.pop("bank_info_name", UNSET)

        def _parse_bank_info_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bank_info_url = _parse_bank_info_url(d.pop("bank_info_url", UNSET))

        bank_info_type = d.pop("bank_info_type", UNSET)

        def _parse_bank_info_remark(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bank_info_remark = _parse_bank_info_remark(d.pop("bank_info_remark", UNSET))

        def _parse_pa_service_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pa_service_url = _parse_pa_service_url(d.pop("pa_service_url", UNSET))

        def _parse_pa_service_remark(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pa_service_remark = _parse_pa_service_remark(d.pop("pa_service_remark", UNSET))

        def _parse_pa_onlappl_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pa_onlappl_url = _parse_pa_onlappl_url(d.pop("pa_onlappl_url", UNSET))

        def _parse_pa_onlappl_remark(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pa_onlappl_remark = _parse_pa_onlappl_remark(d.pop("pa_onlappl_remark", UNSET))

        def _parse_pa_onlappo_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pa_onlappo_url = _parse_pa_onlappo_url(d.pop("pa_onlappo_url", UNSET))

        def _parse_pa_onlappo_remark(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pa_onlappo_remark = _parse_pa_onlappo_remark(d.pop("pa_onlappo_remark", UNSET))

        def _parse_pa_inforeq_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pa_inforeq_url = _parse_pa_inforeq_url(d.pop("pa_inforeq_url", UNSET))

        def _parse_pa_inforeq_remark(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pa_inforeq_remark = _parse_pa_inforeq_remark(d.pop("pa_inforeq_remark", UNSET))

        def _parse_pa_acctopenbh_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pa_acctopenbh_url = _parse_pa_acctopenbh_url(d.pop("pa_acctopenbh_url", UNSET))

        def _parse_pa_acctopenbh_remark(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pa_acctopenbh_remark = _parse_pa_acctopenbh_remark(
            d.pop("pa_acctopenbh_remark", UNSET)
        )

        def _parse_pa_hotline_tel(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pa_hotline_tel = _parse_pa_hotline_tel(d.pop("pa_hotline_tel", UNSET))

        def _parse_pa_hotline_remark(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pa_hotline_remark = _parse_pa_hotline_remark(d.pop("pa_hotline_remark", UNSET))

        def _parse_pa_contact_person(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pa_contact_person = _parse_pa_contact_person(d.pop("pa_contact_person", UNSET))

        def _parse_pa_contact_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pa_contact_email = _parse_pa_contact_email(d.pop("pa_contact_email", UNSET))

        def _parse_pa_contact_tel(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pa_contact_tel = _parse_pa_contact_tel(d.pop("pa_contact_tel", UNSET))

        def _parse_pa_contact_fax(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pa_contact_fax = _parse_pa_contact_fax(d.pop("pa_contact_fax", UNSET))

        def _parse_pa_contact_mobile(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pa_contact_mobile = _parse_pa_contact_mobile(d.pop("pa_contact_mobile", UNSET))

        def _parse_pa_contact_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pa_contact_url = _parse_pa_contact_url(d.pop("pa_contact_url", UNSET))

        def _parse_pa_contact_remark(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pa_contact_remark = _parse_pa_contact_remark(d.pop("pa_contact_remark", UNSET))

        def _parse_ba_service_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ba_service_url = _parse_ba_service_url(d.pop("ba_service_url", UNSET))

        def _parse_ba_service_remark(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ba_service_remark = _parse_ba_service_remark(d.pop("ba_service_remark", UNSET))

        def _parse_ba_onlappl_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ba_onlappl_url = _parse_ba_onlappl_url(d.pop("ba_onlappl_url", UNSET))

        def _parse_ba_onlappl_remark(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ba_onlappl_remark = _parse_ba_onlappl_remark(d.pop("ba_onlappl_remark", UNSET))

        def _parse_ba_onlappo_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ba_onlappo_url = _parse_ba_onlappo_url(d.pop("ba_onlappo_url", UNSET))

        def _parse_ba_onlappo_remark(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ba_onlappo_remark = _parse_ba_onlappo_remark(d.pop("ba_onlappo_remark", UNSET))

        def _parse_ba_inforeq_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ba_inforeq_url = _parse_ba_inforeq_url(d.pop("ba_inforeq_url", UNSET))

        def _parse_ba_inforeq_remark(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ba_inforeq_remark = _parse_ba_inforeq_remark(d.pop("ba_inforeq_remark", UNSET))

        def _parse_ba_acctopenbh_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ba_acctopenbh_url = _parse_ba_acctopenbh_url(d.pop("ba_acctopenbh_url", UNSET))

        def _parse_ba_acctopenbh_remark(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ba_acctopenbh_remark = _parse_ba_acctopenbh_remark(
            d.pop("ba_acctopenbh_remark", UNSET)
        )

        def _parse_ba_hotline_tel(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ba_hotline_tel = _parse_ba_hotline_tel(d.pop("ba_hotline_tel", UNSET))

        def _parse_ba_hotline_remark(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ba_hotline_remark = _parse_ba_hotline_remark(d.pop("ba_hotline_remark", UNSET))

        def _parse_ba_contact_person(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ba_contact_person = _parse_ba_contact_person(d.pop("ba_contact_person", UNSET))

        def _parse_ba_contact_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ba_contact_email = _parse_ba_contact_email(d.pop("ba_contact_email", UNSET))

        def _parse_ba_contact_tel(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ba_contact_tel = _parse_ba_contact_tel(d.pop("ba_contact_tel", UNSET))

        def _parse_ba_contact_fax(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ba_contact_fax = _parse_ba_contact_fax(d.pop("ba_contact_fax", UNSET))

        def _parse_ba_contact_mobile(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ba_contact_mobile = _parse_ba_contact_mobile(d.pop("ba_contact_mobile", UNSET))

        def _parse_ba_contact_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ba_contact_url = _parse_ba_contact_url(d.pop("ba_contact_url", UNSET))

        def _parse_ba_contact_remark(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ba_contact_remark = _parse_ba_contact_remark(d.pop("ba_contact_remark", UNSET))

        record = cls(
            bank_info_name=bank_info_name,
            bank_info_url=bank_info_url,
            bank_info_type=bank_info_type,
            bank_info_remark=bank_info_remark,
            pa_service_url=pa_service_url,
            pa_service_remark=pa_service_remark,
            pa_onlappl_url=pa_onlappl_url,
            pa_onlappl_remark=pa_onlappl_remark,
            pa_onlappo_url=pa_onlappo_url,
            pa_onlappo_remark=pa_onlappo_remark,
            pa_inforeq_url=pa_inforeq_url,
            pa_inforeq_remark=pa_inforeq_remark,
            pa_acctopenbh_url=pa_acctopenbh_url,
            pa_acctopenbh_remark=pa_acctopenbh_remark,
            pa_hotline_tel=pa_hotline_tel,
            pa_hotline_remark=pa_hotline_remark,
            pa_contact_person=pa_contact_person,
            pa_contact_email=pa_contact_email,
            pa_contact_tel=pa_contact_tel,
            pa_contact_fax=pa_contact_fax,
            pa_contact_mobile=pa_contact_mobile,
            pa_contact_url=pa_contact_url,
            pa_contact_remark=pa_contact_remark,
            ba_service_url=ba_service_url,
            ba_service_remark=ba_service_remark,
            ba_onlappl_url=ba_onlappl_url,
            ba_onlappl_remark=ba_onlappl_remark,
            ba_onlappo_url=ba_onlappo_url,
            ba_onlappo_remark=ba_onlappo_remark,
            ba_inforeq_url=ba_inforeq_url,
            ba_inforeq_remark=ba_inforeq_remark,
            ba_acctopenbh_url=ba_acctopenbh_url,
            ba_acctopenbh_remark=ba_acctopenbh_remark,
            ba_hotline_tel=ba_hotline_tel,
            ba_hotline_remark=ba_hotline_remark,
            ba_contact_person=ba_contact_person,
            ba_contact_email=ba_contact_email,
            ba_contact_tel=ba_contact_tel,
            ba_contact_fax=ba_contact_fax,
            ba_contact_mobile=ba_contact_mobile,
            ba_contact_url=ba_contact_url,
            ba_contact_remark=ba_contact_remark,
        )

        record.additional_properties = d
        return record

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
