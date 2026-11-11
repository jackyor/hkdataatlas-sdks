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
        exe_year_en (None | str | Unset): Publisher field type: esriFieldTypeString
        exe_year_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        telephone_en (None | str | Unset): Publisher field type: esriFieldTypeString
        telephone_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        user_en (None | str | Unset): Publisher field type: esriFieldTypeString
        user_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        premium_en (None | str | Unset): Publisher field type: esriFieldTypeString
        premium_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        d_reg_en (None | str | Unset): Publisher field type: esriFieldTypeString
        d_reg_tc (None | str | Unset): Publisher field type: esriFieldTypeString
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
    exe_year_en: None | str | Unset = UNSET
    exe_year_tc: None | str | Unset = UNSET
    telephone_en: None | str | Unset = UNSET
    telephone_tc: None | str | Unset = UNSET
    user_en: None | str | Unset = UNSET
    user_tc: None | str | Unset = UNSET
    premium_en: None | str | Unset = UNSET
    premium_tc: None | str | Unset = UNSET
    d_reg_en: None | str | Unset = UNSET
    d_reg_tc: None | str | Unset = UNSET
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

        exe_year_en: None | str | Unset
        if isinstance(self.exe_year_en, Unset):
            exe_year_en = UNSET
        else:
            exe_year_en = self.exe_year_en

        exe_year_tc: None | str | Unset
        if isinstance(self.exe_year_tc, Unset):
            exe_year_tc = UNSET
        else:
            exe_year_tc = self.exe_year_tc

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

        user_en: None | str | Unset
        if isinstance(self.user_en, Unset):
            user_en = UNSET
        else:
            user_en = self.user_en

        user_tc: None | str | Unset
        if isinstance(self.user_tc, Unset):
            user_tc = UNSET
        else:
            user_tc = self.user_tc

        premium_en: None | str | Unset
        if isinstance(self.premium_en, Unset):
            premium_en = UNSET
        else:
            premium_en = self.premium_en

        premium_tc: None | str | Unset
        if isinstance(self.premium_tc, Unset):
            premium_tc = UNSET
        else:
            premium_tc = self.premium_tc

        d_reg_en: None | str | Unset
        if isinstance(self.d_reg_en, Unset):
            d_reg_en = UNSET
        else:
            d_reg_en = self.d_reg_en

        d_reg_tc: None | str | Unset
        if isinstance(self.d_reg_tc, Unset):
            d_reg_tc = UNSET
        else:
            d_reg_tc = self.d_reg_tc

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
        if exe_year_en is not UNSET:
            field_dict["ExeYearEN"] = exe_year_en
        if exe_year_tc is not UNSET:
            field_dict["ExeYearTC"] = exe_year_tc
        if telephone_en is not UNSET:
            field_dict["TelephoneEN"] = telephone_en
        if telephone_tc is not UNSET:
            field_dict["TelephoneTC"] = telephone_tc
        if user_en is not UNSET:
            field_dict["UserEn"] = user_en
        if user_tc is not UNSET:
            field_dict["UserTC"] = user_tc
        if premium_en is not UNSET:
            field_dict["PremiumEn"] = premium_en
        if premium_tc is not UNSET:
            field_dict["PremiumTC"] = premium_tc
        if d_reg_en is not UNSET:
            field_dict["DRegEn"] = d_reg_en
        if d_reg_tc is not UNSET:
            field_dict["DRegTC"] = d_reg_tc
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

        def _parse_exe_year_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        exe_year_en = _parse_exe_year_en(d.pop("ExeYearEN", UNSET))

        def _parse_exe_year_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        exe_year_tc = _parse_exe_year_tc(d.pop("ExeYearTC", UNSET))

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

        def _parse_user_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_en = _parse_user_en(d.pop("UserEn", UNSET))

        def _parse_user_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_tc = _parse_user_tc(d.pop("UserTC", UNSET))

        def _parse_premium_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        premium_en = _parse_premium_en(d.pop("PremiumEn", UNSET))

        def _parse_premium_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        premium_tc = _parse_premium_tc(d.pop("PremiumTC", UNSET))

        def _parse_d_reg_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        d_reg_en = _parse_d_reg_en(d.pop("DRegEn", UNSET))

        def _parse_d_reg_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        d_reg_tc = _parse_d_reg_tc(d.pop("DRegTC", UNSET))

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
            exe_year_en=exe_year_en,
            exe_year_tc=exe_year_tc,
            telephone_en=telephone_en,
            telephone_tc=telephone_tc,
            user_en=user_en,
            user_tc=user_tc,
            premium_en=premium_en,
            premium_tc=premium_tc,
            d_reg_en=d_reg_en,
            d_reg_tc=d_reg_tc,
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
