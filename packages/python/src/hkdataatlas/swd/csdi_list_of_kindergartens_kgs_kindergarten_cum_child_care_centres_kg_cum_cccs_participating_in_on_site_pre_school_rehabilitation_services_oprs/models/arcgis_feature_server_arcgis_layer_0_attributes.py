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
        nameof_agency_en (None | str | Unset): Publisher field type: esriFieldTypeString
        nameof_agency_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        district_en (None | str | Unset): Publisher field type: esriFieldTypeString
        district_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        nameof_service_team_en (None | str | Unset): Publisher field type: esriFieldTypeString
        nameof_service_team_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        service_team_code_en (None | str | Unset): Publisher field type: esriFieldTypeString
        service_team_code_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        telephonenumberof_service_team_en (None | str | Unset): Publisher field type: esriFieldTypeString
        telephonenumberof_service_team_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        edb_school_no_en (None | str | Unset): Publisher field type: esriFieldTypeString
        edb_school_no_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        location_no_en (None | str | Unset): Publisher field type: esriFieldTypeString
        location_no_tc (None | str | Unset): Publisher field type: esriFieldTypeString
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
    nameof_agency_en: None | str | Unset = UNSET
    nameof_agency_tc: None | str | Unset = UNSET
    district_en: None | str | Unset = UNSET
    district_tc: None | str | Unset = UNSET
    nameof_service_team_en: None | str | Unset = UNSET
    nameof_service_team_tc: None | str | Unset = UNSET
    service_team_code_en: None | str | Unset = UNSET
    service_team_code_tc: None | str | Unset = UNSET
    telephonenumberof_service_team_en: None | str | Unset = UNSET
    telephonenumberof_service_team_tc: None | str | Unset = UNSET
    edb_school_no_en: None | str | Unset = UNSET
    edb_school_no_tc: None | str | Unset = UNSET
    location_no_en: None | str | Unset = UNSET
    location_no_tc: None | str | Unset = UNSET
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

        nameof_agency_en: None | str | Unset
        if isinstance(self.nameof_agency_en, Unset):
            nameof_agency_en = UNSET
        else:
            nameof_agency_en = self.nameof_agency_en

        nameof_agency_tc: None | str | Unset
        if isinstance(self.nameof_agency_tc, Unset):
            nameof_agency_tc = UNSET
        else:
            nameof_agency_tc = self.nameof_agency_tc

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

        nameof_service_team_en: None | str | Unset
        if isinstance(self.nameof_service_team_en, Unset):
            nameof_service_team_en = UNSET
        else:
            nameof_service_team_en = self.nameof_service_team_en

        nameof_service_team_tc: None | str | Unset
        if isinstance(self.nameof_service_team_tc, Unset):
            nameof_service_team_tc = UNSET
        else:
            nameof_service_team_tc = self.nameof_service_team_tc

        service_team_code_en: None | str | Unset
        if isinstance(self.service_team_code_en, Unset):
            service_team_code_en = UNSET
        else:
            service_team_code_en = self.service_team_code_en

        service_team_code_tc: None | str | Unset
        if isinstance(self.service_team_code_tc, Unset):
            service_team_code_tc = UNSET
        else:
            service_team_code_tc = self.service_team_code_tc

        telephonenumberof_service_team_en: None | str | Unset
        if isinstance(self.telephonenumberof_service_team_en, Unset):
            telephonenumberof_service_team_en = UNSET
        else:
            telephonenumberof_service_team_en = self.telephonenumberof_service_team_en

        telephonenumberof_service_team_tc: None | str | Unset
        if isinstance(self.telephonenumberof_service_team_tc, Unset):
            telephonenumberof_service_team_tc = UNSET
        else:
            telephonenumberof_service_team_tc = self.telephonenumberof_service_team_tc

        edb_school_no_en: None | str | Unset
        if isinstance(self.edb_school_no_en, Unset):
            edb_school_no_en = UNSET
        else:
            edb_school_no_en = self.edb_school_no_en

        edb_school_no_tc: None | str | Unset
        if isinstance(self.edb_school_no_tc, Unset):
            edb_school_no_tc = UNSET
        else:
            edb_school_no_tc = self.edb_school_no_tc

        location_no_en: None | str | Unset
        if isinstance(self.location_no_en, Unset):
            location_no_en = UNSET
        else:
            location_no_en = self.location_no_en

        location_no_tc: None | str | Unset
        if isinstance(self.location_no_tc, Unset):
            location_no_tc = UNSET
        else:
            location_no_tc = self.location_no_tc

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
        if nameof_agency_en is not UNSET:
            field_dict["NameofAgencyEN"] = nameof_agency_en
        if nameof_agency_tc is not UNSET:
            field_dict["NameofAgencyTC"] = nameof_agency_tc
        if district_en is not UNSET:
            field_dict["DistrictEN"] = district_en
        if district_tc is not UNSET:
            field_dict["DistrictTC"] = district_tc
        if nameof_service_team_en is not UNSET:
            field_dict["NameofServiceTeamEN"] = nameof_service_team_en
        if nameof_service_team_tc is not UNSET:
            field_dict["NameofServiceTeamTC"] = nameof_service_team_tc
        if service_team_code_en is not UNSET:
            field_dict["ServiceTeamCodeEN"] = service_team_code_en
        if service_team_code_tc is not UNSET:
            field_dict["ServiceTeamCodeTC"] = service_team_code_tc
        if telephonenumberof_service_team_en is not UNSET:
            field_dict["TelephonenumberofServiceTeamEN"] = (
                telephonenumberof_service_team_en
            )
        if telephonenumberof_service_team_tc is not UNSET:
            field_dict["TelephonenumberofServiceTeamTC"] = (
                telephonenumberof_service_team_tc
            )
        if edb_school_no_en is not UNSET:
            field_dict["EDBSchoolNoEN"] = edb_school_no_en
        if edb_school_no_tc is not UNSET:
            field_dict["EDBSchoolNoTC"] = edb_school_no_tc
        if location_no_en is not UNSET:
            field_dict["LocationNoEN"] = location_no_en
        if location_no_tc is not UNSET:
            field_dict["LocationNoTC"] = location_no_tc
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

        def _parse_nameof_agency_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nameof_agency_en = _parse_nameof_agency_en(d.pop("NameofAgencyEN", UNSET))

        def _parse_nameof_agency_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nameof_agency_tc = _parse_nameof_agency_tc(d.pop("NameofAgencyTC", UNSET))

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

        def _parse_nameof_service_team_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nameof_service_team_en = _parse_nameof_service_team_en(
            d.pop("NameofServiceTeamEN", UNSET)
        )

        def _parse_nameof_service_team_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nameof_service_team_tc = _parse_nameof_service_team_tc(
            d.pop("NameofServiceTeamTC", UNSET)
        )

        def _parse_service_team_code_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        service_team_code_en = _parse_service_team_code_en(
            d.pop("ServiceTeamCodeEN", UNSET)
        )

        def _parse_service_team_code_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        service_team_code_tc = _parse_service_team_code_tc(
            d.pop("ServiceTeamCodeTC", UNSET)
        )

        def _parse_telephonenumberof_service_team_en(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        telephonenumberof_service_team_en = _parse_telephonenumberof_service_team_en(
            d.pop("TelephonenumberofServiceTeamEN", UNSET)
        )

        def _parse_telephonenumberof_service_team_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        telephonenumberof_service_team_tc = _parse_telephonenumberof_service_team_tc(
            d.pop("TelephonenumberofServiceTeamTC", UNSET)
        )

        def _parse_edb_school_no_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        edb_school_no_en = _parse_edb_school_no_en(d.pop("EDBSchoolNoEN", UNSET))

        def _parse_edb_school_no_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        edb_school_no_tc = _parse_edb_school_no_tc(d.pop("EDBSchoolNoTC", UNSET))

        def _parse_location_no_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_no_en = _parse_location_no_en(d.pop("LocationNoEN", UNSET))

        def _parse_location_no_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_no_tc = _parse_location_no_tc(d.pop("LocationNoTC", UNSET))

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
            nameof_agency_en=nameof_agency_en,
            nameof_agency_tc=nameof_agency_tc,
            district_en=district_en,
            district_tc=district_tc,
            nameof_service_team_en=nameof_service_team_en,
            nameof_service_team_tc=nameof_service_team_tc,
            service_team_code_en=service_team_code_en,
            service_team_code_tc=service_team_code_tc,
            telephonenumberof_service_team_en=telephonenumberof_service_team_en,
            telephonenumberof_service_team_tc=telephonenumberof_service_team_tc,
            edb_school_no_en=edb_school_no_en,
            edb_school_no_tc=edb_school_no_tc,
            location_no_en=location_no_en,
            location_no_tc=location_no_tc,
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
