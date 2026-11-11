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
        district_en (None | str | Unset): Publisher field type: esriFieldTypeString
        district_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        nameof_organisation_en (None | str | Unset): Publisher field type: esriFieldTypeString
        nameof_organisation_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        ageof_child_en (None | str | Unset): Publisher field type: esriFieldTypeString
        ageof_child_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        telephone_en (None | str | Unset): Publisher field type: esriFieldTypeString
        telephone_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        fax_number_en (None | str | Unset): Publisher field type: esriFieldTypeString
        fax_number_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        typeof_service_en (None | str | Unset): Publisher field type: esriFieldTypeString
        typeof_service_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        capacity_fd_creche_en (None | str | Unset): Publisher field type: esriFieldTypeString
        capacity_fd_creche_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        capacity_hd_creche_en (None | str | Unset): Publisher field type: esriFieldTypeString
        capacity_hd_creche_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        capacity_fd_nursery_en (None | str | Unset): Publisher field type: esriFieldTypeString
        capacity_fd_nursery_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        capacity_hd_nursery_en (None | str | Unset): Publisher field type: esriFieldTypeString
        capacity_hd_nursery_tc (None | str | Unset): Publisher field type: esriFieldTypeString
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
    district_en: None | str | Unset = UNSET
    district_tc: None | str | Unset = UNSET
    nameof_organisation_en: None | str | Unset = UNSET
    nameof_organisation_tc: None | str | Unset = UNSET
    ageof_child_en: None | str | Unset = UNSET
    ageof_child_tc: None | str | Unset = UNSET
    telephone_en: None | str | Unset = UNSET
    telephone_tc: None | str | Unset = UNSET
    fax_number_en: None | str | Unset = UNSET
    fax_number_tc: None | str | Unset = UNSET
    typeof_service_en: None | str | Unset = UNSET
    typeof_service_tc: None | str | Unset = UNSET
    capacity_fd_creche_en: None | str | Unset = UNSET
    capacity_fd_creche_tc: None | str | Unset = UNSET
    capacity_hd_creche_en: None | str | Unset = UNSET
    capacity_hd_creche_tc: None | str | Unset = UNSET
    capacity_fd_nursery_en: None | str | Unset = UNSET
    capacity_fd_nursery_tc: None | str | Unset = UNSET
    capacity_hd_nursery_en: None | str | Unset = UNSET
    capacity_hd_nursery_tc: None | str | Unset = UNSET
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

        nameof_organisation_en: None | str | Unset
        if isinstance(self.nameof_organisation_en, Unset):
            nameof_organisation_en = UNSET
        else:
            nameof_organisation_en = self.nameof_organisation_en

        nameof_organisation_tc: None | str | Unset
        if isinstance(self.nameof_organisation_tc, Unset):
            nameof_organisation_tc = UNSET
        else:
            nameof_organisation_tc = self.nameof_organisation_tc

        ageof_child_en: None | str | Unset
        if isinstance(self.ageof_child_en, Unset):
            ageof_child_en = UNSET
        else:
            ageof_child_en = self.ageof_child_en

        ageof_child_tc: None | str | Unset
        if isinstance(self.ageof_child_tc, Unset):
            ageof_child_tc = UNSET
        else:
            ageof_child_tc = self.ageof_child_tc

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

        fax_number_en: None | str | Unset
        if isinstance(self.fax_number_en, Unset):
            fax_number_en = UNSET
        else:
            fax_number_en = self.fax_number_en

        fax_number_tc: None | str | Unset
        if isinstance(self.fax_number_tc, Unset):
            fax_number_tc = UNSET
        else:
            fax_number_tc = self.fax_number_tc

        typeof_service_en: None | str | Unset
        if isinstance(self.typeof_service_en, Unset):
            typeof_service_en = UNSET
        else:
            typeof_service_en = self.typeof_service_en

        typeof_service_tc: None | str | Unset
        if isinstance(self.typeof_service_tc, Unset):
            typeof_service_tc = UNSET
        else:
            typeof_service_tc = self.typeof_service_tc

        capacity_fd_creche_en: None | str | Unset
        if isinstance(self.capacity_fd_creche_en, Unset):
            capacity_fd_creche_en = UNSET
        else:
            capacity_fd_creche_en = self.capacity_fd_creche_en

        capacity_fd_creche_tc: None | str | Unset
        if isinstance(self.capacity_fd_creche_tc, Unset):
            capacity_fd_creche_tc = UNSET
        else:
            capacity_fd_creche_tc = self.capacity_fd_creche_tc

        capacity_hd_creche_en: None | str | Unset
        if isinstance(self.capacity_hd_creche_en, Unset):
            capacity_hd_creche_en = UNSET
        else:
            capacity_hd_creche_en = self.capacity_hd_creche_en

        capacity_hd_creche_tc: None | str | Unset
        if isinstance(self.capacity_hd_creche_tc, Unset):
            capacity_hd_creche_tc = UNSET
        else:
            capacity_hd_creche_tc = self.capacity_hd_creche_tc

        capacity_fd_nursery_en: None | str | Unset
        if isinstance(self.capacity_fd_nursery_en, Unset):
            capacity_fd_nursery_en = UNSET
        else:
            capacity_fd_nursery_en = self.capacity_fd_nursery_en

        capacity_fd_nursery_tc: None | str | Unset
        if isinstance(self.capacity_fd_nursery_tc, Unset):
            capacity_fd_nursery_tc = UNSET
        else:
            capacity_fd_nursery_tc = self.capacity_fd_nursery_tc

        capacity_hd_nursery_en: None | str | Unset
        if isinstance(self.capacity_hd_nursery_en, Unset):
            capacity_hd_nursery_en = UNSET
        else:
            capacity_hd_nursery_en = self.capacity_hd_nursery_en

        capacity_hd_nursery_tc: None | str | Unset
        if isinstance(self.capacity_hd_nursery_tc, Unset):
            capacity_hd_nursery_tc = UNSET
        else:
            capacity_hd_nursery_tc = self.capacity_hd_nursery_tc

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
        if district_en is not UNSET:
            field_dict["DistrictEN"] = district_en
        if district_tc is not UNSET:
            field_dict["DistrictTC"] = district_tc
        if nameof_organisation_en is not UNSET:
            field_dict["NameofOrganisationEN"] = nameof_organisation_en
        if nameof_organisation_tc is not UNSET:
            field_dict["NameofOrganisationTC"] = nameof_organisation_tc
        if ageof_child_en is not UNSET:
            field_dict["AgeofChildEN"] = ageof_child_en
        if ageof_child_tc is not UNSET:
            field_dict["AgeofChildTC"] = ageof_child_tc
        if telephone_en is not UNSET:
            field_dict["TelephoneEN"] = telephone_en
        if telephone_tc is not UNSET:
            field_dict["TelephoneTC"] = telephone_tc
        if fax_number_en is not UNSET:
            field_dict["FaxNumberEN"] = fax_number_en
        if fax_number_tc is not UNSET:
            field_dict["FaxNumberTC"] = fax_number_tc
        if typeof_service_en is not UNSET:
            field_dict["TypeofServiceEN"] = typeof_service_en
        if typeof_service_tc is not UNSET:
            field_dict["TypeofServiceTC"] = typeof_service_tc
        if capacity_fd_creche_en is not UNSET:
            field_dict["CapacityFDCrecheEN"] = capacity_fd_creche_en
        if capacity_fd_creche_tc is not UNSET:
            field_dict["CapacityFDCrecheTC"] = capacity_fd_creche_tc
        if capacity_hd_creche_en is not UNSET:
            field_dict["CapacityHDCrecheEN"] = capacity_hd_creche_en
        if capacity_hd_creche_tc is not UNSET:
            field_dict["CapacityHDCrecheTC"] = capacity_hd_creche_tc
        if capacity_fd_nursery_en is not UNSET:
            field_dict["CapacityFDNurseryEN"] = capacity_fd_nursery_en
        if capacity_fd_nursery_tc is not UNSET:
            field_dict["CapacityFDNurseryTC"] = capacity_fd_nursery_tc
        if capacity_hd_nursery_en is not UNSET:
            field_dict["CapacityHDNurseryEN"] = capacity_hd_nursery_en
        if capacity_hd_nursery_tc is not UNSET:
            field_dict["CapacityHDNurseryTC"] = capacity_hd_nursery_tc
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

        def _parse_nameof_organisation_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nameof_organisation_en = _parse_nameof_organisation_en(
            d.pop("NameofOrganisationEN", UNSET)
        )

        def _parse_nameof_organisation_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nameof_organisation_tc = _parse_nameof_organisation_tc(
            d.pop("NameofOrganisationTC", UNSET)
        )

        def _parse_ageof_child_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ageof_child_en = _parse_ageof_child_en(d.pop("AgeofChildEN", UNSET))

        def _parse_ageof_child_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ageof_child_tc = _parse_ageof_child_tc(d.pop("AgeofChildTC", UNSET))

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

        def _parse_fax_number_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fax_number_en = _parse_fax_number_en(d.pop("FaxNumberEN", UNSET))

        def _parse_fax_number_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fax_number_tc = _parse_fax_number_tc(d.pop("FaxNumberTC", UNSET))

        def _parse_typeof_service_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        typeof_service_en = _parse_typeof_service_en(d.pop("TypeofServiceEN", UNSET))

        def _parse_typeof_service_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        typeof_service_tc = _parse_typeof_service_tc(d.pop("TypeofServiceTC", UNSET))

        def _parse_capacity_fd_creche_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        capacity_fd_creche_en = _parse_capacity_fd_creche_en(
            d.pop("CapacityFDCrecheEN", UNSET)
        )

        def _parse_capacity_fd_creche_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        capacity_fd_creche_tc = _parse_capacity_fd_creche_tc(
            d.pop("CapacityFDCrecheTC", UNSET)
        )

        def _parse_capacity_hd_creche_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        capacity_hd_creche_en = _parse_capacity_hd_creche_en(
            d.pop("CapacityHDCrecheEN", UNSET)
        )

        def _parse_capacity_hd_creche_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        capacity_hd_creche_tc = _parse_capacity_hd_creche_tc(
            d.pop("CapacityHDCrecheTC", UNSET)
        )

        def _parse_capacity_fd_nursery_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        capacity_fd_nursery_en = _parse_capacity_fd_nursery_en(
            d.pop("CapacityFDNurseryEN", UNSET)
        )

        def _parse_capacity_fd_nursery_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        capacity_fd_nursery_tc = _parse_capacity_fd_nursery_tc(
            d.pop("CapacityFDNurseryTC", UNSET)
        )

        def _parse_capacity_hd_nursery_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        capacity_hd_nursery_en = _parse_capacity_hd_nursery_en(
            d.pop("CapacityHDNurseryEN", UNSET)
        )

        def _parse_capacity_hd_nursery_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        capacity_hd_nursery_tc = _parse_capacity_hd_nursery_tc(
            d.pop("CapacityHDNurseryTC", UNSET)
        )

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
            district_en=district_en,
            district_tc=district_tc,
            nameof_organisation_en=nameof_organisation_en,
            nameof_organisation_tc=nameof_organisation_tc,
            ageof_child_en=ageof_child_en,
            ageof_child_tc=ageof_child_tc,
            telephone_en=telephone_en,
            telephone_tc=telephone_tc,
            fax_number_en=fax_number_en,
            fax_number_tc=fax_number_tc,
            typeof_service_en=typeof_service_en,
            typeof_service_tc=typeof_service_tc,
            capacity_fd_creche_en=capacity_fd_creche_en,
            capacity_fd_creche_tc=capacity_fd_creche_tc,
            capacity_hd_creche_en=capacity_hd_creche_en,
            capacity_hd_creche_tc=capacity_hd_creche_tc,
            capacity_fd_nursery_en=capacity_fd_nursery_en,
            capacity_fd_nursery_tc=capacity_fd_nursery_tc,
            capacity_hd_nursery_en=capacity_hd_nursery_en,
            capacity_hd_nursery_tc=capacity_hd_nursery_tc,
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
