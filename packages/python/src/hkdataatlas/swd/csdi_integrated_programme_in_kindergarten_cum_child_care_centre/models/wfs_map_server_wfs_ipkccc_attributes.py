from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsIPKCCCAttributes")


@_attrs_define
class WfsMapServerWfsIPKCCCAttributes:
    """
    Attributes:
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        dataset_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        dataset_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        name_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        address_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        name_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        address_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        district_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        district_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        gender_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        gender_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        centre_code_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        centre_code_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        telephone_number_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        telephone_number_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        fax_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        fax_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        total_capacity_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        total_capacity_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        northing (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        easting (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        latitude (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        longitude (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        last_update (None | str | Unset): Native XSD type xsd:dateTime. Requiredness is not projected from XML
            occurrence into all JSON queries.
    """

    shape: Any | Unset = UNSET
    objectid: int | Unset = UNSET
    dataset_en: None | str | Unset = UNSET
    dataset_tc: None | str | Unset = UNSET
    name_en: None | str | Unset = UNSET
    address_en: None | str | Unset = UNSET
    name_tc: None | str | Unset = UNSET
    address_tc: None | str | Unset = UNSET
    district_en: None | str | Unset = UNSET
    district_tc: None | str | Unset = UNSET
    gender_en: None | str | Unset = UNSET
    gender_tc: None | str | Unset = UNSET
    centre_code_en: None | str | Unset = UNSET
    centre_code_tc: None | str | Unset = UNSET
    telephone_number_en: None | str | Unset = UNSET
    telephone_number_tc: None | str | Unset = UNSET
    fax_en: None | str | Unset = UNSET
    fax_tc: None | str | Unset = UNSET
    total_capacity_en: None | str | Unset = UNSET
    total_capacity_tc: None | str | Unset = UNSET
    northing: float | None | Unset = UNSET
    easting: float | None | Unset = UNSET
    latitude: float | None | Unset = UNSET
    longitude: float | None | Unset = UNSET
    last_update: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        shape = self.shape

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

        gender_en: None | str | Unset
        if isinstance(self.gender_en, Unset):
            gender_en = UNSET
        else:
            gender_en = self.gender_en

        gender_tc: None | str | Unset
        if isinstance(self.gender_tc, Unset):
            gender_tc = UNSET
        else:
            gender_tc = self.gender_tc

        centre_code_en: None | str | Unset
        if isinstance(self.centre_code_en, Unset):
            centre_code_en = UNSET
        else:
            centre_code_en = self.centre_code_en

        centre_code_tc: None | str | Unset
        if isinstance(self.centre_code_tc, Unset):
            centre_code_tc = UNSET
        else:
            centre_code_tc = self.centre_code_tc

        telephone_number_en: None | str | Unset
        if isinstance(self.telephone_number_en, Unset):
            telephone_number_en = UNSET
        else:
            telephone_number_en = self.telephone_number_en

        telephone_number_tc: None | str | Unset
        if isinstance(self.telephone_number_tc, Unset):
            telephone_number_tc = UNSET
        else:
            telephone_number_tc = self.telephone_number_tc

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

        total_capacity_en: None | str | Unset
        if isinstance(self.total_capacity_en, Unset):
            total_capacity_en = UNSET
        else:
            total_capacity_en = self.total_capacity_en

        total_capacity_tc: None | str | Unset
        if isinstance(self.total_capacity_tc, Unset):
            total_capacity_tc = UNSET
        else:
            total_capacity_tc = self.total_capacity_tc

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

        last_update: None | str | Unset
        if isinstance(self.last_update, Unset):
            last_update = UNSET
        else:
            last_update = self.last_update

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if shape is not UNSET:
            field_dict["shape"] = shape
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
        if gender_en is not UNSET:
            field_dict["GenderEN"] = gender_en
        if gender_tc is not UNSET:
            field_dict["GenderTC"] = gender_tc
        if centre_code_en is not UNSET:
            field_dict["CentreCodeEN"] = centre_code_en
        if centre_code_tc is not UNSET:
            field_dict["CentreCodeTC"] = centre_code_tc
        if telephone_number_en is not UNSET:
            field_dict["TelephoneNumberEN"] = telephone_number_en
        if telephone_number_tc is not UNSET:
            field_dict["TelephoneNumberTC"] = telephone_number_tc
        if fax_en is not UNSET:
            field_dict["FaxEN"] = fax_en
        if fax_tc is not UNSET:
            field_dict["FaxTC"] = fax_tc
        if total_capacity_en is not UNSET:
            field_dict["TotalCapacityEN"] = total_capacity_en
        if total_capacity_tc is not UNSET:
            field_dict["TotalCapacityTC"] = total_capacity_tc
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
        shape = d.pop("shape", UNSET)

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

        def _parse_gender_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gender_en = _parse_gender_en(d.pop("GenderEN", UNSET))

        def _parse_gender_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gender_tc = _parse_gender_tc(d.pop("GenderTC", UNSET))

        def _parse_centre_code_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        centre_code_en = _parse_centre_code_en(d.pop("CentreCodeEN", UNSET))

        def _parse_centre_code_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        centre_code_tc = _parse_centre_code_tc(d.pop("CentreCodeTC", UNSET))

        def _parse_telephone_number_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        telephone_number_en = _parse_telephone_number_en(
            d.pop("TelephoneNumberEN", UNSET)
        )

        def _parse_telephone_number_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        telephone_number_tc = _parse_telephone_number_tc(
            d.pop("TelephoneNumberTC", UNSET)
        )

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

        def _parse_total_capacity_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        total_capacity_en = _parse_total_capacity_en(d.pop("TotalCapacityEN", UNSET))

        def _parse_total_capacity_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        total_capacity_tc = _parse_total_capacity_tc(d.pop("TotalCapacityTC", UNSET))

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

        def _parse_last_update(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_update = _parse_last_update(d.pop("LastUpdate", UNSET))

        wfs_map_server_wfs_ipkccc_attributes = cls(
            shape=shape,
            objectid=objectid,
            dataset_en=dataset_en,
            dataset_tc=dataset_tc,
            name_en=name_en,
            address_en=address_en,
            name_tc=name_tc,
            address_tc=address_tc,
            district_en=district_en,
            district_tc=district_tc,
            gender_en=gender_en,
            gender_tc=gender_tc,
            centre_code_en=centre_code_en,
            centre_code_tc=centre_code_tc,
            telephone_number_en=telephone_number_en,
            telephone_number_tc=telephone_number_tc,
            fax_en=fax_en,
            fax_tc=fax_tc,
            total_capacity_en=total_capacity_en,
            total_capacity_tc=total_capacity_tc,
            northing=northing,
            easting=easting,
            latitude=latitude,
            longitude=longitude,
            last_update=last_update,
        )

        wfs_map_server_wfs_ipkccc_attributes.additional_properties = d
        return wfs_map_server_wfs_ipkccc_attributes

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
