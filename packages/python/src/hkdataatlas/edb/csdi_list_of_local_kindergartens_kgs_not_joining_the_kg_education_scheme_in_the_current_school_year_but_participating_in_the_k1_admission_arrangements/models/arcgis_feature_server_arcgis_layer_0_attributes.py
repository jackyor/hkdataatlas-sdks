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
        row_en (None | str | Unset): Publisher field type: esriFieldTypeString
        row_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        forms_no_quota_en (None | str | Unset): Publisher field type: esriFieldTypeString
        forms_no_quota_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        one_place_per_child_en (None | str | Unset): Publisher field type: esriFieldTypeString
        one_place_per_child_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        vacancies_en (None | str | Unset): Publisher field type: esriFieldTypeString
        vacancies_tc (None | str | Unset): Publisher field type: esriFieldTypeString
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
    row_en: None | str | Unset = UNSET
    row_tc: None | str | Unset = UNSET
    forms_no_quota_en: None | str | Unset = UNSET
    forms_no_quota_tc: None | str | Unset = UNSET
    one_place_per_child_en: None | str | Unset = UNSET
    one_place_per_child_tc: None | str | Unset = UNSET
    vacancies_en: None | str | Unset = UNSET
    vacancies_tc: None | str | Unset = UNSET
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

        row_en: None | str | Unset
        if isinstance(self.row_en, Unset):
            row_en = UNSET
        else:
            row_en = self.row_en

        row_tc: None | str | Unset
        if isinstance(self.row_tc, Unset):
            row_tc = UNSET
        else:
            row_tc = self.row_tc

        forms_no_quota_en: None | str | Unset
        if isinstance(self.forms_no_quota_en, Unset):
            forms_no_quota_en = UNSET
        else:
            forms_no_quota_en = self.forms_no_quota_en

        forms_no_quota_tc: None | str | Unset
        if isinstance(self.forms_no_quota_tc, Unset):
            forms_no_quota_tc = UNSET
        else:
            forms_no_quota_tc = self.forms_no_quota_tc

        one_place_per_child_en: None | str | Unset
        if isinstance(self.one_place_per_child_en, Unset):
            one_place_per_child_en = UNSET
        else:
            one_place_per_child_en = self.one_place_per_child_en

        one_place_per_child_tc: None | str | Unset
        if isinstance(self.one_place_per_child_tc, Unset):
            one_place_per_child_tc = UNSET
        else:
            one_place_per_child_tc = self.one_place_per_child_tc

        vacancies_en: None | str | Unset
        if isinstance(self.vacancies_en, Unset):
            vacancies_en = UNSET
        else:
            vacancies_en = self.vacancies_en

        vacancies_tc: None | str | Unset
        if isinstance(self.vacancies_tc, Unset):
            vacancies_tc = UNSET
        else:
            vacancies_tc = self.vacancies_tc

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
        if row_en is not UNSET:
            field_dict["RowEN"] = row_en
        if row_tc is not UNSET:
            field_dict["RowTC"] = row_tc
        if forms_no_quota_en is not UNSET:
            field_dict["FormsNoQuotaEN"] = forms_no_quota_en
        if forms_no_quota_tc is not UNSET:
            field_dict["FormsNoQuotaTC"] = forms_no_quota_tc
        if one_place_per_child_en is not UNSET:
            field_dict["OnePlacePerChildEN"] = one_place_per_child_en
        if one_place_per_child_tc is not UNSET:
            field_dict["OnePlacePerChildTC"] = one_place_per_child_tc
        if vacancies_en is not UNSET:
            field_dict["VacanciesEN"] = vacancies_en
        if vacancies_tc is not UNSET:
            field_dict["VacanciesTC"] = vacancies_tc
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

        def _parse_row_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        row_en = _parse_row_en(d.pop("RowEN", UNSET))

        def _parse_row_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        row_tc = _parse_row_tc(d.pop("RowTC", UNSET))

        def _parse_forms_no_quota_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        forms_no_quota_en = _parse_forms_no_quota_en(d.pop("FormsNoQuotaEN", UNSET))

        def _parse_forms_no_quota_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        forms_no_quota_tc = _parse_forms_no_quota_tc(d.pop("FormsNoQuotaTC", UNSET))

        def _parse_one_place_per_child_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        one_place_per_child_en = _parse_one_place_per_child_en(
            d.pop("OnePlacePerChildEN", UNSET)
        )

        def _parse_one_place_per_child_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        one_place_per_child_tc = _parse_one_place_per_child_tc(
            d.pop("OnePlacePerChildTC", UNSET)
        )

        def _parse_vacancies_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vacancies_en = _parse_vacancies_en(d.pop("VacanciesEN", UNSET))

        def _parse_vacancies_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vacancies_tc = _parse_vacancies_tc(d.pop("VacanciesTC", UNSET))

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
            row_en=row_en,
            row_tc=row_tc,
            forms_no_quota_en=forms_no_quota_en,
            forms_no_quota_tc=forms_no_quota_tc,
            one_place_per_child_en=one_place_per_child_en,
            one_place_per_child_tc=one_place_per_child_tc,
            vacancies_en=vacancies_en,
            vacancies_tc=vacancies_tc,
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
