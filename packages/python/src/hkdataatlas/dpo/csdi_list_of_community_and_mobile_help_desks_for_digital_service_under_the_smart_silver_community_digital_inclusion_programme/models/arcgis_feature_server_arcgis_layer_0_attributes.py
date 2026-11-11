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
        programme_name_en (None | str | Unset): Publisher field type: esriFieldTypeString
        programme_name_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        programme_name_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        programme_start_month (None | str | Unset): Publisher field type: esriFieldTypeString
        programme_end_month (None | str | Unset): Publisher field type: esriFieldTypeString
        organisation_id (None | str | Unset): Publisher field type: esriFieldTypeString
        organisation_name_en (None | str | Unset): Publisher field type: esriFieldTypeString
        organisation_name_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        organisation_name_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        service_area_en (None | str | Unset): Publisher field type: esriFieldTypeString
        service_area_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        service_area_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        organisation_tel (None | str | Unset): Publisher field type: esriFieldTypeString
        organisation_email (None | str | Unset): Publisher field type: esriFieldTypeString
        organisation_programme_url (None | str | Unset): Publisher field type: esriFieldTypeString
        support_station (None | str | Unset): Publisher field type: esriFieldTypeString
        support_station_address_en (None | str | Unset): Publisher field type: esriFieldTypeString
        support_station_address_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        support_station_address_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        support_station_longitude (None | str | Unset): Publisher field type: esriFieldTypeString
        support_station_latitude (None | str | Unset): Publisher field type: esriFieldTypeString
        support_station_service_hrs_en (None | str | Unset): Publisher field type: esriFieldTypeString
        support_station_service_hrs_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        support_station_service_hrs_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        support_station_tel (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    programme_name_en: None | str | Unset = UNSET
    programme_name_tc: None | str | Unset = UNSET
    programme_name_sc: None | str | Unset = UNSET
    programme_start_month: None | str | Unset = UNSET
    programme_end_month: None | str | Unset = UNSET
    organisation_id: None | str | Unset = UNSET
    organisation_name_en: None | str | Unset = UNSET
    organisation_name_tc: None | str | Unset = UNSET
    organisation_name_sc: None | str | Unset = UNSET
    service_area_en: None | str | Unset = UNSET
    service_area_tc: None | str | Unset = UNSET
    service_area_sc: None | str | Unset = UNSET
    organisation_tel: None | str | Unset = UNSET
    organisation_email: None | str | Unset = UNSET
    organisation_programme_url: None | str | Unset = UNSET
    support_station: None | str | Unset = UNSET
    support_station_address_en: None | str | Unset = UNSET
    support_station_address_tc: None | str | Unset = UNSET
    support_station_address_sc: None | str | Unset = UNSET
    support_station_longitude: None | str | Unset = UNSET
    support_station_latitude: None | str | Unset = UNSET
    support_station_service_hrs_en: None | str | Unset = UNSET
    support_station_service_hrs_tc: None | str | Unset = UNSET
    support_station_service_hrs_sc: None | str | Unset = UNSET
    support_station_tel: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        programme_name_en: None | str | Unset
        if isinstance(self.programme_name_en, Unset):
            programme_name_en = UNSET
        else:
            programme_name_en = self.programme_name_en

        programme_name_tc: None | str | Unset
        if isinstance(self.programme_name_tc, Unset):
            programme_name_tc = UNSET
        else:
            programme_name_tc = self.programme_name_tc

        programme_name_sc: None | str | Unset
        if isinstance(self.programme_name_sc, Unset):
            programme_name_sc = UNSET
        else:
            programme_name_sc = self.programme_name_sc

        programme_start_month: None | str | Unset
        if isinstance(self.programme_start_month, Unset):
            programme_start_month = UNSET
        else:
            programme_start_month = self.programme_start_month

        programme_end_month: None | str | Unset
        if isinstance(self.programme_end_month, Unset):
            programme_end_month = UNSET
        else:
            programme_end_month = self.programme_end_month

        organisation_id: None | str | Unset
        if isinstance(self.organisation_id, Unset):
            organisation_id = UNSET
        else:
            organisation_id = self.organisation_id

        organisation_name_en: None | str | Unset
        if isinstance(self.organisation_name_en, Unset):
            organisation_name_en = UNSET
        else:
            organisation_name_en = self.organisation_name_en

        organisation_name_tc: None | str | Unset
        if isinstance(self.organisation_name_tc, Unset):
            organisation_name_tc = UNSET
        else:
            organisation_name_tc = self.organisation_name_tc

        organisation_name_sc: None | str | Unset
        if isinstance(self.organisation_name_sc, Unset):
            organisation_name_sc = UNSET
        else:
            organisation_name_sc = self.organisation_name_sc

        service_area_en: None | str | Unset
        if isinstance(self.service_area_en, Unset):
            service_area_en = UNSET
        else:
            service_area_en = self.service_area_en

        service_area_tc: None | str | Unset
        if isinstance(self.service_area_tc, Unset):
            service_area_tc = UNSET
        else:
            service_area_tc = self.service_area_tc

        service_area_sc: None | str | Unset
        if isinstance(self.service_area_sc, Unset):
            service_area_sc = UNSET
        else:
            service_area_sc = self.service_area_sc

        organisation_tel: None | str | Unset
        if isinstance(self.organisation_tel, Unset):
            organisation_tel = UNSET
        else:
            organisation_tel = self.organisation_tel

        organisation_email: None | str | Unset
        if isinstance(self.organisation_email, Unset):
            organisation_email = UNSET
        else:
            organisation_email = self.organisation_email

        organisation_programme_url: None | str | Unset
        if isinstance(self.organisation_programme_url, Unset):
            organisation_programme_url = UNSET
        else:
            organisation_programme_url = self.organisation_programme_url

        support_station: None | str | Unset
        if isinstance(self.support_station, Unset):
            support_station = UNSET
        else:
            support_station = self.support_station

        support_station_address_en: None | str | Unset
        if isinstance(self.support_station_address_en, Unset):
            support_station_address_en = UNSET
        else:
            support_station_address_en = self.support_station_address_en

        support_station_address_tc: None | str | Unset
        if isinstance(self.support_station_address_tc, Unset):
            support_station_address_tc = UNSET
        else:
            support_station_address_tc = self.support_station_address_tc

        support_station_address_sc: None | str | Unset
        if isinstance(self.support_station_address_sc, Unset):
            support_station_address_sc = UNSET
        else:
            support_station_address_sc = self.support_station_address_sc

        support_station_longitude: None | str | Unset
        if isinstance(self.support_station_longitude, Unset):
            support_station_longitude = UNSET
        else:
            support_station_longitude = self.support_station_longitude

        support_station_latitude: None | str | Unset
        if isinstance(self.support_station_latitude, Unset):
            support_station_latitude = UNSET
        else:
            support_station_latitude = self.support_station_latitude

        support_station_service_hrs_en: None | str | Unset
        if isinstance(self.support_station_service_hrs_en, Unset):
            support_station_service_hrs_en = UNSET
        else:
            support_station_service_hrs_en = self.support_station_service_hrs_en

        support_station_service_hrs_tc: None | str | Unset
        if isinstance(self.support_station_service_hrs_tc, Unset):
            support_station_service_hrs_tc = UNSET
        else:
            support_station_service_hrs_tc = self.support_station_service_hrs_tc

        support_station_service_hrs_sc: None | str | Unset
        if isinstance(self.support_station_service_hrs_sc, Unset):
            support_station_service_hrs_sc = UNSET
        else:
            support_station_service_hrs_sc = self.support_station_service_hrs_sc

        support_station_tel: None | str | Unset
        if isinstance(self.support_station_tel, Unset):
            support_station_tel = UNSET
        else:
            support_station_tel = self.support_station_tel

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if programme_name_en is not UNSET:
            field_dict["ProgrammeNameEN"] = programme_name_en
        if programme_name_tc is not UNSET:
            field_dict["ProgrammeNameTC"] = programme_name_tc
        if programme_name_sc is not UNSET:
            field_dict["ProgrammeNameSC"] = programme_name_sc
        if programme_start_month is not UNSET:
            field_dict["ProgrammeStartMonth"] = programme_start_month
        if programme_end_month is not UNSET:
            field_dict["ProgrammeEndMonth"] = programme_end_month
        if organisation_id is not UNSET:
            field_dict["OrganisationID"] = organisation_id
        if organisation_name_en is not UNSET:
            field_dict["OrganisationNameEN"] = organisation_name_en
        if organisation_name_tc is not UNSET:
            field_dict["OrganisationNameTC"] = organisation_name_tc
        if organisation_name_sc is not UNSET:
            field_dict["OrganisationNameSC"] = organisation_name_sc
        if service_area_en is not UNSET:
            field_dict["ServiceAreaEN"] = service_area_en
        if service_area_tc is not UNSET:
            field_dict["ServiceAreaTC"] = service_area_tc
        if service_area_sc is not UNSET:
            field_dict["ServiceAreaSC"] = service_area_sc
        if organisation_tel is not UNSET:
            field_dict["OrganisationTel"] = organisation_tel
        if organisation_email is not UNSET:
            field_dict["OrganisationEmail"] = organisation_email
        if organisation_programme_url is not UNSET:
            field_dict["OrganisationProgrammeURL"] = organisation_programme_url
        if support_station is not UNSET:
            field_dict["SupportStation"] = support_station
        if support_station_address_en is not UNSET:
            field_dict["SupportStationAddressEN"] = support_station_address_en
        if support_station_address_tc is not UNSET:
            field_dict["SupportStationAddressTC"] = support_station_address_tc
        if support_station_address_sc is not UNSET:
            field_dict["SupportStationAddressSC"] = support_station_address_sc
        if support_station_longitude is not UNSET:
            field_dict["SupportStationLongitude"] = support_station_longitude
        if support_station_latitude is not UNSET:
            field_dict["SupportStationLatitude"] = support_station_latitude
        if support_station_service_hrs_en is not UNSET:
            field_dict["SupportStationServiceHrsEN"] = support_station_service_hrs_en
        if support_station_service_hrs_tc is not UNSET:
            field_dict["SupportStationServiceHrsTC"] = support_station_service_hrs_tc
        if support_station_service_hrs_sc is not UNSET:
            field_dict["SupportStationServiceHrsSC"] = support_station_service_hrs_sc
        if support_station_tel is not UNSET:
            field_dict["SupportStationTel"] = support_station_tel
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_programme_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        programme_name_en = _parse_programme_name_en(d.pop("ProgrammeNameEN", UNSET))

        def _parse_programme_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        programme_name_tc = _parse_programme_name_tc(d.pop("ProgrammeNameTC", UNSET))

        def _parse_programme_name_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        programme_name_sc = _parse_programme_name_sc(d.pop("ProgrammeNameSC", UNSET))

        def _parse_programme_start_month(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        programme_start_month = _parse_programme_start_month(
            d.pop("ProgrammeStartMonth", UNSET)
        )

        def _parse_programme_end_month(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        programme_end_month = _parse_programme_end_month(
            d.pop("ProgrammeEndMonth", UNSET)
        )

        def _parse_organisation_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        organisation_id = _parse_organisation_id(d.pop("OrganisationID", UNSET))

        def _parse_organisation_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        organisation_name_en = _parse_organisation_name_en(
            d.pop("OrganisationNameEN", UNSET)
        )

        def _parse_organisation_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        organisation_name_tc = _parse_organisation_name_tc(
            d.pop("OrganisationNameTC", UNSET)
        )

        def _parse_organisation_name_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        organisation_name_sc = _parse_organisation_name_sc(
            d.pop("OrganisationNameSC", UNSET)
        )

        def _parse_service_area_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        service_area_en = _parse_service_area_en(d.pop("ServiceAreaEN", UNSET))

        def _parse_service_area_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        service_area_tc = _parse_service_area_tc(d.pop("ServiceAreaTC", UNSET))

        def _parse_service_area_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        service_area_sc = _parse_service_area_sc(d.pop("ServiceAreaSC", UNSET))

        def _parse_organisation_tel(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        organisation_tel = _parse_organisation_tel(d.pop("OrganisationTel", UNSET))

        def _parse_organisation_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        organisation_email = _parse_organisation_email(
            d.pop("OrganisationEmail", UNSET)
        )

        def _parse_organisation_programme_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        organisation_programme_url = _parse_organisation_programme_url(
            d.pop("OrganisationProgrammeURL", UNSET)
        )

        def _parse_support_station(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        support_station = _parse_support_station(d.pop("SupportStation", UNSET))

        def _parse_support_station_address_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        support_station_address_en = _parse_support_station_address_en(
            d.pop("SupportStationAddressEN", UNSET)
        )

        def _parse_support_station_address_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        support_station_address_tc = _parse_support_station_address_tc(
            d.pop("SupportStationAddressTC", UNSET)
        )

        def _parse_support_station_address_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        support_station_address_sc = _parse_support_station_address_sc(
            d.pop("SupportStationAddressSC", UNSET)
        )

        def _parse_support_station_longitude(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        support_station_longitude = _parse_support_station_longitude(
            d.pop("SupportStationLongitude", UNSET)
        )

        def _parse_support_station_latitude(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        support_station_latitude = _parse_support_station_latitude(
            d.pop("SupportStationLatitude", UNSET)
        )

        def _parse_support_station_service_hrs_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        support_station_service_hrs_en = _parse_support_station_service_hrs_en(
            d.pop("SupportStationServiceHrsEN", UNSET)
        )

        def _parse_support_station_service_hrs_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        support_station_service_hrs_tc = _parse_support_station_service_hrs_tc(
            d.pop("SupportStationServiceHrsTC", UNSET)
        )

        def _parse_support_station_service_hrs_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        support_station_service_hrs_sc = _parse_support_station_service_hrs_sc(
            d.pop("SupportStationServiceHrsSC", UNSET)
        )

        def _parse_support_station_tel(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        support_station_tel = _parse_support_station_tel(
            d.pop("SupportStationTel", UNSET)
        )

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            programme_name_en=programme_name_en,
            programme_name_tc=programme_name_tc,
            programme_name_sc=programme_name_sc,
            programme_start_month=programme_start_month,
            programme_end_month=programme_end_month,
            organisation_id=organisation_id,
            organisation_name_en=organisation_name_en,
            organisation_name_tc=organisation_name_tc,
            organisation_name_sc=organisation_name_sc,
            service_area_en=service_area_en,
            service_area_tc=service_area_tc,
            service_area_sc=service_area_sc,
            organisation_tel=organisation_tel,
            organisation_email=organisation_email,
            organisation_programme_url=organisation_programme_url,
            support_station=support_station,
            support_station_address_en=support_station_address_en,
            support_station_address_tc=support_station_address_tc,
            support_station_address_sc=support_station_address_sc,
            support_station_longitude=support_station_longitude,
            support_station_latitude=support_station_latitude,
            support_station_service_hrs_en=support_station_service_hrs_en,
            support_station_service_hrs_tc=support_station_service_hrs_tc,
            support_station_service_hrs_sc=support_station_service_hrs_sc,
            support_station_tel=support_station_tel,
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
