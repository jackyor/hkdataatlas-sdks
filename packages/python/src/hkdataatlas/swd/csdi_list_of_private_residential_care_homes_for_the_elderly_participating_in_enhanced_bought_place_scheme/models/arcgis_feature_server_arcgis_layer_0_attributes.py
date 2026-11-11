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
        dataset_en (None | str | Unset): Publisher field type: esriFieldTypeString
        dataset_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        name_en (None | str | Unset): Publisher field type: esriFieldTypeString
        address_en (None | str | Unset): Publisher field type: esriFieldTypeString
        name_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        address_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        type_of_service_en (None | str | Unset): Publisher field type: esriFieldTypeString
        type_of_service_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        district_en (None | str | Unset): Publisher field type: esriFieldTypeString
        district_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        gender_of_residents_en (None | str | Unset): Publisher field type: esriFieldTypeString
        gender_of_residents_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        religion_en (None | str | Unset): Publisher field type: esriFieldTypeString
        religion_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        diet_en (None | str | Unset): Publisher field type: esriFieldTypeString
        diet_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        number_of_subsidised_places_en (None | str | Unset): Publisher field type: esriFieldTypeString
        number_of_subsidised_places_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        opening_hours_en (None | str | Unset): Publisher field type: esriFieldTypeString
        opening_hours_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        telephone_en (None | str | Unset): Publisher field type: esriFieldTypeString
        telephone_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        fax_en (None | str | Unset): Publisher field type: esriFieldTypeString
        fax_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        email_address_en (None | str | Unset): Publisher field type: esriFieldTypeString
        email_address_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        website_en (None | str | Unset): Publisher field type: esriFieldTypeString
        website_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        remarks_en (None | str | Unset): Publisher field type: esriFieldTypeString
        remarks_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        northing (float | None | Unset): Publisher field type: esriFieldTypeDouble
        easting (float | None | Unset): Publisher field type: esriFieldTypeDouble
        latitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        longitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        last_update (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains unknown.
    """

    objectid: int | Unset = UNSET
    dataset_en: None | str | Unset = UNSET
    dataset_tc: None | str | Unset = UNSET
    name_en: None | str | Unset = UNSET
    address_en: None | str | Unset = UNSET
    name_tc: None | str | Unset = UNSET
    address_tc: None | str | Unset = UNSET
    type_of_service_en: None | str | Unset = UNSET
    type_of_service_tc: None | str | Unset = UNSET
    district_en: None | str | Unset = UNSET
    district_tc: None | str | Unset = UNSET
    gender_of_residents_en: None | str | Unset = UNSET
    gender_of_residents_tc: None | str | Unset = UNSET
    religion_en: None | str | Unset = UNSET
    religion_tc: None | str | Unset = UNSET
    diet_en: None | str | Unset = UNSET
    diet_tc: None | str | Unset = UNSET
    number_of_subsidised_places_en: None | str | Unset = UNSET
    number_of_subsidised_places_tc: None | str | Unset = UNSET
    opening_hours_en: None | str | Unset = UNSET
    opening_hours_tc: None | str | Unset = UNSET
    telephone_en: None | str | Unset = UNSET
    telephone_tc: None | str | Unset = UNSET
    fax_en: None | str | Unset = UNSET
    fax_tc: None | str | Unset = UNSET
    email_address_en: None | str | Unset = UNSET
    email_address_tc: None | str | Unset = UNSET
    website_en: None | str | Unset = UNSET
    website_tc: None | str | Unset = UNSET
    remarks_en: None | str | Unset = UNSET
    remarks_tc: None | str | Unset = UNSET
    northing: float | None | Unset = UNSET
    easting: float | None | Unset = UNSET
    latitude: float | None | Unset = UNSET
    longitude: float | None | Unset = UNSET
    last_update: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        dataset_en: None | str | Unset
        if isinstance(self.dataset_en, Unset):
            dataset_en = UNSET
        else:
            dataset_en = self.dataset_en

        dataset_tc: None | str | Unset
        if isinstance(self.dataset_tc, Unset):
            dataset_tc = UNSET
        else:
            dataset_tc = self.dataset_tc

        name_en: None | str | Unset
        if isinstance(self.name_en, Unset):
            name_en = UNSET
        else:
            name_en = self.name_en

        address_en: None | str | Unset
        if isinstance(self.address_en, Unset):
            address_en = UNSET
        else:
            address_en = self.address_en

        name_tc: None | str | Unset
        if isinstance(self.name_tc, Unset):
            name_tc = UNSET
        else:
            name_tc = self.name_tc

        address_tc: None | str | Unset
        if isinstance(self.address_tc, Unset):
            address_tc = UNSET
        else:
            address_tc = self.address_tc

        type_of_service_en: None | str | Unset
        if isinstance(self.type_of_service_en, Unset):
            type_of_service_en = UNSET
        else:
            type_of_service_en = self.type_of_service_en

        type_of_service_tc: None | str | Unset
        if isinstance(self.type_of_service_tc, Unset):
            type_of_service_tc = UNSET
        else:
            type_of_service_tc = self.type_of_service_tc

        district_en: None | str | Unset
        if isinstance(self.district_en, Unset):
            district_en = UNSET
        else:
            district_en = self.district_en

        district_tc: None | str | Unset
        if isinstance(self.district_tc, Unset):
            district_tc = UNSET
        else:
            district_tc = self.district_tc

        gender_of_residents_en: None | str | Unset
        if isinstance(self.gender_of_residents_en, Unset):
            gender_of_residents_en = UNSET
        else:
            gender_of_residents_en = self.gender_of_residents_en

        gender_of_residents_tc: None | str | Unset
        if isinstance(self.gender_of_residents_tc, Unset):
            gender_of_residents_tc = UNSET
        else:
            gender_of_residents_tc = self.gender_of_residents_tc

        religion_en: None | str | Unset
        if isinstance(self.religion_en, Unset):
            religion_en = UNSET
        else:
            religion_en = self.religion_en

        religion_tc: None | str | Unset
        if isinstance(self.religion_tc, Unset):
            religion_tc = UNSET
        else:
            religion_tc = self.religion_tc

        diet_en: None | str | Unset
        if isinstance(self.diet_en, Unset):
            diet_en = UNSET
        else:
            diet_en = self.diet_en

        diet_tc: None | str | Unset
        if isinstance(self.diet_tc, Unset):
            diet_tc = UNSET
        else:
            diet_tc = self.diet_tc

        number_of_subsidised_places_en: None | str | Unset
        if isinstance(self.number_of_subsidised_places_en, Unset):
            number_of_subsidised_places_en = UNSET
        else:
            number_of_subsidised_places_en = self.number_of_subsidised_places_en

        number_of_subsidised_places_tc: None | str | Unset
        if isinstance(self.number_of_subsidised_places_tc, Unset):
            number_of_subsidised_places_tc = UNSET
        else:
            number_of_subsidised_places_tc = self.number_of_subsidised_places_tc

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

        telephone_en: None | str | Unset
        if isinstance(self.telephone_en, Unset):
            telephone_en = UNSET
        else:
            telephone_en = self.telephone_en

        telephone_tc: None | str | Unset
        if isinstance(self.telephone_tc, Unset):
            telephone_tc = UNSET
        else:
            telephone_tc = self.telephone_tc

        fax_en: None | str | Unset
        if isinstance(self.fax_en, Unset):
            fax_en = UNSET
        else:
            fax_en = self.fax_en

        fax_tc: None | str | Unset
        if isinstance(self.fax_tc, Unset):
            fax_tc = UNSET
        else:
            fax_tc = self.fax_tc

        email_address_en: None | str | Unset
        if isinstance(self.email_address_en, Unset):
            email_address_en = UNSET
        else:
            email_address_en = self.email_address_en

        email_address_tc: None | str | Unset
        if isinstance(self.email_address_tc, Unset):
            email_address_tc = UNSET
        else:
            email_address_tc = self.email_address_tc

        website_en: None | str | Unset
        if isinstance(self.website_en, Unset):
            website_en = UNSET
        else:
            website_en = self.website_en

        website_tc: None | str | Unset
        if isinstance(self.website_tc, Unset):
            website_tc = UNSET
        else:
            website_tc = self.website_tc

        remarks_en: None | str | Unset
        if isinstance(self.remarks_en, Unset):
            remarks_en = UNSET
        else:
            remarks_en = self.remarks_en

        remarks_tc: None | str | Unset
        if isinstance(self.remarks_tc, Unset):
            remarks_tc = UNSET
        else:
            remarks_tc = self.remarks_tc

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

        latitude: float | None | Unset
        if isinstance(self.latitude, Unset):
            latitude = UNSET
        else:
            latitude = self.latitude

        longitude: float | None | Unset
        if isinstance(self.longitude, Unset):
            longitude = UNSET
        else:
            longitude = self.longitude

        last_update = self.last_update

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if dataset_en is not UNSET:
            field_dict["DatasetEN"] = dataset_en
        if dataset_tc is not UNSET:
            field_dict["DatasetTC"] = dataset_tc
        if name_en is not UNSET:
            field_dict["NameEN"] = name_en
        if address_en is not UNSET:
            field_dict["AddressEN"] = address_en
        if name_tc is not UNSET:
            field_dict["NameTC"] = name_tc
        if address_tc is not UNSET:
            field_dict["AddressTC"] = address_tc
        if type_of_service_en is not UNSET:
            field_dict["TypeOfServiceEN"] = type_of_service_en
        if type_of_service_tc is not UNSET:
            field_dict["TypeOfServiceTC"] = type_of_service_tc
        if district_en is not UNSET:
            field_dict["DistrictEN"] = district_en
        if district_tc is not UNSET:
            field_dict["DistrictTC"] = district_tc
        if gender_of_residents_en is not UNSET:
            field_dict["GenderOfResidentsEN"] = gender_of_residents_en
        if gender_of_residents_tc is not UNSET:
            field_dict["GenderOfResidentsTC"] = gender_of_residents_tc
        if religion_en is not UNSET:
            field_dict["ReligionEN"] = religion_en
        if religion_tc is not UNSET:
            field_dict["ReligionTC"] = religion_tc
        if diet_en is not UNSET:
            field_dict["DietEN"] = diet_en
        if diet_tc is not UNSET:
            field_dict["DietTC"] = diet_tc
        if number_of_subsidised_places_en is not UNSET:
            field_dict["NumberOfSubsidisedPlacesEN"] = number_of_subsidised_places_en
        if number_of_subsidised_places_tc is not UNSET:
            field_dict["NumberOfSubsidisedPlacesTC"] = number_of_subsidised_places_tc
        if opening_hours_en is not UNSET:
            field_dict["OpeningHoursEN"] = opening_hours_en
        if opening_hours_tc is not UNSET:
            field_dict["OpeningHoursTC"] = opening_hours_tc
        if telephone_en is not UNSET:
            field_dict["TelephoneEN"] = telephone_en
        if telephone_tc is not UNSET:
            field_dict["TelephoneTC"] = telephone_tc
        if fax_en is not UNSET:
            field_dict["FaxEN"] = fax_en
        if fax_tc is not UNSET:
            field_dict["FaxTC"] = fax_tc
        if email_address_en is not UNSET:
            field_dict["EmailAddressEN"] = email_address_en
        if email_address_tc is not UNSET:
            field_dict["EmailAddressTC"] = email_address_tc
        if website_en is not UNSET:
            field_dict["WebsiteEN"] = website_en
        if website_tc is not UNSET:
            field_dict["WebsiteTC"] = website_tc
        if remarks_en is not UNSET:
            field_dict["RemarksEN"] = remarks_en
        if remarks_tc is not UNSET:
            field_dict["RemarksTC"] = remarks_tc
        if northing is not UNSET:
            field_dict["Northing"] = northing
        if easting is not UNSET:
            field_dict["Easting"] = easting
        if latitude is not UNSET:
            field_dict["Latitude"] = latitude
        if longitude is not UNSET:
            field_dict["Longitude"] = longitude
        if last_update is not UNSET:
            field_dict["LastUpdate"] = last_update

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_dataset_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dataset_en = _parse_dataset_en(d.pop("DatasetEN", UNSET))

        def _parse_dataset_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dataset_tc = _parse_dataset_tc(d.pop("DatasetTC", UNSET))

        def _parse_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_en = _parse_name_en(d.pop("NameEN", UNSET))

        def _parse_address_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_en = _parse_address_en(d.pop("AddressEN", UNSET))

        def _parse_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_tc = _parse_name_tc(d.pop("NameTC", UNSET))

        def _parse_address_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_tc = _parse_address_tc(d.pop("AddressTC", UNSET))

        def _parse_type_of_service_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_of_service_en = _parse_type_of_service_en(d.pop("TypeOfServiceEN", UNSET))

        def _parse_type_of_service_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_of_service_tc = _parse_type_of_service_tc(d.pop("TypeOfServiceTC", UNSET))

        def _parse_district_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_en = _parse_district_en(d.pop("DistrictEN", UNSET))

        def _parse_district_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_tc = _parse_district_tc(d.pop("DistrictTC", UNSET))

        def _parse_gender_of_residents_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gender_of_residents_en = _parse_gender_of_residents_en(
            d.pop("GenderOfResidentsEN", UNSET)
        )

        def _parse_gender_of_residents_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gender_of_residents_tc = _parse_gender_of_residents_tc(
            d.pop("GenderOfResidentsTC", UNSET)
        )

        def _parse_religion_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        religion_en = _parse_religion_en(d.pop("ReligionEN", UNSET))

        def _parse_religion_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        religion_tc = _parse_religion_tc(d.pop("ReligionTC", UNSET))

        def _parse_diet_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        diet_en = _parse_diet_en(d.pop("DietEN", UNSET))

        def _parse_diet_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        diet_tc = _parse_diet_tc(d.pop("DietTC", UNSET))

        def _parse_number_of_subsidised_places_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        number_of_subsidised_places_en = _parse_number_of_subsidised_places_en(
            d.pop("NumberOfSubsidisedPlacesEN", UNSET)
        )

        def _parse_number_of_subsidised_places_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        number_of_subsidised_places_tc = _parse_number_of_subsidised_places_tc(
            d.pop("NumberOfSubsidisedPlacesTC", UNSET)
        )

        def _parse_opening_hours_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        opening_hours_en = _parse_opening_hours_en(d.pop("OpeningHoursEN", UNSET))

        def _parse_opening_hours_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        opening_hours_tc = _parse_opening_hours_tc(d.pop("OpeningHoursTC", UNSET))

        def _parse_telephone_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        telephone_en = _parse_telephone_en(d.pop("TelephoneEN", UNSET))

        def _parse_telephone_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        telephone_tc = _parse_telephone_tc(d.pop("TelephoneTC", UNSET))

        def _parse_fax_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fax_en = _parse_fax_en(d.pop("FaxEN", UNSET))

        def _parse_fax_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fax_tc = _parse_fax_tc(d.pop("FaxTC", UNSET))

        def _parse_email_address_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email_address_en = _parse_email_address_en(d.pop("EmailAddressEN", UNSET))

        def _parse_email_address_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email_address_tc = _parse_email_address_tc(d.pop("EmailAddressTC", UNSET))

        def _parse_website_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website_en = _parse_website_en(d.pop("WebsiteEN", UNSET))

        def _parse_website_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website_tc = _parse_website_tc(d.pop("WebsiteTC", UNSET))

        def _parse_remarks_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remarks_en = _parse_remarks_en(d.pop("RemarksEN", UNSET))

        def _parse_remarks_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remarks_tc = _parse_remarks_tc(d.pop("RemarksTC", UNSET))

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

        def _parse_latitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        latitude = _parse_latitude(d.pop("Latitude", UNSET))

        def _parse_longitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        longitude = _parse_longitude(d.pop("Longitude", UNSET))

        last_update = d.pop("LastUpdate", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            objectid=objectid,
            dataset_en=dataset_en,
            dataset_tc=dataset_tc,
            name_en=name_en,
            address_en=address_en,
            name_tc=name_tc,
            address_tc=address_tc,
            type_of_service_en=type_of_service_en,
            type_of_service_tc=type_of_service_tc,
            district_en=district_en,
            district_tc=district_tc,
            gender_of_residents_en=gender_of_residents_en,
            gender_of_residents_tc=gender_of_residents_tc,
            religion_en=religion_en,
            religion_tc=religion_tc,
            diet_en=diet_en,
            diet_tc=diet_tc,
            number_of_subsidised_places_en=number_of_subsidised_places_en,
            number_of_subsidised_places_tc=number_of_subsidised_places_tc,
            opening_hours_en=opening_hours_en,
            opening_hours_tc=opening_hours_tc,
            telephone_en=telephone_en,
            telephone_tc=telephone_tc,
            fax_en=fax_en,
            fax_tc=fax_tc,
            email_address_en=email_address_en,
            email_address_tc=email_address_tc,
            website_en=website_en,
            website_tc=website_tc,
            remarks_en=remarks_en,
            remarks_tc=remarks_tc,
            northing=northing,
            easting=easting,
            latitude=latitude,
            longitude=longitude,
            last_update=last_update,
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
