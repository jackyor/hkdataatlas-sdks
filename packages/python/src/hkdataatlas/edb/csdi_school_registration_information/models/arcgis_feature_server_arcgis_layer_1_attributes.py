from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer1Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer1Attributes:
    """
    Attributes:
        district_chi (None | str | Unset): Publisher field type: esriFieldTypeString
        district_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        fax_number (None | str | Unset): Publisher field type: esriFieldTypeString
        fax_number_nil (None | str | Unset): Publisher field type: esriFieldTypeString
        finance_type_chi (None | str | Unset): Publisher field type: esriFieldTypeString
        finance_type_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        geo_info_map_url (None | str | Unset): Publisher field type: esriFieldTypeString
        geo_info_map_url_nil (None | str | Unset): Publisher field type: esriFieldTypeString
        location_id (float | None | Unset): Publisher field type: esriFieldTypeDouble
        location_map_url (None | str | Unset): Publisher field type: esriFieldTypeString
        location_map_url_nil (None | str | Unset): Publisher field type: esriFieldTypeString
        provisional_registration_date (None | str | Unset): Publisher field type: esriFieldTypeString
        provisional_registration_date_nil (None | str | Unset): Publisher field type: esriFieldTypeString
        registration_date (None | str | Unset): Publisher field type: esriFieldTypeString
        registration_status_chi (None | str | Unset): Publisher field type: esriFieldTypeString
        registration_status_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        school_address_chi (None | str | Unset): Publisher field type: esriFieldTypeString
        school_address_chi_nil (None | str | Unset): Publisher field type: esriFieldTypeString
        school_address_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        school_level_chi (None | str | Unset): Publisher field type: esriFieldTypeString
        school_level_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        school_name_chi (None | str | Unset): Publisher field type: esriFieldTypeString
        school_name_chi_nil (None | str | Unset): Publisher field type: esriFieldTypeString
        school_name_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        school_number (float | None | Unset): Publisher field type: esriFieldTypeDouble
        school_registration_number (None | str | Unset): Publisher field type: esriFieldTypeString
        school_session_chi (None | str | Unset): Publisher field type: esriFieldTypeString
        school_session_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        school_web_site (None | str | Unset): Publisher field type: esriFieldTypeString
        school_web_site_nil (None | str | Unset): Publisher field type: esriFieldTypeString
        student_gender_chi (None | str | Unset): Publisher field type: esriFieldTypeString
        student_gender_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        telephone_number (None | str | Unset): Publisher field type: esriFieldTypeString
        telephone_number_nil (None | str | Unset): Publisher field type: esriFieldTypeString
        easting (float | None | Unset): Publisher field type: esriFieldTypeDouble
        northing (float | None | Unset): Publisher field type: esriFieldTypeDouble
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    district_chi: None | str | Unset = UNSET
    district_eng: None | str | Unset = UNSET
    fax_number: None | str | Unset = UNSET
    fax_number_nil: None | str | Unset = UNSET
    finance_type_chi: None | str | Unset = UNSET
    finance_type_eng: None | str | Unset = UNSET
    geo_info_map_url: None | str | Unset = UNSET
    geo_info_map_url_nil: None | str | Unset = UNSET
    location_id: float | None | Unset = UNSET
    location_map_url: None | str | Unset = UNSET
    location_map_url_nil: None | str | Unset = UNSET
    provisional_registration_date: None | str | Unset = UNSET
    provisional_registration_date_nil: None | str | Unset = UNSET
    registration_date: None | str | Unset = UNSET
    registration_status_chi: None | str | Unset = UNSET
    registration_status_eng: None | str | Unset = UNSET
    school_address_chi: None | str | Unset = UNSET
    school_address_chi_nil: None | str | Unset = UNSET
    school_address_eng: None | str | Unset = UNSET
    school_level_chi: None | str | Unset = UNSET
    school_level_eng: None | str | Unset = UNSET
    school_name_chi: None | str | Unset = UNSET
    school_name_chi_nil: None | str | Unset = UNSET
    school_name_eng: None | str | Unset = UNSET
    school_number: float | None | Unset = UNSET
    school_registration_number: None | str | Unset = UNSET
    school_session_chi: None | str | Unset = UNSET
    school_session_eng: None | str | Unset = UNSET
    school_web_site: None | str | Unset = UNSET
    school_web_site_nil: None | str | Unset = UNSET
    student_gender_chi: None | str | Unset = UNSET
    student_gender_eng: None | str | Unset = UNSET
    telephone_number: None | str | Unset = UNSET
    telephone_number_nil: None | str | Unset = UNSET
    easting: float | None | Unset = UNSET
    northing: float | None | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        district_chi: None | str | Unset
        if isinstance(self.district_chi, Unset):
            district_chi = UNSET
        else:
            district_chi = self.district_chi

        district_eng: None | str | Unset
        if isinstance(self.district_eng, Unset):
            district_eng = UNSET
        else:
            district_eng = self.district_eng

        fax_number: None | str | Unset
        if isinstance(self.fax_number, Unset):
            fax_number = UNSET
        else:
            fax_number = self.fax_number

        fax_number_nil: None | str | Unset
        if isinstance(self.fax_number_nil, Unset):
            fax_number_nil = UNSET
        else:
            fax_number_nil = self.fax_number_nil

        finance_type_chi: None | str | Unset
        if isinstance(self.finance_type_chi, Unset):
            finance_type_chi = UNSET
        else:
            finance_type_chi = self.finance_type_chi

        finance_type_eng: None | str | Unset
        if isinstance(self.finance_type_eng, Unset):
            finance_type_eng = UNSET
        else:
            finance_type_eng = self.finance_type_eng

        geo_info_map_url: None | str | Unset
        if isinstance(self.geo_info_map_url, Unset):
            geo_info_map_url = UNSET
        else:
            geo_info_map_url = self.geo_info_map_url

        geo_info_map_url_nil: None | str | Unset
        if isinstance(self.geo_info_map_url_nil, Unset):
            geo_info_map_url_nil = UNSET
        else:
            geo_info_map_url_nil = self.geo_info_map_url_nil

        location_id: float | None | Unset
        if isinstance(self.location_id, Unset):
            location_id = UNSET
        else:
            location_id = self.location_id

        location_map_url: None | str | Unset
        if isinstance(self.location_map_url, Unset):
            location_map_url = UNSET
        else:
            location_map_url = self.location_map_url

        location_map_url_nil: None | str | Unset
        if isinstance(self.location_map_url_nil, Unset):
            location_map_url_nil = UNSET
        else:
            location_map_url_nil = self.location_map_url_nil

        provisional_registration_date: None | str | Unset
        if isinstance(self.provisional_registration_date, Unset):
            provisional_registration_date = UNSET
        else:
            provisional_registration_date = self.provisional_registration_date

        provisional_registration_date_nil: None | str | Unset
        if isinstance(self.provisional_registration_date_nil, Unset):
            provisional_registration_date_nil = UNSET
        else:
            provisional_registration_date_nil = self.provisional_registration_date_nil

        registration_date: None | str | Unset
        if isinstance(self.registration_date, Unset):
            registration_date = UNSET
        else:
            registration_date = self.registration_date

        registration_status_chi: None | str | Unset
        if isinstance(self.registration_status_chi, Unset):
            registration_status_chi = UNSET
        else:
            registration_status_chi = self.registration_status_chi

        registration_status_eng: None | str | Unset
        if isinstance(self.registration_status_eng, Unset):
            registration_status_eng = UNSET
        else:
            registration_status_eng = self.registration_status_eng

        school_address_chi: None | str | Unset
        if isinstance(self.school_address_chi, Unset):
            school_address_chi = UNSET
        else:
            school_address_chi = self.school_address_chi

        school_address_chi_nil: None | str | Unset
        if isinstance(self.school_address_chi_nil, Unset):
            school_address_chi_nil = UNSET
        else:
            school_address_chi_nil = self.school_address_chi_nil

        school_address_eng: None | str | Unset
        if isinstance(self.school_address_eng, Unset):
            school_address_eng = UNSET
        else:
            school_address_eng = self.school_address_eng

        school_level_chi: None | str | Unset
        if isinstance(self.school_level_chi, Unset):
            school_level_chi = UNSET
        else:
            school_level_chi = self.school_level_chi

        school_level_eng: None | str | Unset
        if isinstance(self.school_level_eng, Unset):
            school_level_eng = UNSET
        else:
            school_level_eng = self.school_level_eng

        school_name_chi: None | str | Unset
        if isinstance(self.school_name_chi, Unset):
            school_name_chi = UNSET
        else:
            school_name_chi = self.school_name_chi

        school_name_chi_nil: None | str | Unset
        if isinstance(self.school_name_chi_nil, Unset):
            school_name_chi_nil = UNSET
        else:
            school_name_chi_nil = self.school_name_chi_nil

        school_name_eng: None | str | Unset
        if isinstance(self.school_name_eng, Unset):
            school_name_eng = UNSET
        else:
            school_name_eng = self.school_name_eng

        school_number: float | None | Unset
        if isinstance(self.school_number, Unset):
            school_number = UNSET
        else:
            school_number = self.school_number

        school_registration_number: None | str | Unset
        if isinstance(self.school_registration_number, Unset):
            school_registration_number = UNSET
        else:
            school_registration_number = self.school_registration_number

        school_session_chi: None | str | Unset
        if isinstance(self.school_session_chi, Unset):
            school_session_chi = UNSET
        else:
            school_session_chi = self.school_session_chi

        school_session_eng: None | str | Unset
        if isinstance(self.school_session_eng, Unset):
            school_session_eng = UNSET
        else:
            school_session_eng = self.school_session_eng

        school_web_site: None | str | Unset
        if isinstance(self.school_web_site, Unset):
            school_web_site = UNSET
        else:
            school_web_site = self.school_web_site

        school_web_site_nil: None | str | Unset
        if isinstance(self.school_web_site_nil, Unset):
            school_web_site_nil = UNSET
        else:
            school_web_site_nil = self.school_web_site_nil

        student_gender_chi: None | str | Unset
        if isinstance(self.student_gender_chi, Unset):
            student_gender_chi = UNSET
        else:
            student_gender_chi = self.student_gender_chi

        student_gender_eng: None | str | Unset
        if isinstance(self.student_gender_eng, Unset):
            student_gender_eng = UNSET
        else:
            student_gender_eng = self.student_gender_eng

        telephone_number: None | str | Unset
        if isinstance(self.telephone_number, Unset):
            telephone_number = UNSET
        else:
            telephone_number = self.telephone_number

        telephone_number_nil: None | str | Unset
        if isinstance(self.telephone_number_nil, Unset):
            telephone_number_nil = UNSET
        else:
            telephone_number_nil = self.telephone_number_nil

        easting: float | None | Unset
        if isinstance(self.easting, Unset):
            easting = UNSET
        else:
            easting = self.easting

        northing: float | None | Unset
        if isinstance(self.northing, Unset):
            northing = UNSET
        else:
            northing = self.northing

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if district_chi is not UNSET:
            field_dict["DistrictChi"] = district_chi
        if district_eng is not UNSET:
            field_dict["DistrictEng"] = district_eng
        if fax_number is not UNSET:
            field_dict["FaxNumber"] = fax_number
        if fax_number_nil is not UNSET:
            field_dict["FaxNumber_nil"] = fax_number_nil
        if finance_type_chi is not UNSET:
            field_dict["FinanceTypeChi"] = finance_type_chi
        if finance_type_eng is not UNSET:
            field_dict["FinanceTypeEng"] = finance_type_eng
        if geo_info_map_url is not UNSET:
            field_dict["GeoInfoMapUrl"] = geo_info_map_url
        if geo_info_map_url_nil is not UNSET:
            field_dict["GeoInfoMapUrl_nil"] = geo_info_map_url_nil
        if location_id is not UNSET:
            field_dict["LocationID"] = location_id
        if location_map_url is not UNSET:
            field_dict["LocationMapUrl"] = location_map_url
        if location_map_url_nil is not UNSET:
            field_dict["LocationMapUrl_nil"] = location_map_url_nil
        if provisional_registration_date is not UNSET:
            field_dict["ProvisionalRegistrationDate"] = provisional_registration_date
        if provisional_registration_date_nil is not UNSET:
            field_dict["ProvisionalRegistrationDate_nil"] = (
                provisional_registration_date_nil
            )
        if registration_date is not UNSET:
            field_dict["RegistrationDate"] = registration_date
        if registration_status_chi is not UNSET:
            field_dict["RegistrationStatusChi"] = registration_status_chi
        if registration_status_eng is not UNSET:
            field_dict["RegistrationStatusEng"] = registration_status_eng
        if school_address_chi is not UNSET:
            field_dict["SchoolAddressChi"] = school_address_chi
        if school_address_chi_nil is not UNSET:
            field_dict["SchoolAddressChi_nil"] = school_address_chi_nil
        if school_address_eng is not UNSET:
            field_dict["SchoolAddressEng"] = school_address_eng
        if school_level_chi is not UNSET:
            field_dict["SchoolLevelChi"] = school_level_chi
        if school_level_eng is not UNSET:
            field_dict["SchoolLevelEng"] = school_level_eng
        if school_name_chi is not UNSET:
            field_dict["SchoolNameChi"] = school_name_chi
        if school_name_chi_nil is not UNSET:
            field_dict["SchoolNameChi_nil"] = school_name_chi_nil
        if school_name_eng is not UNSET:
            field_dict["SchoolNameEng"] = school_name_eng
        if school_number is not UNSET:
            field_dict["SchoolNumber"] = school_number
        if school_registration_number is not UNSET:
            field_dict["SchoolRegistrationNumber"] = school_registration_number
        if school_session_chi is not UNSET:
            field_dict["SchoolSessionChi"] = school_session_chi
        if school_session_eng is not UNSET:
            field_dict["SchoolSessionEng"] = school_session_eng
        if school_web_site is not UNSET:
            field_dict["SchoolWebSite"] = school_web_site
        if school_web_site_nil is not UNSET:
            field_dict["SchoolWebSite_nil"] = school_web_site_nil
        if student_gender_chi is not UNSET:
            field_dict["StudentGenderChi"] = student_gender_chi
        if student_gender_eng is not UNSET:
            field_dict["StudentGenderEng"] = student_gender_eng
        if telephone_number is not UNSET:
            field_dict["TelephoneNumber"] = telephone_number
        if telephone_number_nil is not UNSET:
            field_dict["TelephoneNumber_nil"] = telephone_number_nil
        if easting is not UNSET:
            field_dict["easting"] = easting
        if northing is not UNSET:
            field_dict["northing"] = northing
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_district_chi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_chi = _parse_district_chi(d.pop("DistrictChi", UNSET))

        def _parse_district_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_eng = _parse_district_eng(d.pop("DistrictEng", UNSET))

        def _parse_fax_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fax_number = _parse_fax_number(d.pop("FaxNumber", UNSET))

        def _parse_fax_number_nil(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fax_number_nil = _parse_fax_number_nil(d.pop("FaxNumber_nil", UNSET))

        def _parse_finance_type_chi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        finance_type_chi = _parse_finance_type_chi(d.pop("FinanceTypeChi", UNSET))

        def _parse_finance_type_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        finance_type_eng = _parse_finance_type_eng(d.pop("FinanceTypeEng", UNSET))

        def _parse_geo_info_map_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        geo_info_map_url = _parse_geo_info_map_url(d.pop("GeoInfoMapUrl", UNSET))

        def _parse_geo_info_map_url_nil(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        geo_info_map_url_nil = _parse_geo_info_map_url_nil(
            d.pop("GeoInfoMapUrl_nil", UNSET)
        )

        def _parse_location_id(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        location_id = _parse_location_id(d.pop("LocationID", UNSET))

        def _parse_location_map_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_map_url = _parse_location_map_url(d.pop("LocationMapUrl", UNSET))

        def _parse_location_map_url_nil(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_map_url_nil = _parse_location_map_url_nil(
            d.pop("LocationMapUrl_nil", UNSET)
        )

        def _parse_provisional_registration_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provisional_registration_date = _parse_provisional_registration_date(
            d.pop("ProvisionalRegistrationDate", UNSET)
        )

        def _parse_provisional_registration_date_nil(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provisional_registration_date_nil = _parse_provisional_registration_date_nil(
            d.pop("ProvisionalRegistrationDate_nil", UNSET)
        )

        def _parse_registration_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        registration_date = _parse_registration_date(d.pop("RegistrationDate", UNSET))

        def _parse_registration_status_chi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        registration_status_chi = _parse_registration_status_chi(
            d.pop("RegistrationStatusChi", UNSET)
        )

        def _parse_registration_status_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        registration_status_eng = _parse_registration_status_eng(
            d.pop("RegistrationStatusEng", UNSET)
        )

        def _parse_school_address_chi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_address_chi = _parse_school_address_chi(d.pop("SchoolAddressChi", UNSET))

        def _parse_school_address_chi_nil(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_address_chi_nil = _parse_school_address_chi_nil(
            d.pop("SchoolAddressChi_nil", UNSET)
        )

        def _parse_school_address_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_address_eng = _parse_school_address_eng(d.pop("SchoolAddressEng", UNSET))

        def _parse_school_level_chi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_level_chi = _parse_school_level_chi(d.pop("SchoolLevelChi", UNSET))

        def _parse_school_level_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_level_eng = _parse_school_level_eng(d.pop("SchoolLevelEng", UNSET))

        def _parse_school_name_chi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_name_chi = _parse_school_name_chi(d.pop("SchoolNameChi", UNSET))

        def _parse_school_name_chi_nil(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_name_chi_nil = _parse_school_name_chi_nil(
            d.pop("SchoolNameChi_nil", UNSET)
        )

        def _parse_school_name_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_name_eng = _parse_school_name_eng(d.pop("SchoolNameEng", UNSET))

        def _parse_school_number(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        school_number = _parse_school_number(d.pop("SchoolNumber", UNSET))

        def _parse_school_registration_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_registration_number = _parse_school_registration_number(
            d.pop("SchoolRegistrationNumber", UNSET)
        )

        def _parse_school_session_chi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_session_chi = _parse_school_session_chi(d.pop("SchoolSessionChi", UNSET))

        def _parse_school_session_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_session_eng = _parse_school_session_eng(d.pop("SchoolSessionEng", UNSET))

        def _parse_school_web_site(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_web_site = _parse_school_web_site(d.pop("SchoolWebSite", UNSET))

        def _parse_school_web_site_nil(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_web_site_nil = _parse_school_web_site_nil(
            d.pop("SchoolWebSite_nil", UNSET)
        )

        def _parse_student_gender_chi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        student_gender_chi = _parse_student_gender_chi(d.pop("StudentGenderChi", UNSET))

        def _parse_student_gender_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        student_gender_eng = _parse_student_gender_eng(d.pop("StudentGenderEng", UNSET))

        def _parse_telephone_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        telephone_number = _parse_telephone_number(d.pop("TelephoneNumber", UNSET))

        def _parse_telephone_number_nil(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        telephone_number_nil = _parse_telephone_number_nil(
            d.pop("TelephoneNumber_nil", UNSET)
        )

        def _parse_easting(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        easting = _parse_easting(d.pop("easting", UNSET))

        def _parse_northing(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        northing = _parse_northing(d.pop("northing", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_1_attributes = cls(
            district_chi=district_chi,
            district_eng=district_eng,
            fax_number=fax_number,
            fax_number_nil=fax_number_nil,
            finance_type_chi=finance_type_chi,
            finance_type_eng=finance_type_eng,
            geo_info_map_url=geo_info_map_url,
            geo_info_map_url_nil=geo_info_map_url_nil,
            location_id=location_id,
            location_map_url=location_map_url,
            location_map_url_nil=location_map_url_nil,
            provisional_registration_date=provisional_registration_date,
            provisional_registration_date_nil=provisional_registration_date_nil,
            registration_date=registration_date,
            registration_status_chi=registration_status_chi,
            registration_status_eng=registration_status_eng,
            school_address_chi=school_address_chi,
            school_address_chi_nil=school_address_chi_nil,
            school_address_eng=school_address_eng,
            school_level_chi=school_level_chi,
            school_level_eng=school_level_eng,
            school_name_chi=school_name_chi,
            school_name_chi_nil=school_name_chi_nil,
            school_name_eng=school_name_eng,
            school_number=school_number,
            school_registration_number=school_registration_number,
            school_session_chi=school_session_chi,
            school_session_eng=school_session_eng,
            school_web_site=school_web_site,
            school_web_site_nil=school_web_site_nil,
            student_gender_chi=student_gender_chi,
            student_gender_eng=student_gender_eng,
            telephone_number=telephone_number,
            telephone_number_nil=telephone_number_nil,
            easting=easting,
            northing=northing,
            objectid=objectid,
        )

        arcgis_feature_server_arcgis_layer_1_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_1_attributes

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
